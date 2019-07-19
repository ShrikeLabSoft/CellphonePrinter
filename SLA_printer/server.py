from flask import Flask, request
from flask_restful import Resource, Api
import RPi.GPIO as gpio
import time
import sys
import serial #to allow communication

port = '/dev/ttyACM0'

sFA = serial.Serial(port,115200)
sFA.flushInput()

app = Flask(__name__)
api = Api(app)

command = 0

@app.route('/')

def motor_setup():
	gpio.setmode(gpio.BCM)
	gpio.setup(18, gpio.OUT)
	gpio.setup(24, gpio.OUT)


def move_z_axis(distance_mm, speed_mm_s):
	
	if(int(distance_mm) < 0):
		gpio.output(18,True)
	else:
		gpio.output(18,False)
	step_counter = float(abs(float(distance_mm))/0.000625)
	period = float(0.000625/float(speed_mm_s))
	steps = 0
	while(step_counter > steps):
		
		gpio.output(24,True)
		gpio.output(24,False)
		steps += 1
		time.sleep(period)
	gpio.output(18,False)
	

def index():
	return 'Phone Printer conection successful -V'


class ApiCall(Resource):
	def get(self, distance,speed):
		print('Distance-> ' + distance + '\n' + 'Speed-> ' + speed + '\n')
		#move_z_axis(distance,speed)

		command = 2
		sFA.write((str(command)+'\r').encode())
		
api.add_resource(ApiCall,'/<distance>,<speed>')

if __name__ == '__main__' :
	#motor_setup()
	app.run(debug=True,host='0.0.0.0')
