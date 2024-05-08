from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey

from magic_ledger import db


@dataclass
class GTTFollowupTransaction(db.Model):
    __tablename__ = "gtt_followup_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    main_transaction_id = Column(Integer, db.ForeignKey("gtt_main_transactions.id"))
    debit_account = Column(String, nullable=False)
    credit_account = Column(String, nullable=False)
    operation = Column(String)
    details = Column(String, nullable=False)
    tx_type = Column(String, nullable=False)
    document_type = Column(String, nullable=True)

    def __init__(
        self,
        main_transaction_id,
        debit_account,
        credit_account,
        operation,
        details,
        tx_type,
        document_type=None,
    ):
        self.main_transaction_id = main_transaction_id
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.operation = operation
        self.details = details
        self.tx_type = tx_type
        self.document_type = document_type

    def __repr__(self):
        return str(self.__getstate__())
