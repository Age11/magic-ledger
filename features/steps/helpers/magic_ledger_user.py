import requests


class MagicLedgerUser:
    selected_project = None
    client = requests.session()

    def __init__(self, base_url):
        self.base_url = base_url

    def create_project(self, context_table):
        for row in context_table:
            req = {
                "name": row["nume"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
                "caen_code": row["cod_caen"],
                "status": "active",
                "org_type": "project",
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
                self.base_url + "/organizations/projects", json=req
            )
            response.headers["location"].split("/")[2]
            self.selected_project = response.headers["location"].split("/")[2]
            return response
