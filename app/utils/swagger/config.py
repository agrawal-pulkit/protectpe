def swagger_template():
    template = {
        "info": {
            "title": "ProtectPe API",
            "description": "API for ProtectPe use",
            "contact": {
                "responsibleOrganization": "ME",
                "responsibleDeveloper": "Me",
                "email": "pulkit.agrawal@phonepe.com",
            },
            "version": "1.0.0"
        },
        # "schemes": [
        #     "https",
        #     "http"
        # ]
    }
    return template


def swagger_config():
    return {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }