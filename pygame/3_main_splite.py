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

# character
character = pygame.image.load("C:\\Users\\류석현\\Desktop\\Python\\pygame\\character.png")
character_size = character.get_rect().size # image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2
character_y_pos = screen_height - character_height


# event roop
running = True # game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if end event
            running = False # not running
    screen.blit(background, (0, 0)) # draw background

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # draw again

# end pygame
pygame.quit()