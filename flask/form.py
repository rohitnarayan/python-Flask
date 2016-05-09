from flask import Flask , render_template, request
from wtforms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jjghhhdbgrad3432hjjjvbhgfredssg'
app.config['CSRF_SESSION_KEY'] = 'jjghhhdbgrad3432hjjjvb8877ttggfdssg'

class myForm(Form):
	name = TextField("Name")
	passwrd = PasswordField("Password")
	submit = SubmitField()

@app.route('/')
def index():
	
	form = myForm()

	return render_template('form.html',form=form)

if __name__=='__main__':
	app.run(debug=True)