import flask

myapp_obj = flask.Flask(__name__)
myapp_obj.config.from_mapping(
  SECRET_KEY = 'my-name-is-khanh',
)
from myapp import routes