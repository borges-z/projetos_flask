from app import app
from flask import render_template, session, redirect, url_for
from ..forms.login_form import loginForm


@app.route('/', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        session['user'] = form.email.data
        return redirect(url_for('home'))
    return render_template('login.html', form=form)