from flask import Blueprint, request, jsonify, render_template
from typing import NamedTuple, Optional
from ..controller import movie_controller
from ..models.movie_model import Pelicula
from ... import principal

movie = Blueprint('movie', __name__, template_folder='../templates')


"""
@movie.route("/peliculas", methods=['GET'])
def peliculas_sala():
    pelicula_lista = movie_controller.lista_peliculas()
    peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista]
    #return render_template('lista_peliculas.html', pelicula_lista=pelicula_lista)
    return jsonify(peliculas_dict)
"""


@movie.route("/peliculas-sala", methods=['GET'])
def peliculas_sala(iden:Optional[int] = None):
    
    if iden is None:
        identificador = principal.leer()
        if identificador is None:
            return render_template('error.html')
        else:
            pelicula_lista_sala = movie_controller.lista_pelicula_teatro_sala(identificador)
            peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista_sala]
            teatro_asociado = movie_controller.theater_index(identificador)
            return render_template('lista_pelicula_sala.html', pelicula_lista_sala=pelicula_lista_sala, teatro=teatro_asociado)
            
    else:
        respuesta = principal.escribir(iden)
        if respuesta == 0:
            pelicula_lista_sala = movie_controller.lista_pelicula_teatro_sala(iden)
            peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista_sala]
            teatro_asociado = movie_controller.theater_index(iden)
            return render_template('lista_pelicula_sala.html', pelicula_lista_sala=pelicula_lista_sala, teatro=teatro_asociado)
        else:
            return "error"
    #return jsonify(peliculas_dict)



@movie.route("/peliculas-proxima", methods=['GET'])
def peliculas_proxima():
    iden = principal.leer()
    if iden is None:
        return render_template('error.html')
    else:
        pelicula_lista_proxima = movie_controller.lista_pelicula_teatro_estreno(iden)
        peliculas_dict = [pelicula._asdict() for pelicula in pelicula_lista_proxima]
        teatro_asociado = movie_controller.theater_index(iden)
        return render_template('lista_pelicula_proxima.html', pelicula_lista_proxima=pelicula_lista_proxima, teatro=teatro_asociado)
    #return jsonify(peliculas_dict)
    