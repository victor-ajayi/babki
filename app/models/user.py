from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String, nullable=False)
    email: str = db.Column(db.String)
    password: str = db.Column(db.String, nullable=False)
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

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

    @property
    def password(self):
        raise AttributeError("password is write-only")

    # Stores password in hashes
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
