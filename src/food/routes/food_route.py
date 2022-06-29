from flask import Blueprint, request, jsonify, render_template
from ..controller import food_controller
from ..models.food_model import Alimento, Bebida

food = Blueprint('food', __name__, template_folder='../templates')

@food.route("/alimentos/<int:iden>", methods=['GET'])
def alimentos_teatro(iden):
    alimentos_lista = food_controller.lista_alimento_teatro(iden)
    alimentos_dict = [alimento._asdict() for alimento in alimentos_lista]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(alimentos_dict)

@food.route("/bebidas/<int:iden>", methods=['GET'])
def bebidas_teatro(iden):
    bebidas_lista = food_controller.lista_bebida_teatro(iden)
    bebidas_dict = [bebida._asdict() for bebida in bebidas_lista]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(bebidas_dict)

   