# -*- coding: utf-8 -*-

import os
import flask

from {{ cookiecutter.repo_name }} import app

#
# 注册通用资源
#
app.register_asset('require.js', 'requirejs/require.js')
app.register_asset('jquery.js', 'jquery/dist/jquery.js')

app.register_asset('bootstrap.js', 'bootstrap/dist/js/bootstrap.js')

app.register_asset('normalize.css', 'normalize.css/normalize.css')


#
# 一些 CSS 库使用相对路径调用其自带的资源文件，其自带的资源文件未经过我们重写打包
#
# 需要用更好的方法改写
#
def _send_bootstrap_file(filename):
    bower_folder = os.path.abspath('%s/%s' % (app.root_path, app.bower_components_folder))
    cache_timeout = app.get_send_file_max_age(filename)
    return flask.send_from_directory(
        bower_folder + '/bootstrap/dist/',
        filename, cache_timeout=cache_timeout)

def _send_fontawesome_file(filename):
    bower_folder = os.path.abspath('%s/%s' % (app.root_path, app.bower_components_folder))
    cache_timeout = app.get_send_file_max_age(filename)
    return flask.send_from_directory(
        bower_folder + '/font-awesome/',
        filename, cache_timeout=cache_timeout)


app.add_url_rule(
    '/assets/vendor/bootstrap/3.3.5/<path:filename>',
    endpoint='/assets/vendor/bootstrap',
    view_func=_send_bootstrap_file
)
app.add_url_rule(
    '/assets/vendor/font-awesome/4.4.0/<path:filename>',
    endpoint='/assets/vendor/font-awesome',
    view_func=_send_fontawesome_file
)
