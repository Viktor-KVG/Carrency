import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Не удалось перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        url = f'https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}'

        payload = {}
        headers = {
            "apikey": "zOCZACafQoJvApTYIRgn2XKBvqsWsBW8"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

#        status_code = response.status_code
#        result = response.text

#        quote_ticker, base_ticker = keys[quote], keys[base]

#        r = requests.get(f'https://api.apilayer.com/currency_data/live?base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(response.content) #[keys[base]]

        return total_base

