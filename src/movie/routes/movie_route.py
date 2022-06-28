from flask import Blueprint, request, jsonify, render_template
from ..controller import movie_controller
from ..models.movie_model import Pelicula

movie = Blueprint('movie', __name__, template_folder='../templates')


"""
@movie.route("/peliculas", methods=['GET'])
def peliculas_sala():
    pelicula_lista = movie_controller.lista_peliculas()
    peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(peliculas_dict)
"""


@movie.route("peliculas-sala/<int:iden>", methods=['GET'])
def peliculas_sala(iden):
    pelicula_lista_sala = movie_controller.lista_pelicula_teatro_sala(iden)
    peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista_sala]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(peliculas_dict)

@movie.route("/peliculas-proxima/<int:iden>", methods=['GET'])
def peliculas_proxima_estreno(iden):
    pelicula_lista_estreno = movie_controller.lista_pelicula_teatro_estreno(iden)
    peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista_estreno]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(peliculas_dict)
    