from app import app
from flask import render_template, flash, url_for, redirect
from ..forms.contato_form import ContatoForm

with open('mensagens.txt', 'w') as f:
    f.write("==================== Inicio ====================\n")

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data
        with open('mensagens.txt', 'a', encoding='utf-8') as f:
            f.write(f"{nome} - {email}\n{mensagem}\n========== FIM =========\n")
        flash("Dados enviados com sucesso!", "form_sucesso")
        return redirect(url_for('contato'))
    return render_template('contato.html', form=form)