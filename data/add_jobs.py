from flask import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    title = StringField('Название работы', validators=[DataRequired()])
    team_leader = IntegerField('ID Тим-Лида', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collabortors = StringField('Рабочие', validators=[DataRequired()])
    is_finished = BooleanField("Закончена работа?")

    submit = SubmitField('Сдать')
