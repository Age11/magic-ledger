import logging

from flask import Blueprint, jsonify, request

from magic_ledger import db
from magic_ledger.liquidity import liquidity_service
from magic_ledger.liquidity.ForeignCurrencyRoll import ForeignCurrencyRoll

bp = Blueprint("liquidity", __name__, url_prefix="/<project_id>/liquidity")


@bp.route("/reserve/", methods=("GET", "POST"))
def add_liquidity(project_id):
    if request.method == "POST":
        logging.info("""Creating currency amount with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)

        currency_reserve = liquidity_service.create_foreign_currency_roll(request.json)

        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/liquidity/reserve/" + str(currency_reserve.id)
        return response
    elif request.method == "GET":
        res = ForeignCurrencyRoll.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in res])


