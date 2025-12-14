from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json_success() -> None:
    """тест с корректными данными"""

    mock_data = '[{"id": 1}, {"id": 2}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("file.json")
        assert result == [{"id": 1}, {"id": 2}]


def test_read_json_invalid_json() -> None:
    """тест с некорректной json строкой"""

    mock_data = "json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("file.json")
        assert result == []


def test_read_json_file_not_found() -> None:
    """тест с ненайденным файлом"""

    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json("fake_file.json")
        assert result == []


def test_read_json_not_list() -> None:
    """JSON не список"""

    mock_data = '{"id": 1}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("fake_file.json")
        assert result == []
