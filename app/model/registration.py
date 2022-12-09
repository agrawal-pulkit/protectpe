import datetime

from app.model.database import db, ma


class Registration(db.Model):
    __tablename__ = 'registration'

    phone_number = db.Column(db.String(20), nullable=True, primary_key=True)
    primary_owner = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    regular_limit = db.Column(db.Integer, nullable=False)
    max_limit = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    qr_code = db.Column(db.String(255), default=True)
    verification_status = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())


class RegistrationSchema(ma.Schema):
    class Meta:
        fields = ('phone_number', 'primary_owner', 'description', 'regular_limit', 'max_limit',
                  'is_active', 'qr_code', 'verification_status', 'created_at')

