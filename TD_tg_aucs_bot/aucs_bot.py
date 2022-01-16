import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from aiogram.types import ParseMode
import aiogram.utils.markdown as ftm
from main import get_aucs


token = "5080462203:AAFf8IFiEkwr-YyywlRMHSirdJ6S6-3k5B0"
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Текущие аукционы"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Получаем текущие аукционы!", reply_markup=keyboard)


@dp.message_handler(Text(equals="Текущие аукционы"))
async def get_cur_aucs(message: types.Message):
    await message.answer("Please wait...")

    get_aucs()

    with open("aucs.json", encoding='utf-8') as file:
        result = json.load(file)

        # card = []
    for item in result:
        card = f"{hlink(item.get('Lot'), item.get('Image_url'))}\n" \
               f"{hbold('Локация: ')} {item.get('Shipping')}\n" \
               f"{hbold('Цена: ')} {item.get('Price')}\n" \
               f"{hbold('Условия доставки: ')} {item.get('Shipping_info')}"

        await message.answer(card, parse_mode='MARKDOWN')


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
