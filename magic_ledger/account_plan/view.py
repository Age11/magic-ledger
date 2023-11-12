import json

from flask import Blueprint
from flask import request
from magic_ledger.account_plan.model import AccountPlan
import logging

bp = Blueprint("account_plan", __name__, url_prefix="/account-plan")
@bp.route("/")
def accounts():
    if request.method == "GET":
        res = AccountPlan.query.all()
        l = []
        for act in res:
            l.append(act.__getstate__())
        json_data = json.dumps([row.__getstate__() for row in res], default=str)
        return json_data


