from flask import Blueprint, request, jsonify, render_template, redirect

from ..models.complaint_model import Contacto

from ..helpers import principal, form1




contact = Blueprint('contact', __name__, template_folder='../templates')

@contact.route("/contactanos", methods=['GET', 'POST'])
def contacto_cliente():
    formulario = form1.Formulario1()
    if request.method == 'GET':
        identificador = principal.leer()
        if identificador is None:
            return render_template('error.html')
        else:
            
            return render_template('contacto.html', formulario=formulario)
            
    if request.method == 'POST' and formulario.validate():
        identificador = principal.leer()
        if identificador is None:
            return render_template('error.html')
        else:
            return redirect("/contactanos")

            """
            email = request.form['email']
            name = request.form['name']
            motivo = request.form['motivo']
            comentario = request.form['comentario']

            if email != '' and name != '' and movito != '----' and comentario != '':

                print(email, name, phone, motivo, comentario, identificador)


                contacto = Contacto(email=email, nombre=name, phone=telefono, tipocomentario=motivo, 
                comentario=comentario, teatroid=identificador)
            """
               
            