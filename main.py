import pygame
import time
import random

width, height = 1000, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame game")

BG = pygame.transform.scale(pygame.image.load("clouds_for_pygame.jpeg"), (width, height))

player_width = 40
player_height = 60

player_vel = 5

def draw(player):
    win.blit(BG, (0, 0))

    pygame.draw.rect(win, "pink", player)

    pygame.display.update()

# function that keeps the window alive
def main():
    run = True

    player = pygame.Rect(200, height - player_height, player_width, player_height)

    clock = pygame.time.Clock()

    while run: # while run is equal to true it will check for the events in the loop
        clock.tick(60) # delays the while loop so it only runs a max of 60 times per second
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:
            player.x -= player_vel 
        if keys[pygame.K_RIGHT] and player.x + player_vel + player_width <= WIDTH:
            player.x += player_vel

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()

