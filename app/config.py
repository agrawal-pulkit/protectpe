import os

ENV = os.getenv('PROTECTPE_API_ENV') if os.getenv('PROTECTPE_API_ENV') else 'dev'


class Config:
    TEST = True
    VERSION_INFO = "1.0.0"


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://protectpe:protectpePassword@127.0.0.1:3306/protectpe'


config_by_name = dict(
    dev=DevelopmentConfig
)