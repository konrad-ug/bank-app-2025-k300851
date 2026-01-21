from behave import *
import requests

URL = "http://localhost:5000"


@step('I send "{tranfer_type}" transfer to "{pesel}" with "{amount}" amount')
def send_transfer(context, tranfer_type, pesel, amount):
    data = {"amount": int(amount), "type": tranfer_type}
    response = requests.post(f"{URL}/api/accounts/{pesel}/transfer", json=data)
    context.response_code = response.status_code

@step("Transfer is accepted")
def transfer_accepted(context):
    assert context.response_code == 200


@step("Transfer is rejected")
def transfer_rejected(context):
    assert context.response_code != 200

