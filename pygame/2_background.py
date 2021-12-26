import pygame

pygame.init()

# setting size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Nado Game")

# background
background = pygame.image.load("C:\\Users\\류석현\\Desktop\\Python\\pygame\\backgruond.png")

# event roop
running = True # game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if end event
            running = False # not running
    screen.blit(background, (0, 0)) # draw background

    pygame.display.update() # draw again

# end pygame
pygame.quit()