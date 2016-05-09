from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

@app.route('/food')
def food():
    food = ['cheese','burger','maggie']
    places = ['kolkata','mumbai','pune','chennai']
    return render_template('food.html',food=food,places=places)



if __name__ == "__main__":
    app.run(debug=True)
