from app import app
from flask import render_template, session, redirect, url_for
from usuarios import USUARIOS

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'use' not in session or session['user'] not in USUARIOS:
        return redirect(url_for('login'))
    usuario = {
        'email': session['user'],
        'nome': USUARIOS[session['user']]['nome']
    }
    return render_template('home.html', usuario=usuario)

@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('login'))