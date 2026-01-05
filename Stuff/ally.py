import pygame
import random

from Stuff import FrameViewer

f = FrameViewer.GameDisplay()

class Ally(pygame.sprite.Sprite):
    cAlly_velocity = 10

    def __init__(self, x, y):
        super().__init__()
        self.ally_img = pygame.image.load('Stuff/images/allies/ice-cream/idle-01.png')
        self.cAlly_img = pygame.transform.scale(self.ally_img, (100, 100))
        self.cAlly_img_rect = self.cAlly_img.get_rect()
        self.cAlly_img_rect.left = x
        self.cAlly_img_rect.top = y - 100
        self.load_ally_frames()

    # load all animation images
    def load_ally_frames(self):
        #setting the animation images -- ice-cream
        self.ally_ani_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-01.png'), (100,100))
        self.ally_ani_img24 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,100))
        self.ally_ani_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,90))
        self.ally_ani_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,80))
        self.ally_ani_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,70))
        self.ally_ani_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,60))
        self.ally_ani_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,50))
        self.ally_ani_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,60))
        self.ally_ani_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,70))
        self.ally_ani_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,80))
        self.ally_ani_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,90))
        self.ally_ani_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,100))
        self.ally_ani_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-01.png'), (100,100))
        
        self.ally_ani_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,100))), True, False)
        self.ally_ani_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,90))), True, False)
        self.ally_ani_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,80))), True, False)
        self.ally_ani_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,70))), True, False)
        self.ally_ani_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,60))), True, False)
        self.ally_ani_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,50))), True, False)
        self.ally_ani_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,60))), True, False)
        self.ally_ani_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,70))), True, False)
        self.ally_ani_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,80))), True, False)
        self.ally_ani_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,90))), True, False)
        self.ally_ani_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/ice-cream/idle-02.png'), (100,100))), True, False)
        self.ally_ani_img25 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-01.png'), (100,100))), True, False)

        self.ally_ani_img_array_01 = [self.ally_ani_img24, self.ally_ani_img3, self.ally_ani_img5, self.ally_ani_img7, self.ally_ani_img9, self.ally_ani_img11, self.ally_ani_img13, self.ally_ani_img15, self.ally_ani_img17, self.ally_ani_img19, self.ally_ani_img21, self.ally_ani_img23]        

        #setting the animation images -- lolli
        self.ally_lolli_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-01.png'), (100,100))
        self.ally_lolli_img24 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,100))
        self.ally_lolli_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,90))
        self.ally_lolli_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,80))
        self.ally_lolli_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,70))
        self.ally_lolli_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,60))
        self.ally_lolli_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,50))
        self.ally_lolli_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,60))
        self.ally_lolli_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,70))
        self.ally_lolli_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,80))
        self.ally_lolli_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,90))
        self.ally_lolli_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,100))
        self.ally_lolli_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-01.png'), (100,100))
        
        self.ally_lolli_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,100))), True, False)
        self.ally_lolli_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,90))), True, False)
        self.ally_lolli_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,80))), True, False)
        self.ally_lolli_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,70))), True, False)
        self.ally_lolli_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,60))), True, False)
        self.ally_lolli_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,50))), True, False)
        self.ally_lolli_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,60))), True, False)
        self.ally_lolli_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,70))), True, False)
        self.ally_lolli_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,80))), True, False)
        self.ally_lolli_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,90))), True, False)
        self.ally_lolli_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-02.png'), (100,100))), True, False)
        self.ally_lolli_img25 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/lolli/idle-01.png'), (100,100))), True, False)

        self.ally_lolli_img_array_01 = [self.ally_lolli_img1, self.ally_lolli_img24, self.ally_lolli_img5, self.ally_lolli_img7, self.ally_lolli_img9, self.ally_lolli_img11, self.ally_lolli_img13, self.ally_lolli_img15, self.ally_lolli_img17, self.ally_lolli_img19, self.ally_lolli_img21, self.ally_lolli_img23]        

        #setting the animation images -- chocolate
        self.ally_chocolate_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-01.png'), (100,100))
        self.ally_chocolate_img24 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,100))
        self.ally_chocolate_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,90))
        self.ally_chocolate_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,80))
        self.ally_chocolate_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,70))
        self.ally_chocolate_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,60))
        self.ally_chocolate_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,50))
        self.ally_chocolate_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,60))
        self.ally_chocolate_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,70))
        self.ally_chocolate_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,80))
        self.ally_chocolate_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,90))
        self.ally_chocolate_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,100))
        self.ally_chocolate_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-01.png'), (100,100))
       
        self.ally_chocolate_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,100))), True, False)
        self.ally_chocolate_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,90))), True, False)
        self.ally_chocolate_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,80))), True, False)
        self.ally_chocolate_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,70))), True, False)
        self.ally_chocolate_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,60))), True, False)
        self.ally_chocolate_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,50))), True, False)
        self.ally_chocolate_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,60))), True, False)
        self.ally_chocolate_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,70))), True, False)
        self.ally_chocolate_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,80))), True, False)
        self.ally_chocolate_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,90))), True, False)
        self.ally_chocolate_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-02.png'), (100,100))), True, False)
        self.ally_chocolate_img25 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/allies/chocolate/idle-01.png'), (100,100))), True, False)

        self.ally_chocolate_img_array_01 = [self.ally_chocolate_img24, self.ally_chocolate_img3, self.ally_chocolate_img5, self.ally_chocolate_img7, self.ally_chocolate_img9, self.ally_chocolate_img11, self.ally_chocolate_img13, self.ally_chocolate_img15, self.ally_chocolate_img17, self.ally_chocolate_img19, self.ally_chocolate_img21, self.ally_chocolate_img23]        

        self.ally_random = [self.ally_ani_img_array_01, self.ally_lolli_img_array_01, self.ally_chocolate_img_array_01]

        self.ally_ani_img_array = random.choice(self.ally_random)
        self.up = True
        self.down = False

        self.current_frame = 0
        self.last_updated = 0
        self.state = 'in_jar'

    def update(self, screen):
        screen.blit(self.cAlly_img, self.cAlly_img_rect)

        if self.cAlly_img_rect.top <= 360:
            self.up = False
            self.down = True
        elif self.cAlly_img_rect.top >= 460:
            self.up = True
            self.down = False

        if self.up:
            self.cAlly_img_rect.top -= self.cAlly_velocity
        elif self.down:
            self.cAlly_img_rect.top += self.cAlly_velocity
    
    #function definition for the allies' bobbing animation
    def allyAnimation(self):
        now = pygame.time.get_ticks()

        if self.state == 'in_jar':
            if now - self.last_updated > 300: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                
                self.current_frame = (self.current_frame + 1) % len(self.ally_ani_img_array)
                self.cAlly_img = self.ally_ani_img_array[self.current_frame]
        self.move()
    
    def draw(self, screen):
        screen.blit(self.cAlly_img, self.cAlly_img_rect)
    
    def move(self):
        self.cAlly_img_rect.x -= 5
