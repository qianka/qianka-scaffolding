# -*- coding: utf-8 -*-

import os

from celery import Celery
from redis import StrictRedis

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
        if '{{ cookiecutter.repo_name | upper }}_CONFIG' in os.environ:
            self.config.from_envvar('{{ cookiecutter.repo_name | upper }}_CONFIG', silent=True)
        else:
            dev_cfg = os.path.abspath(os.path.join(
                os.path.basename(__file__), 'dev.cfg'))
            self.config.from_pyfile(dev_cfg, silent=True)

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
