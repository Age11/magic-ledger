from magic_ledger.inflow.vat_service import VatService
from magic_ledger.invoices.invoice import Invoice
from magic_ledger.inventory.inventory_items import InventoryItem
import magic_ledger.third_parties.organization_service as tps
from magic_ledger.transactions.transaction import Transaction
from magic_ledger import db

class InflowService:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(InflowService, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.vat_service = VatService()

    def register_local_purchase(self, document_type, serial_number, receive_date, due_date, issue_date, payment_status, owner_id,
                       supplier_id, client_id, currency, issuer_name, items):

        #create an invoice
        new_invoice = Invoice(
            document_type=document_type,
            serial_number=serial_number,
            receive_date=receive_date,
            issue_date=issue_date,
            due_date=due_date,
            payment_status=payment_status,
            owner_id=owner_id,
            supplier_id=supplier_id,
            client_id=client_id,
            currency=currency,
            issuer_name=issuer_name,
        )

        value = 0
        vat_amount = 0

        supplier = tps.get_supplier_by_id(supplier_id=supplier_id, owner_id=owner_id)
        client = tps.get_project_organization(owner_id=owner_id)

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

            db.session.add(item)
            new_transaction = Transaction(
                debit_account_id=item.in_analytical_account,
                credit_account_id=supplier.id,
                debit_amount=value,
                credit_amount=value,
                currency="RON",
                transaction_date=new_invoice.receive_date.strftime("%Y-%m-%d"),
                owner_id=owner_id,
                details="details",
            )
            db.session.add(new_transaction)

            self.vat_service.generate_vat_transaction_for_purchase(supplier, client, item)

        new_invoice.total_value = value + vat_amount
        db.session.add(new_invoice)
        db.session.commit()








