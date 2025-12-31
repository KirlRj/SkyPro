import os

import requests
from dotenv import load_dotenv


def transfer_currency(transaction: dict) -> float:
    """функция выводит сумму операции. если валюта не RUB, то обращается к API"""
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")

    if not api_url:
        raise ValueError("API_URL не определен!")
    if not api_key:
        raise ValueError("API_KEY не определен")

    operation = transaction.get("operationAmount")
    if operation:
        amount = float(operation.get("amount", 0))
        currency_code = operation.get("currency", {}).get("code", "RUB")
    else:
        amount = float(transaction.get("amount", 0))
        currency_code = transaction.get("currency_code", "RUB")

    if currency_code != "RUB":
        params = {"from": currency_code, "to": "RUB", "amount": amount}
        headers = {
            "apikey": api_key,
        }
        response = requests.get(api_url, params=params, headers=headers)

        return round(float(response.json().get("result",0)), 2)
    else:
        return float(amount)
