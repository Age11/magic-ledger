from tests.entity_creation_test import test_create_inventory

item1 = {
    "name": "item1",
    "description": "item1",
    "quantity": 1,
    "measurement_unit": "buc",
    "acquisition_price": 100,
    "vat_rate": 19,
    "in_analytical_account": "371",
    "out_analytical_account": "707",
    "inventory_id": 1,
}

item2 = {
    "name": "item1",
    "description": "item1",
    "quantity": 1,
    "measurement_unit": "buc",
    "acquisition_price": 1000,
    "vat_rate": 19,
    "in_analytical_account": "371",
    "out_analytical_account": "707",
    "inventory_id": 1,
}

local_purchase_from_invoice = {
    "document_type": "invoice",
    "serial_number": "ABC",
    "receive_date": "2024-01-01",
    "payment_status": "due",
    "due_date": "2024-01-01",
    "issue_date": "2024-01-01",
    "supplier_id": 2,
    "client_id": 1,
    "currency": "RON",
    "issuer_name": "Vasile Vasile",
    "items": [item1, item2]
}


def test_record_local_purchase(client):
    test_create_inventory(client)
    response = client.post(
        "/1/inflow/local-purchase",
        json=local_purchase_from_invoice,
    )
    assert response.status_code == 201

    response = client.get("/1/transactions/")
    assert response.status_code == 200
    data = response.json
    assert len(data) == 4

    response = client.get("/1/inventory/1/items/")
    assert response.status_code == 200
    assert len(response.json) == 2
