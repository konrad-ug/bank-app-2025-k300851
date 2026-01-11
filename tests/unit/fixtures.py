from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from src.accounts_registry import AccountsRegistry
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
