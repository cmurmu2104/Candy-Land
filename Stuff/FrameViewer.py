import pygame

class GameDisplay:

    def __init__(self):
        # Define Screen Size
        global SCREEN_SIZE
        SCREEN_SIZE = self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1280, 720

        # load background image
        global background
        background = pygame.image.load('Stuff/images/background/background_long.png')
        self.background_width = background.get_width()
        self.background_rect = background.get_rect()
        background = pygame.transform.scale(background, (self.background_width, self.SCREEN_HEIGHT))


    # Function for creating display
    def drawDisplay(self):
        global screen
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('CandyLand')
        screen.blit(background, (0,0))
        return screen

    def shareBackground(self):
        return background

    def defineFont(self):
        # Set the font for the scores
        font = pygame.font.SysFont('comicsans', 32, bold=False)
        return font