from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_login import current_user

class RegistrationForm(FlaskForm):
    