from flask import Flask, render_template, request, session, redirect, url_for, escape

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    session['logged_in'] = False
    return render_template('index2.html',name="Rohit")

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# @app.route('apply')
# def apply():
	

if __name__ == '__main__':
    app.run(debug=True)
