from flask import Blueprint, request, jsonify, render_template

from ..controller import theater_controller
from ..models.theater_model import Teatro

from ..routes import movie_route

from ..helpers import principal, theater_form


theaterss = Blueprint('theater',__name__, template_folder='../templates')

@theaterss.route("/lista-teatros", methods=['GET', 'POST'])
def index():

    formulario = theater_form.Formulario_Teatro(request.form)
    if request.method == 'GET':
        eliminar = principal.delete()
        if eliminar == 0:
           
            teatro_lista = theater_controller.lista_teatros()
            formulario.teatro.choices = [(teatro.id, teatro.nombre+" - "+teatro.nombreciudad) for teatro in teatro_lista]

            teatros_dict = [teatro._asdict() for teatro in teatro_lista]
            return render_template('lista_teatros.html', teatro_lista=teatro_lista, formulario=formulario)
        else:
            return render_template('error.html')
    if request.method == 'POST':
        identi = formulario.teatro.data
        return movie_route.peliculas_sala(identi)
        #return jsonify(teatros_dict)







