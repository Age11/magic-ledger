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


@given("creez o gestiune")
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
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


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
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru achizitie de marfa de la furnizor regim tva normal"
)
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


@given("adaug tratament contabil pentru descarcare din gestiunea de marfuri")
def step_impl(context):
    request_body = {
        "name": "Descărcare marfa din gestiune",
        "description": "Aceasta înregistrare contabila se refera la descărcarea din gestiune a unor mărfuri",
        "main_transaction": {
            "debit_account": "601",
            "credit_account": "371",
            "currency": "RON",
            "details": "Descărcarea din gestiune a unor mărfuri",
            "tx_type": "descărcare",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru înregistrarea chiriei")
def step_impl(context):
    request_body = {
        "name": "Înregistrare chirie",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea cheltuielilor cu chiria",
        "main_transaction": {
            "debit_account": "6123",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu chiria",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu chirie",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given("adaug tratament contabil pentru înregistrarea cheltuielilor cu apa")
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor cu apa",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea cheltuielilor cu apa",
        "main_transaction": {
            "debit_account": "6052",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu apa",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu apa",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given("adaug tratament contabil pentru înregistrarea cheltuielilor cu energia")
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor cu energia",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea cheltuielilor cu energia",
        "main_transaction": {
            "debit_account": "6053",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu energia",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu energia",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru înregistrarea cheltuielilor cu servicii poștale și cu telecomunicațiile"
)
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor poștale și cu telecomunicațiile",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea cheltuielilor poștale și cu telecomunicațiile",
        "main_transaction": {
            "debit_account": "626",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli poștale și cu telecomunicațiile",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli poștale și cu telecomunicațiile",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA normal"
)
def step_impl(context):
    request_body = {
        "name": "Achiziției de obiecte de inventar, regim TVA normal",
        "description": "Aceasta înregistrare contabila se referă la o achiziții de obiecte de inventar de la un furnizor cu regim TVA normal",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Achiziției de obiecte de inventar",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție obiecte de inventar",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA la încasare"
)
def step_impl(context):
    request_body = {
        "name": "Achiziției de obiecte de inventar, regim TVA încasare",
        "description": "Aceasta înregistrare contabila se referă la o achiziții de obiecte de inventar de la un furnizor cu regim TVA încasare",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Achiziției de obiecte de inventar",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4428",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție obiecte de inventar",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru achiziția de active corporale de la furnizor de imobilizări regim TVA normal"
)
def step_impl(context):
    request_body = {
        "name": "Achiziției de active corporale, regim TVA normal",
        "description": "Aceasta înregistrare contabila se referă la o achiziții de active corporale de la un furnizor cu regim TVA normal",
        "main_transaction": {
            "debit_account": "214",
            "credit_account": "404",
            "currency": "RON",
            "details": "Achiziției de active corporale",
            "tx_type": "intrări",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție active corporale",
                "tx_type": "intrări",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru înregistrarea achiziției de materiale consumabile"
)
def step_impl(context):
    request_body = {
        "name": "Înregistrare achiziției de materiale consumabile",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea achiziției de materiale "
        "consumabile",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare achiziției de materiale consumabile",
            "tx_type": "ieșiri",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție materiale consumabile",
                "tx_type": "TVA-vanzare",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru înregistrarea achiziției de materiale consumabile cu TVA la încasare"
)
def step_impl(context):
    request_body = {
        "name": "Înregistrare achiziției de materiale consumabile regim TVA la încasare",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea achiziției de materiale consumabile",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare achiziției de materiale consumabile",
            "tx_type": "ieșiri",
        },
        "followup_transactions": [
            {
                "debit_account": "4428",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA neexigibilă achiziție materiale consumabile",
                "tx_type": "TVA-vanzare",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru înregistrarea achiziției de imobilizări corporale"
)
def step_impl(context):
    request_body = {
        "name": "Înregistrare achiziției de imobilizări corporale",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea achiziției de imobilizări corporale",
        "main_transaction": {
            "debit_account": "214",
            "credit_account": "404",
            "currency": "RON",
            "details": "Înregistrare achiziției de imobilizări corporale",
            "tx_type": "ieșiri",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "404",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție materiale consumabile",
                "tx_type": "TVA-vanzare",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given("adaug tratament contabil pentru înregistrarea cheltuielilor cu uzura")
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor cu uzura",
        "description": "Aceasta înregistrare contabila se refera la înregistrarea cheltuielilor cu uzura",
        "main_transaction": {
            "debit_account": "603",
            "credit_account": "303",
            "currency": "RON",
            "details": "Înregistrare achiziției de imobilizări corporale",
            "tx_type": "ieșiri",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201
