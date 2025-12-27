from unittest.mock import mock_open, patch

import pytest

from src.read_files import read_csv, read_excel


def test_read_csv_basic() -> None:
    mock_data = "name,price\nApple,120\nBanana,90\n"
    expected = [{"name": "Apple", "price": "120"}, {"name": "Banana", "price": "90"}]

    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        result = read_csv("test.csv")
        mock_file.assert_called_once_with("test.csv", newline="", encoding="utf-8")
        assert result == expected


def test_read_csv_empty_file() -> None:
    with patch("builtins.open", mock_open(read_data="")):
        result = read_csv("test.csv")
        assert result == []


def test_read_csv_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_csv("nonexistent.csv")
