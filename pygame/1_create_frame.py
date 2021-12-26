import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Nado Game")

# event roop
running = True # game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if end event
            running = False # not running

# end pygame
pygame.quit()