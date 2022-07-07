from flask import Blueprint, request, jsonify, render_template

solicitud = Blueprint('request', __name__)

@solicitud.route("/solicitudes", methods=['GET', 'POST'])
def solicitudes():
    if request.method == 'GET':
        return render_template('solicitud.html')
    if request.method == 'POST':
        return redirect_request("/solicitudes")