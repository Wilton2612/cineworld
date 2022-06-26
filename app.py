from flask import Flask

from src.theater.routes.theater_route import theater
from src.servant.routes.servant_route import servant
from src.request.routes.request_route import solicitud
from src.movie.routes.movie_route import movie
from src.food.routes.food_route import food
from src.complaint.routes.complaint_route import complaint

app = Flask(__name__)

app.register_blueprint(theater)
app.register_blueprint(servant)
app.register_blueprint(solicitud)
app.register_blueprint(movie)
app.register_blueprint(food)
app.register_blueprint(complaint)



