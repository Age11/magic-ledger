from behave import *
from helpers.magic_ledger_user import MagicLedgerUser

mg = MagicLedgerUser(base_url="http://127.0.0.1:5000")


@given("creez un proiect nou")
def step_impl(context):
    response = mg.create_project(context.table)
    assert response.status_code == 201
