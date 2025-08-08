from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class CalculadoraForm(FlaskForm):
    peso = FloatField("Peso", validators=[DataRequired()], render_kw={"placeholder": "Ex: 72.5"})
    altura = FloatField("Altura", validators=[DataRequired()], render_kw={"placeholder": "Ex: 1.75"})
    submit = SubmitField("Calcular")