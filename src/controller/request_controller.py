from ..models.request_model import Solicitud
from ..database import request_db



"""INSERTA UNA SOLICITUD EN LA BASE DE DATOS"""
def insertar_solicitud_teatro(solici: Solicitud):
    return request_db.insertar_solicitud(solici)
