from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
from datetime import datetime

@dataclass
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    inv_type = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(255), nullable=False)
    serial = db.Column(db.String(255), nullable=False)
    receive_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(255), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

    #add a constructor
    def __init__(self, inv_type, number, serial, receive_date, due_date, state, organization_id):
        self.inv_type = inv_type
        self.number = number
        self.serial = serial
        self.receive_date = datetime.strptime(receive_date, '%Y-%m-%d')
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.state = state
        self.organization_id = organization_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        return state

    def __repr__(self):
        return str(self.__getstate__())

