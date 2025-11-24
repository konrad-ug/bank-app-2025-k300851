from src.personal_account import PersonalAccount
from src.comapny_account import ComapnyAccount
import pytest


@pytest.fixture
def personal_account():
    return PersonalAccount("John", "Doe", "87060979383")


@pytest.fixture
def company_account():
    return ComapnyAccount("Kemar", "587458965")
