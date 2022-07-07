from typing import List

from ..models.food_model import Alimento, Bebida
from ..database import food_db

from ..models.theater_model import Teatro
from ..database import theater_db


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_alimento_teatro(iden:int) -> List[Alimento]:
    return food_db.list_alimento_by_teatro(iden)


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_bebida_teatro(iden:int) -> List[Bebida]:
    return food_db.list_bebida_by_teatro(iden)

"""TEATRO ASOCIADO"""
def theater_index(iden:int) -> Teatro:
    return theater_db.theater_by_index(iden)