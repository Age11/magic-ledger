import pytest
from magic_ledger.organizations.model import Organization
from magic_ledger import db
import json


def test_post_get_organization(client, app):
    response = client.post("/organizations/",
                           json={"name": "test",
                                 "cif": "1234567890",
                                 "nrc": "1234567890",
                                 "phone": "1234567890",
                                 "email": "asdasd@asd.com",
                                 "vat_mode": "on_invoice",
                                 "status": "active",
                                 "type": "project",
                                 "caen_code": "1234"})
    assert response.status_code == 200
    response = client.get("/organizations/")
    assert response.status_code == 200
    resp = json.loads(response.data)[0]
    assert resp["name"] == "test"
    assert resp["cif"] == "1234567890"
    assert resp["nrc"] == "1234567890"
    assert resp["phone"] == "1234567890"
    assert resp["caen_code"] == "1234"
    assert resp["status"] == "active"
    assert resp["type"] == "project"
    assert resp["vat_mode"] == "on_invoice"
    assert resp["creation_date"] is not None
    org_id = resp["id"]

    response = client.post("/addressbook/",
                           json={"country": "Romania",
                                 "stat_or_province": "Bucuresti",
                                 "city": "Bucuresti",
                                 "street": "Strada",
                                 "apartment_or_suite": "1",
                                 "postal_code": "123456",
                                 "organization_id": org_id})
    assert response.status_code == 200
    response = client.get("/addressbook/")
    resp = json.loads(response.data)[0]
    assert resp["country"] == "Romania"
    assert resp["stat_or_province"] == "Bucuresti"
    assert resp["city"] == "Bucuresti"
    assert resp["street"] == "Strada"
    assert resp["apartment_or_suite"] == "1"
    assert resp["postal_code"] == "123456"
    assert resp["organization_id"] == org_id

    response = client.post("/inventory/",
                           json={"inv_type": "inventory",
                                 "name": "test",
                                 "description": "test",
                                 "inventory_method": "fifo",
                                 "organization_id": org_id})
    assert response.status_code == 200
    response = client.get("/inventory/")
    resp = json.loads(response.data)[0]
    assert resp["inv_type"] == "inventory"
    assert resp["name"] == "test"
    assert resp["description"] == "test"
    assert resp["inventory_method"] == "fifo"
    assert resp["organization_id"] == org_id
    inventory_id = resp["id"]

    response = client.post("/invoices/",
                           json={
                               "inv_type": "invoice",
                               "number": "0001",
                               "serial": "FF",
                               "issue_date": "2020-01-01",
                               "receive_date": "2020-01-01",
                               "due_date": "2020-01-01",
                               "payment_status": "paid",
                               "organization_id": org_id,
                               "supplier_id": org_id,
                               "client_id": org_id,
                               "currency": "RON",
                               "amount": 100,
                               "issuer_name": "test"
                           })
    assert response.status_code == 200
    response = client.get("/invoices/")
    resp = json.loads(response.data)[0]
    assert resp["inv_type"] == "invoice"
    assert resp["number"] == "0001"
    assert resp["serial"] == "FF"
    assert resp["receive_date"] == "2020-01-01 00:00:00"
    assert resp["due_date"] == "2020-01-01 00:00:00"
    assert resp["payment_status"] == "paid"
    assert resp["organization_id"] == org_id
    invoice_id = resp["id"]

    response = client.post("/inventory_item/", json={"name": "test",
                                                     "description": "test",
                                                     "quantity": 1,
                                                     "measurement_unit": "buc",
                                                     "acquisition_price": 1,
                                                     "total_value": 1,
                                                     "inventory_id": inventory_id,
                                                     "invoice_id": invoice_id})
    assert response.status_code == 200
    response = client.get("/inventory_item/")
    resp = json.loads(response.data)[0]
    assert resp["name"] == "test"
    assert resp["description"] == "test"
    assert resp["quantity"] == 1
    assert resp["measurement_unit"] == "buc"
    assert resp["acquisition_price"] == 1
    assert resp["total_value"] == 1
    assert resp["inventory_id"] == inventory_id
    assert resp["invoice_id"] == invoice_id
