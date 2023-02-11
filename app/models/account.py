from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.extensions import db


class Account(db.Model):
    __tablename__ = "accounts"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_type: str = db.Column(db.String, nullable=False)
    account_name: str = db.Column(db.String(50))
    bank_name: str = db.Column(db.String)
    amount: float = db.Column(db.Float, server_default="0.0")
    currency: str = db.Column(db.String, server_default="RUB")
    account_number: str = db.Column(db.String(20))
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at: TIMESTAMP = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: TIMESTAMP = db.Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __init__(self, account_type) -> None:
        super().__init__()
        self.account_type = account_type

    def __repr__(self) -> str:
        return f"<Account {self.id}: {self.created_at}>"
