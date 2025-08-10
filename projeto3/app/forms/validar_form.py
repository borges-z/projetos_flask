from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Regexp, Length

class ValidadorForm(FlaskForm):
    cpf = StringField("CPF", validators=[Regexp(r"\d\d\d\.\d\d\d\.\d\d\d-\d\d", message="O CPF deve conter 11 dígitos com a pontuação necessária"), Length(min=14, max=14)], render_kw={"placeholder": "Ex: 000.000.000-00"})
    submit = SubmitField("Validar")