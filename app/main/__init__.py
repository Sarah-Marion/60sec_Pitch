from flask import Blueprint
from .import views, error, forms


main = Blueprint('main', __name__)