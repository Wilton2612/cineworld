from typing import List

from ..models.servant_model import Servicio
from ..database import servant_db

from ..models.theater_model import Teatro
from ..database import theater_db


"""SERVICIOS QUE ESTÁN EN SALA"""
def lista_servicio_teatro(iden:int) -> List[Servicio]:
    return servant_db.list_servicios_by_teatro(iden)

"""TEATRO ASOCIADO"""
def theater_index(iden:int) -> Teatro:
    return theater_db.theater_by_index(iden)