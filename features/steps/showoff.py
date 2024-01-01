from behave import *
from helpers.magic_ledger_user import MagicLedgerUser

mg = MagicLedgerUser(base_url="http://127.0.0.1:5000")


@given("creez un proiect")
def step_impl(context):
    response = mg.create_project(context.table)
    assert response.status_code == 201

@given("creez un furnizor")
def step_impl(context):
    response = mg.create_supplier(context.table)
    assert response.status_code == 201

@given("creez un client")
def step_impl(context):
    response = mg.create_client(context.table)
    assert response.status_code == 201

@given("creez un client agent")
def step_impl(context):
    response = mg.create_client_agent(context.table)
    assert (response.status_code == 201)

@given("creez o entitate afiliata")
def step_impl(context):
    response = mg.create_affiliate_organization(context.table)
    assert response.status_code == 201