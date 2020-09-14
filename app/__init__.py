from flask import Flask
from config import DevConfig, Config_options
from flask_bootstrap import Bootstrap
from app import views
from app import error

#initializing application
app = Flask(__name__,instance_relative_config = True)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(Config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    # will add the views and form
    return app


from app import views