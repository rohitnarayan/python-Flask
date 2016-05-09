from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def homepage(user=None):
    return render_template("profile.html",user=user)
'''
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html",name=name)
'''

if __name__ == "__main__":
    app.run(debug=True)
