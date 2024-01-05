from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db


class StatusEnum(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"

@dataclass
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Enum(StatusEnum), nullable=False)

    # add a constructor
    def __init__(self, project_name, status,  caen_code):
        self.project_name = project_name

        if status == "active":
            self.status = StatusEnum.ACTIVE
        elif status == "inactive":
            self.status = StatusEnum.INACTIVE
        elif status == "deleted":
            self.status = StatusEnum.DELETED

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

        state["creation_date"] = state["creation_date"].strftime("%Y-%m-%d")

        return state

    def __repr__(self):
        return str(self.__getstate__())
