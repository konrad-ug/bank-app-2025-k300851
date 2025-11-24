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
