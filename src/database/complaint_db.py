from typing import List

from ..models.complaint_model import Contacto
from ..utils.bd import obtener_conexion



def insertar_queja(conta: Contacto) -> int:
    try:
        conexion = obtener_conexion()
        sentencia = "INSERT INTO queja(email, nombre, telefono, tipocomentario, comentario, teatro_fk) VALUES ( %s, %s, %s, %s, %s, %s)"
        with conexion.cursor() as cursor:
            cursor.execute(sentencia,(conta.email, conta.nombre, conta.telefono, conta.tipocomentario, conta.comentario, conta.teatroid))
        conexion.commit()
        conexion.close()
        return 0
    except Exception as e:
        print(e)
        return -1

