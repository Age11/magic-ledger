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


@given("înregistrez un articol din factură")
def step_impl(context):
    response = mg.add_invoice_item_no_inventory(context.table)
    assert response.status_code == 201


@given("creez tranzacții din șablon")
def step_impl(context):
    response = mg.make_transaction_from_template(context.table)
    assert response.status_code == 201


@given("scad stocul de mărfuri")
def step_impl(context):
    response = mg.decrease_stock(context.table)
    assert response.status_code == 204


@given("creez o plată")
def step_impl(context):
    resp = mg.create_payment(context.table)
    assert resp.status_code == 201


@given("rezolv plata")
def step_impl(context):
    response = mg.solve_payment(context.table)
    assert response.status_code == 204


# INTRĂRI


@given("adaug tratament contabil pentru înregistrarea chiriei")
def step_impl(context):
    request_body = {
        "name": "Înregistrare chirie",
        "description": "Înregistrarea cheltuielilor cu chiria de la furnizor cu regim TVA Normal",
        "main_transaction": {
            "debit_account": "6123",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu chiria",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu chirie",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given("adaug tratament contabil pentru înregistrarea cheltuielilor cu apa")
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor cu apa",
        "description": "Înregistrarea cheltuielilor cu apa de la furnizor TVA în regim normal",
        "main_transaction": {
            "debit_account": "6052",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu apa",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu apa",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given("adaug tratament contabil pentru înregistrarea cheltuielilor cu energia")
def step_impl(context):
    request_body = {
        "name": "Înregistrare cheltuielilor cu energia",
        "description": "Înregistrarea cheltuielilor cu energia de la furnizor cu în TVA regim normal",
        "main_transaction": {
            "debit_account": "6051",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu energia",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli cu energia",
                "tx_type": "intrări",
                "document_type": "factură",
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
        "description": "Înregistrarea cheltuielilor cu telecomunicațiile de la furnizor cu regim TVA normal",
        "main_transaction": {
            "debit_account": "626",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare cheltuieli poștale și cu telecomunicațiile",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA cheltuieli poștale și cu telecomunicațiile",
                "tx_type": "intrări",
                "document_type": "factură",
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
        "description": "Achiziție de obiecte de inventar de la un furnizor cu regim TVA normal",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Achiziției de obiecte de inventar",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție obiecte de inventar",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA normal și dare în folosință"
)
def step_impl(context):
    request_body = {
        "name": "Achiziției de obiecte de inventar, regim TVA încasare",
        "description": "Achiziții de obiecte de inventar de la un furnizor cu regim TVA normal și dare în folosință",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Achiziției de obiecte de inventar",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție obiecte de inventar",
                "tx_type": "intrări",
                "document_type": "factură",
            },
            {
                "debit_account": "603",
                "credit_account": "303",
                "operation": "*1",
                "details": "Înregistrare dare în folosință obiecte de inventar",
                "tx_type": "intrări",
                "document_type": "proces-verbal",
            },
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA la încasare și dare în folosință"
)
def step_impl(context):
    request_body = {
        "name": "Achiziției de obiecte de inventar, regim TVA încasare, dare în folosință",
        "description": "Achiziții de obiecte de inventar de la un furnizor cu regim TVA încasare",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Achiziției de obiecte de inventar",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4428",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție obiecte de inventar",
                "tx_type": "intrări",
                "document_type": "factură",
            },
            {
                "debit_account": "603",
                "credit_account": "303",
                "operation": "*1",
                "details": "Înregistrare dare în folosință obiecte de inventar",
                "tx_type": "intrări",
                "document_type": "proces-verbal",
            },
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
        "description": "Achiziții de active corporale de la un furnizor cu regim TVA normal",
        "main_transaction": {
            "debit_account": "214",
            "credit_account": "404",
            "currency": "RON",
            "details": "Achiziției de active corporale",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "404",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție active corporale",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru înregistrarea achiziției de materiale consumabile, regim TVA normal"
)
def step_impl(context):
    request_body = {
        "name": "Înregistrare achiziției de materiale consumabile, regim TVA normal",
        "description": "Înregistrarea achiziției de materiale consumabile regim TVA normal ",
        "main_transaction": {
            "debit_account": "303",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare achiziției de materiale consumabile",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție materiale consumabile",
                "tx_type": "intrări",
                "document_type": "factură",
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
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4428",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA neexigibilă achiziție materiale consumabile",
                "tx_type": "intrări",
                "document_type": "factură",
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
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "404",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție materiale consumabile",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    resp = mg.add_accounting_treatment(request_body)
    assert resp.status_code == 201


@given(
    "adaug tratament contabil pentru achiziție de marfă de la furnizor regim tva normal"
)
def step_impl(context):
    request_body = {
        "name": "Achiziție de mărfuri de la furnizor regim tva normal",
        "description": "Achiziții de mărfuri de la un furnizor, regimul de tva normal",
        "main_transaction": {
            "debit_account": "371",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare achiziție marfă",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru achiziție de servicii de la furnizor regim tva la încasare"
)
def step_impl(context):
    request_body = {
        "name": "Achiziție de servicii, regim tva normal",
        "description": "Achiziții de servicii de la un furnizor, regim TVA normal",
        "main_transaction": {
            "debit_account": "628",
            "credit_account": "401",
            "currency": "RON",
            "details": "Înregistrare achiziție servicii",
            "tx_type": "intrări",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4428",
                "credit_account": "401",
                "operation": "*19/100",
                "details": "Înregistrare TVA achiziție servicii",
                "tx_type": "intrări",
                "document_type": "factură",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


# IEȘIRI


@given("adaug tratament contabil pentru vânzare către client regim tva normal")
def step_impl(context):
    request_body = {
        "name": "Vânzare de mărfuri, regim tva normal",
        "description": "Vânzarea de mărfuri către un client care aplica regimul de tva normal",
        "main_transaction": {
            "debit_account": "4111",
            "credit_account": "707",
            "currency": "RON",
            "details": "Înregistrare venituri din vânzări",
            "tx_type": "ieșiri",
            "document_type": "factură",
        },
        "followup_transactions": [
            {
                "debit_account": "4111",
                "credit_account": "4427",
                "operation": "*19/100",
                "details": "Înregistrare TVA vânzare marfă",
                "tx_type": "ieșiri",
                "document_type": "factură",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru vânzare către client regim tva normal cu încasare directă"
)
def step_impl(context):
    request_body = {
        "name": "Vânzare de mărfuri cu încasare directă în cont, regim tva normal",
        "description": "Vânzarea de mărfuri către un client care aplica regimul de tva normal și încasare directă",
        "main_transaction": {
            "debit_account": "5121",
            "credit_account": "707",
            "currency": "RON",
            "details": "Înregistrare venituri din vânzări",
            "tx_type": "ieșiri",
            "document_type": "bon-fiscal",
        },
        "followup_transactions": [
            {
                "debit_account": "5121",
                "credit_account": "4427",
                "operation": "*19/100",
                "details": "Înregistrare TVA vânzare marfă",
                "tx_type": "ieșiri",
                "document_type": "bon-fiscal",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru descărcare din gestiunea de mărfuri")
def step_impl(context):
    request_body = {
        "name": "Descărcare marfă din gestiune",
        "description": "Descărcarea din gestiune a mărfurilor vândute",
        "main_transaction": {
            "debit_account": "607",
            "credit_account": "371",
            "currency": "RON",
            "details": "Descărcarea din gestiune a unor mărfuri",
            "tx_type": "descărcare",
            "document_type": "factură",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru descărcare din gestiunea de mărfuri pe baza de bon fiscal"
)
def step_impl(context):
    request_body = {
        "name": "Descărcare marfă din gestiune",
        "description": "Descărcarea din gestiune a mărfurilor vândute",
        "main_transaction": {
            "debit_account": "607",
            "credit_account": "371",
            "currency": "RON",
            "details": "Descărcarea din gestiune a unor mărfuri",
            "tx_type": "descărcare",
            "document_type": "bon-fiscal",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata salariilor")
def step_impl(context):
    request_body = {
        "name": "Plata salariu si taxe",
        "description": "Înregistrarea salariilor datorate si a taxelor aferente",
        "main_transaction": {
            "debit_account": "641",
            "credit_account": "421",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu salariile",
            "tx_type": "salarii",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [
            {
                "debit_account": "421",
                "credit_account": "431",
                "operation": "*25/100",
                "details": "Contribuție asigurări sociale - CAS",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "421",
                "credit_account": "437",
                "operation": "*10/100",
                "details": "Contribuții de asigurări sociale de sănătate - CASS",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "421",
                "credit_account": "444",
                # 660 este deducerea personala
                "operation": "(X*65/100) *10/100",
                "details": "Impozit pe venit",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "646",
                "credit_account": "436",
                "operation": "*2.25/100",
                "details": "Contribuția asiguratorie de muncă",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru cheltuieli cu salariile fără normă întreagă")
def step_impl(context):
    request_body = {
        "name": "Plata salariu jumătate normă și taxe aferente",
        "description": "Înregistrarea salariilor fără normă întreagă datorate si a taxelor aferente",
        "main_transaction": {
            "debit_account": "641",
            "credit_account": "421",
            "currency": "RON",
            "details": "Înregistrare cheltuieli cu salariile",
            "tx_type": "salarii",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [
            {
                "debit_account": "421",
                "credit_account": "431",
                "operation": "*25/100",
                "details": "Contribuție asigurări sociale - CAS",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "421",
                "credit_account": "437",
                "operation": "*10/100",
                "details": "Contribuții de asigurări sociale de sănătate - CASS",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "421",
                "credit_account": "444",
                # 660 este deducerea personala
                "operation": "(X*65/100 - 660)*10/100",
                "details": "Impozit pe venit",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "646",
                "credit_account": "436",
                "operation": "*2.25/100",
                "details": "Contribuția asiguratorie de muncă",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "6458",
                "credit_account": "4315",
                "operation": "775-X*25/100",
                "details": "Contribuția asiguratorie de muncă",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
            {
                "debit_account": "6458",
                "credit_account": "4316",
                "operation": "310-X*10/100",
                "details": "Contribuția asiguratorie de muncă",
                "tx_type": "salarii",
                "document_type": "ștat de plată",
            },
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


# ÎNCHIDERI


@given(
    "adaug tratament contabil pentru înregistrarea cheltuielilor cu amortizarea imobilizărilor"
)
def step_impl(context):
    request_body = {
        "name": "Cheltuieli cu amortizarea imobilizărilor",
        "description": "Cheltuieli cu amortizarea imobilizărilor",
        "main_transaction": {
            "debit_account": "6811",
            "credit_account": "2814",
            "currency": "RON",
            "details": "Cheltuieli cu amortizarea imobilizărilor",
            "tx_type": "închideri",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


# BANCĂ
@given("adaug tratament contabil pentru incasare in cont de la client")
def step_impl(context):
    request_body = {
        "name": "Încasare în cont de la client",
        "description": "Încasarea in cont de la un client",
        "main_transaction": {
            "debit_account": "5121",
            "credit_account": "4111",
            "currency": "RON",
            "details": "Încasare în cont de la client",
            "tx_type": "încasare",
            "document_type": "OP",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru incasare credit pe termen scurt in cont")
def step_impl(context):
    request_body = {
        "name": "Încasare credit pe termen scurt în cont",
        "description": "Încasare credit pe termen scurt în cont",
        "main_transaction": {
            "debit_account": "5121",
            "credit_account": "5191",
            "currency": "RON",
            "details": "Încasare credit pe termen scurt în cont",
            "tx_type": "încasare",
            "document_type": "OP",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru incasare in casa de la client")
def step_impl(context):
    request_body = {
        "name": "Încasare în casă de la client",
        "description": "Încasare în casă de la client",
        "main_transaction": {
            "debit_account": "5311",
            "credit_account": "4111",
            "currency": "RON",
            "details": "Încasare în casă de la client",
            "tx_type": "încasare",
            "document_type": "OP",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata furnizor din cont")
def step_impl(context):
    request_body = {
        "name": "Plată furnizor din cont",
        "description": "Plată furnizor din cont",
        "main_transaction": {
            "debit_account": "401",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plată furnizor din cont",
            "tx_type": "plată",
            "document_type": "OP",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata furnizor din cont cu exigibilizare TVA")
def step_impl(context):
    request_body = {
        "name": "Plată furnizor din cont și exigibilizare TVA",
        "description": "Plată furnizor din cont",
        "main_transaction": {
            "debit_account": "401",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plată furnizor din cont",
            "tx_type": "plată",
            "document_type": "OP",
        },
        "followup_transactions": [
            {
                "debit_account": "4426",
                "credit_account": "4428",
                "operation": "*19/119",
                "details": "Exigibilizare TVA",
                "tx_type": "TVA-plata",
                "document_type": "OP",
            }
        ],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata furnizor din casă")
def step_impl(context):
    request_body = {
        "name": "Plata furnizor din casă",
        "description": "Plata furnizor din casă",
        "main_transaction": {
            "debit_account": "401",
            "credit_account": "5311",
            "currency": "RON",
            "details": "Plata furnizor din casă",
            "tx_type": "plată",
            "document_type": "Chitanță",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata salarii din casă")
def step_impl(context):
    request_body = {
        "name": "Plata salariului din casă",
        "description": "Plata salariului din casă",
        "main_transaction": {
            "debit_account": "421",
            "credit_account": "5311",
            "currency": "RON",
            "details": "Plata salariului din casă",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata asigurării sociale")
def step_impl(context):
    request_body = {
        "name": "Plata asigurării sociale",
        "description": "Plata asigurării sociale",
        "main_transaction": {
            "debit_account": "4315",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plata asigurării sociale",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata asigurării sociale de sănătate")
def step_impl(context):
    request_body = {
        "name": "Plata asigurării sociale de sănătate",
        "description": "Plata furnizor din casă",
        "main_transaction": {
            "debit_account": "4316",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plata asigurării sociale de sănătate",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata contribuției asiguratorie de munca")
def step_impl(context):
    request_body = {
        "name": "Plata contribuției asiguratorie de munca",
        "description": "Plata contribuției asiguratorie de munca",
        "main_transaction": {
            "debit_account": "436",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plata contribuției asiguratorie de munca",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given(
    "adaug tratament contabil pentru plata impozitului pe venit de natura salariilor"
)
def step_impl(context):
    request_body = {
        "name": "Plata impozitului pe venit de natura salariilor",
        "description": "Plata impozitului pe venit de natura salariilor",
        "main_transaction": {
            "debit_account": "444",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plata impozitului pe venit de natura salariilor",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("adaug tratament contabil pentru plata TVA de plată")
def step_impl(context):
    request_body = {
        "name": "Plata TVA de plată",
        "description": "Plata TVA de plată",
        "main_transaction": {
            "debit_account": "4423",
            "credit_account": "5121",
            "currency": "RON",
            "details": "Plata TVA de plată",
            "tx_type": "plată",
            "document_type": "ștat de plată",
        },
        "followup_transactions": [],
    }
    response = mg.add_accounting_treatment(request_body)
    assert response.status_code == 201


@given("wait 1 second")
def step_impl(context):
    import time

    time.sleep(1)
    pass
