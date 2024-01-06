from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from magic_ledger import db


@dataclass
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    project_name = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, project_name, status, caen_code):
        self.project_name = project_name
        self.status = status
        self.caen_code = caen_code

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        state["creation_date"] = state["creation_date"].strftime("%Y-%m-%d")

        return state

    def __repr__(self):
        return str(self.__getstate__())

    def update_fields(self, var):
        for key, value in var.items():
            setattr(self, key, value)
