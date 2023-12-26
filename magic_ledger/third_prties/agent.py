from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db


class AgentTypeEnum(Enum):
    SUPPLIER = "supplier"
    CLIENT = "client"
    EMPLOYEE = "employee"


@dataclass
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=True)
    surname = db.Column(db.String(255), nullable=False)
    agent_type = db.Column(db.Enum(AgentTypeEnum), nullable=False)
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
        name,
        middle_name,
        surname,
        agent_type,
        cnp,
        owner_id,
        address_id,
        banking_details_id,
    ):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.cnp = cnp
        self.owner_id = owner_id
        self.address_id = address_id
        self.banking_details_id = banking_details_id

        if agent_type == "supplier":
            self.agent_type = AgentTypeEnum.SUPPLIER
        elif agent_type == "client":
            self.agent_type = AgentTypeEnum.CLIENT
        elif agent_type == "employee":
            self.agent_type = AgentTypeEnum.EMPLOYEE

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]

        state["creation_date"] = str(state["creation_date"])

        if state.get("agent_type") is AgentTypeEnum.SUPPLIER:
            state["agent_type"] = "supplier"
        elif state.get("agent_type") is AgentTypeEnum.CLIENT:
            state["agent_type"] = "client"
        elif state.get("agent_type") is AgentTypeEnum.EMPLOYEE:
            state["agent_type"] = "employee"
        return state

    def __repr__(self):
        return str(self.__getstate__())
