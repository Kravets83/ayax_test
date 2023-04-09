from scanner_handler import CheckQr
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_db():
    with patch('scanner_handler.CheckQr.check_in_db') as mock_db:
        yield mock_db


def test_check_in_db_true(mock_db):
    mock_db.return_value = True
    assert CheckQr.check_in_db('123') == True


def test_check_in_db_none(mock_db):
    mock_db.return_value = None
    assert CheckQr.check_in_db('4564') == None


def test_check_color_min_len():
    min_len = CheckQr()
    assert min_len.check_len_color('') == None


# def test_check_color_number():
#     number = CheckQr()
#     assert number.check_len_color('1') == TypeError


def test_check_color_red():
    red = CheckQr()
    assert red.check_len_color('123') == 'Red'


def test_check_color_red_small_letter():
    red_small_letter = CheckQr()
    assert red_small_letter.check_len_color('qwe') == 'Red'


def test_check_color_red_big_letter():
    red_big_letter = CheckQr()
    assert red_big_letter.check_len_color('QWE') == 'Red'


def test_check_color_green():
    green = CheckQr()
    assert green.check_len_color('12345') == 'Green'


def test_check_color_Fuzzy_Wuzzy():
    fuzzy = CheckQr()
    assert fuzzy.check_len_color('1234567') == 'Fuzzy Wuzzy'
