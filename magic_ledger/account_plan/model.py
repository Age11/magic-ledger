from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
from enum import Enum


class AccountTypeEnum(Enum):
    ACTIVE = 'activ'
    PASIVE = 'pasiv'
    BIFUNCTIONAL = 'bifunctional'
    UNSPECIFIED = 'nespecificat'


@dataclass
class AccountPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    account = db.Column(db.String(255), nullable=False)
    acc_name = db.Column(db.String(255), nullable=False)
    acc_type = db.Column(db.String(255), nullable=False)

    def __init__(self, account, acc_name, acc_type):
        self.account = account
        self.acc_name = acc_name
        self.acc_type = acc_type

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        return state

    def __repr__(self):
        return str(self.__getstate__())
