import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ( 
    Message, 
    KeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    WebAppInfo,
    CallbackQuery
    )
from .config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()
# start comandasi
@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await message.answer(f"Sa'lem, {u.first_name}")

# help comandasi
@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "/start - Botti iske tu'siriw\n"
        "/help - Ja'rdem\n" 
        "/contact - contact almasiw"
    )

@dp.message(Command("contact"))
async def contact(message:Message):
    k = [
        [
            KeyboardButton(text="Send  contact", request_contact=True)
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer("Bul contact!", reply_markup=mark)

@dp.message(F.contact)
async def get_contact(message: Message):
    await message.answer("get contact!")


# Reply keyboard
@dp.message(Command("keyboard"))
async def keyboard(message: Message):
    k = [
        [
            KeyboardButton(text="🔎Anime izlew")
        ],
        [
            KeyboardButton(text="📚Qollanba"),
            KeyboardButton(text="💵Reklama ha'm hamiyliq")
        ],
        [
            KeyboardButton(text="💎Vip satip aliw"),
            KeyboardButton(text="👤 Profile")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer("Bul keyboard", reply_markup=mark)
# remove komomandasi
@dp.message(Command("removekb"))
async def remove_keyboard(message: Message):
    rm_mark = ReplyKeyboardRemove()
    await message.answer("Bul knopka joq qiladi !", reply_markup=rm_mark)


# Inline Keyboard
@dp.message(Command("inline"))
async def inline_keyboard(message: Message):
    # link = WebAppInfo(url="https://www.google.com")
    btns = [
        [
            InlineKeyboardButton(text="Buttom1", callback_data="1")
        ], 
        [
            InlineKeyboardButton(text="Buttom2", callback_data="2")
        ],
        [
            InlineKeyboardButton(text="Buttom3", callback_data="3")
        ]
    ]
    mark = InlineKeyboardMarkup(inline_keyboard=btns)
    await message.answer("Bul inline keyboard!", reply_markup=mark)

@dp.callback_query(F.data)
async def calback(call: CallbackQuery):
    data = call.data
    await call.message.delete()
    await call.message.answer(f"Buttom: {data}")
# # contact comandasi
# @dp.message(Command("contact"))
# async def get_contact(message: Message):
#     await message.answer(f"Nomer:")
#     await message.answer(f"At:")

# text = bye bul by sozinn uslap aladi
@dp.message(F.text.lower() == "bye")
async def bye(message: Message):
    await message.answer(f"Saw aman bol")

# bul ha'mme textlerdi uslap aladi
@dp.message(F.text)
async def text(message: Message):
    text = message.text
    await message.answer("Text qabil qilinbaydi!")



# bul bot iske qosilganda info aliw yamasa isletillgen de
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":  
    asyncio.run(main=main())


# start basqan waqitta knopka shigariw 4 ten az bolmawi kk 
# inline knopka jaratiw 4 qalegen qatar ga inline knopka bir na'rse islewi sha'rt emes 

