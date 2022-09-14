from flask import request
from flask.views import MethodView

from .service import Service, AbstractAuthService


class Controller(MethodView):
    """Абстрактный контроллер - точка доступа к сущности, основной слой фраемворка"""

    def __init__(self, service: Service, auth_service: AbstractAuthService):
        self.service = service
        self.auth_service = auth_service
        self._json = None
        self.args = request.args

    @property
    def json(self):
        if not self._json:
            self._json = request.json
        return self._json

    @property
    def user(self):
        return self.auth_service.user
