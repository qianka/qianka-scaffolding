# -*- coding: utf-8 -*-

import code
import readline
import rlcompleter

from {{ cookiecutter.repo_name}} import app
from {{ cookiecutter.repo_name}} import db


app.ready(web=False, worker=False)

try:
    exports = {'db': db}

    readline.set_completer(rlcompleter.Completer(exports).complete)
    readline.parse_and_bind("tab: complete")
    shell = code.InteractiveConsole(exports)
    shell.interact()
finally:
    db.reset()
