import pygame

from Stuff import FrameViewer

f = FrameViewer.GameDisplay()
font = f.defineFont()

COLOR = (255, 255, 255)
WHITE = (100,24,98)

class Topscore:
    def __init__(self):
        self.high_score = 0
    # def top_score(self, score):
    #     if score > self.high_score:
    #         self.high_score = score
    #     return self.high_score
    
    def currentScore(self, score, screen):
        score_font = font.render('Treasure Points:'+str(score), True, COLOR)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (200, 720 - (720/9))
        score_font_surface = pygame.Surface((score_font_rect.width + 10, score_font_rect.height + 10))
        score_font_surface.fill(WHITE)
        score_font_surface.blit(score_font,(0,0))
        screen.blit(score_font_surface, (200 - score_font_rect.width / 2, 640 - score_font_rect.height / 2))
        screen.blit(score_font, score_font_rect)
    
    def allyScore(self, score, screen):
        score_font = font.render('Ally Appeared:'+str(score), True, COLOR)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (600, 720 - (720/9))
        score_font_surface = pygame.Surface((score_font_rect.width + 10, score_font_rect.height + 10))
        score_font_surface.fill(WHITE)
        score_font_surface.blit(score_font,(0,0))
        screen.blit(score_font_surface, (600 - score_font_rect.width / 2, 640 - score_font_rect.height / 2))
        screen.blit(score_font, score_font_rect)
    
    def enemyScore(self, score, screen):
        score_font = font.render('Enemy Appeared:'+str(score), True, COLOR)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (1000, 720 - (720/9))
        score_font_surface = pygame.Surface((score_font_rect.width + 10, score_font_rect.height + 10))
        score_font_surface.fill(WHITE)
        score_font_surface.blit(score_font,(0,0))
        screen.blit(score_font_surface, (1000 - score_font_rect.width / 2, 640 - score_font_rect.height / 2))
        screen.blit(score_font, score_font_rect)
    
    def level_count(self, level, screen):
        level_font = font.render('Level:'+str(level), True, COLOR)
        level_font_rect = level_font.get_rect()
        level_font_rect.center = (200, 50)
        level_font_surface = pygame.Surface((level_font_rect.width + 10, level_font_rect.height + 10))
        level_font_surface.fill(WHITE)
        level_font_surface.blit(level_font,(0,0))
        screen.blit(level_font_surface, (200 - level_font_rect.width / 2, 50 - level_font_rect.height / 2))
        screen.blit(level_font, level_font_rect)
    
    def totalScore(self, score, screen):
        score_font = font.render('Total Score:'+str(score), True, COLOR)
        score_font_rect = score_font.get_rect()
        score_font_rect.center = (600, 50)
        score_font_surface = pygame.Surface((score_font_rect.width + 10, score_font_rect.height + 10))
        score_font_surface.fill(WHITE)
        score_font_surface.blit(score_font,(0,0))
        screen.blit(score_font_surface, (600 - score_font_rect.width / 2, 50 - score_font_rect.height / 2))
        screen.blit(score_font, score_font_rect)