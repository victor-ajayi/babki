from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String, nullable=False)
    email: str = db.Column(db.String)
    password_hash: str = db.Column(db.String, nullable=False)
    cash: float = db.Column(db.Float, server_default="0.0")
    savings: float = db.Column(db.Float, server_default="0.0")
    debt: float = db.Column(db.Float, server_default="0.0")
    loans: float = db.Column(db.Float, server_default="0.0")
    created_at: TIMESTAMP = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: TIMESTAMP = db.Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __init__(self, username, password_hash) -> None:
        super().__init__()
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"
