from flask import render_template
from . import admin

@admin.app_errorhandler(404)
def for_Ow_four(error):
    """
    Function to render the 404 error page
    """
    
    return render_template('fourOwfour.html'),404