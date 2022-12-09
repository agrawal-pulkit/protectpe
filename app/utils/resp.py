from flask_restful import abort
from app.config import Config


class Resp:

    @staticmethod
    def success(resp_data={}, status=200, *args, **kwargs):
        output_data = {'status': 'success', 'version_info': dict(version=Config.VERSION_INFO), 'data': resp_data}
        return output_data, status

    @staticmethod
    def error(message='', status=400, *args, **kwargs):
        output_data = {'status': 'error', 'version_info': dict(version=Config.VERSION_INFO), 'message': message}
        return output_data, status

    @staticmethod
    def abort(status, *args, **kwargs):
        return abort(status, *args, **kwargs)
