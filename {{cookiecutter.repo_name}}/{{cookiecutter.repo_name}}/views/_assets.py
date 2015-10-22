# -*- coding: utf-8 -*-

from {{ cookiecutter.repo_name }} import app


#
# 全局资源文件
#

FILTERS_J2_STYLUS = ['jinja2', 'stylus', 'cssmin']
FILTERS_J2_COFFEESCRIPT = ['jinja2', 'coffeescript', 'uglifyjs']
FILTERS_J2_CSS = ['jinja2', 'cssmin']
FILTERS_J2_JAVASCRIPT = ['jinja2', 'uglifyjs']

app.register_asset(
    'site.css',
    'normalize.css/normalize.css'
)

app.register_asset(
    'site.js',
    'requirejs/require.js',
    ('config.coffee', FILTERS_J2_COFFEESCRIPT)
)

app.register_asset('_.js', '_empty.js')
app.register_asset('_.css', '_empty.css')
