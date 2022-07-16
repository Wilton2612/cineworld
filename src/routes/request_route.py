from flask import Blueprint, request, jsonify, render_template, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect

from ..controller import servant_controller
from ..models.servant_model import Servicio

from ..controller import request_controller
from ..models.request_model import Solicitud

from ..helpers import principal, request_form


solicitud = Blueprint('request', __name__)



@solicitud.route("/solicitudes", methods=['GET', 'POST'])
def solicitudes():

    identificador = principal.leer()
    if identificador is None:
            abort(403)
    else:
        formulario = request_form.Formulario_Solicitud(request.form)
        servicios = servant_controller.lista_servicio_teatro(identificador)
        formulario.servicio.choices = [(ser.idservicio, ser.nombre) for ser in servicios]
        if request.method == 'GET':
            return render_template('solicitud.html', formulario=formulario)
            
        if request.method == 'POST' and formulario.validate():
            email = formulario.email.data
            name = formulario.nombre.data
            phone = formulario.telefono.data
            servicio = formulario.servicio.data
            comentario = formulario.comentario.data
            solicitud = Solicitud(email=email, nombre=name, telefono=int(phone), servicioid=int(servicio), 
                informacion=comentario, teatroid=int(identificador))
            requetss = request_controller.insertar_solicitud_teatro(solicitud)

            if requetss == 0:
                return redirect(url_for('request.solicitudes'))
            else:
                return render_template('error2.html')
        else:
            return render_template('solicitud.html',formulario=formulario )
