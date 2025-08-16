from app import app
from flask import render_template
from ..services import contato_service

@app.route('/')
def home():
    contatos = contato_service.listar_contatos()
    return render_template('home.html', contatos=contatos)