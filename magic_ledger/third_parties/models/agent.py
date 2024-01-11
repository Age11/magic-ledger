from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db


@dataclass
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    agent_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    agent_type = db.Column(db.String(50), nullable=False)
    cnp = db.Column(db.String(13), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addressbook.id"), nullable=False)
    banking_details_id = db.Column(
        db.Integer, db.ForeignKey("banking_details.id"), nullable=False
    )

    # Misc info
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)

    def __init__(
        self,
        agent_name,
        last_name,
        agent_type,
        cnp,
        owner_id,
        address_id,
        banking_details_id,
    ):
        self.agent_name = agent_name
        self.last_name = last_name
        self.cnp = cnp
        self.owner_id = owner_id
        self.address_id = address_id
        self.banking_details_id = banking_details_id
        self.agent_type = agent_type

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
