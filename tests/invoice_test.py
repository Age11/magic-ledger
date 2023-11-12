import csv
import json
import pytest

@pytest.fixture(autouse=True)
def provision_organizations(client, app):
    # read the test data organizations csv file and map the data to dictionaries
    with open(r'C:\Users\ageor\PycharmProjects\magic-ledger\tests\test_data\organizations.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        org_data = list(csv_reader)
        print(org_data)
    for org in org_data:
        # map the data to the organization model
        org_payload = {
            "name": org["name"],
            "cif": org["cif"],
            "nrc": org["nrc"],
            "phone": org["phone"],
            "email": org["email"],
            "vat_mode": org["vat_mode"],
            "status": org["status"],
            "type": org["type"],
            "caen_code": org["caen_code"]
        }

        # create the organization
        response = client.post("/organizations/",
                               json=org_payload)
        assert response.status_code == 201

        org_id = str(response.headers['location']).split('/')[2]

        address = {
            "country": org["country"],
            "stat_or_province": org["stat_or_province"],
            "city": org["city"],
            "street": org["street"],
            "apartment_or_suite": org["apartment_or_suite"],
            "postal_code": org["postal_code"],
            "organization_id": org_id
        }

        response = client.post("/organizations/addressbook",
                               json=address)
        assert response.status_code == 200

        bank_details = {
            "account": org["account"],
            "details": org["details"],
            "organization_id": org_id}

        response = client.post("/organizations/banking-details",
                                 json=bank_details)
        assert response.status_code == 200

    response = client.get("/organizations/")
    assert response.status_code == 200
    resp = json.loads(response.data)
    assert len(resp) == 5

def test_inventory_items(client, app):
    response = client.get("/organizations/")
    for org in json.loads(response.data):
        if org["type"] == "project":
            org_id = org["id"]
            break
    inventory = {
        "name" : "test",
        "description" : "inventar1",
        "inv_type" : "marfuri",
        "inventory_method": "lifo",
        "organization_id" : org_id
    }
    response = client.post("/inventory/", json=inventory)
    assert response.status_code == 200






