import requests


class MagicLedgerUser:
    selected_project = None
    client = requests.session()

    def __init__(self, base_url):
        self.base_url = base_url

    def create_project(self, context_table):
        for row in context_table:
            req = {
                "project_name": row["nume"],
                "organization_name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
                "caen_code": row["cod_caen"],
                "status": "active",
                "org_type": row["tip"],
                "country": row["tara"],
                "state_or_province": row["judet"],
                "city": row["oras"],
                "street": row["strada"],
                "apartment_or_suite": row["numar"],
                "postal_code": row["cod_postal"],
                "phone": row["telefon"],
                "email": row["email"],
                "account": row["cont_bancar"],
                "details": row["detalii"]
            }
            response = self.client.post(
                self.base_url + "/projects/", json=req
            )
            assert response.status_code == 201
            self.selected_project = response.headers["location"].split("/")[2]
            return response

    def create_supplier(self, context_table):
        for row in context_table:
            req = {
                "name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
                "caen_code": row["cod_caen"],
                "status": "active",
                "org_type": row["tip"],
                "country": row["tara"],
                "state_or_province": row["judet"],
                "city": row["oras"],
                "street": row["strada"],
                "apartment_or_suite": row["numar"],
                "postal_code": row["cod_postal"],
                "phone": row["telefon"],
                "email": row["email"],
                "account": row["cont_bancar"],
                "details": row["detalii"],
            }
            response = self.client.post(
                self.base_url + "/1/third-parties/organizations/suppliers/", json=req
            )
            assert response.status_code == 201
            return response

    def create_client(self, context_table):
        for row in context_table:
            req = {
                "name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
                "caen_code": row["cod_caen"],
                "status": "active",
                "org_type": row["tip"],
                "country": row["tara"],
                "state_or_province": row["judet"],
                "city": row["oras"],
                "street": row["strada"],
                "apartment_or_suite": row["numar"],
                "postal_code": row["cod_postal"],
                "phone": row["telefon"],
                "email": row["email"],
                "account": row["cont_bancar"],
                "details": row["detalii"],
            }
            response = self.client.post(
                self.base_url + "/1/third-parties/organizations/clients/", json=req
            )
            assert response.status_code == 201
            return response

    def create_client_agent(self, context_table):
        for row in context_table:
            req = {

                "name": row["nume"],
                "middle_name": row["prenume1"],
                "surname": row["prenume"],
                "cnp": row["cnp"],
                "country": row["tara"],
                "state_or_province": row["judet"],
                "city": row["oras"],
                "street": row["strada"],
                "apartment_or_suite": row["numar"],
                "postal_code": row["cod_postal"],
                "phone": row["telefon"],
                "email": row["email"],
                "account": row["cont"],
                "details": row["detalii"],

            }
            response = self.client.post(
                self.base_url + "/1/third-parties/agents/clients/", json=req
            )
            assert response.status_code == 201
            return response

    def create_affiliate_organization(self, context_table):
        for row in context_table:
            req = {
                "name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
                "caen_code": row["cod_caen"],
                "status": "active",
                "org_type": row["tip"],
                "country": row["tara"],
                "state_or_province": row["judet"],
                "city": row["oras"],
                "street": row["strada"],
                "apartment_or_suite": row["numar"],
                "postal_code": row["cod_postal"],
                "phone": row["telefon"],
                "email": row["email"],
                "account": row["cont_bancar"],
                "details": row["detalii"],
            }
            response = self.client.post(
                self.base_url + "/1/third-parties/organizations/affiliates/", json=req
            )
            assert response.status_code == 201
            return response
