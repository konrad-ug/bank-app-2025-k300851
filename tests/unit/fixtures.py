from src.personal_account import PersonalAccount
from src.comapny_account import ComapnyAccount
from src.accounts_registry import AccountsRegistry
import pytest


@pytest.fixture
def personal_account():
    return PersonalAccount("John", "Doe", "87060979383")


@pytest.fixture
def company_account():
    return ComapnyAccount("Kemar", "587458965")


@pytest.fixture
def accounts_registry_empty():
    return AccountsRegistry()


@pytest.fixture
def accounts_registry_filled():
    registry = AccountsRegistry()
    registry.accounts = [
        PersonalAccount("John", "Doe", "87060979383"),
        PersonalAccount("Adam", "Smith", "88102073355"),
        PersonalAccount("Alan", "Adams", "01271638886")
    ]
    return registry
