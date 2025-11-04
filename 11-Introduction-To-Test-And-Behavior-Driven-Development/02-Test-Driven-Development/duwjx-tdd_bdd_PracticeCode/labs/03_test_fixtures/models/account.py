# models/account.py
import logging
from sqlalchemy.sql import func
from . import db   # ⬅ import relativ

logger = logging.getLogger(__name__)

class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(32), nullable=True)
    disabled = db.Column(db.Boolean(), nullable=False, default=False)
    date_joined = db.Column(db.Date, nullable=False, server_default=func.current_date())

    def __repr__(self):
        return f'<Account {self.name!r}>'

    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_dict(self, data: dict) -> None:
        for key, value in data.items():
            setattr(self, key, value)

    def create(self):
        logger.info("Creating %s", self.name)
        db.session.add(self)
        db.session.commit()

    def update(self):
        logger.info("Saving %s", self.name)
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        logger.info("Deleting %s", self.name)
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls) -> list:
        logger.info("Processing all Accounts")
        return cls.query.all()

    @classmethod
    def find(cls, account_id: int):
        logger.info("Processing lookup for id %s ...", account_id)
        return cls.query.get(account_id)        # ok pentru acest lab
        # alternativ SQLAlchemy 2.0: return db.session.get(cls, account_id)
