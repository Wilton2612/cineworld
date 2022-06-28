from typing import List
from ..models.food_model import Alimento, Bebida
from ..database import food_db


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_alimento_teatro(iden:int) -> List[Alimento]:
    return food_db.list_alimento_by_teatro(iden)


"""PELICULAS QUE ESTÁN EN SALA"""
def lista_bebida_teatro(iden:int) -> List[Bebida]:
    return food_db.list_bebida_by_teatro(iden)