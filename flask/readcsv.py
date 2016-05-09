from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
	names = readCsv()
	return render_template('csvfile.html',names=names)

def readCsv():

	with open('scores.txt') as csvfile:
		readHandle = csv.reader(csvfile)
		names=[]
		for row in readHandle:
			names = names+[row]
	csvfile.close()
	return names

if __name__ == '__main__':
	app.run(debug=True)