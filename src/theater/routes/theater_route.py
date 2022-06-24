from flask import Blueprint

theater = Blueprint('theater', __name__)

@theater.route("/teatro")
def index():
    return "Theaters"


