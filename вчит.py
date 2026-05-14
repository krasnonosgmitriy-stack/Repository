import asyncio
import base64
import sqlite3
from aiogram import Bot, Dispatcher, html
from aiogram.client import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, BufferedInputFile, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import keyboard
from config import BOT_TOKEN

dp = Dispatcher()
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
            [keyboardButton(text="Опис"),
             keyboardButton(text="/films")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f"Hello {message.from_user.first_name}", reply_markup=keyboard)

@dp.message(CommandStart("help"))
async def help_handler(message: Message):
    await message.answer("Опис бота")

async def show_films(message: Message):
    records = get_records()
    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"record_{record_id}"),
         for record_id, name in records
        ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer("Оберить запис", reply_markup=reply_markup)

@dp.message(CommandStart("films"))
async def films_handler(message: Message):
    await show_films(message)

@dp.call_query(lambda c: c.data.startswith("record_"))
async def button_handler(callback: CallbackQuery):
    record_id = int(callback.data.replace("record_", ""))

    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT description, poster FROM films WHERE id = ?", (record_id,))
    film = cursor.fetchall()
    conn.close()

    desc, poster = film
    if "," in poster:
        poster = poster.split(",")[1]

    image_bytes = base64.b64decode(poster)
    await callback.message.reply_photo(
        photo=BufferedInputFile(image_bytes, filename="poster.jpg"),






import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import BOT_TOKEN

dp = Dispatcher()

movies = {
    "1": {
        "name": "Інтерстеллар",
        "info": "Науково-фантастичний фільм про подорож у космос.",
        "image": "interstellar.jpg"
    },
    "2": {
        "name": "Титанік",
        "info": "Історична драма про катастрофу корабля.",
        "image": "titanic.jpg"
    }
}

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"Привіт, {message.from_user.full_name}!\n"
        "Я бот для роботи з фільмами 🎬"
    )

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Доступні команди:\n\n"
        "/movies — список фільмів\n"
        "/add_movie Назва_Опис — додати фільм (через _)\n"
        "/help — список команд"
    )

@dp.message(Command("movies"))
async def movies_handler(message: Message):
    text = "Список фільмів:\n\n"
    for key, movie in movies.items():
        text += f"{key}. {movie['name']} — {movie['info']}\n"
    await message.answer(text)

@dp.message(Command("add_movie"))
async def add_movie_handler(message: Message):
    try:
        text = message.text.replace("/add_movie ", "")

        name, info = text.split("_")
        movie_id = str(len(movies) + 1)

        movies[movie_id] = {
            "name": name.strip(),
            "info": info.strip(),
            "image": "default.jpg"
        }

        await message.answer("Фільм додано 🎬")

    except ValueError:
        await message.answer("Неправильний формат!\nВикористай:\n/add_movie Назва_Опис")

@dp.message()
async def echo_handler(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())