from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_wtf.csrf import CSRFProtect


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'



bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()
# login_manager = LoginManager()
csrf = CSRFProtect()



def create_app(config_state):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_state])


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    #
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    app.add_template_global(reversed, name='reversed')


    # Configure UpoadSet
    configure_uploads(app,photos)
    
    
    return app
