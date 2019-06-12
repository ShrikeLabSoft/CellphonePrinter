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

    display_width = 1000
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
        scaled_image = pygame.transform.scale(screen_image, (200, 200))
        image(x,y,scaled_image)
        pygame.display.update()
        pygame.time.wait(1000)
        formlabs_image_number += 1
        if (formlabs_image_number == 550):
            break

    pygame.quit()

start = time.time()

id_servo = 1
z_resolution = 0.1
initial_position = 15
fileDir = os.path.dirname(os.path.realpath('__file__'))
#ser = serial.Serial('/dev/ttyUSB0',57600, timeout=2)
#set_position(id_servo, initial_position)
init_image(id_servo)
end = time.time()
print("Lenovo Thinkpad W540 Intel Core i7 2.4GHz 8Gb RAM 8 Cores")
print("Time used to process images with computer")
print(end - start)
quit()
