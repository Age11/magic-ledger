import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset


bp = Blueprint("assets", __name__, url_prefix="/<project_id>/assets")


@bp.route("/", methods=("GET", "POST"))
def assets(project_id):
    if request.method == "POST":
        logging.info("""Creating asset with the following data:""")
        logging.info(request.json)

        asset_name = request.json["asset_name"]
        description = request.json["description"]
        asset_class = request.json["asset_class"]
        depreciation_method = request.json["depreciation_method"]
        total_duration = request.json["total_duration"]
        total_amount = request.json["total_amount"]
        acquisition_date = request.json["acquisition_date"]
        recording_date = request.json["recording_date"]
        analytical_account = request.json["analytical_account"]
        deprecation_analytical_account = request.json["deprecation_analytical_account"]

        asset = Asset(
            asset_name=asset_name,
            description=description,
            asset_class=asset_class,
            depreciation_method=depreciation_method,
            total_amount=total_amount,
            total_duration=total_duration,
            acquisition_date=acquisition_date,
            owner_id=project_id,
            recording_date=recording_date,
            analytical_account=analytical_account,
            deprecation_analytical_account=deprecation_analytical_account,
        )

        db.session.add(asset)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/assets/" + str(asset.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = Asset.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in res])
