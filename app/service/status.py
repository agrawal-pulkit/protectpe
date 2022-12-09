import logging

from app.model.database import db
from app.model.transaction import Transaction
from app.service.transaction import TransactionService
from app.utils.resp import Resp

log = logging.getLogger(__name__)


class TransStatusService:

    @staticmethod
    def update_trans_status(trans_id, data):
        trans = Transaction.query.filter_by(id=trans_id).first()
        if not trans:
            return "Transaction id {} dose not exist.".format(trans_id)
        try:
            updated_user = Transaction.query.filter_by(
                id=trans_id).update(data, synchronize_session='fetch')
            db.session.commit()
            return Resp.success(TransactionService.get_trans(trans_id))
        except Exception as e:
            log.exception("error in update creds: {}".format(e))
            db.session.rollback()
            raise
        finally:
            db.session.close()


