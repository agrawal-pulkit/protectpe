import datetime
import logging
from flask import request

from app.model.database import db
from app.model.registration import Registration, RegistrationSchema
from app.utils.helper import save_changes
from app.utils.resp import Resp

# Import QRCode from pyqrcode
import pyqrcode
get_reg_schema = RegistrationSchema()
get_all_reg_schema = RegistrationSchema(many=True)
log = logging.getLogger(__name__)


class RegistrationService:

    @staticmethod
    def get_all_registration():
        params = request.args
        try:
            reg_query = Registration.query
            if params.get('primary_owner'):
                reg_query = reg_query.filter(Registration.primary_owner == params.get('primary_owner'))
            if params.get('phone_number'):
                reg_query = reg_query.filter(Registration.phone_nubmer == params.get('phone_number'))
            return Resp.success(get_all_reg_schema.dump(reg_query.order_by(Registration.created_at.desc()).all()))
        except Exception as e:
            log.exception("error in getting reg: {}".format(e))
            return Resp.error("error")

    @staticmethod
    def register_protectpe(data):
        log.debug("registration data: {}".format(data))
        user = Registration.query.filter_by(phone_number=data.get('phone_number')).first()
        if user:
            return Resp.success("{} is already registered as protectpe in system".format(data.get('phone_number')))
        qr_code = pyqrcode.create(data.get('phone_number') + data.get('description'))

        new_reg = Registration(
            phone_number=data.get('phone_number'),
            primary_owner=data.get('primary_owner'),
            description=data.get('description'),
            regular_limit=data.get('regular_limit'),
            max_limit=data.get('max_limit'),
            is_active=data.get('is_active', True),
            verification_status=data.get('verification_status', "IN_PROGRESS"),
            qr_code=qr_code,
            created_at=datetime.datetime.now()
        )
        save_changes(new_reg)
        return Resp.success(RegistrationService.get_a_reg(data.get('phone_number')))

    @staticmethod
    def update_reg_status(phone_number, data):
        phone_number_data = Registration.query.filter_by(phone_number=phone_number).first()
        if not phone_number_data:
            return "Registration {} dose not exist.".format(phone_number_data)
        try:
            updated_user = Registration.query.filter_by(
                phone_number=phone_number).update(data, synchronize_session='fetch')
            db.session.commit()
            return Resp.success(RegistrationService.get_a_reg(phone_number))
        except Exception as e:
            log.exception("error in update creds: {}".format(e))
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def get_a_reg(phone_number):
        try:
            reg = Registration.query.filter_by(phone_number=phone_number).first()
            return get_reg_schema.dump(reg)
        except Exception as e:
            log.exception("error in getting reg: {}".format(e))
            return "error"
