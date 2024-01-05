import logging

from flask import Blueprint, jsonify, request

from magic_ledger import db
from magic_ledger.exchange.ExchangeRates import ExchangeRate

bp = Blueprint("exchange", __name__, url_prefix="/exchange/")

@bp.route("/", methods=("GET", "POST"))
def exchange():
    if request.method == "POST":
        logging.info("""Creating exchange entry following data:""")
        logging.info(request.json)

        currency_type = request.json["currency_type"]
        value_in_ref_currency = request.json["value_in_ref_currency"]
        reference_currency = request.json["reference_currency"]
        date = request.json["date"]

        new_exchange_entry = ExchangeRate(
            currency_type=currency_type,
            value=value_in_ref_currency,
            reference_currency=reference_currency,
            date=date
        )

        db.session.add(new_exchange_entry)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/exchange/" + str(new_exchange_entry.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        exchange_board = ExchangeRate.query.all()
        return jsonify([row.__getstate__() for row in exchange_board])
