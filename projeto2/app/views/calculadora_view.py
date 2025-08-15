from app import app
from flask import render_template, redirect, url_for, flash
from ..forms.calculadora_form import CalculadoraForm

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    form = CalculadoraForm()
    if form.validate_on_submit():
        peso = form.peso.data
        altura = form.altura.data
        imc = peso / (altura * altura)
        classificacao = ""
        if peso <= 0 or altura <= 0:
            flash("Os dados não podem ser zero ou menor que zero!", "Aviso")
            return redirect(url_for('calculadora'))
        if imc < 18.5:
            classificacao = "Baixo peso"
        elif imc >= 18.5 and imc <= 24.9:
            classificacao = "Peso Normal"
        elif imc >= 25 and imc <= 29.9:
            classificacao = "Excesso de peso"
        elif imc >= 30 and imc <= 34.9:
            classificacao = "Obesidade de Classe 1"
        elif imc >= 35 and imc <= 39.9:
            classificacao = "Obesidade de Classe 2"
        elif imc >= 40:
            classificacao = "Obesidade de Classe 3"
        print(imc)
        print(classificacao)
        return render_template('calcular.html', form=form, classificacao=classificacao)
    return render_template('calcular.html', form=form)
