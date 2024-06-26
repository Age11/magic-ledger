import json
from datetime import datetime

project_ABC = {
    "project_name": "ABC",
    "vat_mode": "facturare",
    "status": "active",
    "organization_name": "CARMEN IMPEX TM SRL",
    "cif": "5420048",
    "nrc": "J29/747/1994",
    "caen_code": "4941",
    "country": "Romania",
    "state_or_province": "Prahova",
    "city": "Sinaia",
    "street": "Stanjeneilor",
    "apartment_or_suite": "16",
    "postal_code": "106100",
    "phone": "0721222222",
    "email": "contact@carmenimpextm.com",
    "account": "RO49AAAA1B31007593840000",
    "details": "AAAA BANK",
}
p3 = {
    "project_name": "XXXs",
    "caen_code": "4941",
    "vat_mode": "facturare",
    "status": "active",
    "organization_name": "xxx",
    "cif": "XXXXXX",
    "nrc": "xxx11",
    "country": "xxx",
    "state_or_province": "xxx",
    "city": "xxx",
    "street": "xxx",
    "apartment_or_suite": "xxx",
    "postal_code": "xxx",
    "phone": "xxx",
    "email": "xxx",
    "account": "xxx",
    "details": "xxx",
}


def test_create_project(client):
    response = client.post("/projects/", json=project_ABC)
    assert response.status_code == 201
    assert response.headers["location"] == "/projects/1"

    response = client.get("/projects/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id"] == 1
    assert data["project_name"] == "ABC"
    assert data["status"] == "active"
    assert data["creation_date"] is not None

    response = client.get("/projects/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["project_name"] == "ABC"
    assert data[0]["city"] == "Sinaia"
    assert data[0]["details"] == "AAAA BANK"

    response = client.get("/projects/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["project_name"] == "ABC"


def test_create_project2(client):
    response = client.post("/projects/", json=p3)
    assert response.status_code == 201
    assert response.headers["location"] == "/projects/1"

    resp = client.get("/1/third-parties/organizations/projects/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 1
    assert data[0]["organization_name"] == "xxx"
    assert "id" in data[0].keys()


organization_AAA = {
    "organization_name": "ADA ONLINE SRL",
    "cif": "31845110",
    "nrc": "J01/375/2013",
    "country": "Romania",
    "state_or_province": "Prahova",
    "city": "Sinaia",
    "street": "Stanjeneilor",
    "apartment_or_suite": "16",
    "postal_code": "106100",
    "phone": "0721222222",
    "email": "contact@carmenimpextm.com",
    "account": "RO49AAAA1B31007593840000",
    "details": "AAAA BANK",
    "vat_mode": "facturare",
}


def test_create_supplier_organization(client):
    client.post("/projects/", json=project_ABC)
    response = client.post(
        "/1/third-parties/organizations/suppliers/", json=organization_AAA
    )
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    org_id = response.headers["location"].split("/")[-1]

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["organization_name"] == "ADA ONLINE SRL"
    assert data["cif"] == "31845110"
    assert data["nrc"] == "J01/375/2013"
    assert data["org_type"] == "supplier"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/suppliers/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["organization_name"] == "ADA ONLINE SRL"
    assert data["cif"] == "31845110"
    assert data["nrc"] == "J01/375/2013"
    assert data["org_type"] == "supplier"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/suppliers/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]

    assert data["organization_name"] == "ADA ONLINE SRL"
    assert data["cif"] == "31845110"
    assert data["nrc"] == "J01/375/2013"
    assert data["org_type"] == "supplier"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2


# def test_update_supplier(client):
#     test_create_supplier_organization(client)
#     organization_AAA["organization_name"] = "AAA ONLINE SRL"
#     organization_AAA["details"] = "BBBB BANK"
#     resp = client.put("/1/third-parties/organizations/2", json=organization_AAA)
#     assert resp.status_code == 201
#
#     response = client.get("/1/third-parties/organizations/suppliers/full/")
#     assert response.status_code == 200
#     resp_data = json.loads(response.data)
#     assert len(resp_data) == 1
#     data = resp_data[0]
#     assert data["organization_name"] == "AAA ONLINE SRL"
#     assert data["details"] == "BBBB BANK"
#
#     assert data["postal_code"] == "106100"


organization_AAB = {
    "organization_name": "XXX AMSTERFARM SRL",
    "cif": "31105210",
    "nrc": "J11/275/2003",
    "country": "Romania",
    "state_or_province": "Prahova",
    "city": "Sinaia",
    "street": "Fanfarei",
    "apartment_or_suite": "112",
    "postal_code": "106100",
    "phone": "0721333333",
    "email": "contact@amst.com",
    "account": "RO49AAAA1B31006591820999",
    "details": "AAAA BANK",
    "vat_mode": "facturare",
}


def test_create_client_organization(client):
    client.post("/projects/", json=project_ABC)
    response = client.post(
        "/1/third-parties/organizations/clients/", json=organization_AAB
    )
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["organization_name"] == "XXX AMSTERFARM SRL"
    assert data["cif"] == "31105210"
    assert data["nrc"] == "J11/275/2003"
    assert data["org_type"] == "client"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/clients/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["organization_name"] == "XXX AMSTERFARM SRL"
    assert data["cif"] == "31105210"
    assert data["nrc"] == "J11/275/2003"
    assert data["org_type"] == "client"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2


def test_update_client(client):
    test_create_client_organization(client)
    organization_AAA["organization_name"] = "AAA ONLINE SRL"
    organization_AAA["details"] = "BBBB BANK"
    resp = client.put("/1/third-parties/organizations/2", json=organization_AAA)
    assert resp.status_code == 201


agent_EI = {
    "agent_name": "Emilian",
    "last_name": "Ionescu",
    "cnp": "1880202226699",
    "country": "Romania",
    "state_or_province": "Prahova",
    "city": "Sinaia",
    "street": "AAAAAA",
    "apartment_or_suite": "100",
    "postal_code": "106100",
    "phone": "0721666555",
    "email": "ionemi@email.com",
    "account": "RO49AAAA1B31007593840001",
    "details": "AAAA BANK",
}


def test_create_affiliate_organization(client):
    client.post("/projects/", json=project_ABC)
    response = client.post(
        "/1/third-parties/organizations/affiliates/", json=organization_AAB
    )
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    org_id = response.headers["location"].split("/")[-1]

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["organization_name"] == "XXX AMSTERFARM SRL"
    assert data["cif"] == "31105210"
    assert data["nrc"] == "J11/275/2003"
    assert data["org_type"] == "affiliate"
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/affiliates/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1


def test_create_agent_client(client):
    client.post("/projects/", json=project_ABC)
    response = client.post("/1/third-parties/agents/clients/", json=agent_EI)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/agents/1"

    response = client.get("/1/third-parties/agents/1")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["agent_name"] == "Emilian"
    assert data["cnp"] == "1880202226699"
    assert data["agent_type"] == "client"
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/agents/clients/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["agent_name"] == "Emilian"
    assert data["last_name"] == "Ionescu"
    assert data["cnp"] == "1880202226699"
    assert data["agent_type"] == "client"
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2


agent_VV = {
    "agent_name": "Vasile",
    "last_name": "Vasile",
    "cnp": "1600207895599",
    "agent_type": "supplier",
    "country": "Romania",
    "state_or_province": "Prahova",
    "city": "Sinaia",
    "street": "AAAAAA",
    "apartment_or_suite": "100",
    "postal_code": "106100",
    "phone": "0721666555",
    "email": "vasi@email.com",
    "account": "RO49AAAA1B31007593840001",
    "details": "AAAA BANK",
}


def test_create_all_types(client):
    client.post("/projects/", json=project_ABC)
    resp1 = client.post(
        "/1/third-parties/organizations/suppliers/", json=organization_AAA
    )
    assert resp1.status_code == 201
    assert resp1.headers["location"] == "/1/third-parties/organizations/2"

    organization_AAA["org_type"] = "supplier"
    resp2 = client.post("/1/third-parties/organizations/", json=organization_AAA)
    assert resp2.status_code == 201
    assert resp2.headers["location"] == "/1/third-parties/organizations/3"

    resp3 = client.post(
        "/1/third-parties/organizations/clients/", json=organization_AAB
    )
    assert resp3.status_code == 201
    assert resp3.headers["location"] == "/1/third-parties/organizations/4"

    organization_AAB["org_type"] = "client"
    resp4 = client.post("/1/third-parties/organizations/", json=organization_AAB)
    assert resp4.status_code == 201
    assert resp4.headers["location"] == "/1/third-parties/organizations/5"

    resp5 = client.post("/1/third-parties/agents/clients/", json=agent_EI)
    assert resp5.status_code == 201
    assert resp5.headers["location"] == "/1/third-parties/agents/1"

    agent_EI["agent_type"] = "client"
    resp6 = client.post("/1/third-parties/agents/", json=agent_EI)
    assert resp6.status_code == 201
    assert resp6.headers["location"] == "/1/third-parties/agents/2"

    resp7 = client.post("/1/third-parties/agents/suppliers/", json=agent_VV)
    assert resp7.status_code == 201
    assert resp7.headers["location"] == "/1/third-parties/agents/3"


stock_inventory = {
    "name": "inventar marfuri",
    "description": "inventar marfuri",
    "inventory_method": "fifo",
}


def test_create_inventory(client):
    test_create_all_types(client)
    response = client.post("/1/inventories/", json=stock_inventory)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/inventories/1"

    response = client.get("/1/inventories/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

    data = data[0]
    assert data["name"] == "inventar marfuri"
    assert data["description"] == "inventar marfuri"
    assert data["inventory_method"] == "fifo"
    assert data["owner_id"] == 1
    assert data["id"] == 1


invoice = {
    "serial_number": "FF0001",
    "invoice_date": "2020-01-01",
    "due_date": "2020-01-01",
    "supplier_id": "2",
    "client_id": "1",
    "currency": "RON",
    "amount": "100",
    "invoice_type": "primită",
    "payment_type": "plată",
    "vat_amount": "19",
    "issuer_name": "Valise Vasile",
    "amount_due": 119,
}

transaction_on_invoice = {
    "debit_account": "371",
    "credit_account": "401",
    "debit_amount": 100,
    "credit_amount": 100,
    "currency": "RON",
    "transaction_date": "2020-01-01",
    "details": "achizitie marfuri",
    "tx_type": "intrari",
    "document_type": "factura",
    "document_serial_number": "FF0001",
    "document_id": 1,
}


def test_create_invoice_and_transaction(client):
    test_create_all_types(client)
    response = client.post("/1/invoices/", json=invoice)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/invoices/1"

    response = client.get("/1/invoices/")
    data = json.loads(response.data)
    assert len(data) == 1
    data = data[0]
    data["owner_id"] = 1
    data["id"] = 1
    assert data["serial_number"] == "FF0001"
    assert data["invoice_date"] == "2020-01-01"
    assert data["supplier_id"] == 2
    assert data["client_id"] == 1
    assert data["currency"] == "RON"
    assert data["amount"] == 100
    assert data["invoice_type"] == "primită"

    response = client.post("/1/transactions/", json=transaction_on_invoice)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/transactions/1"

    response = client.get("/1/transactions/1/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["debit_account"] == "371"
    assert data["document_id"] == 1

    resp = client.get("/1/payments/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 1
    data = data[0]
    assert data["payment_status"] == "restantă"
    assert data["amount_due"] == 119
    assert data["amount_paid"] == 0
    assert data["invoice_id"] == 1
    assert data["payment_type"] == "plată"
    assert data["owner_id"] == 1

    response = client.put(
        "/1/payments/1/pay/", json={"amount": 119, "installment_type": "bancă"}
    )
    assert response.status_code == 204

    resp = client.get("/1/payments/1/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["payment_status"] == "plătită"

    response = client.get("/1/invoices/2020-01/all")


item = {
    "name": "paracetamol",
    "description": "medicament",
    "quantity": 50,
    "measurement_unit": "cutie",
    "acquisition_price": 100,
    "sale_price": 102,
    "currency": "RON",
    "vat_rate": 19,
    "invoice_id": 1,
    "inventory_id": 1,
    "acquisition_date": "2023-10-01",
}


def test_create_item(client):
    test_create_inventory(client)

    response = client.post("/1/invoices/", json=invoice)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/invoices/1"

    response = client.post("/1/inventories/1/items/", json=item)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/inventories/1/items/1"

    response = client.get("/1/inventories/1/items/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

    response = client.get("/1/inventories/1/items/1/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "paracetamol"
    assert data["description"] == "medicament"
    assert data["quantity"] == 50
    assert data["measurement_unit"] == "cutie"
    assert data["acquisition_price"] == 100
    assert data["inventory_id"] == 1
    assert data["total_value"] == 5000
    assert data["sale_price"] == 102
    assert data["vat_rate"] == 19
    assert data["currency"] == "RON"
    assert data["acquisition_date"] == "2023-10-01"

    dec = {"quantity": 10, "invoice_id": 1}

    response = client.put("/1/inventories/1/items/1/decrease-stock/", json=dec)
    assert response.status_code == 204

    response = client.get("/1/inventories/1/items/1/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "paracetamol"
    assert data["description"] == "medicament"
    assert data["quantity"] == 40
    assert data["total_value"] == 4000


transaction = {
    "debit_account": "371",
    "credit_account": "401",
    "debit_amount": 100,
    "credit_amount": 100,
    "currency": "RON",
    "transaction_date": "2020-01-01",
    "details": "achizitie marfuri",
    "tx_type": "intrari",
    "document_type": "factura",
    "document_serial_number": "FF0001",
}


def test_create_transaction(client):
    test_create_all_types(client)
    response = client.post("/1/transactions/", json=transaction)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/transactions/1"

    response = client.get("/1/transactions/1/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["debit_account"] == "371"
    assert data["credit_account"] == "401"
    assert data["debit_amount"] == 100
    assert data["credit_amount"] == 100
    assert data["currency"] == "RON"
    assert data["details"] == "achizitie marfuri"
    assert data["tx_type"] == "intrari"
    # TODO check that the account balance is updated


init_balance = [
    {
        "balance_date": "2023-11-01",
        "analytical_account": "371",
        "initial_debit": 10,
        "initial_credit": 100,
        "cumulated_debit": 100,
        "cumulated_credit": 100,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "401",
        "initial_debit": 10,
        "initial_credit": 100,
        "cumulated_debit": 100,
        "cumulated_credit": 100,
    },
]


def test_take_initial_balance(client):
    test_create_all_types(client)
    resp = client.post("/1/account-balance/", json=init_balance)
    assert resp.status_code == 201

    resp = client.get("/1/account-balance/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 2


def test_close_balance(client):
    test_take_initial_balance(client)
    resp = client.put("/1/account-balance/close/2023-11")
    assert resp.status_code == 201

    resp = client.get("/1/account-balance/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 4


car = {
    "asset_name": "masina",
    "description": "o masina",
    "initial_value": 10000,
    "inventory_value": 10000,
    "current_value": 9000,
    "depreciation_method": "liniară",
    "total_duration": 48,
    "acquisition_date": "2022-09",
    "recording_date": "2023-11",
}


def test_create_asset(client):
    test_create_all_types(client)
    response = client.post("/1/assets/", json=car)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/assets/1"

    response = client.get("/1/assets/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    data = data[0]
    assert data["asset_name"] == "masina"
    assert data["description"] == "o masina"
    assert data["depreciation_method"] == "liniară"
    assert data["initial_value"] == 10000
    assert data["inventory_value"] == 10000
    assert data["current_value"] == 9000
    assert data["total_duration"] == 48
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["remaining_duration"] == 35
    assert data["remaining_amount"] == 9000.00
    assert data["deprecated_amount"] == 0.0
    assert data["rounded_monthly_amount"] == 257.14
    assert data["acquisition_date"] == "2022-09-01 00:00:00"


holding = {
    "organization_id": 2,
    "holding_type": "shares",
    "quantity": 100,
    "aquisition_price": 100,
    "analytical_account": "261",
    "aquisition_date": "2021-09-01",
}


def test_create_financial_holding(client):
    test_create_all_types(client)
    response = client.post("/1/financial-holdings/", json=holding)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/financial-holdings/1"

    response = client.get("/1/financial-holdings/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1


currency_reserve = {
    "currency": "EUR",
    "quantity": 10417,
    "acquisition_price": 4.799,
    "analytical_account": "5124",
    "acquisition_date": "2023-09-01",
    "roll_type": "cash",
}


def test_create_foreign_currency_roll(client):
    test_create_all_types(client)
    response = client.post("/1/liquidity/reserve/", json=currency_reserve)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/liquidity/reserve/1"

    response = client.get("/1/liquidity/reserve/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1


exchange_rate1 = {
    "currency_type": "EUR",
    "value_in_ref_currency": 4.799,
    "reference_currency": "RON",
    "date": "2023-09-01",
}

exchange_rate2 = {
    "currency_type": "EUR",
    "value_in_ref_currency": 4.97,
    "reference_currency": "RON",
    "date": "2023-09-01",
}


def test_exchange_rate_entry(client):
    r1 = client.post("/exchange/", json=exchange_rate1)
    assert r1.status_code == 201
    assert r1.headers["location"] == "/exchange/1"

    r2 = client.post("/exchange/", json=exchange_rate2)
    assert r2.status_code == 201
    assert r2.headers["location"] == "/exchange/2"

    resp = client.get("/exchange/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 2


salary = {
    "id": 2,
    "name": "Plata salariu si taxe",
    "description": "Inregistrarea salariilor datorate si a taxelor aferente",
    "main_transaction": {
        "debit_account": "641",
        "credit_account": "421",
        "currency": "RON",
        "details": "Inregistrare cheltuieli cu salariile",
        "tx_type": "salarii",
        "document_type": "stat plata",
    },
    "followup_transactions": [
        {
            "debit_account": "421",
            "credit_account": "431",
            "operation": "*25/100",
            "details": "Contributie asigurari sociale - CAS",
            "tx_type": "salarii",
            "document_type": "stat plata",
        },
        {
            "debit_account": "421",
            "credit_account": "437",
            "operation": "*10/100",
            "details": "Contribuții de asigurări sociale de sănătate - CASS",
            "tx_type": "salarii",
            "document_type": "stat plata",
        },
        {
            "debit_account": "421",
            "credit_account": "444",
            "operation": "*65/100*10/100",
            "details": "Impozit pe venit de natura salarii",
            "tx_type": "salarii",
            "document_type": "stat plata",
        },
    ],
}


def test_create_transaction_template(client):
    r1 = client.post("/1/transaction-group-templates/", json=salary)
    assert r1.status_code == 201

    r2 = client.get("/1/transaction-group-templates/")
    assert r2.status_code == 200
    data = json.loads(r2.data)
    assert len(data) == 1
    data = data[0]
    assert data["id"] == 1

    r3 = client.post(
        "/1/transaction-group-templates/1/use-template",
        json={
            "transaction_date": "2023-09-01",
            "amount": 4000,
            "document_serial_number": "F0001",
            "document_id": 1,
        },
    )
    assert r3.status_code == 201
    data = json.loads(r3.data)
    assert len(data) == 4

    r4 = client.get("/1/transactions/")
    assert r4.status_code == 200
    data = json.loads(r4.data)
    assert len(data) == 4

    r5 = client.get("/1/account-balance/")
    assert r5.status_code == 200
    data = json.loads(r5.data)
    assert len(data) == 5


purchase = {
    "name": "Achiziție de mărfuri de la furnizor regim tva normal",
    "description": "Aceasta inregistrare contabila se refera la achizitia de marfuri de la un furnizor care aplica regimul de tva normal",
    "main_transaction": {
        "debit_account": "371",
        "credit_account": "401",
        "currency": "RON",
        "details": "Inregistrare achizitie marfuri",
        "tx_type": "intrări",
        "document_type": "factura",
    },
    "followup_transactions": [
        {
            "debit_account": "4426",
            "credit_account": "401",
            "operation": "*19/100",
            "details": "Inregistrare TVA",
            "tx_type": "TVA-incasare",
            "document_type": "factura",
        }
    ],
}


def test_create_transaction_template2(client):
    r1 = client.post("/1/transaction-group-templates/", json=purchase)
    assert r1.status_code == 201

    r2 = client.get("/1/transaction-group-templates/")
    assert r2.status_code == 200
    data = json.loads(r2.data)
    assert len(data) == 1
    data = data[0]
    assert data["id"] == 1

    r3 = client.get("/1/transaction-group-templates/intrări")
    assert r3.status_code == 200
    data = json.loads(r3.data)
    assert len(data) == 1

    r3 = client.post(
        "/1/transaction-group-templates/1/use-template",
        json={
            "transaction_date": "2023-09-01",
            "amount": 1000,
            "document_serial_number": "F0001",
            "document_id": -1,
        },
    )
    assert r3.status_code == 201
    data = json.loads(r3.data)
    assert len(data) == 2

    r4 = client.get("/1/transactions/")
    assert r4.status_code == 200
    data = json.loads(r4.data)
    assert len(data) == 2

    r5 = client.get("/1/account-balance/")
    assert r5.status_code == 200
    data = json.loads(r5.data)
    assert len(data) == 3

    r6 = client.get("/1/account-balance/2023-09")
    assert r6.status_code == 200
    data = json.loads(r6.data)
    assert len(data) == 3

    r7 = client.get(f"/1/account-balance/{datetime.now().strftime('%Y-%m')}")
    assert r7.status_code == 200
    data = json.loads(r7.data)
    assert len(data) == 0


sell = {
    "name": "Vanzare de marfuri catre client regim tva normal",
    "description": "Aceasta inregistrare contabila se refera la vanzarea de marfuri catre un client care aplica regimul de tva normal",
    "main_transaction": {
        "debit_account": "4111",
        "credit_account": "707",
        "currency": "RON",
        "details": "Înregistrare venituri din vanzari",
        "tx_type": "ieșiri",
        "document_type": "factura",
    },
    "followup_transactions": [
        {
            "debit_account": "4111",
            "credit_account": "4427",
            "operation": "*19/100",
            "details": "Inregistrare TVA",
            "tx_type": "TVA-vanzare",
            "document_type": "factura",
        },
        {
            "debit_account": "607",
            "credit_account": "371",
            "operation": "*1",
            "details": "Descarcare din gestiune",
            "tx_type": "ieșiri",
            "document_type": "proces-verbal",
        },
    ],
}


def test_create_transaction_template3(client):
    r1 = client.post("/1/transaction-group-templates/", json=purchase)
    assert r1.status_code == 201

    r2 = client.post("/1/transaction-group-templates/", json=salary)
    assert r2.status_code == 201

    r3 = client.post("/1/transaction-group-templates/", json=sell)
    assert r3.status_code == 201

    r4 = client.get("/1/transaction-group-templates/ieșiri")
    assert r4.status_code == 200
    data = json.loads(r4.data)
    assert len(data) == 1


inv = {
    "serial_number": "FF0001",
    "invoice_date": "2024-04-16",
    "due_date": "2024-04-16",
    "supplier_id": "2",
    "client_id": "1",
    "currency": "RON",
    "amount": 100,
    "invoice_type": "primită",
    "payment_type": "plată",
    "vat_amount": 19,
    "issuer_name": "Valise Vasile",
    "amount_due": 119,
}

inv2 = {
    "serial_number": "FF0002",
    "invoice_date": "2024-04-16",
    "due_date": "2024-04-16",
    "supplier_id": "1",
    "client_id": "4",
    "currency": "RON",
    "amount": 100,
    "invoice_type": "emisă",
    "payment_type": "încasare",
    "vat_amount": 19,
    "issuer_name": "Valise Vasile",
    "amount_due": 119,
}

it1 = {
    "name": "paracetamol",
    "description": "medicament",
    "quantity": 50,
    "measurement_unit": "cutie",
    "acquisition_price": 100,
    "sale_price": 102,
    "currency": "RON",
    "vat_rate": 19,
    "invoice_id": 1,
    "inventory_id": 1,
    "acquisition_date": "2024-04-16",
}

it2 = {
    "name": "aspirina",
    "description": "medicament",
    "quantity": 50,
    "measurement_unit": "cutie",
    "acquisition_price": 100,
    "sale_price": 102,
    "currency": "RON",
    "vat_rate": 19,
    "invoice_id": 1,
    "inventory_id": 1,
    "acquisition_date": "2024-04-16",
}


def test_journals(client):
    test_create_invoice_and_transaction(client)
    response = client.post("/1/inventories/1/items/", json=it1)
    assert response.status_code == 201

    response = client.post("/1/invoices/", json=inv)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/invoices/2"

    response = client.get("/1/invoices/")
    data = json.loads(response.data)
    assert len(data) == 2
    response = client.post("/1/inventories/1/items/", json=it2)
    assert response.status_code == 201

    response = client.post("/1/invoices/", json=inv2)
    assert response.status_code == 201
    response = client.get("/1/invoices/")
    data = json.loads(response.data)
    assert len(data) == 3

    response = client.put(
        "/1/inventories/1/items/1/decrease-stock/",
        json={"quantity": 10, "invoice_id": 3},
    )
    assert response.status_code == 204

    resp = client.get("/1/reports/2024-04/purchase/")
    assert resp.status_code == 200

    resp = client.get("/1/reports/2024-04/sales/")
    assert resp.status_code == 200

    resp = client.get("/1/payments/2024-04/payable/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 1

    resp = client.get("/1/payments/2024-04/receivable/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 1


balance = [
    {
        "balance_date": "2024-04-02",
        "analytical_account": "707",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 2000.0,
    },
    {
        "balance_date": "2024-04-02",
        "analytical_account": "601",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 1000.0,
        "cumulated_credit": 0.0,
    },
]


def test_profit(client):
    client.post("/1/account-balance/", json=balance)
    resp = client.get("/1/account-balance/profit-or-loss/2024-04")
    assert resp.status_code == 200
    amount = json.loads(resp.data)
    assert amount == 1000.00


balance = [
    {
        "balance_date": "2024-04-02",
        "analytical_account": "707",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 2000.0,
    },
    {
        "balance_date": "2024-04-02",
        "analytical_account": "601",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 3000.0,
        "cumulated_credit": 0.0,
    },
]


def test_profit(client):
    client.post("/1/account-balance/", json=balance)
    resp = client.get("/1/account-balance/profit-or-loss/2024-04")
    assert resp.status_code == 200
    amount = json.loads(resp.data)
    assert amount == -1000.00


def test_general_ledger(client):
    test_create_transaction_template2(client)
    dates = client.get("/1/transactions/available-dates/")
    assert dates.status_code == 200
    dates = json.loads(dates.data)
    assert len(dates) == 1

    general_ledger = client.get("/1/reports/general-ledger/2023-09/401")
    assert general_ledger.status_code == 200
    data = json.loads(general_ledger.data)


sale_template = {
    "name": "Vanzare de marfuri catre client regim tva normal",
    "description": "Aceasta inregistrare contabila se refera la vanzarea de marfuri catre un client care aplica regimul de tva normal",
    "main_transaction": {
        "debit_account": "4111",
        "credit_account": "707",
        "currency": "RON",
        "details": "Înregistrare venituri din vanzari",
        "tx_type": "ieșiri",
        "document_type": "factura",
    },
    "followup_transactions": [
        {
            "debit_account": "4111",
            "credit_account": "4427",
            "operation": "*19/100",
            "details": "Inregistrare TVA",
            "tx_type": "TVA-vanzare",
            "document_type": "factura",
        }
    ],
}

unload_stock = {
    "name": "Descărcare marfa din gestiune",
    "description": "Aceasta înregistrare contabila se refera la descărcarea din gestiune a unor mărfuri",
    "main_transaction": {
        "debit_account": "607",
        "credit_account": "371",
        "currency": "RON",
        "details": "Descărcarea din gestiune a unor mărfuri",
        "tx_type": "descărcare",
        "document_type": "factura",
    },
    "followup_transactions": [],
}


def test_close_vat(client):
    r1 = client.post("/1/transaction-group-templates/", json=purchase)
    assert r1.status_code == 201

    r2 = client.post("/1/transaction-group-templates/", json=sale_template)
    assert r2.status_code == 201

    r3 = client.post("/1/transaction-group-templates/", json=unload_stock)
    assert r3.status_code == 201

    r4 = client.get("/1/transaction-group-templates/")
    assert r4.status_code == 200
    data = json.loads(r4.data)
    assert len(data) == 3

    r5 = client.post(
        "/1/transaction-group-templates/1/use-template",
        json={
            "transaction_date": "2024-05-01",
            "amount": 1000,
            "document_serial_number": "F0001",
            "document_id": 1,
        },
    )
    assert r5.status_code == 201
    data = json.loads(r5.data)
    assert len(data) == 2

    r6 = client.post(
        "/1/transaction-group-templates/2/use-template",
        json={
            "transaction_date": "2024-05-02",
            "amount": 2000,
            "document_serial_number": "F0001",
            "document_id": 1,
        },
    )
    assert r6.status_code == 201
    data = json.loads(r6.data)
    assert len(data) == 2

    r7 = client.post(
        "/1/transaction-group-templates/3/use-template",
        json={
            "transaction_date": "2024-05-02",
            "amount": 1000,
            "document_serial_number": "F0001",
            "document_id": 1,
        },
    )
    assert r7.status_code == 201
    data = json.loads(r7.data)
    assert len(data) == 1

    r8 = client.get("/1/transactions/")
    assert r7.status_code == 201
    data = json.loads(r8.data)
    assert len(data) == 5

    r9 = client.put("/1/transactions/generate-close-vat-transactions/2024-05/")
    assert r9.status_code == 201

    r10 = client.get("/1/transactions/")
    assert r10.status_code == 200
    data = json.loads(r10.data)
    assert len(data) == 7

    r11 = client.put(
        "/1/transactions/generate-close-income-expenses-transactions/2024-05/"
    )
    assert r11.status_code == 201

    r12 = client.get("/1/transactions/")
    assert r12.status_code == 200
    data = json.loads(r12.data)
    assert len(data) == 9


balance_nov = [
    {
        "balance_date": "2023-11-01",
        "analytical_account": "1012",
        "initial_debit": 0.0,
        "initial_credit": 200.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 0.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "121",
        "initial_debit": 0.0,
        "initial_credit": 600.0,
        "cumulated_debit": 9067.0,
        "cumulated_credit": 10000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "2133",
        "initial_debit": 10000.0,
        "initial_credit": 0.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 0.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "2813",
        "initial_debit": 0.0,
        "initial_credit": 1000.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 0.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "371",
        "initial_debit": 2000.0,
        "initial_credit": 0.0,
        "cumulated_debit": 5000.0,
        "cumulated_credit": 6000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "401",
        "initial_debit": 0.0,
        "initial_credit": 10100.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 5950.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4111",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 11900.0,
        "cumulated_credit": 10000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "421",
        "initial_debit": 0.0,
        "initial_credit": 500.0,
        "cumulated_debit": 1650.0,
        "cumulated_credit": 3000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4315",
        "initial_debit": 0.0,
        "initial_credit": 100.0,
        "cumulated_debit": 100.0,
        "cumulated_credit": 750.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4316",
        "initial_debit": 0.0,
        "initial_credit": 50.0,
        "cumulated_debit": 50.0,
        "cumulated_credit": 300.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "436",
        "initial_debit": 0.0,
        "initial_credit": 11.0,
        "cumulated_debit": 11.0,
        "cumulated_credit": 67.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4423",
        "initial_debit": 0.0,
        "initial_credit": 100.0,
        "cumulated_debit": 100.0,
        "cumulated_credit": 950.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4426",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 950.0,
        "cumulated_credit": 950.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "4427",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 1900.0,
        "cumulated_credit": 1900.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "444",
        "initial_debit": 0.0,
        "initial_credit": 9.0,
        "cumulated_debit": 9.0,
        "cumulated_credit": 100.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "5121",
        "initial_debit": 500.0,
        "initial_credit": 0.0,
        "cumulated_debit": 10000.0,
        "cumulated_credit": 770.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "5311",
        "initial_debit": 170.0,
        "initial_credit": 0.0,
        "cumulated_debit": 0.0,
        "cumulated_credit": 0.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "607",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 6000.0,
        "cumulated_credit": 6000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "641",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 3000.0,
        "cumulated_credit": 3000.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "6461",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 67.0,
        "cumulated_credit": 67.0,
    },
    {
        "balance_date": "2023-11-01",
        "analytical_account": "707",
        "initial_debit": 0.0,
        "initial_credit": 0.0,
        "cumulated_debit": 10000.0,
        "cumulated_credit": 10000.0,
    },
]


def test_month_close(client):
    r1 = client.post("http://localhost:5000/1/account-balance/", json=balance_nov)
    assert r1.status_code == 201

    r2 = client.put(
        "http://localhost:5000/1/transactions/generate-close-vat-transactions/2023-11/"
    )
    assert r2.status_code == 201

    r3 = client.put("http://localhost:5000/1/account-balance/close/2023-11")
    assert r3.status_code == 201
