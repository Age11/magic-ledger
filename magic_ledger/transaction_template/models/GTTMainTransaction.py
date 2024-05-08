from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey

from magic_ledger import db


@dataclass
class GTTMainTransaction(db.Model):
    __tablename__ = "gtt_main_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    debit_account = Column(String, nullable=False)
    credit_account = Column(String, nullable=False)
    currency = Column(String)
    details = Column(String, nullable=False)
    tx_type = Column(String, nullable=False)
    document_type = Column(String, nullable=True)

    def __init__(
        self,
        debit_account,
        credit_account,
        currency,
        details,
        tx_type,
        document_type=None,
    ):
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.currency = currency
        self.details = details
        self.tx_type = tx_type
        self.document_type = document_type

    def __repr__(self):
        return str(self.__getstate__())
