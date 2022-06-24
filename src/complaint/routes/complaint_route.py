from flask import Blueprint

complaint = Blueprint('complaint', __name__)

@complaint.route("/queja")
def index():
    return "Quejas"