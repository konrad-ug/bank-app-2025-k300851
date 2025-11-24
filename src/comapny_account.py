from src.account import Account


class ComapnyAccount(Account):
    def __init__(self, name, nip):
        super().__init__(trasnfer_fee=-5)
        self.name = name
        if len(nip) != 10:
            nip = "Invalid"
        self.nip = nip
 
    def take_loan(self, amount):
        if amount <= 0 or -1775 not in self.history or 2 * amount > self.balance:
            return False
        self.balance += amount
        return True

