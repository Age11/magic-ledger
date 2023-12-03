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


@dataclass
class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    org_type = db.Column(db.Enum(OrgTypeEnum), nullable=False)
    # cod identificare fiscala
    cif = db.Column(db.String(10), nullable=False)
    # numar registru comrt
    nrc = db.Column(db.String(20), nullable=False)

    # Setari generale
    caen_code = db.Column(db.String(4), nullable=False)
    # Misc info
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addressbook.id"), nullable=False)
    banking_details_id = db.Column(
        db.Integer, db.ForeignKey("banking_details.id"), nullable=False
    )

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
    ):
        self.name = name
        self.cif = cif
        self.nrc = nrc
        self.caen_code = caen_code
        self.owner_id = owner_id
        self.address_id = address_id
        self.banking_details_id = banking_details_id

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
