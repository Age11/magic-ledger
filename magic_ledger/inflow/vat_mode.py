ON_CASH_IN = "on_cash_in"
ON_INVOICE = "on_invoice"
NO_VAT = "no_vat"
IMPORT = "import"
UNDETERMINED = "undetermined"

is_valid_vat_mode = lambda vat_mode: vat_mode in [ON_INVOICE, ON_CASH_IN, NO_VAT, IMPORT, UNDETERMINED]
