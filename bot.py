import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# настройка логгирования
logging.basicConfig(level=logging.INFO)

# создание экземпляра бота
bot = Bot(token='6284083728:AAFV3wDx9Y8RTg2MBdw6bn4MKMQwe5OfawU')
dp = Dispatcher(bot)

# хендлер для команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Отправляет приветственное сообщение и помощь по использованию бота
    """
    text = md.text(
        md.hbold("Привет, я бот Капитан-Бенгард!"), "\n\n",
        "Я могу помочь тебе в разных вещах. Вот список доступных команд:\n",
        "/help - получить помощь\n",
        "/about - узнать информацию обо мне\n",
        "/echo - повторить ваше сообщение\n",
        "/photo - Фото"
    )
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

# хендлер для команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    Отправляет список доступных команд
    """
    text = md.text(
        "Вот список доступных команд:\n",
        "/help - получить помощь\n",
        "/about - узнать информацию обо мне\n",
        "/echo - повторить ваше сообщение\n",
        "/photo - Фото"
    )
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

# хендлер для команды /about
@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    """
    Отправляет информацию о боте
    """
    text = "Я бот, Капитан-Бенгард"
    await message.reply(text)

# хендлер для команды /echo
@dp.message_handler(commands=['echo'])
async def echo_message(message: types.Message):
    """
    Повторяет сообщение пользователя
    """
    await message.reply(message.text)

# хендлер для команды /photo
@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    """
    Отправляет фотографию пользователю
    """
    # Открытие файла изображения
    with open('./img/foto1.jpg', 'rb') as photo:
        # Отправка фотографии в сообщении
        await message.answer_photo(photo, caption='Очень охрененная инфа "CЮДА НА..!"')

        text = "Капитан-Бенгард Представляет!"
        await message.reply(text)

# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)