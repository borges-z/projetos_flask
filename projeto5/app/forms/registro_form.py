from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from usuarios import USUARIOS

class registroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmar_senha = PasswordField("Confirmar_senha", validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField("Cadastrar")

    def validate_email(self, campo):
        if campo.data in USUARIOS:
            print(campo.data)
            raise ValidationError("O email informado já foi cadastrado!")
    def validate_nome(self, campo):
        for usuario in USUARIOS:
            if USUARIOS[usuario]['nome'] == campo.data:
                raise ValidationError("Já existe um usuário com esse nome!")