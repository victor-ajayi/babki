from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.extensions import db


class Transaction(db.Model):
    __tablename__ = "transactions"
