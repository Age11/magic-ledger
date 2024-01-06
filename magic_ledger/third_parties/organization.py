from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from magic_ledger import db


@dataclass
class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    organization_name = db.Column(db.String(255), nullable=False)
    org_type = db.Column(db.String(20), nullable=False)
    cif = db.Column(db.String(10), nullable=False)
    nrc = db.Column(db.String(20), nullable=False)

    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addressbook.id"), nullable=False)
    banking_details_id = db.Column(
        db.Integer, db.ForeignKey("banking_details.id"), nullable=False
    )

    vat_mode = db.Column(db.String(20), nullable=False)

    def __init__(
            self,
            organization_name,
            cif,
            nrc,
            org_type,
            owner_id,
            address_id,
            banking_details_id,
            vat_mode
    ):
        self.organization_name = organization_name
        self.cif = cif
        self.nrc = nrc
        self.owner_id = owner_id
        self.address_id = address_id
        self.banking_details_id = banking_details_id

        self.vat_mode = vat_mode

        self.org_type = org_type

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]

        state["creation_date"] = str(state["creation_date"])

        return state

    def __repr__(self):
        return str(self.__getstate__())

    def update_fields(self, var):
        for key, value in var.items():
            setattr(self, key, value)

