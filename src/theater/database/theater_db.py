from typing import List
from ..models.theater_model import Teatro
from ...utils.bd import obtener_conexion


def list_all() -> List[Teatro]:
    conexion = obtener_conexion()
    sentencia = "SELECT * FROM cine.teatro"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia)
        teatros = cursor.fetchall()
    conexion.close()


    teatros_lista = []
    for record in teatros:
        theater = Teatro(id=record[0], nombre=record[1], nombreciudad=record[2], imagen=record[3])
        teatros_lista.append(theater)

    return teatros_lista
    
def theater_by_index(iden:int) -> [Teatro]:
    conexion = obtener_conexion()
    sentencia = "SELECT * FROM cine.teatro WHERE cine.teatro.idteatro = %s;"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        teatro = cursor.fetchone()
    conexion.close()

    teatro_re = Teatro(id=teatro[0], nombre=teatro[1], nombreciudad=teatro[2], imagen=teatro[3])

    return teatro_re


