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
                "organization_name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
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
                "organization_name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
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

                "agent_name": row["nume"],
                "last_name": row["prenume"],
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
                "organization_name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "on_invoice",
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

    def add_asset(self, context_table):
        for row in context_table:
            req = {
                "asset_name": row["asset_name"],
                "description": row["descriere"],
                "asset_class": row["clasa"],
                "analytical_account": row["cont_analitic"],
                "deprecation_analytical_account": row["cont_analitic_amortizare"],
                "depreciation_method": "straight_line" if row["tip_amortizare"] == "liniara" else row["tip_amortizare"],
                "total_duration": int(row["durata_utilizare"]),
                "total_amount": int(row["valoare_totala"]),
                "acquisition_date": row["data_achizitie"],
                "recording_date": row["data_inregistrare"],
            }
            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/assets/", json=req
            )
            assert response.status_code == 201
            return response

    def add_financial_holding(self, context_table, holding_type):
        for row in context_table:
            req = {
                "owner_id": self.selected_project,
                "organization_id": int(row["id_organizatie"]),
                "holding_type": holding_type,
                "quantity": int(row["cantitate"]),
                "aquisition_price": int(row["pret_achizitie"]),
                "analytical_account": row["cont_analitic"],
                "aquisition_date": row["data_achizitie"],
            }

            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/financial-holdings/", json=req
            )
            assert response.status_code == 201
            return response

    def add_liquidity_reserve(self, context_table):
        for row in context_table:
            req = {
                "owner_id": self.selected_project,
                "currency": row["moneda"],
                "quantity": int(row["cantitate"]),
                "acquisition_price": float(row["pret_achizitie"]),
                "analytical_account": row["cont_analitic"],
                "acquisition_date": row["data_achizitie"],
                "roll_type": row["tip_rulaj_valuta"],
            }

            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/liquidity/reserve/", json=req
            )
            assert response.status_code == 201
            return response

    def get_initial_account_balance(self, context_table, month):
        req_body = []
        for row in context_table:
            req = {
                "balance_date": month,
                "analytical_account": row["cont"],
                "initial_debit": float(row["debit_initial"]),
                "initial_credit": float(row["credit_initial"]),
                "debit": float(row["debit"]),
                "credit": float(row["credit"])
            }
            req_body.append(req)
        response = self.client.post(
            self.base_url + "/" + self.selected_project + "/account-balance/", json=req_body
        )
        assert response.status_code == 201
        return response

    close_month = get_initial_account_balance

    def close_balance_for_month(self, month):
        response = self.client.post(
            self.base_url + "/" + self.selected_project + "/account-balance/close/" + month
        )
        assert response.status_code == 201
        return response

    def add_transaction(self, context_table):
        for row in context_table:
            req = {
                "debit_account": row["cont_debit"],
                "credit_account": row["cont_credit"],
                "debit_amount": float(row["suma_debit"]),
                "credit_amount": float(row["suma_credit"]),
                "transaction_date": row["data"],
                "details": row["descriere"],
                "currency": "RON",
                "owner_id": self.selected_project
             }
            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/transactions/", json=req
            )
            assert response.status_code == 201
        return True

