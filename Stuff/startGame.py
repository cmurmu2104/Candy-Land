import pygame
import sys
pygame.init()

from Stuff import FrameViewer
from Stuff import candyGameLoop

f = FrameViewer.GameDisplay()
c_GL = candyGameLoop

color = pygame.Color(0,0,0)

def start_game(screen, screenBackground):
    start_img = pygame.image.load('Stuff/images/background/PressAnyKeyToStart.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (1280/2, 720/2)
    screen.blit(start_img, start_img_rect)

    # while loop to keep the window available until quit
    while True:
        # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                c_GL.game_loop()

        pygame.display.update()

def stop_game(screen, screenBackground):
    stop_img = pygame.image.load('Stuff/images/background/YouWin.png')
    stop_img_rect = stop_img.get_rect()
    stop_img_rect.center = (1280/2, 720/2)
    screen.blit(stop_img, stop_img_rect)

    # while loop to keep the window available until quit
    while True:
        # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()