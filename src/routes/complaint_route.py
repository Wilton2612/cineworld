from flask import Blueprint, request, jsonify, render_template, redirect, url_for

from ..models.complaint_model import Contacto
from ..controller import complaint_controller

from ..helpers import principal, form1




contact = Blueprint('contact', __name__, template_folder='../templates')

@contact.route("/contactanos", methods=['GET', 'POST'])
def contacto_cliente():
   
    identificador = principal.leer()
    if identificador is None:
            return render_template('error.html')
    else:
        formulario = form1.Formulario1(request.form)
        if request.method == 'GET':
            print("eyyyyy")
            return render_template('contacto.html', formulario=formulario)
            
        if request.method == 'POST' and formulario.validate():
            print("porque")
            email = formulario.email.data
            name = formulario.nombre.data
            phone = formulario.telefono.data
            motivo= formulario.motivo.data
            comentario = formulario.comentario.data
            print(email, name, phone, motivo, comentario, identificador)
            contacto = Contacto(email=email, nombre=name, telefono=int(phone), tipocomentario=motivo, 
                comentario=comentario, teatroid=int(identificador))
            contact = complaint_controller.insertar_queja_teatro(contacto)

            if contact == 0:
                return redirect(url_for('contact.contacto_cliente'))
            else:
                return "OCURRIO UN ERROR"
        else:
            print("errorrrrr")
            return render_template('contacto.html',formulario=formulario )
        
            """
                contacto = Contacto(email=email, nombre=name, phone=telefono, tipocomentario=motivo, 
                comentario=comentario, teatroid=identificador)
            """
               
            