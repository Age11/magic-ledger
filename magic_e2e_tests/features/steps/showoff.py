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
    assert response.status_code == 201


@given("creez o entitate afiliata")
def step_impl(context):
    response = mg.create_affiliate_organization(context.table)
    assert response.status_code == 201


@given("adaug o imobilizare corporala")
def step_impl(context):
    response = mg.add_asset(context.table)
    assert response.status_code == 201


@given('adaug "{holding_type}" detinute la entitatea afiliata')
def step_impl(context, holding_type):
    response = mg.add_financial_holding(context.table, holding_type)
    assert response.status_code == 201


@given("actualizez rulaj valutar")
def step_impl(context):
    response = mg.add_liquidity_reserve(context.table)
    assert response.status_code == 201


@given('preiau balanta de verificare pentru luna "{month}"')
def step_impl(context, month):
    print(month)
    response = mg.get_initial_account_balance(context.table, month)
    assert response.status_code == 201


@given('inchid luna "{month}"')
def step_impl(context, month):
    print(month)
    response = mg.close_balance_for_month(month)
    assert response.status_code == 201


@given("inregistrez tranzactii")
def step_impl(context):
    response = mg.add_transaction(context.table)
    assert response.status_code == 201


@given("creez un inventar")
def step_impl(context):
    response = mg.create_inventory(context.table)
    assert response.status_code == 201


@given("adaug un articol")
def step_impl(context):
    response = mg.add_item(context.table)
    assert response.status_code == 201


@given("adaug un articol in inventar")
def step_impl(context):
    response = mg.add_inventory_item(context.table)
    assert response.status_code == 201


@given("adaug o factura")
def step_impl(context):
    response = mg.add_invoice(context.table)
    assert response.status_code == 201


@given("adaug un articol din factura in inventar")
def step_impl(context):
    response = mg.add_invoice_item(context.table)
    assert response.status_code == 201
