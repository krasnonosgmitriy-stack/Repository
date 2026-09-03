import asyncio
import base64
import logging
import sqlite3
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, BufferedInputFile, KeyboardButton, ReplyKeyboardMarkup

from config import BOT_TOKEN

dp = Dispatcher()

logger = logging.getLogger(__name__)
def get_records():
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM films")
    records = cursor.fetchall()
    conn.close()
    return records
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
    logger.info("start_bot")
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=keyboard)

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Опис бота")



@dp.message(Command("films"))
async def show_films(message: Message):
    records = get_records()

    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"record_{record_id}")]
        for record_id, name in records
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer("Оберіть фільм:", reply_markup=reply_markup)

@dp.callback_query(lambda c: c.data.startswith("record_"))
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


class FilmForm(StatesGroup):
    name = State()
    description = State()
    poster = State()
    change_desc = State()
    change_poster = State()

class UpdateFilmForm(StatesGroup):
    select = State()
    field = State()
    value = State()

class DeleteFilmForm(StatesGroup):
    select = State()
    confirm = State()

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
async def get_name(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FilmForm.poster)
    await message.answer("Введіть ссилку на постер:")


@dp.message(FilmForm.poster)
async def get_poster(message: Message, state: FSMContext):
    photo = message.photo[-1]
    file = await message.bot.get_file(photo.file_id)
    file_bytes = await message.bot.download_file(file.file_path)

    # Конвертуємо в base64
    image_base64 = "data:image/jpeg;base64," + base64.b64encode(file_bytes.read()).decode("utf-8")
    data = await state.get_data()
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO films (name, description, poster) VALUES(?,?,?)", (data["name"], data["description"], image_base64))
    conn.commit()
    conn.close()
    await state.clear()
    await message.answer("Вce додано")

@dp.message(Command("update_film"))
async def update_film(message: Message, state: FSMContext):
    records = get_records()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=name, callback_data=f"update_{record_id}")]
        for record_id, name in records
    ])
    await state.set_state(UpdateFilmForm.select)
    await message.answer("Оберіть фільм для редагування", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("update_"))
async def select_film_to_update(callback: CallbackQuery, state: FSMContext):
    records_id = int(callback.data.replace("update_", ""))
    await state.update_data(records_id=records_id)
    await state.set_state(UpdateFilmForm.field)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назва", callback_data="field_name")],
        [InlineKeyboardButton(text="Опис", callback_data="field_description")],
        [InlineKeyboardButton(text="Постер", callback_data="field_poster")],
    ])
    await callback.message.answer("Що хочете змінити?", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("field_"))
async def select_field(callback: CallbackQuery, state: FSMContext):
    field = callback.data.replace("field_", "")
    await state.update_data(field=field)
    await state.set_state(UpdateFilmForm.value)

    await callback.message.answer("Введіть нове значення")


@dp.message(Command("delete_film"))
async def delete_film(message: Message, state: FSMContext):
    records = get_records()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=name, callback_data=f"delete_{record_id}")]
        for record_id, name in records
    ])
    await state.set_state(DeleteFilmForm.select)
    await message.answer("Оберить фільм для видалення", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("delete_"))
async def select_film_to_delete(callback: CallbackQuery, state: FSMContext):
    records_id = int(callback.data.replace("delete_", ""))
    await state.update_data(records_id=records_id)
    await state.set_state(DeleteFilmForm.confirm)

    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM films WHERE id = ?", (records_id,))
    film = cursor.fetchone()
    conn.close()

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="так видалити", callback_data="confirm_delete"),
            InlineKeyboardButton(text="Скасувати", callback_data="cancel_delete"),
        ]
    ])

    await callback.answer()
    await callback.message.answer(
        f"Ви впевнені що хочете видалити фільм '{film[0]}'?",
        reply_markup=keyboard
    )



@dp.callback_query(lambda c: c.data == "confirm_delete")
async def confirm_delete(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    records_id = data["records_id"]

    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("DELETE  FROM films WHERE id = ?", (records_id,))
    conn.commit()
    conn.close()

    await state.clear()
    await callback.answer()
    await callback.message.answer("Фільм видаленно")

@dp.message(Command("delete"))
async def cmd_delete(message: Message, state: FSMContext):
    records = get_records()
    if not records:
        return await message.answer("Немає фільмів для видалення")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{name}", callback_data=f"del_{record_id}")]
        for record_id, name in records
    ])
    await message.answer("Оберить фільм який подрібно видалити", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("del_"))
async def delete_callback(callback: CallbackQuery):
    logger.info(f"Користувач {callback.from_user.full_name} натиснув видалення")
    record_id = int(callback.data.replace("del_", ""))

    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("DELETE  FROM films WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

    await callback.message.edit_text("фільм було успішно видаленно з бази даних")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "cancel_delete")
async def cancel_delete(callback: CallbackQuery, state: FSMContext):
    await callback.clear()
    await callback.answer()
    await callback.message.delete("Видалення скасовано")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="bot_2.log")
    asyncio.run(main())
