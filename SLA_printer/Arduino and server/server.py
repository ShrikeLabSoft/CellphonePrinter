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
	def get(self, motor, direc, speed):

		print('Motor-> ' + motor + 'Direction-> ' + direc + '\n' + 'Speed-> ' + speed + '\n')

		sFA.write((str(motor)+'\r').encode())
		sFA.write((str(direc)+'\r').encode())
		sFA.write((str(speed)+'\r').encode())
		
api.add_resource(ApiCall,'/<motor>,<direc>,<speed>')

if __name__ == '__main__' :
	app.run(debug=True,host='0.0.0.0')
