from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired


class OrderForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    description = TextAreaField('Опишите функционал бота, которого вы хотите получить', validators=[DataRequired()])
    sumbit = SubmitField('Хочу такого бота')