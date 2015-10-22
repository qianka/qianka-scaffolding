# -*- coding: utf-8 -*-

from {{ cookiecutter.repo_name }} import app
app.ready(worker=False)


def load_module_recursively(module):
    import pkgutil
    for loader, name, ispkg in pkgutil.iter_modules(module.__path__):
        module_name = '%s.%s' % (module.__name__, name)
        print('loading view: %s' % module_name)
        _module = __import__(module_name, fromlist=[''])

        if ispkg:
            load_module_recursively(_module)


from {{ cookiecutter.repo_name }} import views
load_module_recursively(views)

app.test_request_context().push()
app.build_assets()
