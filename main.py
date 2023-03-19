import asyncio # ассинхрон
import logging # для информативности

#Весь каркас
from aiogram import Bot, Dispatcher
from Core.Handlers.Basic import get_start, get_photo, get_help # импорт функции приветствия, сохранение фото, команды /help, /start
from Core.API.Currency_parsing import get_values, get_converter # информация о парсинге валюты, информация о доступной валюте /values
from Core.Settings import settings # настройка бота(Токен, id админа, API и т.д)
from aiogram.filters import Command #назначение команды
from aiogram import F # press F(F=объект message)
from Core.Utils.Commands import set_commands


async def start_bot(bot: Bot): # Функция, чтоб знать, когда бот запущен
    await set_commands(bot) # добавление кнопки меню
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot): # Функция, чтоб знать, когда бот остановлен
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start(): # запуск бота ассинхрона

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')


    dp = Dispatcher() # объект апдейтов, регистрация
    dp.startup.register(start_bot) # регистрация отправки уведомления админу бота о запуске его
    dp.shutdown.register(stop_bot) # регистрация отправки уведомления админу бота об остановки его
    dp.message.register(get_photo, F.photo) # сохранение фото в проекте(временное размещение)
    dp.message.register(get_values, Command(commands=['values'])) # регистрация команды о всей валюте /values
    dp.message.register(get_help, Command(commands=['help'])) # регистрация команды для помощи /help
    dp.message.register(get_start, Command(commands=['start', 'run'])) # регистрация приветственной команды /start
    dp.message.register(get_converter)  # регистрация команды о конвертации /convert
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close() # закрывает сессию бота


if __name__ == "__main__":
    asyncio.run(start())