import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.assets.assets import Asset
from magic_ledger.financial_holdings.financial_holdings import FinancialHoldings

bp = Blueprint("financial_holdings", __name__, url_prefix="/<project_id>/financial-holdings")


@bp.route("/", methods=("GET", "POST"))
def financial_holdings(project_id):
    if request.method == "POST":
        logging.info("""Creating financial holding with the following data:""")
        logging.info(request.json)

        owner_id = project_id
        organization_id = request.json["organization_id"]
        holding_type = request.json["holding_type"]
        quantity = request.json["quantity"]
        aquisition_price = request.json["aquisition_price"]
        analytical_account = request.json["analytical_account"]
        aquisition_date = request.json["aquisition_date"]

        financial_holding = FinancialHoldings(
            owner_id=owner_id,
            organization_id=organization_id,
            holding_type=holding_type,
            quantity=quantity,
            aquisition_price=aquisition_price,
            analytical_account=analytical_account,
            aquisition_date=aquisition_date,
        )

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
