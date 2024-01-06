from magic_ledger import db
from magic_ledger.financial_holdings.financial_holdings import FinancialHoldings

def create_financial_holding(request_body):
    financial_holding_data = {k: request_body[k] for k in
                          ("owner_id", "organization_id", "holding_type", "quantity", "aquisition_price", "analytical_account", "aquisition_date")}
    new_financial_holding = FinancialHoldings(**financial_holding_data)
    db.session.add(new_financial_holding)
    db.session.commit()
    return new_financial_holding


