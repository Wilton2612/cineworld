from flask import Blueprint, request, jsonify
from ..controller import theater_controller

theater = Blueprint('theater', __name__)

@theater.route("/teatros", method=['GET'])
def index():

    teatro_lista = theater_controller.lista_teatros()
    return "Theaters"


