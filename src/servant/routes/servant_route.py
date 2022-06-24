from flask import Blueprint

servant = Blueprint('servant', __name__)

@servant.route("/servicio")
def index():
    return "Servants"