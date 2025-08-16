from app import db

class contatoModel(db.Model):
    id_contato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(50))