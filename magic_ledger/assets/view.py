import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset

bp = Blueprint("assets", __name__, url_prefix="/assets")


@bp.route("/", methods=("GET", "POST"))
def inventory():
    if request.method == "POST":
        logging.info("""Creating asset with the following data:""")
        logging.info(request.json)

        name = request.json["name"]
        description = request.json["description"]
        asset_class = request.json["asset_class"]
        depreciation_method = request.json["depreciation_method"]
        total_duration = request.json["total_duration"]
        total_amount = request.json["total_amount"]
        acquisition_date = request.json["acquisition_date"]
        organization_id = request.json["organization_id"]

        asset = Asset(
            name=name,
            description=description,
            asset_class=asset_class,
            depreciation_method=depreciation_method,
            total_amount=total_amount,
            total_duration=total_duration,
            acquisition_date=acquisition_date,
            organization_id=organization_id,
        )

        db.session.add(asset)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/assets/" + str(asset.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = Asset.query.all()
        return jsonify([row.__getstate__() for row in res])
