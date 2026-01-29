from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from src.accounts_registry import AccountsRegistry
from src.repositories.mongo_accounts_repository import MongoAccountsRepository
import pytest


@pytest.fixture
def personal_account():
    return PersonalAccount("John", "Doe", "87060979383")


@pytest.fixture(autouse=True)
def mock_requests(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
    mocker.patch("src.company_account.requests.get", return_value=mock_response)


@pytest.fixture
def company_account(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": {"subject": {"statusVat": "Czynny"}}}
    mocker.patch("src.company_account.requests.get", return_value=mock_response)
    return CompanyAccount("Kemar", "5874589874")


@pytest.fixture
def accounts_registry_empty(mocker):
    mock_collection = mocker.Mock()
    mock_collection.find.return_value = []

    mock_mongo = mocker.MagicMock()
    mock_mongo.__getitem__.return_value = {"accounts": mock_collection}
    mocker.patch(
        "src.repositories.mongo_accounts_repository.pymongo.MongoClient",
        return_value=mock_mongo,
    )

    mongo = MongoAccountsRepository()
    return AccountsRegistry(mongo)


@pytest.fixture
def accounts_registry_filled(mocker):
    accounts = [
        PersonalAccount("John", "Doe", "87060979383"),
        PersonalAccount("Adam", "Smith", "88102073355"),
        PersonalAccount("Alan", "Adams", "01271638886"),
    ]
    mock_collection = mocker.Mock()
    mock_collection.find.return_value = [{**acc.to_dict(), "national_id": acc.national_id} for acc in accounts]

    mock_mongo = mocker.MagicMock()
    mock_mongo.__getitem__.return_value = {"accounts": mock_collection}
    mocker.patch(
        "src.repositories.mongo_accounts_repository.pymongo.MongoClient",
        return_value=mock_mongo,
    )

    mongo = MongoAccountsRepository()
    registry = AccountsRegistry(mongo)
    registry.accounts = accounts

    return registry
