import os
from unittest.mock import Mock, patch

import pytest

from src.external_api import transfer_currency


def make_transaction(amount: str, code: str) -> dict:
    """функция для создания тестовой транзакции"""
    return {
        "operationAmount": {
            "amount": amount,
            "currency": {"code": code, "name": code},
        }
    }


@patch.dict(os.environ, {"API_KEY": "key", "API_URL": "https://qwery.com"})
def test_transfer_currency_rub() -> None:
    """тест валюта RUB, вернуть amount как float"""
    transaction = make_transaction("100.50", "RUB")
    result = transfer_currency(transaction)
    assert result == 100.50
    assert isinstance(result, float)


@patch("src.external_api.requests.get")
@patch.dict(os.environ, {"API_KEY": "key", "API_URL": "https://qwery.com"})
def test_transfer_currency_usd(mock_get: Mock) -> None:
    """тест валюта не RUB, вызвать API"""
    transaction = make_transaction("10", "USD")
    mock_response = Mock()
    mock_response.json.return_value = {"result": 750.5}
    mock_get.return_value = mock_response

    result = transfer_currency(transaction)
    assert result == 750.5
    mock_get.assert_called_once()

    args, kwargs = mock_get.call_args
    assert kwargs["params"] == {"from": "USD", "to": "RUB", "amount": 10.0}
