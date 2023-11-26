import csv
import json

import pytest


@pytest.fixture(autouse=True)
def provision_organizations(client, app):
    # read the test data organizations csv file and map the data to dictionaries
    with open(
        r"C:\Users\ageor\PycharmProjects\magic-ledger\tests\test_data\organizations.csv",
        mode="r",
    ) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        org_data = list(csv_reader)
        print(org_data)
    for org in org_data:
        # map the data to the organization model
        org_payload = {
            "name": org["name"],
            "cif": org["cif"],
            "nrc": org["nrc"],
            "vat_mode": org["vat_mode"],
            "status": org["status"],
            "org_type": org["org_type"],
            "caen_code": org["caen_code"],
        }

        # create the organization
        response = client.post("/organizations/", json=org_payload)
        assert response.status_code == 201

        org_id = str(response.headers["location"]).split("/")[2]

        address = {
            "country": org["country"],
            "state_or_province": org["state_or_province"],
            "city": org["city"],
            "street": org["street"],
            "apartment_or_suite": org["apartment_or_suite"],
            "postal_code": org["postal_code"],
            "phone": org["phone"],
            "email": org["email"],
            "organization_id": org_id,
        }

        response = client.post("/organizations/addressbook", json=address)
        assert response.status_code == 200

        bank_details = {
            "account": org["account"],
            "details": org["details"],
            "organization_id": org_id,
        }

        response = client.post("/organizations/banking-details", json=bank_details)
        assert response.status_code == 200

    response = client.get("/organizations/")
    assert response.status_code == 200
    resp = json.loads(response.data)
    assert len(resp) == 5


def test_inventory_items(client, app):
    response = client.get("/organizations/")
    for org in json.loads(response.data):
        if org["org_type"] == "project":
            org_id = org["id"]
            break
    inventory = {
        "name": "test",
        "description": "inventar1",
        "inv_type": "marfuri",
        "inventory_method": "lifo",
        "organization_id": org_id,
    }

    response = client.post("/inventory/", json=inventory)
    assert response.status_code == 201
    inventory_id = response.headers["location"].split("/")[2]

    chocolate_invoice = {
        "inv_type": "invoice",
        "number": "0002",
        "serial": "FF",
        "issue_date": "2023-11-11",
        "receive_date": "2023-11-11",
        "due_date": "2023-12-11",
        "payment_status": "due",
        "organization_id": 1,
        "supplier_id": 2,
        "client_id": 1,
        "currency": "RON",
        "amount": 100,
        "issuer_name": "issuer_name",
    }

    response = client.post("/invoices/", json=chocolate_invoice)
    assert response.status_code == 201
    invoice_id = response.headers["location"].split("/")[2]

    inv_item = {
        "inventory_id": inventory_id,
        "name": "ciocolata",
        "description": "ciocolata cu lapte",
        "measurement_unit": "buc",
        "quantity": 10,
        "acquisition_price": 10,
        "invoice_id": invoice_id,
    }
    response = client.post("/inventory/items/", json=inv_item)
    assert response.status_code == 201

    # record the transaction
    transaction = {
        "debit_account_id": "371",
        "credit_account_id": "401",
        "debit_amount": 100,
        "credit_amount": 100,
        "currency": "RON",
        "transaction_date": "2023-11-11",
        "organization_id": org_id,
        "details": "Achizitionat 10 ciocolati de la furnizori",
    }
    response = client.post("/transactions/", json=transaction)
    assert response.status_code == 201