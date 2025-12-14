import os

import requests
from dotenv import load_dotenv


def transfer_currency(transaction: dict) -> float:
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")

    if not api_url:
        raise ValueError("API_URL не определен!")
    if not api_key:
        raise ValueError("API_KEY не определен")

    operation = transaction["operationAmount"]
    amount = float(operation["amount"])
    currency = operation["currency"]

    if currency["code"] != "RUB":
        params = {"from": currency["code"], "to": "RUB", "amount": amount}
        headers = {
            "apikey": api_key,
        }
        response = requests.get(api_url, params=params, headers=headers)
        return round(float(response.json()["result"]), 2)
    else:
        return float(amount)
