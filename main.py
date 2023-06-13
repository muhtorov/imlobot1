import logging

from aiogram import Bot, Dispatcher, executor, types
from testword import testword

API_TOKEN = '6165374248:AAH3HJQTNbdBYwkIvmnVH4ML7FuI_yzG6S4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom IMLO BOT ga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun biror bir so'z yuboring!")

@dp.message_handler()
async def testIMLO(message: types.Message):
    word = message.text
    result = testword(word)
    if result['available']:
        response = f"To'g'ri: {word.capitalize()}"
    else:
        response = f"Noto'g'ri:     {word.capitalize()}\n"
        for text in result['matches']:
            response += f"To'g'ri: {text.capitalize()}\n"
        await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)