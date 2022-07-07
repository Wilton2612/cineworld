from flask import Blueprint, request, jsonify, render_template

from ..controller import servant_controller
from ..models.servant_model import Servicio

from ..helpers import principal


servant = Blueprint('servant', __name__, template_folder='../templates')

@servant.route("/servicios", methods=['GET'])
def servicios_teatro():
    identificador = principal.leer()
    if identificador is None:
        return render_template('error.html')
    else:
        servicios_lista = servant_controller.lista_servicio_teatro(identificador)
        servicios_dict = [servicio._asdict() for servicio in servicios_lista]
        teatro_asociado = servant_controller.theater_index(identificador)
        return render_template('servicios.html', servicios_lista=servicios_lista, teatro=teatro_asociado)
        #return jsonify(servicios_dict)