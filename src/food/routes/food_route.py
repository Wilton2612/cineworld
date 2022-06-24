from flask import Blueprint

food = Blueprint('food', __name__)

@food.route("/alimento")
def index():
    return "alimentos"