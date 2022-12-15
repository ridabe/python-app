from app import Form, StringField, DataRequired, PasswordField, EmailField

class registerForm(Form):
    userName = StringField("userName", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
class loginForm(Form):    
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])    