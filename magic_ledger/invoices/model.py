from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
from datetime import datetime
from enum import Enum
from magic_ledger.misc.currency import Currency


class InventoryMethodEnum(Enum):
    PAID = "paid"
    DUE = "due"

@dataclass
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    inv_type = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(255), nullable=False)
    serial = db.Column(db.String(255), nullable=False)
    issue_date = db.Column(db.DateTime)
    receive_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.Enum(InventoryMethodEnum), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    currency = db.Column(db.Enum(Currency), nullable=False)
    issuer_name = db.Column(db.String(255))
    amount = db.Column(db.Float, nullable=False)

    # add a constructor
    def __init__(self, inv_type, number, serial, receive_date, due_date, issue_date, payment_status, organization_id,
                 supplier_id, client_id, currency, issuer_name, amount):
        self.inv_type = inv_type
        self.number = number
        self.serial = serial
        self.receive_date = datetime.strptime(receive_date, '%Y-%m-%d')
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.issue_date = datetime.strptime(issue_date, '%Y-%m-%d')
        self.organization_id = organization_id
        self.supplier_id = supplier_id
        self.client_id = client_id
        self.issuer_name = issuer_name
        self.amount = amount

        if payment_status == "paid":
            self.payment_status = InventoryMethodEnum.PAID
        elif payment_status == "due":
            self.payment_status = InventoryMethodEnum.DUE

        if currency == "RON":
            self.currency = Currency.RON
        elif currency == "EUR":
            self.currency = Currency.EUR

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        if (state['payment_status'] == InventoryMethodEnum.PAID):
            state['payment_status'] = "paid"
        elif (state['payment_status'] == InventoryMethodEnum.DUE):
            state['payment_status'] = "due"

        if (state['currency'] == Currency.RON):
            state['currency'] = "RON"
        elif (state['currency'] == Currency.EUR):
            state['currency'] = "EUR"
        return state

    def __repr__(self):
        return str(self.__getstate__())
