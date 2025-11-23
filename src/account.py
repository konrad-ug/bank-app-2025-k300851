

class Account:
    def __init__(self, trasnfer_fee):
        self.balance = 0
        self.history = []
        self.trasnfer_fee = trasnfer_fee

    def transfer(self, amount, transfer_type):
        if amount < 0:
            return False

        match transfer_type:
            case "incoming":
                self.change_balance(amount)
                return True
            case "outgoing":
                if amount <= self.balance:
                    self.change_balance(-amount)
                    return True

        return False

    def change_balance(self, amount):
        self.balance += amount
        self.history.append(amount)
    
    def express_transfer(self, amount, ):
        if self.transfer(amount, "outgoing"):
            self.change_balance(self.trasnfer_fee)
