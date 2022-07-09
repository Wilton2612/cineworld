from ..models.complaint_model import Contacto
from ..database import complaint_db



"""INSERTA UNA QUEJA EN LA BASE DE DATOS"""
def insertar_queja_teatro(conta: Contacto):
    return complaint_db.insertar_queja(conta)
