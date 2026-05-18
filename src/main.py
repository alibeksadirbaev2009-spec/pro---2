import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await message.answer(f"Hello, {u.first_name}")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "/start - Botti iske tu'siriw\n"
        "/help - Ja'rdem\n" 
        "/contact - contact almasiw"
    )

@dp.message(Command("contact"))
async def get_contact(message: Message):
    await message.answer(f"Nomer:")
    await message.answer(f"At:")


@dp.message(F.text.lower() == "bye")
async def bye(message: Message):
    await message.answer(f"Saw aman bol")

@dp.message(F.text)
async def text(message: Message):
    text = message.text
    await message.answer("Text qabil qilinbaydi!")




async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main=main())