import logging
from app.model.database import db

log = logging.getLogger(__name__)


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        log.exception("error in save creds: {}".format(e))
        db.session.rollback()
        raise
    finally:
        db.session.close()