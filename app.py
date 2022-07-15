import os
from flask import Flask, url_for, send_from_directory
from flask_wtf.csrf import CSRFProtect


from src.routes.theater_route import theaterss
from src.routes.servant_route import servant
from src.routes.request_route import solicitud
from src.routes.movie_route import movie
from src.routes.food_route import food
from src.routes.complaint_route import contact
from src.routes.errors import errors


app = Flask(__name__)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

app.register_blueprint(theaterss, url_prefix='/')
app.register_blueprint(servant, url_prefix='/')
app.register_blueprint(solicitud, url_prefix='/')
app.register_blueprint(movie, url_prefix='/')
app.register_blueprint(food, url_prefix='/')
app.register_blueprint(contact, url_prefix='/')
app.register_blueprint(errors)


