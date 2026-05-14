import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, BufferedInputFile, KeyboardButton, ReplyKeyboardMarkup
from config import BOT_TOKEN

dp = Dispatcher()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'films.db')

def get_records():
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM films")
    records = cursor.fetchall()
    conn.close()
    return records

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
        "Я бот для роботи з фільмами "
    )


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Доступні команди:\n\n"
        "/movies — список фільмів\n"
        "/add_movie Назва | Опис — додати фільм\n"
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
    text = message.text.replace("/add_movie ", "")

    if "_" not in text:
        await message.answer("Формат:\n/add_movie Назва _ Опис")
        return

    name, info = text.split("_")
    movie_id = str(len(movies) + 1)

    movies[movie_id] = {
        "name": name.strip(),
        "info": info.strip(),
        "image": "default.jpg"
    }

    await message.answer("Фільм успішно додано 🎬")


@dp.message()
async def echo_handler(message: Message):
    await message.send_copy(chat_id=message.chat.id)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

@dp.message(Command("films"))
async def show_films(message: Message):
    records = get_records()

    @dp.message(Command("films"))
    async def show_films(message: Message):
        records = get_records()

        keyboard = [
            [InlineKeyboardButton(text=name, callback_data=f"record_{record_id}")]
            for record_id, name in records
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
        await message.answer("Оберіть фільм:", reply_markup=reply_markup)

    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer("оберить фильм: ", reply_markup=reply_markup)