import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset
from magic_ledger.financial_holdings import financial_holdings_service
from magic_ledger.financial_holdings.financial_holdings import FinancialHoldings

bp = Blueprint("financial_holdings", __name__, url_prefix="/<project_id>/financial-holdings")


@bp.route("/", methods=("GET", "POST"))
def financial_holdings(project_id):
    if request.method == "POST":
        logging.info("""Creating financial holding with the following data:""")
        request.json["owner_id"] = project_id
        logging.info(request.json)

        financial_holding = financial_holdings_service.create_financial_holding(request.json)

        db.session.add(financial_holding)
        db.session.commit()
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = "/" + project_id + "/financial-holdings/" + str(financial_holding.id)
        response.autocorrect_location_header = False
        return response
    elif request.method == "GET":
        res = FinancialHoldings.query.filter_by(owner_id=project_id).all()
        return jsonify([row.__getstate__() for row in res])
