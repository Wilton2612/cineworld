from flask import Blueprint, request, jsonify, render_template

from ..controller import theater_controller
from ..models.theater_model import Teatro

from ..routes import movie_route

from ..helpers import principal

theaterss = Blueprint('theater',__name__, template_folder='../templates')

@theaterss.route("/lista-teatros", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        eliminar = principal.delete()
        if eliminar == 0:
            teatro_lista = theater_controller.lista_teatros()
            teatros_dict = [teatro._asdict() for teatro in teatro_lista]
            return render_template('lista_teatros.html', teatro_lista=teatro_lista)
        else:
            return render_template('error.html')
    if request.method == 'POST':
        identi = request.form['identificador']
        if identi == "Elige un teatro":
            return render_template('error.html')
        else:
            return movie_route.peliculas_sala(identi)
        
    #return jsonify(teatros_dict)







