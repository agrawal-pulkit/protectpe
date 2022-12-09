import json
import logging

from app.model.registration import Registration
from app.model.transaction import Transaction
from sqlalchemy import and_
from sqlalchemy.sql import func

from app.utils.resp import Resp

log = logging.getLogger(__name__)


class ReportService:

    @staticmethod
    def get_agg_data(primary_owner):
        rows = Registration.query \
            .outerjoin(Transaction, and_(Registration.phone_number == Transaction.user_id)) \
            .filter(Registration.primary_owner == primary_owner)\
            .with_entities(Transaction.user_id, Registration.description,
                           func.sum(Transaction.transaction_amount)) \
            .group_by(Transaction.user_id, Registration.description) \
            .order_by(Transaction.user_id).all()
        report = {
            'total_amount': 0
        }
        for row in rows:
            amount = int(row[2])
            report[row[0]] = {'description': row[1], "amount": amount}
            report['total_amount'] += amount
        print(report)
        return Resp.success(report)


