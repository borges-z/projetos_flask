from app import app
from flask import render_template, redirect, url_for, flash, request
from ..forms.contato_form import contatoForm
from ..entidades.contato import Contato
from ..services import contato_service
from ..models.contato_model import contatoModel

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = contatoForm()
    if form.validate_on_submit():
        contato = contatoModel(
            nome = form.nome.data,
            email = form.email.data,
            telefone = form.telefone.data
        )
        contato_service.cadastrar_contato(contato)
        flash('Contato cadastrado com sucesso!', 'sucesso')
        return redirect(url_for('home'))
    return render_template('cadastrar_contato.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    contato_db = contato_service.listar_contato(id)
    if not contato_db:
        return redirect(url_for('home'))
    form = contatoForm(obj=contato_db)
    if form.validate_on_submit():
        contato = Contato(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data)
        resultado = contato_service.editar_contato(id, contato)
        if not resultado:
            flash(resultado, 'erro')
            return render_template('contato.html', form=form, id_contato=contato_db.id_contato)
        flash('Contato editado com sucesso', 'sucesso')
        return redirect(url_for('home'))
    return render_template('contato.html', form=form, id_contato=contato_db.id_contato)

@app.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    contato_db = contato_service.listar_contato(id)
    if not contato_db:
        return redirect(url_for('home'))
    contato_service.excluir_contato(id)
    flash("Contato excluído com sucesso", 'sucesso')
    return redirect(url_for('home')) 