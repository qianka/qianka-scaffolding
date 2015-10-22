# -*- coding: utf-8 -*-

from flask import render_template

from {{ cookiecutter.repo_name }} import app


@app.route('/')
def index():
    return render_template('index.html')
