import pygame
import random

from Stuff import FrameViewer

f = FrameViewer.GameDisplay()

class LevelKey(pygame.sprite.Sprite):
    key_velocity = 10

    def __init__(self):
        super().__init__()
        self.key_img = pygame.image.load('Stuff/images/key.png')
        self.key_img = pygame.transform.scale(self.key_img, (100, 100))
        self.key_img_rect = self.key_img.get_rect()
        self.key_img_rect.left = 840
        self.key_img_rect.top = 1280/2 - 180
        #self.load_key_frames()
        self.up = True
        self.down = False
    
    # load all animation images
    def load_key_frames(self):
        #setting the animation images -- key
        self.key_ani_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))
        self.key_ani_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (50,100))
        self.key_ani_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (0,100))
        self.key_ani_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (50,100))
        self.key_ani_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))
        self.key_ani_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (50,100))
        self.key_ani_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (0,100))
        self.key_ani_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (50,100))
        self.key_ani_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))
        self.key_ani_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))
        self.key_ani_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))
        self.key_ani_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/key.png'), (100,100))

        self.key_ani_img_array = [self.key_ani_img1, self.key_ani_img2, self.key_ani_img3, self.key_ani_img4, self.key_ani_img5, self.key_ani_img6, self.key_ani_img7, self.key_ani_img8, self.key_ani_img9]
        
        self.current_frame = 0
        self.last_updated = 0
        self.state = 'rotate'
    
    #function definition for the key' rotation animation
    def keyAnimation(self):
        now = pygame.time.get_ticks()

        if self.state == 'rotate':
            if now - self.last_updated > 300: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.key_ani_img_array)
                self.key_img = self.key_ani_img_array[self.current_frame]
    
    def draw(self, screen):
        screen.blit(self.key_img, self.key_img_rect)
    
    def update(self,screen):
        screen.blit(self.key_img, self.key_img_rect)

        if self.key_img_rect.top <= 360:
            self.up = False
            self.down = True
        elif self.key_img_rect.top >= 460:
            self.up = True
            self.down = False

        if self.up:
            self.key_img_rect.top -= self.key_velocity
        elif self.down:
            self.key_img_rect.top += self.key_velocity
        
        self.move()
    
    def move(self):
        self.key_img_rect.x -= 5