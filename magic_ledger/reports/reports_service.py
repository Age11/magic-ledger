from magic_ledger.inventory.inventory_service import get_items_from_invoice
from magic_ledger.invoices import client_types
from magic_ledger.invoices.invoice_service import (
    get_all_incoming_invoices_by_date,
    get_all_outgoing_invoices_by_date,
)
from magic_ledger.third_parties.service.agent_service import get_agent_by_id
from magic_ledger.third_parties.service.organization_service import (
    get_supplier_by_id,
    get_client_by_id,
)
from magic_ledger.transactions.transaction_service import get_all_transactions_for_month


def generate_purchase_journal(owner_id, invoice_date):
    # This function generates a buy report
    invs = get_all_incoming_invoices_by_date(owner_id, invoice_date)
    res = []
    for inv in invs:
        supplier = get_supplier_by_id(inv.supplier_id, owner_id)
        items = get_items_from_invoice(inv.id)
        regular_amount = 0
        regular_vat_amount = 0
        reduced_amount = 0
        reduced_vat_amount = 0
        no_vat_amount = 0
        for item in items:
            if item.vat_rate == 19:
                regular_amount += item.total_value
                regular_vat_amount += item.total_value * item.vat_rate / 100
            elif item.vat_rate == 0:
                no_vat_amount += item.total_value
            else:
                reduced_amount += item.total_value
                reduced_vat_amount += item.total_value * item.vat_rate / 100

        payed = True
        if supplier.vat_mode == "on_cash_in" and inv.payment_status == "restantă":
            payed = False
        res.append(
            {
                "date": inv.invoice_date.strftime("%Y-%m-%d"),
                "supplier_name": supplier.organization_name,
                "supplier_vat_code": "NOT_IMPLEMENTED",
                "total": inv.total_amount,
                "amount": inv.amount,
                "vat_amount": inv.vat_amount,
                "regular_amount": regular_amount,
                "regular_vat_amount": regular_vat_amount,
                "reduced_amount": reduced_amount,
                "reduced_vat_amount": reduced_vat_amount,
                "no_vat_amount": no_vat_amount,
                "payed": payed,
            }
        )
    return res


def generate_sales_journal(owner_id, invoice_date):
    # This function generates a buy report
    invs = get_all_outgoing_invoices_by_date(owner_id, invoice_date)
    res = []
    for inv in invs:
        if inv.client_type == client_types.ORGANIZATION:
            client = get_client_by_id(inv.client_id, owner_id)
            client_name = client.organization_name
        elif inv.client_type == client_types.PERSON:
            client = get_agent_by_id(inv.client_id, owner_id)
            client_name = client.agent_name + " " + client.last_name

        items = get_items_from_invoice(inv.id)
        regular_amount = 0
        regular_vat_amount = 0
        reduced_amount = 0
        reduced_vat_amount = 0
        no_vat_amount = 0
        for item in items:
            if item.vat_rate == 19:
                regular_amount += item.total_value
                regular_vat_amount += item.total_value * item.vat_rate / 100
            elif item.vat_rate == 0:
                no_vat_amount += item.total_value
            else:
                reduced_amount += item.total_value
                reduced_vat_amount += item.total_value * item.vat_rate / 100

        payed = True
        # TODO gaseste cazuri de neexigibilitate
        # if supplier.vat_mode == "on_cash_in" and inv.payment_status == "restantă":
        #     payed = False
        res.append(
            {
                "date": inv.invoice_date.strftime("%Y-%m-%d"),
                "client_name": client_name,
                "client_vat_code": "NOT_IMPLEMENTED",
                "total": inv.total_amount,
                "amount": inv.amount,
                "vat_amount": inv.vat_amount,
                "regular_amount": regular_amount,
                "regular_vat_amount": regular_vat_amount,
                "reduced_amount": reduced_amount,
                "reduced_vat_amount": reduced_vat_amount,
                "no_vat_amount": no_vat_amount,
                "payed": payed,
            }
        )
    return res


def get_general_ledger_entry(owner_id, balance_date, account):
    transactions = get_all_transactions_for_month(owner_id, balance_date)
    res = {"debit": [], "credit": []}
    for tx in transactions:
        if tx.debit_account == account:
            res["debit"].append(
                {
                    "account": account,
                    "date": tx.transaction_date.strftime("%Y-%m-%d"),
                    "debit": tx.debit_amount,
                }
            )
        if tx.credit_account == account:
            res["credit"].append(
                {
                    "account": account,
                    "date": tx.transaction_date.strftime("%Y-%m-%d"),
                    "credit": tx.credit_amount,
                }
            )
    return res
