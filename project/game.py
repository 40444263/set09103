import os
import pygame
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def main():
    pygame.init()
    pygame.display.set_mode((1,1))

    while 1:
        events = pygame.event.get()
        for e in events:
            pass

if __name__ == '__main__':
    main()
