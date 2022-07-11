from flask import Flask

from src.routes.theater_route import theaterss
from src.routes.servant_route import servant
from src.routes.request_route import solicitud
from src.routes.movie_route import movie
from src.routes.food_route import food
from src.routes.complaint_route import contact


app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

    

app.register_blueprint(theaterss, url_prefix='/')
app.register_blueprint(servant, url_prefix='/')
app.register_blueprint(solicitud, url_prefix='/')
app.register_blueprint(movie, url_prefix='/')
app.register_blueprint(food, url_prefix='/')
app.register_blueprint(contact, url_prefix='/')



