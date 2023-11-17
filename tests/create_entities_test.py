import json
from tests.test_data import test_data

def test_post_get_entities(client, app):
    #create an organization
    org_data = test_data['organizations'][0]
    response = client.post("/organizations/",
                           json=org_data)
    assert response.status_code == 201
    assert response.headers['location'] == '/organizations/1'

    org_path = response.headers['location']
    response = client.get(org_path)
    assert response.status_code == 200
    resp = json.loads(response.data)
    assert resp["name"] == "test"

    #retrieve all organization

    response = client.get("/organizations/")
    assert response.status_code == 200

    #verify the response
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

    #save the id
    org_id = resp["id"]

    #add organization address
    org_address = test_data['address'][0]
    org_address["organization_id"] = org_id
    response = client.post("/organizations/addressbook",
                           json=org_address)
    assert response.status_code == 200

    #retrieve all addresses
    response = client.get("/organizations/addressbook")
    resp = json.loads(response.data)[0]

    #verify the response
    assert resp["country"] == "Romania"
    assert resp["stat_or_province"] == "Bucuresti"
    assert resp["city"] == "Bucuresti"
    assert resp["street"] == "Strada"
    assert resp["apartment_or_suite"] == "1"
    assert resp["postal_code"] == "123456"
    assert resp["organization_id"] == org_id

    #add organization banking details
    bank_details = test_data['banking_details'][0]
    bank_details["organization_id"] = org_id
    response = client.post("/organizations/banking-details", json=bank_details)
    assert response.status_code == 200

    #retrieve all banking details
    response = client.get("/organizations/banking-details")
    resp = json.loads(response.data)[0]

    #verify the response
    assert resp["account"] == "test"
    assert resp["details"] == "test"
    assert resp["organization_id"] == org_id

    #add organization inventory
    org_inventory = test_data['inventory'][0]
    org_inventory["organization_id"] = org_id
    response = client.post("/inventory/",
                           json=org_inventory)
    assert response.status_code == 201

    #retrieve all inventoryes
    response = client.get("/inventory/")
    resp = json.loads(response.data)[0]

    #verify the response
    assert resp["inv_type"] == "stock"
    assert resp["name"] == "test"
    assert resp["description"] == "test"
    assert resp["inventory_method"] == "fifo"
    assert resp["organization_id"] == org_id
    inventory_id = resp["id"]

    #add invoice
    org_invoice = test_data['invoices'][0]
    org_invoice["organization_id"] = org_id
    org_invoice["supplier_id"] = org_id
    org_invoice["client_id"] = org_id
    response = client.post("/invoices/",
                           json=org_invoice)
    assert response.status_code == 201

    #retrieve all invoices
    response = client.get("/invoices/")
    resp = json.loads(response.data)[0]

    #verify the response
    assert resp["inv_type"] == "invoice"
    assert resp["number"] == "0001"
    assert resp["serial"] == "FF"
    assert resp["receive_date"] == "2020-01-01 00:00:00"
    assert resp["due_date"] == "2020-01-01 00:00:00"
    assert resp["issue_date"] == "2020-01-01 00:00:00"
    assert resp["payment_status"] == "paid"
    assert resp["organization_id"] == org_id
    assert resp["supplier_id"] == org_id
    assert resp["client_id"] == org_id
    assert resp["amount"] == 100.00
    assert resp["currency"] == "RON"
    assert resp["issuer_name"] == "issuer_name"
    invoice_id = resp["id"]

    #add inventory item
    item = test_data['items'][0]
    item["inventory_id"] = inventory_id
    item["invoice_id"] = invoice_id
    response = client.post("/inventory/items/", json=item)
    assert response.status_code == 201

    #retrieve all inventory items
    response = client.get("/inventory/items/")
    resp = json.loads(response.data)[0]

    #verify the response
    assert resp["name"] == "test"
    assert resp["description"] == "test"
    assert resp["quantity"] == 1
    assert resp["measurement_unit"] == "buc"
    assert resp["acquisition_price"] == 100
    assert resp["total_value"] == 100
    assert resp["inventory_id"] == inventory_id
    assert resp["invoice_id"] == invoice_id

    #

    response = client.get("/account-plan/")
    assert response.status_code == 200
    resp = json.loads(response.data)
