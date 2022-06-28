from typing import List
from ..models.food_model import Alimento, Bebida
from ...utils.bd import obtener_conexion


def list_alimento_by_teatro(iden:int)-> List[Alimento]:
    conexion = obtener_conexion()
    sentencia = """SELECT cine.alimento.idalimento, cine.alimento.nombre, cine.alimento.precio, cine.bebida.*
                FROM cine.alimento, cine.bebida, cine.teatro_alimento
                WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND 
                cine.alimento.bebida_fk = cine.bebida.idbebida AND 
                cine.teatro_alimento.idteatro = %s;"""
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        alimentos= cursor.fetchall()
    conexion.close()


    alimentos_lista = []
    for record in alimentos:
        alimento = Alimento(idalimento=record[0], nombre1=record[1], precio1=record[2], idbebida=record[3], 
        nombre2=record[4], precio2=record[5])
        alimentos_lista.append(alimento)

    return alimentos_lista

def list_bebida_by_teatro(iden:int)-> List[Bebida]:
    conexion = obtener_conexion()
    sentencia = """SELECT cine.bebida.*
                FROM cine.alimento, cine.bebida, cine.teatro_alimento
                WHERE cine.alimento.idalimento = cine.teatro_alimento.idalimento AND 
                cine.alimento.bebida_fk = cine.bebida.idbebida AND 
                cine.teatro_alimento.idteatro = %s;"""
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        bebidas= cursor.fetchall()
    conexion.close()


    bebidas_lista = []
    for record in bebidas:
        bebida = Bebida(idbebida=record[0], nombre=record[1], precio=record[2])
        bebidas_lista.append(bebida)

    return bebidas_lista