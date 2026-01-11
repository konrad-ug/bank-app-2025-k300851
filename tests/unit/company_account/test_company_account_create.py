from src.company_account import CompanyAccount
from tests.unit.fixtures import mock_requests
import pytest


class TestComapnyAccount:
    def test_account_create(self):
        account = CompanyAccount("Kemar", "5874589874")
        assert account.name == "Kemar"
        assert account.nip == "5874589874"

    @pytest.mark.parametrize("nip", ["587458987", "58745898748"])
    def test_account_create_invalid_nip(self, nip):
        account = CompanyAccount("Kemar", nip)
        assert account.nip == "Invalid"

    def test_account_create_not_registered(self, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 400
        mocker.patch("src.company_account.requests.get", return_value=mock_response)
    
        with pytest.raises(ValueError) as exception_info:
            account = CompanyAccount("Kemar", "5874589874")
        assert str(exception_info.value) == "Company not registered!!"

    def test_account_create_invalid_vat_status(self, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": {"subject": {"statusVat": None}}}
        mocker.patch("src.company_account.requests.get", return_value=mock_response)

        with pytest.raises(ValueError) as exception_info:
            account = CompanyAccount("Kemar", "5874589874")
        assert str(exception_info.value) == "Company not registered!!"
