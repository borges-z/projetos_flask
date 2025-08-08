from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import Length, Email, DataRequired

class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    mensagem = TextAreaField("Mensagem", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Enviar")