from flask import Blueprint, request, jsonify, render_template, abort
from typing import NamedTuple, Optional
from ..controller import movie_controller
from ..models.movie_model import Pelicula
from ..helpers import principal

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
            abort(403)
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
            abort(403)
    #return jsonify(peliculas_dict)


@movie.route("/peliculas-sala/<int:iden>", methods=['GET'])
def pelicula_particular(iden):
    
    identificador = principal.leer()
    if identificador is None:
        return abort(403)
    else:

        pelicula_sala = movie_controller.pelicula_teatro_sala(iden, identificador)
        horarios_pelicula = movie_controller.horario_pelicula(iden)
        teatro_asociado = movie_controller.theater_index(identificador)
        return render_template('pelicula_sala.html', pelicula_sala=pelicula_sala, lista_horarios=horarios_pelicula, teatro_asociado=teatro_asociado)
        
    
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


@movie.route("/peliculas-proxima/<int:iden>", methods=['GET'])
def pelicula_particular_estreno(iden):
    
    identificador = principal.leer()
    if identificador is None:
        return abort(403)
    else:

        pelicula_sala = movie_controller.pelicula_teatro_proxima(iden, identificador)
        teatro_asociado = movie_controller.theater_index(identificador)
        return render_template('pelicula_proxima.html', pelicula_sala=pelicula_sala, teatro_asociado=teatro_asociado)
        
    
    #return jsonify(peliculas_dict)