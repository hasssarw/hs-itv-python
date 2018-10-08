from flask import Flask
import psycopg2
from flask.json import jsonify
#from waitress import serve

     


app = Flask(__name__)

@app.route('/users/<string:username>')
#serve(app, host='0.0.0.0',port=8080)

def hello_world(username=None):
	if username == 'Elena':
		val = 'Senior Data Scientist'
	elif username == 'Karishma':
		val = 'Senior Analyst'
	elif username == 'Rob':
		val = 'MI6 Secret Agent'
	elif username == 'Annie':
		val = 'Data Scientist'
	elif username == 'Hassan':
		val = 'Alteryx Salesman'
	else:
		val = 'Unknown'

	return("Hello {}!, You are a {}!".format(username,val))

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)