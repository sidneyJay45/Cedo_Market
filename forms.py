from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
   
    username = StringField(label='Username', validators=[DataRequired(), Length(min=4, max=20)])
    email_address = StringField(label='Email Address', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired(),])
    password = PasswordField(label='Password', validators=[DataRequired(),])
    submit = SubmitField(label='Login')


class PurchaseItemForm(FlaskForm):
  submit = SubmitField(label='Purchase')


class SellItemForm(FlaskForm):
  item = StringField('Item', validators=[DataRequired()])
  submit = SubmitField(label='Sell Item!')

class PurchaseItemForm(FlaskForm):
  item = StringField('Item', validators=[DataRequired()])
  submit = SubmitField('Purchase Item')

