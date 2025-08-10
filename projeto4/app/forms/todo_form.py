from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class todoForm(FlaskForm):
    tarefa = StringField("Tarefa", validators=[DataRequired()])
    status = SelectField("Status", validators=[DataRequired()], choices=[("1","Pendente"), ("2","Em progresso"), ("3","Concluído")])
    submit = SubmitField("Adicionar")