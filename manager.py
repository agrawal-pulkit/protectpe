from app import create_app
from app import config
from app.model import database

app = create_app(config.ENV)
app.app_context().push()


def run():
    app.run(debug=True, port=9001, host="0.0.0.0")


def init_db():
    print('init_db')
    database.db.create_all()


def clean_db():
    database.db.drop_all()
    database.db.create_all()

run()