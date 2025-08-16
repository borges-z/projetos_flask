from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from ..models.contato_model import contatoModel

class contatoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email(), DataRequired()])
    telefone = TelField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def validate_email(self, email):
        resultado = contatoModel.query.filter_by(email=email.data).first()
        if resultado:
            raise ValidationError("Email já cadastrado!")