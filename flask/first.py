from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

@app.route('/profile/<username>')
def profile(username):
    return "Profile : %s" % username


if __name__ == '__main__':
    app.run(debug=True)
