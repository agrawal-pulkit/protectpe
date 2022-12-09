import datetime

from app.model.database import db, ma


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    merchant_upi_id = db.Column(db.String(50), nullable=False)
    transaction_amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())


class TransactionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'merchant_upi_id', 'transaction_amount', 'status', 'created_at')

