# -*- coding: utf-8 -*-

from celery import Celery

from qianka.flaskext import QKFlask
from qianka.flaskext.sessions import RedisSessionInterface
from qianka.flaskext.sqlalchemy import QKFlaskSQLAlchemy
from qianka.sqlalchemy import QKSQLAlchemy


celery = Celery()
db = QKSQLAlchemy()


class Application(QKFlask):
    def __init__(self):
        super(Application, self).__init__(
            __name__,
            bower_components_folder='../bower_components'
        )

        from . import default_settings
        self.config.from_object(default_settings)
        # TODO:

    def prepare_session(self):
        from redis import StrictRedis
        url = self.config.get('SESSION_REDIS', None)
        if url is None:
            return
        redis = StrictRedis.from_url(url)
        self.session_interface = RedisSessionInterface(redis=redis)


    def ready(self, **kwargs):
        if kwargs.get('db', True):
            QKFlaskSQLAlchemy(db, self)

        if kwargs.get('worker', False):
            self.prepare_celery(celery)

        # always configure celery
        celery.conf.update(self.config)

        if kwargs.get('web', True):
            self.prepare_templates()
            self.prepare_webassets()
            self.prepare_session()

app = Application()
