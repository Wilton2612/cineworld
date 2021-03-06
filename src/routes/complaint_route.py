from flask import Blueprint, request, jsonify, render_template, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect

from ..models.complaint_model import Contacto
from ..controller import complaint_controller

from ..helpers import principal, complaint_form




contact = Blueprint('contact', __name__, template_folder='../templates')



@contact.route("/contactanos", methods=['GET', 'POST'])
def contacto_cliente():
   
    identificador = principal.leer()
    if identificador is None:
        abort(403)
    else:
        formulario = complaint_form.Formulario_Queja(request.form)
        if request.method == 'GET':
            return render_template('contacto.html', formulario=formulario)
            
        if request.method == 'POST' and formulario.validate():
            email = formulario.email.data
            name = formulario.nombre.data
            phone = formulario.telefono.data
            motivo= formulario.motivo.data
            comentario = formulario.comentario.data
            contacto = Contacto(email=email, nombre=name, telefono=int(phone), tipocomentario=motivo, 
                comentario=comentario, teatroid=int(identificador))
            contact = complaint_controller.insertar_queja_teatro(contacto)

            if contact == 0:
                return redirect(url_for('contact.contacto_cliente'))
            else:
                return render_template('error2.html')
        else:
            return render_template('contacto.html',formulario=formulario )
        
