from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.extensions import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id: int = db.Column(db.Integer, db.Foreignkey("accounts.id"))
    account_name: str = db.Column(db.String)
    amount: float = db.Column(db.Float, nullable=False)
    is_debit: bool = db.Column(db.Boolean, nullable=False)
    category: str = db.Column(db.String, server_default="Other")
    created_at: TIMESTAMP = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    def __init__(self, name, amount, is_debit) -> None:
        super().__init__()
        self.account_name = name
        self.amount = amount
        self.is_debit = is_debit

    def __repr__(self) -> str:
        return f"<Transaction {self.id}: {self.created_at}>"
