from __future__ import annotations

from dataclasses import dataclass

from magic_ledger import db


@dataclass
class Addressbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    country = db.Column(db.String(255), nullable=False)
    state_or_province = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    apartment_or_suite = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(
            self,
            country,
            state_or_province,
            city,
            street,
            apartment_or_suite,
            postal_code,
            phone,
            email,
    ):
        self.country = country
        self.state_or_province = state_or_province
        self.city = city
        self.street = street
        self.apartment_or_suite = apartment_or_suite
        self.postal_code = postal_code
        self.phone = phone
        self.email = email

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())

    def update_fields(self, var):
        for key, value in var.items():
            setattr(self, key, value)
