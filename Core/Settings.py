import requests
import json


#Хранение настроек с помощью Dataclass
from environs import Env
from dataclasses import dataclass


exchanges = {
    "рубль": "RUB",
    "евро": "EUR",
    "доллар": "USD",
    "тенге": "KZT",
    "лира": "TRY",
    "юань": "CNY",
    "вон": "KRW"
}


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str): #функция формирования настроек
    env = Env()
    env.read_env(path)
    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID"),
        )
    )


class APIException(Exception):
        pass


class Convertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно рассчитать одинаковые валюты')

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"""Не удалось обработать кол-во '{amount}'""")

        r = requests.get(f'https://v6.exchangerate-api.com/v6/df12dc7be69130a26958bdc3/latest/{exchanges[quote]}')
        data = json.loads(r.content)
        money = data['conversion_rates'][exchanges[base]] * float(amount)
        return money

settings = get_settings('secret') # считывание настроек с этого файла
print(settings)
