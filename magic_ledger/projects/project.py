from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db


class StatusEnum(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"


class VatModeEnum(Enum):
    ON_CASH_IN = "on_cash_in"
    ON_INVOICE = "on_invoice"
    NO_VAT = "no_vat"
    UNDETERMINED = "undetermined"


@dataclass
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Enum(StatusEnum), nullable=False)
    vat_mode = db.Column(db.Enum(VatModeEnum), nullable=False)

    # add a constructor
    def __init__(self, project_name, status, vat_mode, caen_code):
        self.project_name = project_name

        if status == "active":
            self.status = StatusEnum.ACTIVE
        elif status == "inactive":
            self.status = StatusEnum.INACTIVE
        elif status == "deleted":
            self.status = StatusEnum.DELETED

        if vat_mode == "on_cash_in":
            self.vat_mode = VatModeEnum.ON_CASH_IN
        elif vat_mode == "on_invoice":
            self.vat_mode = VatModeEnum.ON_INVOICE
        elif vat_mode == "no_vat":
            self.vat_mode = VatModeEnum.NO_VAT
        elif vat_mode == "undetermined":
            self.vat_mode = VatModeEnum.UNDETERMINED
        self.caen_code = caen_code

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]

        if state.get("status") is StatusEnum.ACTIVE:
            state["status"] = "active"
        elif state.get("status") is StatusEnum.INACTIVE:
            state["status"] = "inactive"
        elif state.get("status") is StatusEnum.DELETED:
            state["status"] = "deleted"

        state["creation_date"] = str(state["creation_date"])

        if state.get("vat_mode") is VatModeEnum.ON_CASH_IN:
            state["vat_mode"] = "on_cash_in"
        elif state.get("vat_mode") is VatModeEnum.ON_INVOICE:
            state["vat_mode"] = "on_invoice"
        elif state.get("vat_mode") is VatModeEnum.NO_VAT:
            state["vat_mode"] = "no_vat"
        elif state.get("vat_mode") is VatModeEnum.UNDETERMINED:
            state["vat_mode"] = "undetermined"

        return state

    def __repr__(self):
        return str(self.__getstate__())
