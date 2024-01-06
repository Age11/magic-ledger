import magic_ledger.inflow.vat_mode as vat_mode
import magic_ledger.transactions.transaction_service as txn_service

class VatService:

    #it's  a singleton
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(VatService, cls).__new__(cls)
        return cls.__instance


    def generate_vat_transaction_for_purchase(self, supplier, client, item):
        if client.vat_mode == vat_mode.ON_INVOICE:
            if supplier.vat_mode == vat_mode.ON_INVOICE:
                pass



