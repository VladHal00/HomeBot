from aiogram import Bot, types
from Core.Settings import APIException, Convertor, exchanges


async def get_values(message: types.Message): # Доступная валюта(/values)
    text = "Доступные валюты:"
    for key in exchanges.keys():
        text = '\n'.join((text, key))
    await message.answer(text)


async def get_converter(message: types.Message, bot: Bot): # функция конвертации валюты
    try:
        value = message.text.split()
        if len(value) != 3:
            raise APIException('Слишком много параметров')
        quote, base, amount = value
        total_base = Convertor.get_price(quote, base, amount)
    except APIException as e:
        await message.answer(f'Ошибка пользователя.\n{e}')
    except Exception as e:
        await bot.send_message(message.chat.id, f"Не удалось обработать команду\n{e}")
    else:
        text = f'Цена {amount} {quote} в {base} равна: {total_base}'
        await bot.send_message(message.chat.id, text)