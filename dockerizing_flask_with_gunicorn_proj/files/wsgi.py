#!/usr/local/bin/python
  
import logging
import sys
import re
import os

from flask_web_app.controller.app import app

class ReverseProxied(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
    if script_name:
      environ['SCRIPT_NAME'] = script_name
      path_info = environ['PATH_INFO']
      if path_info.startswith(script_name):
        environ['PATH_INFO'] = path_info[len(script_name):]

    scheme = environ.get('HTTP_X_FORWARDED_PROTO', '')
    if scheme:
      environ['wsgi.url_scheme'] = scheme
    return self.app(environ, start_response)

app.wsgi_app = ReverseProxied(app.wsgi_app)


class writer(object):
    line = ""
    def write(self,data):
      self.line += data
      if re.match(".*\n$",data):
        logger.log(self.line.rstrip())
        self.line = ''
    def __del__(self):
      if self.line != '':
        logger.log(self.line.rstrip())

if os.environ['DC_LOCALIZE'] != 'dev' and os.environ['DC_LOCALIZE'] != 'laptop':
  sys.stderr = writer()
  sys.stdout = writer()
else:
  sys.stdout = sys.stderr

if __name__ == "__main__":
    from flup.server.fcgi import WSGIServer
    WSGIServer(app).run()
