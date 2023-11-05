from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
@dataclass
class BankingDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    account = db.Column(db.String(255), nullable=False)
    details = db.Column(db.String(255), nullable=False)
    #must belong to an organization
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

    #add a constructor
    def __init__(self, account, organization_id, details):
        self.account = account
        self.details = details
        self.organization_id = organization_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        return state

    def __repr__(self):
        return str(self.__getstate__())

