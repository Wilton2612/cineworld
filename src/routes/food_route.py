from flask import Blueprint, request, jsonify, render_template, abort

from ..controller import food_controller
from ..models.food_model import Alimento, Bebida

from ..helpers import principal

food = Blueprint('food', __name__, template_folder='../templates')

@food.route("/alimentos", methods=['GET'])
def alimentos_teatro():

    identificador = principal.leer()
    if identificador is None:
        abort(403)
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
        abort(403)
    else:
        bebidas_lista = food_controller.lista_bebida_teatro(identificador)
        bebidas_dict = [bebida._asdict() for bebida in bebidas_lista]
        teatro_asociado = food_controller.theater_index(identificador)
        return render_template('bebidas.html', bebidas_lista=bebidas_lista, teatro=teatro_asociado)
        #return jsonify(bebidas_dict)


@food.route("/taquilla", methods=['GET'])
def taquilla():
    return render_template('entradas.html')

#<!--<input type="hidden" name="csrf_token"  value="{{csrf_token()}}"/>-->