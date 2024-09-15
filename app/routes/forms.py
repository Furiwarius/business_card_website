from wtforms import Form, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class ContactForm(Form):
    username = StringField(label="Имя: ", validators=[DataRequired()])
    phonenumber = IntegerField(label="Ваш номер: ", validators=[DataRequired(), NumberRange(11)])
    email = StringField(label="Email: ", validators=[DataRequired()])
    submit = SubmitField("Оставить заявку")