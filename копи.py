import asyncio
import base64
import sqlite3
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup,
    CallbackQuery, BufferedInputFile, KeyboardButton, ReplyKeyboardMarkup
)

from config import BOT_TOKEN

dp = Dispatcher()

# --- База даних ---
def get_records():
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM films")
    records = cursor.fetchall()
    conn.close()
    return records

# --- Команда /start ---
@dp.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Опис"),
             KeyboardButton(text="/films")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=keyboard)

# --- Команда /help ---
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Опис бота")

# --- Команда /films ---
@dp.message(Command("films"))
async def show_films(message: Message):
    records = get_records()
    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"record_{record_id}")]
        for record_id, name in records
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer("Оберіть фільм:", reply_markup=reply_markup)

# --- Callback для вибору фільму ---
@dp.callback_query(Command(startswith="record_"))
async def record_button(callback: CallbackQuery):
    film_id = int(callback.data.replace("record_", ""))
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT description, poster FROM films WHERE id = ?", (film_id,))
    film = cursor.fetchone()
    conn.close()

    desc, poster = film
    if "," in poster:
        poster = poster.split(",")[1]

    image_bytes = base64.b64decode(poster)

    await callback.message.reply_photo(
        photo=BufferedInputFile(image_bytes, filename="poster.jpg"),
        caption=desc,
    )

# --- FSM для додавання фільму ---
class FilmForm(StatesGroup):
    name = State()
    description = State()
    poster = State()
    change_desc = State()
    change_poster = State()

# --- Додавання нового фільму ---
@dp.message(Command("add_film"))
async def add_film(message: Message, state: FSMContext):
    await state.set_state(FilmForm.name)
    await message.answer("Введіть назву фільму:")

@dp.message(FilmForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FilmForm.description)
    await message.answer("Введіть опис фільму:")

@dp.message(FilmForm.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.poster)
    await message.answer("Надішліть фото постера:")

@dp.message(FilmForm.poster)
async def get_poster(message: Message, state: FSMContext):
    if not message.photo:
        await message.answer("Будь ласка, надішліть фото.")
        return
    photo = message.photo[-1]
    file = await message.bot.get_file(photo.file_id)
    file_bytes = await message.bot.download_file(file.file_path)

    image_base64 = "data:image/jpeg;base64," + base64.b64encode(file_bytes.read()).decode("utf-8")
    data = await state.get_data()
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO films (name, description, poster) VALUES(?,?,?)",
                   (data["name"], data["description"], image_base64))
    conn.commit()
    conn.close()
    await state.clear()
    await message.answer("Все додано ✅")

# --- Зміна опису ---
@dp.message(Command("change_desc"))
async def change_desc_start(message: Message, state: FSMContext):
    records = get_records()
    text = "Список фільмів:\n" + "\n".join([f"{rid}: {name}" for rid, name in records])
    await message.answer(text)
    await message.answer("Введіть ID фільму та новий опис у форматі:\n<ID> <новий опис>")
    await state.set_state(FilmForm.change_desc)

@dp.message(FilmForm.change_desc)
async def change_desc(message: Message, state: FSMContext):
    try:
        parts = message.text.split(" ", 1)
        film_id = int(parts[0])
        new_desc = parts[1]

        conn = sqlite3.connect('films.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE films SET description = ? WHERE id = ?", (new_desc, film_id))
        conn.commit()
        conn.close()

        await state.clear()
        await message.answer("Опис успішно змінено ✅")
    except Exception as e:
        await message.answer(f"Помилка: {e}\nФормат має бути: <ID> <новий опис>")

# --- Запуск ---
async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
