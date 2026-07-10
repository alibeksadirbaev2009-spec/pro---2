import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .config import settings

bot = Bot(settings.COW)
dp = Dispatcher()
# start comandasi
@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await message.answer(f"Sa'lem, {u.first_name}")

# bul bot iske qosilganda info aliw yamasa isletillgen de
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":  
    asyncio.run(main=main())
