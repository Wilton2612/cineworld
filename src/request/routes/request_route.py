from flask import Blueprint

solicitud = Blueprint('request', __name__)

@solicitud.route("/solicitud")
def index():
    return "requests"