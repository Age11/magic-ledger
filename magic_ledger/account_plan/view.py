import json
import logging

from flask import Blueprint, request

from magic_ledger.account_plan.model import AccountPlan

bp = Blueprint("account_plan", __name__, url_prefix="/account-plan")


@bp.route("/")
def accounts():
    if request.method == "GET":
        res = AccountPlan.query.all()
        l = []
        for act in res:
            l.append(act.__getstate__())
        return [row.__getstate__() for row in res]
