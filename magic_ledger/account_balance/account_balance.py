from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from magic_ledger import db


@dataclass
class AccountBalance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    analytical_account = db.Column(
        db.String(255), db.ForeignKey("account_plan.account"), nullable=False
    )
    initial_debit = db.Column(db.Float, nullable=False)
    initial_credit = db.Column(db.Float, nullable=False)

    cumulated_debit = db.Column(db.Float, nullable=False)
    cumulated_credit = db.Column(db.Float, nullable=False)

    current_turnover_debit = db.Column(db.Float, nullable=False)
    current_turnover_credit = db.Column(db.Float, nullable=False)

    total_debit_balance = db.Column(db.Float, nullable=False)
    total_credit_balance = db.Column(db.Float, nullable=False)

    final_debit_balance = db.Column(db.Float, nullable=False)
    final_credit_balance = db.Column(db.Float, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    balance_date = db.Column(db.DateTime, nullable=False)

    processed = db.Column(db.Boolean, nullable=False)

    def __init__(self, analytical_account, owner_id, balance_date_string):
        self.owner_id = owner_id
        self.analytical_account = analytical_account

        self.initial_debit = 0
        self.initial_credit = 0

        self.cumulated_debit = 0
        self.cumulated_credit = 0

        self.current_turnover_debit = 0
        self.current_turnover_credit = 0

        self.total_debit_balance = 0
        self.total_credit_balance = 0

        self.final_debit_balance = 0
        self.final_credit_balance = 0

        self.balance_date = datetime.strptime(balance_date_string, "%Y-%m-%d")
        self.processed = False

    def update_balance(
        self,
        initial_debit=0,
        initial_credit=0,
        cumulated_debit=0,
        cumulated_credit=0,
        current_rollover_debit=0,
        current_rollover_credit=0,
    ):
        self.initial_debit += initial_debit
        self.initial_credit += initial_credit
        self.cumulated_debit += cumulated_debit
        self.cumulated_credit += cumulated_credit
        self.current_turnover_debit += current_rollover_debit
        self.current_turnover_credit += current_rollover_credit

    def cumulate_amounts(self):
        self.cumulated_debit += self.current_turnover_debit
        self.cumulated_credit += self.current_turnover_credit
        self.current_turnover_debit = 0
        self.current_turnover_credit = 0

    def calculate_total_amounts(self):
        self.total_debit_balance = self.initial_debit + self.cumulated_debit
        self.total_credit_balance = self.initial_credit + self.cumulated_credit

    def calculate_final_amounts(self):
        if self.total_debit_balance > self.total_credit_balance:
            self.final_debit_balance = (
                self.total_debit_balance - self.total_credit_balance
            )
            self.final_credit_balance = 0
        elif self.total_credit_balance > self.total_debit_balance:
            self.final_debit_balance = 0
            self.final_credit_balance = (
                self.total_credit_balance - self.total_debit_balance
            )

    def __getstate__(self):
        state = self.__dict__.copy()
        state["balance_date"] = state["balance_date"].strftime("%Y-%m")
        del state["_sa_instance_state"]
        return state

    def __repr__(self):
        return str(self.__getstate__())
