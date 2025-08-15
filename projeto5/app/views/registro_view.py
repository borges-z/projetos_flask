from app import app
from flask import render_template, redirect, url_for
from ..forms.registro_form import registroForm
from usuarios import USUARIOS


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = registroForm()
    if form.validate_on_submit():
        USUARIOS[form.email.data] = {
            'nome': form.nome.data,
            'senha': form.senha.data
        }
        return redirect(url_for('login'))
    return render_template('registro.html', form=form)