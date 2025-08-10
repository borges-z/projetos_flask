from app import app
from flask import render_template
from ..forms.validar_form import ValidadorForm

@app.route("/", methods=["GET", "POST"])
def validar():
    form = ValidadorForm()
    if form.validate_on_submit():
        CPF = form.cpf.data
        CPF = CPF.replace(".", "").replace("-", "")

        primeiro_passo = False
        segundo_passo = False

        index = 10
        soma = 0
        for cpf in CPF[:9]:
            resultado = int(cpf) * index
            index -= 1
            soma += resultado
        resultado = soma % 11
        if resultado < 2:
            numero_magico = 0
        elif resultado >= 2:
            numero_magico = 11 - resultado
        if numero_magico == int(CPF[9]):
            primeiro_passo = True
        else:
            return render_template("validar.html", form=form, validado=False)
        index = 11
        soma = 0
        for cpf in CPF[:10]:
            resultado = int(cpf) * index
            index -= 1
            soma += resultado
        resultado = soma % 11
        if resultado < 2:
            numero_magico = 0
        elif resultado >= 2:
            numero_magico = 11 - resultado
        if numero_magico == int(CPF[10]):
            segundo_passo = True
        else:
            return render_template("validar.html", form=form, validado=False)
        if primeiro_passo == True and segundo_passo == True:
            return render_template("validar.html", form=form, validado=True)

    return render_template("validar.html", form=form)