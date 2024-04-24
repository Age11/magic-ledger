from magic_ledger import db
from magic_ledger.assets.assets import Asset


def create_asset(request_body):
    asset_data = {
        k: request_body[k]
        for k in (
            "asset_name",
            "description",
            "depreciation_method",
            "initial_value",
            "inventory_value",
            "current_value",
            "total_duration",
            "acquisition_date",
            "recording_date",
            "owner_id",
        )
    }
    new_asset = Asset(**asset_data)
    db.session.add(new_asset)
    db.session.commit()
    return new_asset


def get_all(owner_id):
    return Asset.query.filter_by(owner_id=owner_id).all()
