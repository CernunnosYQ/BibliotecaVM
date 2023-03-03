from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

import environment

environment.setEnv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_DATABASE']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'the most secret key'
db = SQLAlchemy(app)

class Libros(db.Model):
    id_libros = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(75), nullable=False)
    autor = db.Column(db.String(75), nullable=False)
    status = db.Column(db.String(100))

    def obtenerDatos(self):
        return [self.id_libros, self.titulo, self.autor, self.status]

    def __repr__(self):
        return '<Titulo: {}, Autor: {}, Status: {}>'.format(self.titulo, self.autor, self.status)

@app.route('/')
def dashboard():
    aux_list = Libros.query.all()
    data = []
    for i in aux_list:
        data.append(i.obtenerDatos())
            
    return render_template('dashboard.html', datos = data)

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        a_id_libro = request.form['id_libro']
        a_titulo = request.form['titulo']
        a_autor = request.form['autor']
        a_status = request.form['estatus']

        if a_id_libro == '':
            nuevo_libro = Libros(titulo=a_titulo, autor=a_autor, status=a_status)
            db.session.add(nuevo_libro)
            db.session.commit()
        else:
            libro = Libros.query.filter_by(id_libros=int(a_id_libro)).first()
            libro.titulo = a_titulo
            libro.autor = a_autor
            libro.status = a_status

            db.session.commit()

        return 'Update Complete'

@app.route('/newcsv', methods=['POST'])
def newCsv():
    if request.method == 'POST':
        csv = request.form['csv']
        lineas = csv.split(',\n')
        
        for linea in lineas:
            linea = linea.split(',')
            a_titulo = linea[0].capitalize()
            a_autor = linea[1].title()
            a_status = linea[2].capitalize()

            nuevo_libro = Libros(titulo=a_titulo, autor=a_autor, status=a_status)
            db.session.add(nuevo_libro)
            db.session.commit()

        return 'Booklist Added'

@app.route('/delete', methods=['POST'])
def delete_book():
    if request.method == 'POST':
        a_id_libro = request.form['id_libro']
        libro = Libros.query.filter_by(id_libros=a_id_libro).first()

        db.session.delete(libro)
        db.session.commit()

    return 'Book Deleted'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context(): db.create_all()
    app.run(debug=True)