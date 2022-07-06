from typing import List

from ..models.movie_model import Pelicula
from ..database import movie_db

from ...theater.models.theater_model import Teatro
from ...theater.database import theater_db


def lista_peliculas() -> List[Pelicula]:
     return movie_db.list_all()


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_pelicula_teatro_sala(iden:int) -> List[Pelicula]:
    return movie_db.list_pelicula_by_teatro_sala(iden)

"""PELICULAS QUE ESTÁN PRÓXIMAS A ESTRENAR"""
def lista_pelicula_teatro_estreno(iden:int) -> List[Pelicula]:
    return movie_db.list_pelicula_by_teatro_estreno(iden)

"""TEATRO ASOCIADO"""
def theater_index(iden:int) -> Teatro:
    return theater_db.theater_by_index(iden)

