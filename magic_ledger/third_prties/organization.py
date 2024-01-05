from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db



class OrgTypeEnum(Enum):
    SUPPLIER = "supplier"
    CLIENT = "client"
    AFFILIATE = "affiliate"
    PROJECT = "project"

class VatModeEnum(Enum):
    ON_CASH_IN = "on_cash_in"
    ON_INVOICE = "on_invoice"
    NO_VAT = "no_vat"
    IMPORT = "import"
    UNDETERMINED = "undetermined"

@dataclass
class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    org_type = db.Column(db.Enum(OrgTypeEnum), nullable=False)
    cif = db.Column(db.String(10), nullable=False)
    nrc = db.Column(db.String(20), nullable=False)

    caen_code = db.Column(db.String(4), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addressbook.id"), nullable=False)
    banking_details_id = db.Column(
        db.Integer, db.ForeignKey("banking_details.id"), nullable=False
    )

    vat_mode = db.Column(db.Enum(VatModeEnum), nullable=False)

    def __init__(
        self,
        name,
        cif,
        nrc,
        org_type,
        caen_code,
        owner_id,
        address_id,
        banking_details_id,
        vat_mode
    ):
        self.name = name
        self.cif = cif
        self.nrc = nrc
        self.caen_code = caen_code
        self.owner_id = owner_id
        self.address_id = address_id
        self.banking_details_id = banking_details_id

        if vat_mode == "on_cash_in":
            self.vat_mode = VatModeEnum.ON_CASH_IN
        elif vat_mode == "on_invoice":
            self.vat_mode = VatModeEnum.ON_INVOICE
        elif vat_mode == "import":
            self.vat_mode = VatModeEnum.IMPORT
        elif vat_mode == "no_vat":
            self.vat_mode = VatModeEnum.NO_VAT
        elif vat_mode == "undetermined":
            self.vat_mode = VatModeEnum.UNDETERMINED

        if org_type == "affiliate":
            self.org_type = OrgTypeEnum.AFFILIATE
        elif org_type == "supplier":
            self.org_type = OrgTypeEnum.SUPPLIER
        elif org_type == "client":
            self.org_type = OrgTypeEnum.CLIENT
        elif org_type == "project":
            self.org_type = OrgTypeEnum.PROJECT

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]

        state["creation_date"] = str(state["creation_date"])

        if state.get("vat_mode") is VatModeEnum.ON_CASH_IN:
            state["vat_mode"] = "on_cash_in"
        elif state.get("vat_mode") is VatModeEnum.ON_INVOICE:
            state["vat_mode"] = "on_invoice"
        elif state.get("vat_mode") is VatModeEnum.NO_VAT:
            state["vat_mode"] = "no_vat"
        elif state.get("vat_mode") is VatModeEnum.UNDETERMINED:
            state["vat_mode"] = "undetermined"

        if state.get("org_type") is OrgTypeEnum.AFFILIATE:
            state["org_type"] = "affiliate"
        elif state.get("org_type") is OrgTypeEnum.SUPPLIER:
            state["org_type"] = "supplier"
        elif state.get("org_type") is OrgTypeEnum.CLIENT:
            state["org_type"] = "client"
        elif state.get("org_type") is OrgTypeEnum.PROJECT:
            state["org_type"] = "project"

        return state

    def __repr__(self):
        return str(self.__getstate__())
