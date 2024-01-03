import json

project_ABC = {
    "project_name": "ABC",
    "vat_mode": "on_invoice",
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


def test_create_project(client):
    response = client.post("/projects/", json=project_ABC)
    assert response.status_code == 201
    assert response.headers["location"] == "/projects/1"

    response = client.get("/projects/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["id"] == 1
    assert data["project_name"] == "ABC"
    assert data["vat_mode"] == "on_invoice"
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


organization_AAA = {
    "name": "ADA ONLINE SRL",
    "cif": "31845110",
    "nrc": "J01/375/2013",
    "caen_code": "4791",
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


def test_create_supplier_organization(client):
    client.post("/projects/", json=project_ABC)
    response = client.post("/1/third-parties/organizations/suppliers/", json=organization_AAA)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    org_id = response.headers["location"].split("/")[-1]

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["name"] == 'ADA ONLINE SRL'
    assert data["cif"] == '31845110'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J01/375/2013'
    assert data["org_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/suppliers/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["name"] == 'ADA ONLINE SRL'
    assert data["cif"] == '31845110'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J01/375/2013'
    assert data["org_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/suppliers/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]

    assert data["name"] == 'ADA ONLINE SRL'
    assert data["cif"] == '31845110'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J01/375/2013'
    assert data["org_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    assert data["country"] == 'Romania'
    assert data["state_or_province"] == 'Prahova'
    assert data["city"] == 'Sinaia'
    assert data["street"] == 'Stanjeneilor'
    assert data["apartment_or_suite"] == '16'
    assert data["postal_code"] == '106100'
    assert data["phone"] == '0721222222'
    assert data["email"] == 'contact@carmenimpextm.com'

    assert data["account"] == 'RO49AAAA1B31007593840000'
    assert data["details"] == 'AAAA BANK'

    assert data["creation_date"] is not None


def test_update_supplier(client):
    test_create_supplier_organization(client)
    organization_AAA["name"] = "AAA ONLINE SRL"
    organization_AAA["details"] = "BBBB BANK"
    resp = client.put("/1/third-parties/organizations/suppliers/2", json=organization_AAA)
    assert resp.status_code == 201

    response = client.get("/1/third-parties/organizations/suppliers/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]
    assert data["name"] == 'AAA ONLINE SRL'
    assert data["details"] == 'BBBB BANK'

    assert data["postal_code"] == '106100'


organization_AAB = {
    "name": "XXX AMSTERFARM SRL",
    "cif": "31105210",
    "nrc": "J11/275/2003",
    "caen_code": "4791",
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
}


def test_create_client_organization(client):
    client.post("/projects/", json=project_ABC)
    response = client.post("/1/third-parties/organizations/clients/", json=organization_AAB)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    org_id = response.headers["location"].split("/")[-1]

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["name"] == 'XXX AMSTERFARM SRL'
    assert data["cif"] == '31105210'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J11/275/2003'
    assert data["org_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/clients/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["name"] == 'XXX AMSTERFARM SRL'
    assert data["cif"] == '31105210'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J11/275/2003'
    assert data["org_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/organizations/clients/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]

    assert data["name"] == 'XXX AMSTERFARM SRL'
    assert data["cif"] == '31105210'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J11/275/2003'
    assert data["org_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    assert data["country"] == 'Romania'
    assert data["state_or_province"] == 'Prahova'
    assert data["city"] == 'Sinaia'
    assert data["street"] == 'Fanfarei'
    assert data["apartment_or_suite"] == '112'
    assert data["postal_code"] == '106100'
    assert data["phone"] == '0721333333'
    assert data["email"] == 'contact@amst.com'

    assert data["account"] == 'RO49AAAA1B31006591820999'
    assert data["details"] == 'AAAA BANK'

    assert data["creation_date"] is not None


def test_update_client(client):
    test_create_client_organization(client)
    organization_AAA["name"] = "AAA ONLINE SRL"
    organization_AAA["details"] = "BBBB BANK"
    resp = client.put("/1/third-parties/organizations/clients/2", json=organization_AAA)
    assert resp.status_code == 201

    response = client.get("/1/third-parties/organizations/clients/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]
    assert data["name"] == 'AAA ONLINE SRL'
    assert data["details"] == 'BBBB BANK'

    assert data["postal_code"] == '106100'


agent_EI = {
    "name": "Emilian",
    "middle_name": "-",
    "surname": "Ionescu",
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
    response = client.post("/1/third-parties/organizations/affiliates/", json=organization_AAB)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/organizations/2"

    org_id = response.headers["location"].split("/")[-1]

    response = client.get("/1/third-parties/organizations/2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["name"] == 'XXX AMSTERFARM SRL'
    assert data["cif"] == '31105210'
    assert data["caen_code"] == '4791'
    assert data["nrc"] == 'J11/275/2003'
    assert data["org_type"] == 'affiliate'
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

    assert data["name"] == 'Emilian'
    assert data["middle_name"] == '-'
    assert data["surname"] == 'Ionescu'
    assert data["cnp"] == '1880202226699'
    assert data["agent_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/agents/clients/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["name"] == 'Emilian'
    assert data["middle_name"] == '-'
    assert data["surname"] == 'Ionescu'
    assert data["cnp"] == '1880202226699'
    assert data["agent_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/agents/clients/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]

    data = resp_data[0]
    assert data["name"] == 'Emilian'
    assert data["middle_name"] == '-'
    assert data["surname"] == 'Ionescu'
    assert data["cnp"] == '1880202226699'
    assert data["agent_type"] == 'client'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    assert data["country"] == 'Romania'
    assert data["state_or_province"] == 'Prahova'
    assert data["city"] == 'Sinaia'
    assert data["street"] == 'AAAAAA'
    assert data["apartment_or_suite"] == '100'
    assert data["postal_code"] == '106100'
    assert data["phone"] == '0721666555'
    assert data["email"] == 'ionemi@email.com'

    assert data["account"] == 'RO49AAAA1B31007593840001'
    assert data["details"] == 'AAAA BANK'

    assert data["creation_date"] is not None


agent_VV = {
    "name": "Vasile",
    "middle_name": "Vasile",
    "surname": "Vasile",
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


def test_create_agent_supplier(client):
    client.post("/projects/", json=project_ABC)
    response = client.post("/1/third-parties/agents/suppliers/", json=agent_VV)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/third-parties/agents/1"

    response = client.get("/1/third-parties/agents/1")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["name"] == 'Vasile'
    assert data["middle_name"] == 'Vasile'
    assert data["surname"] == 'Vasile'
    assert data["cnp"] == '1600207895599'
    assert data["agent_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/agents/suppliers/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1

    data = resp_data[0]
    assert data["name"] == 'Vasile'
    assert data["middle_name"] == 'Vasile'
    assert data["surname"] == 'Vasile'
    assert data["cnp"] == '1600207895599'
    assert data["agent_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    response = client.get("/1/third-parties/agents/suppliers/full/")
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert len(resp_data) == 1
    data = resp_data[0]

    data = resp_data[0]
    assert data["name"] == 'Vasile'
    assert data["middle_name"] == 'Vasile'
    assert data["surname"] == 'Vasile'
    assert data["cnp"] == '1600207895599'
    assert data["agent_type"] == 'supplier'
    assert data["owner_id"] == 1
    assert data["id"] == 2
    assert data["banking_details_id"] == 2
    assert data["address_id"] == 2

    assert data["country"] == 'Romania'
    assert data["state_or_province"] == 'Prahova'
    assert data["city"] == 'Sinaia'
    assert data["street"] == 'AAAAAA'
    assert data["apartment_or_suite"] == '100'
    assert data["postal_code"] == '106100'
    assert data["phone"] == '0721666555'
    assert data["email"] == 'vasi@email.com'

    assert data["account"] == 'RO49AAAA1B31007593840001'
    assert data["details"] == 'AAAA BANK'

    assert data["creation_date"] is not None


def test_create_all_types(client):
    client.post("/projects/", json=project_ABC)
    resp1 = client.post("/1/third-parties/organizations/suppliers/", json=organization_AAA)
    assert resp1.status_code == 201
    assert resp1.headers["location"] == "/1/third-parties/organizations/2"

    organization_AAA["org_type"] = "supplier"
    resp2 = client.post("/1/third-parties/organizations/", json=organization_AAA)
    assert resp2.status_code == 201
    assert resp2.headers["location"] == "/1/third-parties/organizations/3"

    resp3 = client.post("/1/third-parties/organizations/clients/", json=organization_AAB)
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

    agent_VV["agent_type"] = "supplier"
    resp8 = client.post("/1/third-parties/agents/", json=agent_VV)
    assert resp8.status_code == 201
    assert resp8.headers["location"] == "/1/third-parties/agents/4"


stock_inventory = {
    "inv_type": "stock",
    "name": "inventar marfuri",
    "description": "inventar marfuri",
    "inventory_method": "fifo",
}


def test_create_inventory(client):
    test_create_all_types(client)
    response = client.post("/1/inventory/", json=stock_inventory)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/inventory/1"

    response = client.get("/1/inventory/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

    data = data[0]
    assert data["inv_type"] == "stock"
    assert data["name"] == "inventar marfuri"
    assert data["description"] == "inventar marfuri"
    assert data["inventory_method"] == "fifo"
    assert data["owner_id"] == 1
    assert data["id"] == 1


invoice = {
    "inv_type": "invoice",
    "number": "0001",
    "serial": "FF",
    "issue_date": "2020-01-01",
    "receive_date": "2020-01-01",
    "due_date": "2020-01-01",
    "payment_status": "paid",
    "supplier_id": "2",
    "client_id": "1",
    "currency": "RON",
    "amount": "100",
    "issuer_name": "Valise Vasile",
}


def test_create_invoice(client):
    test_create_all_types(client)
    response = client.post("/1/invoices/", json=invoice)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/invoices/1"

    response = client.get("/1/invoices/")
    data = json.loads(response.data)
    assert len(data) == 1
    data = data[0]
    data['owner_id'] = 1
    data['id'] = 1


item = {
    "name": "paracetamol",
    "description": "medicament",
    "quantity": 1,
    "measurement_unit": "cutie",
    "acquisition_price": 100,
    "total_value": 100,
    "invoice_id": 1,
}


def test_create_item(client):
    test_create_inventory(client)
    response = client.post("/1/inventory/1/items/", json=item)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/inventory/1/items/1"
    #
    response = client.get("/1/inventory/1/items/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1

    data = data[0]
    assert data["name"] == "paracetamol"
    assert data["description"] == "medicament"
    assert data["quantity"] == 1
    assert data["measurement_unit"] == "cutie"
    assert data["acquisition_price"] == 100
    assert data["inventory_id"] == 1
    assert data["total_value"] == 100


transaction = {
    "debit_account": "371",
    "credit_account": "401",
    "debit_amount": 100,
    "credit_amount": 100,
    "currency": "RON",
    "transaction_date": "2020-01-01",
    "details": "achizitie marfuri",
}


def test_create_transaction(client):
    test_create_all_types(client)
    response = client.post("/1/transactions/", json=transaction)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/transactions/1"

    response = client.get("/1/transactions/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["debit_account_id"] == "371"
    assert data["debit_account_name"] == "MARFURI"
    assert data["credit_account_id"] == "401"
    assert data["credit_account_name"] == "FURNIZORI"
    assert data["debit_amount"] == 100
    assert data["credit_amount"] == 100
    assert data["currency"] == "RON"
    assert data["details"] == "achizitie marfuri"
    # TODO check that the account balance is updated


car = {
    "asset_name": "masina",
    "description": "o masina",
    "asset_class": "21",
    "analytical_account": "2133",
    "deprecation_analytical_account": "2813",
    "total_amount": 30000,
    "depreciation_method": "straight_line",
    "total_duration": 5,
    "acquisition_date": "2021-09",
    "recording_date": "2023-11"
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
    assert data["asset_class"] == "21"
    assert data["depreciation_method"] == "straight_line"
    assert data["total_amount"] == 30000
    assert data["total_duration"] == 5
    assert data["owner_id"] == 1
    assert data["id"] == 1
    assert data["remaining_duration"] == 35
    assert data["remaining_amount"] == 17500
    assert data["deprecated_amount"] == 12500
    assert data["monthly_amount"] == 500
    assert data["analytical_account"] == "2133"
    assert data["deprecation_analytical_account"] == "2813"

    # TODO fix this
    assert data["acquisition_date"] == "Wed, 01 Sep 2021 00:00:00 GMT"


holding = {
    "owner_id": 1,
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
    "currency_type": "EUR",
    "quantity": 10417,
    "acquisition_price": 4.799,
    "analytical_account": "5124",
    "acquisition_date": "2023-09-01",
}


def test_create_foreign_currency_reserve(client):
    test_create_all_types(client)
    response = client.post("/1/liquidity/reserve/", json=currency_reserve)
    assert response.status_code == 201
    assert response.headers["location"] == "/1/liquidity/reserve/1"

    response = client.get("/1/liquidity/reserve/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1


init_balance = [{"balance_date": "2021-11",
                 "analytical_account": "371",
                 "initial_debit": 10,
                 "initial_credit": 100,
                 "debit": 100,
                 "credit": 100
                 },
                {"balance_date": "2021-11",
                 "analytical_account": "401",
                 "initial_debit": 500,
                 "initial_credit": 100,
                 "debit": 350,
                 "credit": 250
                 }]


def test_take_initial_balance(client):
    test_create_all_types(client)
    resp = client.post("/1/account-balance/", json=init_balance)
    assert resp.status_code == 201

    resp = client.get("/1/account-balance/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert len(data) == 2
