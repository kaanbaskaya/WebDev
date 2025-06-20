from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField,EmailField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email

#Erstellt Register
class CreateRegisternForm(FlaskForm):  
    #Felder für die Eingabe für die Registrierung
    name = StringField('Name', [DataRequired(), Length(min=2)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    university = SelectField('Universität', choices=[], coerce=int, validators=[DataRequired()])
    birthday = DateField('Date of Birth', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Finish')