from flask import Flask

from src.theater.routes.theater_route import theaterss
from src.servant.routes.servant_route import servant
from src.request.routes.request_route import solicitud
from src.movie.routes.movie_route import movie
from src.food.routes.food_route import food
from src.complaint.routes.complaint_route import complaint
from src.principal import princi

app = Flask(__name__)


    

app.register_blueprint(theaterss, url_prefix='/')
app.register_blueprint(servant, url_prefix='/')
app.register_blueprint(solicitud, url_prefix='/')
app.register_blueprint(movie, url_prefix='/')
app.register_blueprint(food, url_prefix='/')
app.register_blueprint(complaint, url_prefix='/')
app.register_blueprint(princi, url_prefix='/')


