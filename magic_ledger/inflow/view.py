import logging

from flask import Blueprint, flash, jsonify, request

from magic_ledger import db
from magic_ledger.inflow.inflow_service import InflowService
from magic_ledger.inventory.inventory import Inventory
from magic_ledger.inventory.inventory_items import InventoryItem

bp = Blueprint("inflow", __name__, url_prefix="/<project_id>/inflow")
inflow_service = InflowService()


@bp.route("/local-purchase", methods=("GET", "POST"))
def inventory(project_id):
    if request.method == "POST":
        logging.info("""Creating inventory with the following data:""")
        logging.info(request.json)

        inflow_service.register_local_purchase(document_type=request.json["document_type"],
                                               serial_number=request.json["serial_number"],
                                               receive_date=request.json["receive_date"],
                                               due_date=request.json["due_date"],
                                               issue_date=request.json["issue_date"],
                                               payment_status=request.json["payment_status"],
                                               owner_id=project_id,
                                               supplier_id=request.json["supplier_id"],
                                               client_id=request.json["client_id"],
                                               currency=request.json["currency"],
                                               issuer_name=request.json["issuer_name"],
                                               items=request.json["items"])

        response = jsonify()
        response.status_code = 201
        return response
