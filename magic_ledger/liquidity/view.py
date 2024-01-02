import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset
from magic_ledger.financial_holdings.financial_holdings import FinancialHoldings
from magic_ledger.liquidity.ForeignCurrencyReserves import ForeignCurrencyReserves

bp = Blueprint("liquidity_reserves", __name__, url_prefix="/<project_id>/liquidity")


@bp.route("/reserve/", methods=("GET", "POST"))
def add_liquidity(project_id):
    if request.method == "POST":
        logging.info("""Creating currency amount with the following data:""")
        logging.info(request.json)

        owner_id = project_id
        currency_type = request.json["currency_type"]
        quantity = request.json["quantity"]
        acquisition_price = request.json["acquisition_price"]
        analytical_account = request.json["analytical_account"]
        acquisition_date = request.json["acquisition_date"]

        currency_reserve = ForeignCurrencyReserves(
            owner_id=owner_id,
            currency_type=currency_type,
            quantity=quantity,
            acquisition_price=acquisition_price,
            analytical_account=analytical_account,
            acquisition_date=acquisition_date,
        )

        db.session.add(currency_reserve)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/liquidity/reserve/" + str(currency_reserve.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = ForeignCurrencyReserves.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in res])
