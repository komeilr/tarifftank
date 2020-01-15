from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField, StringField, SubmitField, validators

class ContactForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email(), validators.Length(max=255)])
    subject = StringField('Subject', [validators.DataRequired()])
    message = TextAreaField('Message', [validators.DataRequired()])
    submit = SubmitField('Send')
    recaptcha = RecaptchaField()

class SearchForm(FlaskForm):
    keyword = StringField('search', [validators.DataRequired()])