from flask import Flask, request
from flask_restful import Resource, Api
import time
import sys
import serial 

port = '/dev/ttyACM0'

sFA = serial.Serial(port,115200)
sFA.flushInput()

app = Flask(__name__)
api = Api(app)

command = 0

@app.route('/')
	

def index():
	return 'Phone Printer conection successful -V'


class ApiCall(Resource):
	def get(self, distance,speed):
		print('Distance-> ' + distance + '\n' + 'Speed-> ' + speed + '\n')

		command = 2
		sFA.write((str(command)+'\r').encode())
		
api.add_resource(ApiCall,'/<distance>,<speed>')

if __name__ == '__main__' :
	app.run(debug=True,host='0.0.0.0')
