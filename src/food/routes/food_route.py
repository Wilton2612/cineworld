from flask import Blueprint, request, jsonify, render_template

from ..controller import food_controller
from ..models.food_model import Alimento, Bebida

from ... import principal

food = Blueprint('food', __name__, template_folder='../templates')

@food.route("/alimentos", methods=['GET'])
def alimentos_teatro():

    identificador = principal.leer()
    if identificador is None:
        return render_template('error.html')
    else:
        alimentos_lista = food_controller.lista_alimento_teatro(identificador)
        alimentos_dict = [alimento._asdict() for alimento in alimentos_lista]
        teatro_asociado = food_controller.theater_index(identificador)
        return render_template('alimentos.html', alimentos_lista=alimentos_lista, teatro=teatro_asociado)
        #return jsonify(alimentos_dict)

@food.route("/bebidas", methods=['GET'])
def bebidas_teatro():
    identificador = principal.leer()
    if identificador is None:
        return render_template('error.html')
    else:
        bebidas_lista = food_controller.lista_bebida_teatro(identificador)
        bebidas_dict = [bebida._asdict() for bebida in bebidas_lista]
        teatro_asociado = food_controller.theater_index(identificador)
        return render_template('bebidas.html', bebidas_lista=bebidas_lista, teatro=teatro_asociado)
        #return jsonify(bebidas_dict)

   