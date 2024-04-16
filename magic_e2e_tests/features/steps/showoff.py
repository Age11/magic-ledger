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


@given('preiau balanta de verificare pentru "{date}"')
def step_impl(context, date):
    print(date)
    response = mg.create_initial_account_balance(context.table, date)
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


@given("adaug tratament contabil pentru plata salariilor")
def step_impl(context):
    request_body = {
        "name": "Plata salariu si taxe",
        "description": "Inregistrarea salariilor datorate si a taxelor aferente",
        "main_transaction": {
            "debit_account": "641",
            "credit_account": "421",
            "currency": "RON",
            "details": "Inregistrare cheltuieli cu salariile",
            "tx_type": "salarii",
        },
        "followup_transactions": [
            {
                "debit_account": "421",
                "credit_account": "431",
                "operation": "*25/100",
                "details": "Contributie asigurari sociale - CAS",
                "tx_type": "salarii",
            },
            {
                "debit_account": "421",
                "credit_account": "437",
                "operation": "*10/100",
                "details": "Contribuții de asigurări sociale de sănătate - CASS",
                "tx_type": "salarii",
            },
            {
                "debit_account": "421",
                "credit_account": "444",
                "operation": "*65/100*10/100",
                "details": "Impozit pe venit",
                "tx_type": "salarii",
            },
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201

    @given("adaug tratament contabil pentru achizitie de la furnizor regim tva normal")
    def step_impl(context):
        request_body = {
            "name": "Achiziție de mărfuri de la furnizor regim tva normal",
            "description": "Aceasta inregistrare contabila se refera la achizitia de marfuri de la un furnizor care aplica regimul de tva normal",
            "main_transaction": {
                "debit_account": "371",
                "credit_account": "401",
                "currency": "RON",
                "details": "Inregistrare achizitie marfuri",
                "tx_type": "intrări",
            },
            "followup_transactions": [
                {
                    "debit_account": "4426",
                    "credit_account": "401",
                    "operation": "*19/100",
                    "details": "Inregistrare TVA",
                    "tx_type": "TVA-încasare",
                }
            ],
        }
        response = mg.add_accounting_treatment(request_body)
        assert response.status_code == 201

    @given("adaug tratament contabil pentru achizitie cu tva normal si discount 10%")
    def step_impl(context):
        request_body = {
            "name": "Achizitie marfuri cu TVA in regim  normal  si discount 10%",
            "description": "Achizitie marfuri cu TVA in regim  normal 19%  si plata din cont ",
            "main_transaction": {
                "debit_account": "371",
                "credit_account": "401",
                "currency": "RON",
                "details": "Achizitie marfa",
                "tx_type": "intrări",
            },
            "followup_transactions": [
                {
                    "debit_account": "4426",
                    "credit_account": "401",
                    "operation": "*19/100",
                    "details": "plata tva",
                    "tx_type": "TVA-încasare",
                },
                {
                    "debit_account": "371",
                    "credit_account": "401",
                    "operation": "*10/100*-1",
                    "details": "discount",
                    "tx_type": "intrări",
                },
                {
                    "debit_account": "4426",
                    "credit_account": "401",
                    "operation": "*10/100*19/100*-1",
                    "details": "tva discount",
                    "tx_type": "intrări",
                },
            ],
        }

    @given("adaug tratament contabil pentru vanzare catre client regim tva normal")
    def step_impl(context):
        request_body = {
            "name": "Vanzare de marfuri catre client regim tva normal",
            "description": "Aceasta inregistrare contabila se refera la vanzarea de marfuri catre un client care aplica regimul de tva normal",
            "main_transaction": {
                "debit_account": "4111",
                "credit_account": "707",
                "currency": "RON",
                "details": "Înregistrare venituri din vanzari",
                "tx_type": "ieșiri",
            },
            "followup_transactions": [
                {
                    "debit_account": "4111",
                    "credit_account": "4427",
                    "operation": "*19/100",
                    "details": "Inregistrare TVA",
                    "tx_type": "TVA-vanzare",
                },
                {
                    "debit_account": "607",
                    "credit_account": "371",
                    "operation": "*1",
                    "details": "Descarcare din gestiune",
                    "tx_type": "ieșiri",
                },
            ],
        }
        response = mg.add_accounting_treatment(request_body)
        assert response.status_code == 201

    @given("adaug tratament contabil pentru incasare in cont de la client")
    def step_impl(context):
        request_body = {
            "name": "Încasare în cont de la client",
            "description": "Aceasta inregistrare contabila se refera la incasarea in cont de la un client",
            "main_transaction": {
                "debit_account": "5121",
                "credit_account": "4111",
                "currency": "RON",
                "details": "Încasare în cont de la client",
                "tx_type": "bancă",
            },
            "followup_transactions": [],
        }
        response = mg.add_accounting_treatment(request_body)
        assert response.status_code == 201

    @given("adaug tratament contabil pentru incasare in casa de la client")
    def step_impl(context):
        request_body = {
            "name": "Încasare în casă de la client",
            "description": "Aceasta inregistrare contabila se refera la casa in cont de la un client",
            "main_transaction": {
                "debit_account": "5311",
                "credit_account": "4111",
                "currency": "RON",
                "details": "Încasare în casa de la client",
                "tx_type": "casă",
            },
            "followup_transactions": [],
        }
        response = mg.add_accounting_treatment(request_body)
        assert response.status_code == 201

    @given("adaug tratament contabil pentru plata furnizor din cont")
    def step_impl(context):
        request_body = {
            "name": "Plată furnizor din cont",
            "description": "Aceasta inregistrare contabila se refera la plata din cont a unui furnizor",
            "main_transaction": {
                "debit_account": "401",
                "credit_account": "5121",
                "currency": "RON",
                "details": "Încasare în casa de la client",
                "tx_type": "bancă",
            },
            "followup_transactions": [],
        }
        response = mg.add_accounting_treatment(request_body)
        assert response.status_code == 201

        @given("adaug tratament contabil pentru plata furnizor din casă")
        def step_impl(context):
            request_body = {
                "name": "Plata furnizor din casă",
                "description": "Aceasta inregistrare contabila se refera la plata din casa a unui furnizor",
                "main_transaction": {
                    "debit_account": "401",
                    "credit_account": "5311",
                    "currency": "RON",
                    "details": "Încasare în casa de la client",
                    "tx_type": "casă",
                },
                "followup_transactions": [],
            }
            response = mg.add_accounting_treatment(request_body)
            assert response.status_code == 201
