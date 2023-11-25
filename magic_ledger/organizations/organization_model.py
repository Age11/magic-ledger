from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db


class StatusEnum(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"


class OrgTypeEnum(Enum):
    PROJECT = "project"
    SUPPLIER = "supplier"
    CLIENT = "client"


class VatModeEnum(Enum):
    ON_CASH_IN = "on_cash_in"
    ON_INVOICE = "on_invoice"
    NO_VAT = "no_vat"
    UNDETERMINED = "undetermined"


@dataclass
class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    # cod identificare fiscala
    cif = db.Column(db.String(10), nullable=False)
    # numar registru comrt
    nrc = db.Column(db.String(20), nullable=False)

    # Setari generale
    vat_mode = db.Column(db.Enum(VatModeEnum), nullable=False)
    caen_code = db.Column(db.String(4), nullable=False)
    # Misc info
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Enum(StatusEnum), nullable=False)
    org_type = db.Column(db.Enum(OrgTypeEnum), nullable=False)

    # add a constructor
    def __init__(self, name, cif, nrc, org_type, status, vat_mode, caen_code):
        self.name = name
        self.cif = cif
        self.nrc = nrc
        if vat_mode == "on_cash_in":
            self.vat_mode = VatModeEnum.ON_CASH_IN
        elif vat_mode == "on_invoice":
            self.vat_mode = VatModeEnum.ON_INVOICE
        elif vat_mode == "no_vat":
            self.vat_mode = VatModeEnum.NO_VAT
        elif vat_mode == "undetermined":
            self.vat_mode = VatModeEnum.UNDETERMINED
        self.caen_code = caen_code

        if status == "active":
            self.status = StatusEnum.ACTIVE
        elif status == "inactive":
            self.status = StatusEnum.INACTIVE

        if org_type == "project":
            self.org_type = OrgTypeEnum.PROJECT
        elif org_type == "supplier":
            self.org_type = OrgTypeEnum.SUPPLIER
        elif org_type == "client":
            self.org_type = OrgTypeEnum.CLIENT

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

        if state.get("org_type") is OrgTypeEnum.PROJECT:
            state["org_type"] = "project"
        elif state.get("org_type") is OrgTypeEnum.SUPPLIER:
            state["org_type"] = "supplier"
        elif state.get("org_type") is OrgTypeEnum.CLIENT:
            state["org_type"] = "client"

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
