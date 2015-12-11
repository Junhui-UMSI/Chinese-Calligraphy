from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField


class ContactForm(Form):
  name = TextField("Name")
  email = EmailField("Email")
  password = TextField("Password")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
#
# class ProfileForm(Form):
#   name = TextField("Name")
#   email = EmailField("Email")
#   password = TextField("Password")
#   subject = TextField("Subject")
#   message = TextAreaField("Message")
#   submit = SubmitField("Send")
class GeturlForm(Form):
    imageurl = TextField("imageurl")
    submit = SubmitField("Collect this masterpieces")
