from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey

from magic_ledger import db


@dataclass
class GroupTransactionTemplate(db.Model):
    __tablename__ = "group_transaction_template"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    main_transaction_id = Column(Integer, db.ForeignKey("gtt_main_transactions.id"))

    def __init__(
        self,
        name,
        description,
        main_transaction_id,
        owner_id,
    ):
        self.owner_id = owner_id
        self.name = name
        self.description = description
        self.main_transaction_id = main_transaction_id

    def __repr__(self):
        return str(self.__getstate__())

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["_sa_instance_state"]
        return state
