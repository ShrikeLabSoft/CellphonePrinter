import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time

#Setting up the pins for the stepper motor driver
def motor_setup():
	gpio.setmode(gpio.BCM)
	#GPIO23 = Direction
	#GPIO24 = Step
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

#The motor has a step angle of 1.8°
#the screw has a diameter of 6mm
#Easydriver has been configured to run at 1/8 microstep
#Each microstep size is ideally 0.625um
	
def move_z_axis(distance_mm, speed_mm_s):
    if(distance_mm < 0):
        gpio.output(23,True)
    else:
        gpio.output(23,False)
    step_counter = int(abs(distance_mm)/0.000625)
    period = float(0.000625/speed_mm_s)
    print(period)
    print(step_counter)
    steps = 0
    while(step_counter > steps):
        gpio.output(24, True)
        gpio.output(24, False)
        steps += 1	
        time.sleep(period)
    gpio.cleanup()

