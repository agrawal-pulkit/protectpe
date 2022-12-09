from app.resource.reports import ReportResource
from app.resource.status import TransStatusResource
from app.resource.health import HealthResource
from app.resource.registration import RegistrationResource, RegistrationUpdateResource
from app.resource.transaction import TransactionResource


def create_resources(api):
    health_resource(api)
    registration_resource(api)
    transaction_resource(api)
    status_resource(api)
    report_resource(api)


def registration_resource(api):
    api.add_resource(RegistrationResource, '/register')
    api.add_resource(RegistrationUpdateResource, '/register/<string:phone_number>')


def transaction_resource(api):
    api.add_resource(TransactionResource, '/transaction')


def status_resource(api):
    api.add_resource(TransStatusResource, '/status/<string:trans_id>')


def report_resource(api):
    api.add_resource(ReportResource, '/report/<string:primary_owner>')


def health_resource(api):
    api.add_resource(HealthResource, '/health', '/')