from flask import Flask, render_template, request, url_for
import mysql.connector as myc

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('names.html')

@app.route('/getdata')
def fetch():
	conn = myc.connect(user='root', password='', host='localhost', database='test')
	curs = conn.cursor()
	sql = "SELECT * FROM country"
	cursor.execute(sql)
	data = curs.fetchall()
	return data

if __name__ == "__main__":
    app.run(debug=True)