from flask import Blueprint, request, jsonify, render_template
from ..controller import theater_controller
from ..models.theater_model import Teatro



theater = Blueprint('theater',__name__, template_folder='templates', url_prefix="/lista")

@theater.route("/teatros")
def index():
    teatro_lista = theater_controller.lista_teatros()
    teatros_dict = [teatro._asdict() for teatro in teatro_lista]
    return render_template('theater/lista_teatros.html', teatro_lista=teatro_lista)


