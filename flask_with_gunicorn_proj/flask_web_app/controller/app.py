from flask import Flask, Response
import logging
from flask_web_app.view.submission import submission

log = logging.getLogger(__file__)

app = Flask(__name__)

class ReverseProxied(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
    print("script_name:",script_name)
    if script_name:
      environ['SCRIPT_NAME'] = script_name
      path_info = environ['PATH_INFO']
      print("path_info:",path_info)
      if path_info.startswith(script_name):
        environ['PATH_INFO'] = path_info[len(script_name):]

    scheme = environ.get('HTTP_X_FORWARDED_PROTO', '')
    if scheme:
      environ['wsgi.url_scheme'] = scheme
    print("script_name:",script_name)
    return self.app(environ, start_response)

app.wsgi_app = ReverseProxied(app.wsgi_app)
app.register_blueprint(submission)


@app.errorhandler(500)
def custom500(error):
    print(error)
    return Response(f"Error: {error}\n\n", content_type='text/plain'), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9595, debug=True)

