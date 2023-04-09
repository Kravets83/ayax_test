
class CheckQr:
    def __init__(self):
        self.color = None
        self.check_out = lambda exp, callback: callback if exp else lambda: None

    def check_in_db(self, qr):
        raise ConnectionError

    def check_len_color(self, qr):
        color = {
            3: 'Red',
            5: 'Green',
            7: 'Fuzzy Wuzzy'
        }
        self.color = color.get(len(qr))
        return self.color

    def scan_check_out_list(self, qr):
        return [
            (self.check_out(not self.check_len_color(qr), lambda:
                [self.send_error(f"Error: Wrong qr length {len(qr)}")]

                     )),
            (self.check_out(not self.check_in_db(qr), lambda:
                [self.send_error("Not in DB")]

                     ))
        ]

    def check_scanned_device(self, qr: str):
        for func in self.scan_check_out_list(qr):
            if func():
                return func()                                 # add func() too return
        message = f"hallelujah {qr}"
        return self.can_add_device(message)                   # add return
        # self.can_add_device(f"hallelujah {qr}")

    @staticmethod
    def can_add_device(message: str):
        return message

    @staticmethod
    def send_error(error: str):
        return error



class CheckQrFakeDB(CheckQr):
    def __init__(self):
        super().__init__()
        self.fake_db = ['123','12345','1234567']

    def check_in_db(self, qr):
        if qr in self.fake_db:
            return True
        else:
            return None


a = CheckQrFakeDB()

# print(a.check_in_db('123'))
# print(a.check_len_color('123'))
# l=((a.scan_check_out_list('11')))
# print(a.can_add_device(l[0]()))

print(a.check_scanned_device('123'))

