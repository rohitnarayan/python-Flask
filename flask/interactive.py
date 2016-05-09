from flask import Flask, render_template, request, url_for, redirect, jsonify
import mysql.connector as mycon

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("back.html")


@app.route('/inter')
def inter():
	return render_template('interactive.html')

@app.route('/background', methods=['POST'])
def background():
	name = request.form['name']
	email = request.form['email']
	return "data submitted"

@app.route('/getdata')
def getdata():

	conn = mycon.connect(user='root',password='',host='localhost',database='test')
	cursor = conn.cursor()
	sql = "SELECT *FROM country"
	cursor.execute(sql)
	k = cursor.fetchall()
	redirect('/inter')
	return render_template('interactive.html',country=k)

if __name__=='__main__':
	app.run(debug=True)