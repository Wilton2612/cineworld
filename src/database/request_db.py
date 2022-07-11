from typing import List

from ..models.request_model import Solicitud
from ..utils.bd import obtener_conexion



def insertar_solicitud(solici: Solicitud) -> int:
    try:
        conexion = obtener_conexion()
        sentencia = "INSERT INTO solicitud(email, nombre, telefono, informacion, servicio_fk, teatro_fk) VALUES ( %s, %s, %s, %s, %s, %s)"
        with conexion.cursor() as cursor:
            cursor.execute(sentencia,(solici.email, solici.nombre, solici.telefono, solici.informacion, solici.servicioid, solici.teatroid))
        conexion.commit()
        conexion.close()
        return 0
    except Exception as e:
        print(e)
        return -1
