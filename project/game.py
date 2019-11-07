import os
import pygame

def main():
    pygame.init()
    fenetre = pygame.display.set_mode((800,800))
    perso = pygame.image.load("perso.png").convert()
    fenetre.blit(perso, (200,300))

    while 1:
        events = pygame.event.get()
        for e in events:
            pass

if __name__ == '__main__':
    main()
