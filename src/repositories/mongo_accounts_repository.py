from src.repositories.accounts_repository import AccountsRepository
from src.personal_account import PersonalAccount
import pymongo


class MongoAccountsRepository(AccountsRepository):
    def __init__(self, url="", database_name="local"):
        self.client = pymongo.MongoClient(url)
        self.db = self.client[database_name]
        self.accounts = self.db["accounts"]

    def save_all(self, data: list['PersonalAccount']):
        self.accounts.delete_many({})
        print(data)
        for account in data:
            self.accounts.update_one(
                {"national_id": account.national_id},
                {"$set": account.to_dict()},
                upsert=True,
            )

    def load_all(self) -> list['PersonalAccount']:
        data = self.accounts.find()
        result = []
        for account in data:
            personal = PersonalAccount(account["first_name"], account["last_name"], account["national_id"])
            personal.balance = account["balance"]
            personal.history = account["history"]
            result.append(personal)
        return result
