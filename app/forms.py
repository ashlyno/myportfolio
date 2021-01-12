from wtforms import Form, StringField, TextAreaField, SubmitField, validators, ValidationError

class contactForm(Form):
    name = StringField("name", [validators.DataRequired()])
    email = StringField("email", [validators.DataRequired()])
    subject = StringField("subject", [validators.DataRequired()])
    message = TextAreaField("message", [validators.DataRequired()])
    submit = SubmitField("Send")