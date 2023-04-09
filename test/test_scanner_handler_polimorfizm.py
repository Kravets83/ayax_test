import pytest
from scanner_handler import CheckQr

red = "123"
green = "12345"
fuzzy = "1234567"


class CheckQrFakeDB(CheckQr):
    def __init__(self):
        super().__init__()
        self.fake_db = [red, green, fuzzy, '1234']

    def check_in_db(self, qr):
        if qr in self.fake_db:
            return True
        else:
            return None


def test_conect_db():
    checker = CheckQrFakeDB()
    assert checker.check_in_db('') == None
    assert checker.check_in_db(red) == True


def test_check_len_color():
    checker = CheckQrFakeDB()
    # assert checker.check_len_color() == None  # qr - empty (додати значення за умовченням або виключення)
    assert checker.check_len_color("") == None  # qr - empty str
    assert checker.check_len_color(red) == "Red"  # qr len str = 3 == color = red
    assert checker.check_len_color(green) == "Green"  # qr len str = 5 == color = green
    assert checker.check_len_color(fuzzy) == "Fuzzy Wuzzy"  # qr len str = 7 == color = fuzzy wuzzy
    assert checker.check_len_color("qqqqqqQ") == "Fuzzy Wuzzy"  # qr len str = 7 == color = fuzzy wuzzy
    assert checker.check_len_color("jbdvbrkbkebrv rjbjkrbvjkbe") == None  # qr long str


def test_scan_check_out_list():
    checker = CheckQrFakeDB()
    # create list
    assert len(checker.scan_check_out_list("")) == 2


def test_check_scanned_device():
    checker = CheckQrFakeDB()
    # qr non correct length
    assert checker.check_scanned_device("123456") == ["Error: Wrong qr length 6"]
    # qr not in base
    assert checker.check_scanned_device("12346") == ["Not in DB"]
    # qr in base
    assert checker.check_scanned_device(red) == "hallelujah 123"


def test_staticmethod():
    checker = CheckQrFakeDB()
    # check printing
    assert checker.send_error('error!!!!') == 'error!!!!'
    # check printing
    assert checker.can_add_device('devise in base') == 'devise in base'
