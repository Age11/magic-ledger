import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset
import magic_ledger.assets.asset_service as asset_service


bp = Blueprint("assets", __name__, url_prefix="/<project_id>/assets")


@bp.route("/", methods=("GET", "POST"))
def assets(project_id):
    if request.method == "POST":
        logging.info("""Creating asset with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)

        asset = asset_service.create_asset(request.json)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/assets/" + str(asset.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = asset_service.get_all(project_id)
        return jsonify([row.__getstate__() for row in res])
