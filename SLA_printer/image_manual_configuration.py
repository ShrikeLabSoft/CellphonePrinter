import pygame, sys

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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
                y_size += step
            if event.key == pygame.K_s:
                y_size -= step
            if event.key == pygame.K_p:
            	print("X image size: " + str(x_size))
            	print("Y image size: " + str(y_size))
            	print("X screen coordinate: " + str(x))
            	print("Y screen coordinate: " + str(y))

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
    clock.tick(20)
    

    			
				
    