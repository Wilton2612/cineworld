import pymysql

def obtener_conexion():
    try:
        return  pymysql.connect(host='localhost', user='root', 
                                           password='', db='cine')
    except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        return None
        print("Ocurre un error: ", e)


