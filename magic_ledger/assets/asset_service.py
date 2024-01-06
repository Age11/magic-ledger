from magic_ledger import db
from magic_ledger.assets.assets import Asset


def create_asset(request_body):
    asset_data = {k: request_body[k] for k in
                          ("asset_name", "description", "asset_class", "depreciation_method", "total_amount", "total_duration", "acquisition_date", "recording_date", "analytical_account", "deprecation_analytical_account", "owner_id")}
    new_asset = Asset(**asset_data)
    db.session.add(new_asset)
    db.session.commit()
    return new_asset

def get_all(owner_id):
    return Asset.query.filter_by(owner_id=owner_id).all()