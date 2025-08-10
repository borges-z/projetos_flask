from app import app
from flask import render_template, session, redirect, url_for
from ..forms.todo_form import todoForm

@app.route('/', methods=["GET", "POST"])
def todo():
    if "tarefas" not in session:
        print("entrou")
        session['tarefas'] = []
    form = todoForm()
    print(len(session['tarefas']))
    if form.validate_on_submit():
        tarefa = form.tarefa.data
        status = form.status.data
        print(session['tarefas'])
        tarefas = session.get("tarefas", [])
        tarefas.append([tarefa, status])
        session['tarefas'] = tarefas
        return redirect(url_for("todo"))
    return render_template("todo_view.html", form=form, tarefas=session['tarefas'])