import datetime
import logging
import os
from binascii import hexlify
from flask import request
from sqlalchemy.sql import func

from app.model.registration import Registration, RegistrationSchema
from app.model.transaction import Transaction, TransactionSchema
from app.utils.helper import save_changes
from app.utils.resp import Resp

log = logging.getLogger(__name__)
get_trans_schema = TransactionSchema(many=True)
get_reg_schema = RegistrationSchema()


class TransactionService:

    @staticmethod
    def get_all_transaction():
        params = request.args
        try:
            reg_query = Transaction.query
            if params.get('user_id'):
                reg_query = reg_query.filter(Transaction.user_id == params.get('user_id'))
            return Resp.success(get_trans_schema.dump(reg_query.all()))
        except Exception as e:
            log.exception("error in getting reg: {}".format(e))
            return Resp.error("error")

    @staticmethod
    def create_transaction(data):
        log.debug("create_transaction data: {}".format(data))
        status = data.get('status')
        user = Registration.query.filter_by(phone_number=data.get('user_id')).first()
        if user:
            log.debug('user_data: {}'.format(user))

            # check if requested amount is greater than max limit.
            if user.max_limit < data.get('transaction_amount'):
                return Resp.error("user's max limit for one day is {} and transaction amount is {}"
                                  .format(user.max_limit, data.get('transaction_amount')))
            else:
                log.debug("user's max limit for one day is {} and transaction amount is {}"
                          .format(user.max_limit, data.get('transaction_amount')))

            # check the auto approve status
            if user.regular_limit <= data.get('transaction_amount'):
                status = 'IN_PROGRESS'
            else:
                log.debug('AUTO_APPROVED')
                status = "AUTO_APPROVE"
            log.debug("status: {}".format(status))

            # find if total transaction limit is exceeding more than max_limit in one day.
            total_amount = Transaction.query.filter_by(user_id=data.get('user_id'))\
                .filter(Transaction.status.like('%APPROVE%'))\
                    .with_entities(func.sum(Transaction.transaction_amount)).scalar()
            if total_amount and user.max_limit < total_amount:
                return Resp.error("user's max limit for one day is {} and total transaction done by user is {}"
                                  .format(user.max_limit, total_amount))
            else:
                log.debug("user's max limit for one day is {} and total transaction done by user is {}"
                                  .format(user.max_limit, total_amount))
            # save transaction
            trans_id = hexlify(os.urandom(8)).decode()
            new_trans = Transaction(
                id=trans_id,
                user_id=data.get('user_id'),
                merchant_upi_id=data.get('merchant_upi_id'),
                transaction_amount=data.get('transaction_amount'),
                status= status,
                created_at=datetime.datetime.now()
            )
            save_changes(new_trans)
            return Resp.success(TransactionService.get_trans(trans_id))
        else:
            return Resp.error("user_id {} is not registered in protectpe account.".format(data.get('user_id')))

    @staticmethod
    def get_trans(trans_id):
        try:
            reg = Transaction.query.filter_by(id=trans_id).all()
            return get_trans_schema.dump(reg)
        except Exception as e:
            log.exception("error in getting reg: {}".format(e))
            return "error"
