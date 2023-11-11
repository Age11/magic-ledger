from __future__ import annotations

from dataclasses import dataclass
from magic_ledger import db
@dataclass
class Addressbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    country = db.Column(db.String(255), nullable=False)
    stat_or_province = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    apartment_or_suite = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    #must belong to an organization
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

    #add a constructor
    def __init__(self, country, stat_or_province, city, street, apartment_or_suite, postal_code, organization_id):
        self.country = country
        self.stat_or_province = stat_or_province
        self.city = city
        self.street = street
        self.apartment_or_suite = apartment_or_suite
        self.postal_code = postal_code
        self.organization_id = organization_id

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_sa_instance_state']
        return state

    def __repr__(self):
        return str(self.__getstate__())

