from flask import request
from flask.views import MethodView

from .service import Service


class Controller(MethodView):
    """Абстрактный контроллер - точка доступа к сущности, основной слой фраемворка"""

    def __init__(self, service: Service):
        self.service = service
        self._json = None
        self.args = request.args

    @property
    def json(self):
        if not self._json:
            self._json = request.json
        return self._json
