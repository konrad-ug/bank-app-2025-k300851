from src.personal_account import PersonalAccount

class AccountsRegistry:
    def __init__(self):
        self.accounts: list[PersonalAccount] = []

    def add_account(self, account: PersonalAccount):
        if isinstance(account, PersonalAccount) and self.get_by_national_id(account.national_id) is None:
            self.accounts.append(account)
    
    def get_by_national_id(self, national_id: str) -> PersonalAccount | None:
        for account in self.accounts:
            if account.national_id == national_id:
                return account

    def get_all(self) -> list[PersonalAccount]:
        return self.accounts

    def count(self) -> int:
        return len(self.accounts)
    
    def delete(self, national_id: str):
        acc = self.get_by_national_id(national_id)
        if acc:
            self.accounts.remove(acc)
            return True
        return False
    
    def update(self, national_id: str, params: dict[str, str]):
        acc = self.get_by_national_id(national_id)
        if not acc:
            return False
        if "name" in params:
            acc.first_name = params["name"]
        if "surname" in params:
            acc.last_name = params["surname"]
        if "pesel" in params:
            acc.national_id = params["pesel"]
        return True
    
