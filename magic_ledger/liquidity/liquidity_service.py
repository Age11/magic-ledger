from magic_ledger import db
from magic_ledger.liquidity.ForeignCurrencyRoll import ForeignCurrencyRoll


def create_foreign_currency_roll(request_body):
    roll_data = {k: request_body[k] for k in (
        "owner_id", "currency", "quantity", "acquisition_price", "analytical_account", "acquisition_date", "roll_type")}

    new_roll = ForeignCurrencyRoll(**roll_data)
    db.session.add(new_roll)
    db.session.commit()
    return new_roll