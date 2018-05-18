import os

class Config:
    """
    General configuration parent class
    """
    #pass
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://marion:{os.environ.get("DATABASE_PASSWORD")}@localhost/60secPitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    