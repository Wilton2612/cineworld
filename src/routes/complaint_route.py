from flask import Blueprint, request, jsonify, render_template

contact = Blueprint('contact', __name__, template_folder='../templates')

@contact.route("/contactanos", methods=['GET', 'POST'])
def contacto_cliente():
    if request.method == 'GET':
        return render_template('contacto.html')
    if request.method == 'POST':
        return redirect_request("/contactanos")