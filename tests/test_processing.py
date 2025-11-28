import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(sample_data: list) -> None:
    result = filter_by_state(sample_data, state="EXECUTED")
    assert [item["id"] for item in result] == [41428829, 939719570]


def test_filter_canceled(sample_data: list) -> None:
    result = filter_by_state(sample_data, state="CANCELED")
    assert [item["id"] for item in result] == [594226727, 615064591]


def test_sort_by_date(sample_data: list) -> None:
    result = sort_by_date(sample_data, sort=True)
    assert [item["id"] for item in result] == [41428829, 615064591, 594226727, 939719570]


def test_sort_ascending(sample_data: list) -> None:
    result = sort_by_date(sample_data, sort=False)
    assert [item["id"] for item in result] == [939719570, 594226727, 615064591, 41428829]
