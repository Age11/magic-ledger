from magic_ledger.invoices.invoice import Invoice
from magic_ledger.misc.currency import Currency
from magic_ledger.inventory.inventory_items import InventoryItem
from magic_ledger.transactions.transaction import Transaction
from magic_ledger.liquidity.LiquidityService import LiquidityService

class InflowService:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(InflowService, cls).__new__(cls)
        return cls.__instance

    def local_purchase(self, inv_type, serial_number, receive_date, due_date, issue_date, payment_status, project_id,
                       supplier_id, client_id, currency, issuer_name, items):

        #create an invoice
        new_invoice = Invoice(
            inv_type=inv_type,
            serial_number=serial_number,
            receive_date=receive_date,
            issue_date=issue_date,
            due_date=due_date,
            payment_status=payment_status,
            owner_id=project_id,
            supplier_id=supplier_id,
            client_id=client_id,
            currency=currency,
            issuer_name=issuer_name,
        )

        value = 0
        vat_amount = 0

        for item_data in items:
            item = InventoryItem(
                name=item_data["name"],
                description=item_data["description"],
                quantity=item_data["quantity"],
                measurement_unit=item_data["measurement_unit"],
                acquisition_price=item_data["acquisition_price"],
                vat_rate=item_data["vat_rate"],
                in_analytical_account=item_data["in_analytical_account"],
                out_analytical_account=item_data["out_analytical_account"],
                inventory_id=item_data["inventory_id"],
                invoice_id=new_invoice.id,
            )
            value += item.value
            vat_amount += item.vat_amount

        new_invoice.total_value = value + vat_amount

        #insert a transaction for the invoice
        new_transaction = Transaction(
            debit_account_id="401",
            credit_account_id="271",
            debit_amount=value,
            credit_amount=value,
            currency="RON",
            transaction_date=new_invoice.receive_date,
            owner_id=project_id,
            details="details",
        )

        #handle the VAT transaction
        vat_transaction = Transaction(
            debit_account_id="401",
            credit_account_id="4427",
            debit_amount=vat_amount,
            credit_amount=vat_amount,
            currency="RON",
            transaction_date=new_invoice.receive_date,
            owner_id=project_id,
            details="details",
        )








