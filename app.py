from flask import Flask
from flask_mysqldb import MySQL

from src.theater.routes.theater_route import theater
from src.servant.routes.servant_route import servant
from src.request.routes.request_route import solicitud
from src.movie.routes.movie_route import movie
from src.food.routes.food_route import food
from src.complaint.routes.complaint_route import complaint

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='cine'    

mysql = MySQL(app)

app.register_blueprint(theater)
app.register_blueprint(servant)
app.register_blueprint(solicitud)
app.register_blueprint(movie)
app.register_blueprint(food)
app.register_blueprint(complaint)


if __name__ == '__main__':
    app.run(port=8080, debug=True)

