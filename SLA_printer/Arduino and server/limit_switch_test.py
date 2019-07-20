import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time

enable_motor = True
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

switchPin = 17
gpio.setup(switchPin, gpio.IN, pull_up_down = gpio.PUD_UP)  

#Setting up the pins for the stepper motor driver
def motor_setup():
    #GPIO23 = Direction
    #GPIO24 = Step
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_UP)

#The motor has a step angle of 1.8
#the screw has a diameter of 6mm
#Easydriver has been configured to run at 1/8 microstep
#Each microstep size is ideally 0.625um

def check_switch():
    switchVal = gpio.input(switchPin)
    if(switchVal == True):
        print('Not pressed')
        return True
    else:
        print("pressed")
        return False


def move_z_axis(distance_mm, speed_mm_s):
    if(distance_mm < 0):
        gpio.output(23,True)
    else:
        gpio.output(23,False)
    step_counter = int(abs(distance_mm)/0.000625)
    period = float(0.000625/speed_mm_s)
    steps = 0
    
    while(step_counter > steps and check_switch()):#gpio.input(10)):
        gpio.output(24, True)
        gpio.output(24, False)
        steps += 1  
        time.sleep(period)
    
motor_setup()
move_z_axis(-5, 50)
gpio.cleanup()