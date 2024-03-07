# importar flask y la base de datos
from flask import render_template
from app import app, productos

@app.route('/')
def init():
    all_products = productos.find()
    return render_template('listarProductos.html', productos = all_products)