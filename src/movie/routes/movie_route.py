from flask import Blueprint

movie = Blueprint('movie', __name__)

@movie.route("/pelicula")
def index():
    return "peliculas"