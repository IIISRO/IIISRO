from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField, validators, ValidationError
from wtforms.validators import DataRequired, Length


def validate_email(form, field):
        if not "@gmail.com" in field.data:
            raise ValidationError("Field must be with @gmail.com")

class ContactForm(FlaskForm):
    your_name = StringField(label='Your Name', name="name", validators=[DataRequired(), Length(min = 3, max = 30)], render_kw={"placeholder": "Enter your name"})
    email = EmailField(label="Email", name = "email", validators=[DataRequired(), validate_email,Length(min = 3, max = 20)], render_kw={"placeholder": "Enter your email address"})
    services = SelectField(label="Needed Services", name = "service", choices=[("", "Choose Services"), ("OStr", "Online Store"), ("eCB", "eCommerce Business"), ("UUD", "UI/UX Design"), ("OSer", "Online Services")])
    budget = SelectField(label="Budget", name = "budget", choices=[("", "Select Budget"), (1500, "1500 $"), (2000, "2000 $"), (2500, "2500 $")])
    message = TextAreaField(label="Message", name = "message", render_kw={"placeholder": "Your message here ..."}, validators=[validators.Optional()])
    

            
    