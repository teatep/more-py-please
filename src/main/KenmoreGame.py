import pygame
import os

def main():
    pygame.init()

    path = os.path.join("src/main/resources/images/", "heart.png")
    background = pygame.image.load(path)

    pygame.display.set_caption("Talia is testing out pygame")
     
    screen = pygame.display.set_mode((240,180))
    screen.blit(background, (50,50))

    pygame.display.flip()

    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     
     
if __name__=="__main__":
    main()