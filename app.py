from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.comfig["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///biblioteca.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capa = db.Column(db.String)
    texto = db.Column(db.String)
    titulo = db.Column(db.String)
    valor = db.Column(db.Float)
    link = db.Column(db.String, unique=True, nullable=False)

#rota para adicionar livro
@app.route("api/book/add", methods=["POST"])
def add_book():
    data = request.json

    if "capa" in data and "titulo" in data and "valor" in data:
        book = Book(capa=data["capa"], texto=data['texto'], titulo=data["titulo"], valor=data["valor"], link=data["link"])
        db.session.add(book)
        db.session.commit()

        return jsonify({"message" : "Book added succesfully!"})
    return jsonify({"Message" : "invalid product data"}), 400