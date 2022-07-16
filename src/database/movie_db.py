from typing import List, Optional
from ..models.movie_model import Pelicula, Horario
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


"""PELICULA EN PARTICULAR QUE ESTÁN EN SALA"""
def pelicula_by_teatro_sala(iden_pelicula:int, iden_teatro:int)-> Optional[Pelicula]:

    try:

        conexion = obtener_conexion()
        sentencia = "SELECT cine.pelicula.* FROM cine.teatro_pelicula, cine.pelicula WHERE cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=1 AND cine.teatro_pelicula.idteatro=%s AND cine.pelicula.idpelicula= %s;"
        with conexion.cursor() as cursor:
            cursor.execute(sentencia, (iden_teatro, iden_pelicula))
            pelicula = cursor.fetchone()
        conexion.close()


    
        pelicula_only = Pelicula(idpelicula=pelicula[0], nombre=pelicula[1], duracion=pelicula[2], genero=pelicula[3], 
            descripcion=pelicula[4], trailer=pelicula[5], director=pelicula[6], reparto=pelicula[7], estreno=pelicula[8],
            imagen=pelicula[9])
        return pelicula_only 
    except Exception as e:
        return 0
        
  



"""HORARIOS DE UNA PELICULA EN PARTICULAR"""
def list_horario_pelicula(iden:int) -> List[Horario]:
    conexion = obtener_conexion()
    sentencia = "SELECT cine.horario.* FROM cine.horario, cine.pelicula_horario WHERE cine.pelicula_horario.idhorario = cine.horario.idhorario AND cine.pelicula_horario.idpelicula = %s;"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        horarios = cursor.fetchall()
    conexion.close()


    horarios_lista = []
    for record in horarios:
        horario = Horario(idhorario=record[0], hora=record[1])
        horarios_lista.append(horario)

    return horarios_lista



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



"""PELICULA EN PARTICULAR QUE ESTÁ PRÓXIMA ESTRENAR"""
def pelicula_by_teatro_proxima(iden_pelicula:int, iden_teatro:int)-> Optional[Pelicula]:
    try:

        conexion = obtener_conexion()
        sentencia = "SELECT cine.pelicula.* FROM cine.teatro_pelicula, cine.pelicula WHERE cine.teatro_pelicula.idpelicula=cine.pelicula.idpelicula AND cine.pelicula.estreno=0 AND cine.teatro_pelicula.idteatro=%s AND cine.pelicula.idpelicula= %s;"
        with conexion.cursor() as cursor:
            cursor.execute(sentencia, (iden_teatro, iden_pelicula))
            pelicula = cursor.fetchone()
        conexion.close()


        
        pelicula_only = Pelicula(idpelicula=pelicula[0], nombre=pelicula[1], duracion=pelicula[2], genero=pelicula[3], 
            descripcion=pelicula[4], trailer=pelicula[5], director=pelicula[6], reparto=pelicula[7], estreno=pelicula[8],
            imagen=pelicula[9])
        return pelicula_only
    except Exception as e:
        return 0
    