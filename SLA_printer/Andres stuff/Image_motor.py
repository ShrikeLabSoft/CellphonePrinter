#######################################################################
#  Name:                 Basic Motor and Image controller
#  File Name:            Image_motor.py    (To Be Defined)
#  Start Date:           21/May/2019
#  Developed by:         ShrikeLab
#  Programmer:           Andres Garcia Rubio
#  Experiment:           SLA Printing
#  References:           
#  Language:             Python
#  Abstract:             Script for oxygen sensor using protocol TCP/IP
#  Hardware:             Ubuntu 64 bit/ Raspberry Pi Zero W
#  IDE:                  Sublime Text
#  Notes:                
#
#The STL slicer we're using comes from https://formlabs.com/blog/open-source-dlp-slicer/
#http://www.mattkeeter.com/projects/dlp/
#######################################################################


import os
import pygame
import serial
import time
from PIL import Image



#checksum for motor command
def checksum(numbers):
    added = sum(numbers)
    lower_byte = added & 255
    inverted = lower_byte ^ 255
    return inverted

#send a commando over wire to the motor
def send_command(id_servo,commands):
    orders = [id_servo,len(commands)+1] + commands
    try:
        values = bytearray([0xFF,0xFF,0xFF]+orders+[checksum(orders)])
        ser.write(values)
        time.sleep(0.5)
        ser_bytes = ser.readline()
        return(list(ser_bytes))
    except:
        print("Keyboard Interrupt")
 
 #echo command to motor      
def echo(id_servo):
    commands = [0xF1]
    send_command(id_servo,commands)
    
def read_position(id_servo):
    commands = [0xF2,0x8C,0X02]
    return(send_command(id_servo,commands))


def set_position(id_servo, position):
    digital_position = mm_to_stroke(position)
    position = [digital_position%256,digital_position//256]
    commands = [0xF3,0x86]
    send_command(id_servo,commands+position)
    
def mm_to_stroke(milimeters):
    return (int(milimeters*136.5))

 #return analog distance to the motor
def analog_read_mm(id_servo):
    position_data = read_position(id_servo)
    pygame.time.wait(100)
    data_numbers = [ord(num) for num in position_data[6:8]]
    analog_dist = (data_numbers[1]*256 + data_numbers[0])*0.007326
    print(analog_dist)
    return(analog_dist)
    

def increase(id_servo):
    set_position(id_servo, analog_read_mm(id_servo)+z_resolution)
    
def decrease(id_servo):
    set_position(id_servo, analog_read_mm(id_servo)-z_resolution)
    
def cycle(id_servo):
    decrease(id_servo)
    increase(id_servo)
    
def make_string_picture(number):
    filename = os.path.join(fileDir, 'Images/out'+str(number).zfill(4)+'.png')
    return(filename)
        
def modify_formlabs(image):
    im = Image.open(image)
    bg = Image.new("RGB", im.size, (0,0,0))
    bg.paste(im,im)
    bg.save("Images/new_image.jpg")

def init_image(id_servo):
    
    formlabs_image_number = 0
    
    def cycle(id_servo):
        decrease(id_servo)
        increase(id_servo)
    
    def image(x,y,image_to_display):
        gameDisplay.blit(image_to_display, (x,y))
    
    pygame.init()

    display_width = 2000
    display_height = 1000

    gameDisplay = pygame.display.set_mode((display_width,display_height))

    black = (0,0,0)
    white = (255,255,255)
    
    clock = pygame.time.Clock()
    crashed = False
    screen_image = pygame.image.load('new_image.jpg')

    x =  (display_width * 0.1)
    y = (display_height * 0.1)
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
        #main running program
        gameDisplay.fill(black)
        screen_image = pygame.image.load(make_string_picture(formlabs_image_number))
        image(x,y,screen_image)
        formlabs_image_number =+ 1
        decrease(id_servo)
        print("decreased")
        pygame.display.update()
        pygame.time.wait(1500)
        increase(id_servo)
        print("increased")
        increase(id_servo)
        print("increased")
        pygame.time.wait(1500)
        formlabs_image_number += 1

    pygame.quit()

id_servo = 1
z_resolution = 0.1
initial_position = 15
fileDir = os.path.dirname(os.path.realpath('__file__'))
ser = serial.Serial('/dev/ttyUSB0',57600, timeout=2)
set_position(id_servo, initial_position)
init_image(id_servo)
quit()
