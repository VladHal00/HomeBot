from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

# Здесь создание кнопок меню и краткий гайд по ним
async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь по боту'
        ),
        BotCommand(
            command='values',
            description='Информация о всей доступной валюте'
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())