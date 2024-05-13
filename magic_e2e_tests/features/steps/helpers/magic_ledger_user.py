import json

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
                "vat_mode": "facturare",
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
            response = self.client.post(self.base_url + "/projects/", json=req)
            assert response.status_code == 201
            self.selected_project = response.headers["location"].split("/")[2]
            return response

    def create_supplier(self, context_table):
        for row in context_table:
            req = {
                "organization_name": row["organizatie"],
                "cif": row["cif"],
                "nrc": row["nrc"],
                "vat_mode": "facturare",
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
                "vat_mode": "facturare",
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
                "vat_mode": "facturare",
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
                "depreciation_method": row["tip_amortizare"],
                "total_duration": int(row["durata_utilizare"]),
                "initial_value": float(row["valoare_initiala"]),
                "inventory_value": float(row["valoare_inventar"]),
                "current_value": float(row["valoare_curenta"]),
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
                self.base_url + "/" + self.selected_project + "/financial-holdings/",
                json=req,
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
                self.base_url + "/" + self.selected_project + "/liquidity/reserve/",
                json=req,
            )
            assert response.status_code == 201
            return response

    def create_initial_account_balance(self, context_table, date):
        req_body = []
        for row in context_table:
            req = {
                "balance_date": date,
                "analytical_account": row["cont"],
                "initial_debit": float(row["debit_initial"]),
                "initial_credit": float(row["credit_initial"]),
                "cumulated_debit": float(row["debit_cumulat"]),
                "cumulated_credit": float(row["credit_cumulat"]),
            }
            req_body.append(req)
        print(req_body)
        response = self.client.post(
            self.base_url + "/" + self.selected_project + "/account-balance/",
            json=req_body,
        )
        assert response.status_code == 201
        return response

    close_month = create_initial_account_balance

    def close_balance_for_month(self, balance_date):
        r1 = self.client.put(
            f"{self.base_url}/{self.selected_project}/transactions/generate-close-vat-transactions/{balance_date}"
        )
        assert r1.status_code == 201
        r2 = self.client.put(
            f"{self.base_url}/{self.selected_project}/transactions/generate-close-income-expenses-transactions/{balance_date}"
        )
        assert r2.status_code == 201
        r3 = self.client.put(
            f"{self.base_url}/{self.selected_project}/account-balance/close/{balance_date}"
        )
        assert r3.status_code == 201

        return r3

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
                "owner_id": self.selected_project,
            }
            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/transactions/", json=req
            )
            assert response.status_code == 201
        return True

    def create_inventory(self, context_table):
        for row in context_table:
            req = {
                "name": row["nume"],
                "description": row["descriere"],
                "inventory_method": row["metoda_inventariere"],
            }
            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/inventories/", json=req
            )
            return response

    def add_item(self, context):
        for row in context:
            req = {
                "name": row["nume_articol"],
                "description": row["descriere"],
                "quantity": int(row["cantitate"]),
                "measurement_unit": row["unitate_masura"],
                "acquisition_price": round(float(row["pret_unitar"]), 2),
                "sale_price": round(float(row["pret_vanzare"]), 2),
                "currency": "RON",
                "vat_rate": round(float(row["cota_tva"]), 2),
                "invoice_id": -int(self.selected_project),
            }

            if "data_achizitie" in row.headings:
                req["acquisition_date"] = row["data_achizitie"]

            response = self.client.post(
                self.base_url
                + "/"
                + self.selected_project
                + "/inventories/"
                + "-"
                + self.selected_project
                + "/items/",
                json=req,
            )
            return response

    def add_inventory_item(self, context):
        for row in context:
            req = {
                "name": row["nume_articol"],
                "description": row["descriere"],
                "quantity": int(row["cantitate"]),
                "measurement_unit": row["unitate_masura"],
                "acquisition_price": round(float(row["pret_unitar"]), 2),
                "sale_price": round(float(row["pret_vanzare"]), 2),
                "currency": "RON",
                "vat_rate": round(float(row["cota_tva"]), 2),
                "invoice_id": -int(self.selected_project),
                "acquisition_date": row["data_achizitie"],
            }
            response = self.client.post(
                self.base_url
                + "/"
                + self.selected_project
                + "/inventories/"
                + row["id_inventar"]
                + "/items/",
                json=req,
            )
            return response

    def add_invoice(self, context):
        for row in context:
            req = {
                "serial_number": row["serie"],
                "invoice_type": row["tip_factura"],
                "payment_type": row["tip_plata"],
                "invoice_date": row["data_factura"],
                "due_date": row["data_scadenta"],
                "supplier_id": int(row["id_furnizor"]),
                "client_id": int(row["id_client"]),
                "currency": row["moneda"],
                "amount": round(float(row["valoare_factura"]), 2),
                "vat_amount": round(float(row["valoare_tva"]), 2),
                "amount_due": round(float(row["valoare_factura"]), 2)
                + round(float(row["valoare_tva"]), 2),
                "issuer_name": row["nume_emitent"],
            }
            if "tip_client" in row.headings:
                req["client_type"] = row["tip_client"]
            response = self.client.post(
                self.base_url + "/" + self.selected_project + "/invoices/", json=req
            )
            return response

    def add_invoice_item(self, context):
        for row in context:
            if row["pret_vanzare"] == "N/A":
                req = {
                    "name": row["nume_articol"],
                    "description": row["descriere"],
                    "quantity": int(row["cantitate"]),
                    "measurement_unit": row["unitate_masura"],
                    "acquisition_price": round(float(row["pret_unitar"]), 2),
                    "sale_price": None,
                    "currency": "RON",
                    "vat_rate": round(float(row["cota_tva"]), 2),
                    "invoice_id": row["id_factura"],
                }
            else:
                req = {
                    "name": row["nume_articol"],
                    "description": row["descriere"],
                    "quantity": int(row["cantitate"]),
                    "measurement_unit": row["unitate_masura"],
                    "acquisition_price": round(float(row["pret_unitar"]), 2),
                    "sale_price": round(float(row["pret_vanzare"]), 2),
                    "currency": "RON",
                    "vat_rate": round(float(row["cota_tva"]), 2),
                    "invoice_id": row["id_factura"],
                }
            response = self.client.post(
                self.base_url
                + "/"
                + self.selected_project
                + "/inventories/"
                + row["id_inventar"]
                + "/items/",
                json=req,
            )
            return response

    def add_invoice_item_no_inventory(self, context):
        for row in context:
            req = {
                "name": row["nume_articol"],
                "description": row["descriere"],
                "quantity": int(row["cantitate"]),
                "measurement_unit": row["unitate_masura"],
                "acquisition_price": round(float(row["pret_unitar"]), 2),
                "sale_price": None,
                "currency": "RON",
                "vat_rate": round(float(row["cota_tva"]), 2),
                "invoice_id": row["id_factura"],
            }
            response = self.client.post(
                self.base_url
                + "/"
                + self.selected_project
                + "/inventories/"
                + "-1"
                + "/items/",
                json=req,
            )
            return response

    def add_accounting_treatment(self, request_body):
        response = self.client.post(
            self.base_url
            + "/"
            + self.selected_project
            + "/transaction-group-templates/",
            json=request_body,
        )
        return response

    def make_transaction_from_template(self, context):
        for row in context:
            req = {
                "transaction_date": row["data_inregistrarii"],
                "amount": round(float(row["suma"]), 2),
                "document_serial_number": row["serie_document"],
                "document_id": row["id_document"],
            }

            response = self.client.post(
                self.base_url
                + "/"
                + self.selected_project
                + "/transaction-group-templates/"
                + str(row["id_sablon"])
                + "/use-template",
                json=req,
            )
        return response

    def decrease_stock(self, context):
        for row in context:
            r1 = requests.put(
                f'{self.base_url}/{self.selected_project}/inventories/{row["id_gestiune"]}/items/{row["id_articol"]}/decrease-stock',
                json={
                    "quantity": int(row["cantitate"]),
                    "invoice_id": row["id_factura"],
                },
            )
            return r1

    def create_payment(self, context):
        for row in context:
            req = {
                "amount": round(float(row["suma"]), 2),
                "amount_due": round(float(row["suma"]), 2),
                "payment_date": row["data_plata"],
                "payment_type": row["tip_plata"],
                "payment_status": "restantă",
                "due_date": row["data_scadenta"],
                "currency": "RON",
                "invoice_id": row["id_factura"],
                "transaction_id": row["id_tranzactie"],
            }
            response = self.client.post(
                f"{self.base_url}/{self.selected_project}/payments/", json=req
            )
            return response

    def solve_payment(self, context):
        for row in context:
            r1 = requests.put(
                f'{self.base_url}/{self.selected_project}/payments/{row["id_plata"]}/pay',
                json={
                    "amount": round(float(row["suma"]), 2),
                    "installment_type": row["tip_plată"],
                },
            )
            return r1

    def add_payment(self, context):
        for row in context:
            req = {
                "payment_date": row["data_plata"],
                "due_date": row["data_scadenta"],
                "amount_due": round(float(row["suma"]), 2),
                "payment_type": row["tip_plata"],
                "payment_status": "restantă",
                "currency": "RON",
                "invoice_id": row["id_factura"],
            }
            response = self.client.post(
                f"{self.base_url}/{self.selected_project}/payments/", json=req
            )
            return response
