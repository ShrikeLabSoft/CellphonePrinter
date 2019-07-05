# -*- coding: utf-8 -*-
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
import pygame, sys
import serial


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
    data_numbers = [ord(num) for num in position_data[6:8]]
    analog_dist = (data_numbers[1]*256 + data_numbers[0])*0.007326
    print(analog_dist)
    return(analog_dist)
    

def increase(id_servo):
    set_position(id_servo, analog_read_mm(id_servo)+1)
    
def decrease(id_servo):
    set_position(id_servo, analog_read_mm(id_servo)-1)
    
def cycle(id_servo):
    decrease(id_servo)
    increase(id_servo)


black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Keyboard Example')
size = [1920,1080]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

x = 100
y = 100
x_size = 200
y_size = 200

# using this to set the size of the rectange
# using this to also move the rectangle
step = 20

# by default the key repeat is disabled
# call set_repeat() to enable it
pygame.key.set_repeat(50, 50)
test_image = pygame.image.load('itsworking.png')

while True:
    id_servo = 1
    ser = serial.Serial('/dev/ttyUSB0',57600, timeout=2) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gpio.cleanup()
            sys.exit()
        # check if key is pressed
        # if you use event.key here it will give you error at runtime
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= step
            if event.key == pygame.K_RIGHT:
                x += step
            if event.key == pygame.K_UP:
                y -= step
            if event.key == pygame.K_DOWN:
                y += step
            if event.key == pygame.K_DOWN:
                y += step
            if event.key == pygame.K_d:
                x_size += step
            if event.key == pygame.K_a:
                x_size -= step
            if event.key == pygame.K_w:
                y_size += stepimport serial
            if event.key == pygame.K_s:
                y_size -= step
            if event.key == pygame.K_p:
                print("X image size: " + str(x_size))
                print("Y image size: " + str(y_size))
                print("X screen coordinate: " + str(x))
                print("Y screen coordinate: " + str(y))
            if event.key == pygame.K_j:
                increase(id_servo)
            if event.key == pygame.K_n:
                increase(id_servo)

            # checking if left modifier is pressed
            if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                if event.key == pygame.K_LEFT:
                    x = 0
                if event.key == pygame.K_RIGHT:
                    x = 1920- step
                if event.key == pygame.K_UP:
                    y = 0
                if event.key == pygame.K_DOWN:
                    y = 1080 - step
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)


    screen.fill(black)

    scaled_image = pygame.transform.scale(test_image, (x_size, y_size))
    screen.blit(scaled_image, (x,y))

    pygame.display.update()
    clock.tick(5)


