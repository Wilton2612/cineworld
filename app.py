from flask import Flask

from src.routes.theater_route import theaterss
from src.routes.servant_route import servant
from src.routes.request_route import solicitud
from src.routes.movie_route import movie
from src.routes.food_route import food
from src.routes.complaint_route import contact
from src.helpers.principal import princi

app = Flask(__name__)


    

app.register_blueprint(theaterss, url_prefix='/')
app.register_blueprint(servant, url_prefix='/')
app.register_blueprint(solicitud, url_prefix='/')
app.register_blueprint(movie, url_prefix='/')
app.register_blueprint(food, url_prefix='/')
app.register_blueprint(contact, url_prefix='/')
app.register_blueprint(princi, url_prefix='/')


