from src.account import Account


class ComapnyAccount(Account):
    def __init__(self, name, nip):
        super().__init__(trasnfer_fee=-5)
        self.name = name
        if len(nip) != 10:
            nip = "Invalid"
        self.nip = nip
