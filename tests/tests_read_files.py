from unittest.mock import MagicMock, mock_open, patch

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


def test_read_excel_basic() -> None:
    # Создаём мок DataFrame с методом to_dict
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"name": "Apple", "price": 120}, {"name": "Banana", "price": 90}]

    with patch("pandas.read_excel", return_value=mock_df) as mock_read_excel:
        result = read_excel("dummy.xlsx")
        mock_read_excel.assert_called_once_with("test.xlsx", sheet_name=0)
        assert result == [{"name": "Apple", "price": 120}, {"name": "Banana", "price": 90}]


def test_read_excel_custom_sheet() -> None:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"col1": 1, "col2": 2}]

    with patch("pandas.read_excel", return_value=mock_df) as mock_read_excel:
        result = read_excel("test.xlsx", sheet_name=0)
        mock_read_excel.assert_called_once_with("test.xlsx", sheet_name="0")
        assert result == [{"col1": 1, "col2": 2}]


def test_read_excel_empty() -> None:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = []

    with patch("pandas.read_excel", return_value=mock_df):
        result = read_excel("test.xlsx")
        assert result == []


def test_read_excel_file_not_found() -> None:
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_excel("nonexistent.xlsx")
