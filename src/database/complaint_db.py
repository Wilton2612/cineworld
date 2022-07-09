from typing import List

from ..models.complaint_model import Contacto
from ..utils.bd import obtener_conexion



def insertar_queja(conta: Contacto) -> int:
    try:
        conexion = obtener_conexion()

        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO queja VALUES(email, nombre, telefono, tipocomentario, comentario, teatro_fk) VALUES (%s, %s, %s, %s, %s, %s)",
                        (conta.email, conta.nombre, conta.telefono, conta.tipocomentario, conta.comentario, conta.teatroid))
        conexion.commit()
        conexion.close()
        return 0
    except Exception as e:
        return -1

