from pathlib import Path
from typing import Any
from unittest.mock import mock_open, patch

with patch("builtins.open", mock_open()):
    from src.decorators import log
    from src.masks import get_mask_card_number

import pytest


def test_log_print_success(capsys: Any) -> None:

    decorated = log()(get_mask_card_number)
    result = decorated("1234567812345678")

    captured = capsys.readouterr()

    assert result == "1234 56** **** 5678"
    assert "Функция get_mask_card_number выполнена 'Успешно'!" in captured.out

    assert "Передаваемые данные в функцию get_mask_card_number: ('1234567812345678',), {}" in captured.out


def test_log_print_error(capsys: Any) -> None:
    decorated = log()(get_mask_card_number)
    with pytest.raises(ValueError):
        decorated("1234abcd12345678")

    captured = capsys.readouterr()

    assert "Ошибка выполнения функции! Ошибка: В номере карты должны быть только цифры!" in captured.out


def test_log_file(tmp_path: Path) -> None:
    log_file = tmp_path / "log.txt"

    decorated = log(str(log_file))(get_mask_card_number)
    decorated("1234567812345678")

    content = log_file.read_text(encoding="utf-8")
    assert "Функция get_mask_card_number выполнена 'Успешно'!" in content
    assert "Передаваемые данные в функцию get_mask_card_number: ('1234567812345678',), {}" in content
