from aiogram import Bot
from aiogram.types import Message



async def get_start(message: Message, bot: Bot): # Приветствие (/start)
    await bot.send_message(message.from_user.id, f'Привет <b>{message.from_user.first_name}</b>. Рад тебя видеть! Чтоб узнать о боте, напиши /help')


async def get_help(message: Message, bot: Bot): # Помощь по боту(/help)
    await bot.send_message(message.from_user.id, f'Давай <b>{message.from_user.first_name}</b> расскажу немного о боте. Бот создается для домашнего пользования.\n'
                                                 f'В будущем появится возможность смотреть прогноз погоды, записывать планы на день/определенный день.\n'
                                                 f'Сейчас бот умеет конвертировать валюту, для этого нужно:\n'
                                                 f'1. Посмотреть список доступной валюты(/values)\n'
                                                 f'2. Из списка выбрать валюту из которой в которую хотим конвертировать\n'
                                                 f'Пример: рубль доллар 100, пишем с маленькой буквы в конце количество валюты.\n'
                                                 f'Так же Бот умеет сохранять фотографии, достаточно отправить фотографию, которую хотите сохранить.\n'
                                                 f'(на данный момент фотографии сохраняются в самом проекте')


async def get_photo(message: Message, bot: Bot): # функция для сохранения фотографий
    await message.answer(f'Картинку сохранил.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


