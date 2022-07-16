from typing import List, Optional

from ..models.movie_model import Pelicula, Horario
from ..database import movie_db

from ..models.theater_model import Teatro
from ..database import theater_db



def lista_peliculas() -> List[Pelicula]:
     return movie_db.list_all()


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_pelicula_teatro_sala(iden:int) -> List[Pelicula]:
    return movie_db.list_pelicula_by_teatro_sala(iden)


"""PELICULA EN PARTICULAR QUE ESTÁN EN SALA"""
def pelicula_teatro_sala(iden_pelicula:int, iden_teatro:int) -> Optional[Pelicula]:
    return movie_db.pelicula_by_teatro_sala(iden_pelicula, iden_teatro)

"""HORARIOS DE UNA PELICULA EN PARTICULAR"""
def horario_pelicula(iden:int) -> List[Horario]:
    return movie_db.list_horario_pelicula(iden)


"""PELICULAS QUE ESTÁN PRÓXIMAS A ESTRENAR"""
def lista_pelicula_teatro_estreno(iden:int) -> List[Pelicula]:
    return movie_db.list_pelicula_by_teatro_estreno(iden)

"""PELICULA EN PARTICULAR QUE ESTÁ PRÓXIMA A ESTRENAR"""
def pelicula_teatro_proxima(iden_pelicula:int, iden_teatro:int) -> Optional[Pelicula]:
    return movie_db.pelicula_by_teatro_proxima(iden_pelicula, iden_teatro)


"""TEATRO ASOCIADO"""
def theater_index(iden:int) -> Teatro:
    return theater_db.theater_by_index(iden)

