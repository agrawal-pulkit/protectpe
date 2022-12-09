from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(session_options={"expire_on_commit": False})
ma = Marshmallow()