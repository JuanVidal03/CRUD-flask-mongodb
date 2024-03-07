# importar flask y coleccion de la db
from flask import Flask, render_template
from app import app, categorias

@app.route('/categorias')
def get_categoria():
    todas_las_categorias = categorias.find()
    return render_template('listarProductos.html', categorias = todas_las_categorias)