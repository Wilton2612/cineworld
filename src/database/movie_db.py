from typing import List
from ..models.movie_model import Pelicula
from ..utils.bd import obtener_conexion



def list_all()-> List[Pelicula]:
    conexion = obtener_conexion()
    sentencia = "SELECT * FROM cine.pelicula"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia)
        peliculas = cursor.fetchall()
    conexion.close()


    peliculas_lista = []
    for record in peliculas:
        pelicula = Pelicula(idpelicula=record[0], nombre=record[1], duracion=record[2], genero=record[3], 
        descripcion=record[4], trailer=record[5], director=record[6], reparto=record[7], estreno=record[8],
        imagen=record[9])
        peliculas_lista.append(pelicula)

    return peliculas_lista


"""PELICULAS QUE ESTÁN EN SALA"""
def list_pelicula_by_teatro_sala(iden:int)-> List[Pelicula]:
    conexion = obtener_conexion()
    sentencia = "SELECT cine.pelicula.* FROM cine.teatro_pelicula, cine.pelicula WHERE cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=1 AND cine.teatro_pelicula.idteatro = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        peliculas = cursor.fetchall()
    conexion.close()


    peliculas_lista = []
    for record in peliculas:
        pelicula = Pelicula(idpelicula=record[0], nombre=record[1], duracion=record[2], genero=record[3], 
        descripcion=record[4], trailer=record[5], director=record[6], reparto=record[7], estreno=record[8],
        imagen=record[9])
        peliculas_lista.append(pelicula)

    return peliculas_lista

"""PELICULAS QUE ESTÁN PRÓXIMAS A ESTRENAR"""
def list_pelicula_by_teatro_estreno(iden:int)-> List[Pelicula]:
    conexion = obtener_conexion()
    sentencia = "SELECT cine.pelicula.* FROM cine.teatro_pelicula, cine.pelicula WHERE cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=0 AND cine.teatro_pelicula.idteatro = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        peliculas = cursor.fetchall()
    conexion.close()


    peliculas_lista = []
    for record in peliculas:
        pelicula = Pelicula(idpelicula=record[0], nombre=record[1], duracion=record[2], genero=record[3], 
        descripcion=record[4], trailer=record[5], director=record[6], reparto=record[7], estreno=record[8],
        imagen=record[9])
        peliculas_lista.append(pelicula)

    return peliculas_lista