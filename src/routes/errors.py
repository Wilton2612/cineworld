from flask import Blueprint, render_template, abort



errors = Blueprint('errors',__name__)


@errors.app_errorhandler(404)
def page_not_found(err):
    return render_template('page_not_found.html'), 404


@errors.app_errorhandler(403)
def error_access(err):
    return render_template('error.html'), 403



