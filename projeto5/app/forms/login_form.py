from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from usuarios import USUARIOS

class loginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Login")

    def validate_email(self, campo):
        if not campo.data in USUARIOS:
            raise ValidationError("Email não encontrado")
        
    def validate_senha(self, campo):
        if self.email.data not in USUARIOS:
            return
        if USUARIOS[self.email.data]['senha'] != campo.data:
            raise ValidationError("Senha incorreta!")