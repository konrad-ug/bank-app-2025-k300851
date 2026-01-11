from tests.unit.fixtures import personal_account, company_account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from datetime import datetime
import pytest


class TestSendEmail:
    email_address = "test@test.pl"

    @pytest.mark.parametrize("result", [True, False])
    def test_send_email_personal_account(self, personal_account: PersonalAccount, mocker, result):
        mock_send = mocker.patch("src.personal_account.SMTPClient.send", return_value=result)
        personal_account.history = [100, -50, 10]
        assert personal_account.send_history_via_email(self.email_address) == result
        self.asset_send_email(mock_send, personal_account.history, "Personal")
    
    @pytest.mark.parametrize("result", [True, False])
    def test_send_email_company_account(self, company_account: CompanyAccount, mocker, result):
        mock_send = mocker.patch("src.company_account.SMTPClient.send", return_value=result)
        company_account.history = [100, -50, 10]
        assert company_account.send_history_via_email(self.email_address) == result
        self.asset_send_email(mock_send, company_account.history, "Company")

    def asset_send_email(self, mock_send, history, account_type_text):
        mock_send.assert_called_once()
        subject = mock_send.call_args[1]["subject"]
        text = mock_send.call_args[1]["text"]
        email_address = mock_send.call_args[1]["email_address"]
        assert subject == "Account Transfer History " + datetime.now().strftime("%Y-%m-%d")
        assert text == f"{account_type_text} account history: {history}"
        assert email_address == self.email_address

