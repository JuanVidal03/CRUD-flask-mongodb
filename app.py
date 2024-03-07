# inicializando flask y mongo
import pymongo
from flask import Flask
app = Flask(__name__)
# para subir las imagenes000
app.config['UPLOAD_FOLDER'] = './static/img'

# conexion base de datos
coexion = pymongo.MongoClient('mongodb://localhost:27017')
db = coexion['crud-flask-mongo']
productos = db['productos']
categorias = db['categorias']


# controladores
from controllers.producto_contoller import *
from controllers.categoria_controller import *


# corriendo servidor
if __name__ == '__main__':
    app.run(port=8080, debug=True)