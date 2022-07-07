from typing import List
from ..models.servant_model import Servicio
from ..utils.bd import obtener_conexion



"""SERVICIOS QUE ESTÁN EN SALA"""
def list_servicios_by_teatro(iden:int) -> List[Servicio]:
    conexion = obtener_conexion()
    sentencia = "SELECT cine.servicio.* FROM cine.teatro_servicio, cine.servicio WHERE cine.teatro_servicio.idservicio = cine.servicio.idservicio AND cine.teatro_servicio.idteatro = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sentencia, (iden,))
        servicios = cursor.fetchall()
    conexion.close()


    servicios_lista = []
    for record in servicios:
        servicio = Servicio(idservicio=record[0], nombre=record[1], descripcion=record[2], condiciones=record[3], 
        imagen=record[4])
        servicios_lista.append(servicio)

    return servicios_lista