import os

class Config:
    """
    General configuration parent class
    """
    #pass
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')


    GOOGLE_LOGIN_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_LOGIN_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

    OAUTH_CREDENTIALS={
    'google': {
    'id': GOOGLE_LOGIN_CLIENT_ID,
    'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
    }

    POSTS_PER_PAGE = 1

    # email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME",)
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD",'')
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")

    # Flask-User settings
    USER_APP_NAME = "60sec Pitch"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = True
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@divergeglobal.com"

    @staticmethod
    def init_app(app):
        pass


    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """

    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://marion:enlightenedaf03@localhost/pitch'

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}