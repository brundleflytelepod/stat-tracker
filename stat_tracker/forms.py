from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, URL
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                              EqualTo('verify_password',
                                       message='Passwords did not match')])
    verify_password = PasswordField('Verify Password')


class AddNewAction(Form):
    name = StringField('Action Name', validators=[DataRequired()])

class EditAction(Form):
    name = StringField('Action Name', validators=[DataRequired()])

class AddNewStat(Form):
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    date = DateField('Date YYYY-MM-DD', validators=[DataRequired()])
