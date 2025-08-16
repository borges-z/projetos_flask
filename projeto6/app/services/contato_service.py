from app import db
from ..models.contato_model import contatoModel

def listar_contatos():
    contatos = contatoModel.query.all()
    return contatos

def listar_contato(id):
    contato = contatoModel.query.filter_by(id_contato=id).first()
    return contato

def cadastrar_contato(contato):
    db.session.add(contato)
    db.session.commit()

def editar_contato(id, contato):
    contato_db = contatoModel.query.filter_by(id_contato=id).first()
    contato_db.nome = contato.nome
    contato_db.email = contato.email
    contato_db.telefone = contato.telefone
    db.session.commit()

def excluir_contato(id):
    contato = listar_contato(id)
    db.session.delete(contato)
    db.session.commit()
