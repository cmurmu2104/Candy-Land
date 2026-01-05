import pygame
import random

from Stuff import FrameViewer

f = FrameViewer.GameDisplay()

class Enemy(pygame.sprite.Sprite):
    cEnemy_velocity = 10

    def __init__(self, x, y, block_left, count):
        super().__init__()
        self.enemy_img = pygame.image.load('Stuff/images/enemies/celery/jump-01.png')
        self.cEnemy_img = pygame.transform.scale(self.enemy_img, (100, 100))
        self.cEnemy_img_rect = self.cEnemy_img.get_rect()
        # self.cEnemy_img_rect.left = 840
        # self.cEnemy_img_rect.top = 1280/2 - 180
        self.cEnemy_img_rect.left = x - 100
        self.cEnemy_img_rect.top = y - 100
        self.eOnBlock = block_left
        self.eCount = count
        self.load_enemy_frames()
        # self.up = True
        # self.down = False
    
    # load all animation images
    def load_enemy_frames(self):
        #setting the animation images -- celery
        self.enemy_ani_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))
        self.enemy_ani_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-02.png'), (100,100))
        self.enemy_ani_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-03.png'), (100,100))
        self.enemy_ani_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-04.png'), (100,100))
        self.enemy_ani_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-05.png'), (100,100))
        self.enemy_ani_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))
        self.enemy_ani_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-02.png'), (100,100))
        self.enemy_ani_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-03.png'), (100,100))
        self.enemy_ani_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-04.png'), (100,100))
        self.enemy_ani_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-05.png'), (100,100))
        self.enemy_ani_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))
        self.enemy_ani_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))
        
        self.enemy_ani_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))), True, False)
        self.enemy_ani_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,90))), True, False)
        self.enemy_ani_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,80))), True, False)
        self.enemy_ani_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,70))), True, False)
        self.enemy_ani_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,60))), True, False)
        self.enemy_ani_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,50))), True, False)
        self.enemy_ani_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,60))), True, False)
        self.enemy_ani_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,70))), True, False)
        self.enemy_ani_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,80))), True, False)
        self.enemy_ani_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,90))), True, False)
        self.enemy_ani_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))), True, False)
        self.enemy_ani_img24 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/celery/jump-01.png'), (100,100))), True, False)
        
        self.enemy_ani_img_array_01 = [self.enemy_ani_img1, self.enemy_ani_img2, self.enemy_ani_img3, self.enemy_ani_img4, self.enemy_ani_img5, self.enemy_ani_img6, self.enemy_ani_img7, self.enemy_ani_img8, self.enemy_ani_img9, self.enemy_ani_img10, self.enemy_ani_img11]  

        #setting the animation images -- pumpkin
        self.enemy_gourd_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))
        self.enemy_gourd_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-02.png'), (100,100))
        self.enemy_gourd_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-03.png'), (100,100))
        self.enemy_gourd_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-04.png'), (100,100))
        self.enemy_gourd_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-05.png'), (100,100))
        self.enemy_gourd_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))
        self.enemy_gourd_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-02.png'), (100,100))
        self.enemy_gourd_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-03.png'), (100,100))
        self.enemy_gourd_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-04.png'), (100,100))
        self.enemy_gourd_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-05.png'), (100,100))
        self.enemy_gourd_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))
        self.enemy_gourd_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))
       
        self.enemy_gourd_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))), True, False)
        self.enemy_gourd_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,90))), True, False)
        self.enemy_gourd_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,80))), True, False)
        self.enemy_gourd_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,70))), True, False)
        self.enemy_gourd_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,60))), True, False)
        self.enemy_gourd_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,50))), True, False)
        self.enemy_gourd_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,60))), True, False)
        self.enemy_gourd_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,70))), True, False)
        self.enemy_gourd_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,80))), True, False)
        self.enemy_gourd_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,90))), True, False)
        self.enemy_gourd_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))), True, False)
        self.enemy_gourd_img24 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/gourd/jump-01.png'), (100,100))), True, False)
        
        self.enemy_gourd_img_array_01 = [self.enemy_gourd_img1, self.enemy_gourd_img2, self.enemy_gourd_img3, self.enemy_gourd_img4, self.enemy_gourd_img5, self.enemy_gourd_img6, self.enemy_gourd_img7, self.enemy_gourd_img8, self.enemy_gourd_img9, self.enemy_gourd_img10, self.enemy_gourd_img11]  
        
        #setting the animation images -- pumpkin
        self.enemy_pumpkin_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))
        self.enemy_pumpkin_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-02.png'), (100,100))
        self.enemy_pumpkin_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-03.png'), (100,100))
        self.enemy_pumpkin_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-04.png'), (100,100))
        self.enemy_pumpkin_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-05.png'), (100,100))
        self.enemy_pumpkin_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))
        self.enemy_pumpkin_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-02.png'), (100,100))
        self.enemy_pumpkin_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-03.png'), (100,100))
        self.enemy_pumpkin_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-04.png'), (100,100))
        self.enemy_pumpkin_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-05.png'), (100,100))
        self.enemy_pumpkin_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))
        self.enemy_pumpkin_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))
       
        self.enemy_pumpkin_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))), True, False)
        self.enemy_pumpkin_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,90))), True, False)
        self.enemy_pumpkin_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,80))), True, False)
        self.enemy_pumpkin_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,70))), True, False)
        self.enemy_pumpkin_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,60))), True, False)
        self.enemy_pumpkin_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,50))), True, False)
        self.enemy_pumpkin_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,60))), True, False)
        self.enemy_pumpkin_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,70))), True, False)
        self.enemy_pumpkin_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,80))), True, False)
        self.enemy_pumpkin_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,90))), True, False)
        self.enemy_pumpkin_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))), True, False)
        self.enemy_pumpkin_img24 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/pumpkin/roll-01.png'), (100,100))), True, False)
        
        self.enemy_pumpkin_img_array_01 = [self.enemy_pumpkin_img1, self.enemy_pumpkin_img2, self.enemy_pumpkin_img3, self.enemy_pumpkin_img4, self.enemy_pumpkin_img5, self.enemy_pumpkin_img6, self.enemy_pumpkin_img7, self.enemy_pumpkin_img8, self.enemy_pumpkin_img9, self.enemy_pumpkin_img10, self.enemy_pumpkin_img11]  

        #setting the animation images -- tomato
        self.enemy_tomato_img1 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))
        self.enemy_tomato_img2 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-02.png'), (100,100))
        self.enemy_tomato_img3 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-03.png'), (100,100))
        self.enemy_tomato_img4 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-04.png'), (100,100))
        self.enemy_tomato_img5 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-05.png'), (100,100))
        self.enemy_tomato_img6 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))
        self.enemy_tomato_img7 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-02.png'), (100,100))
        self.enemy_tomato_img8 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-03.png'), (100,100))
        self.enemy_tomato_img9 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-04.png'), (100,100))
        self.enemy_tomato_img10 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-05.png'), (100,100))
        self.enemy_tomato_img11 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))
        self.enemy_tomato_img12 = pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))
       
        self.enemy_tomato_img13 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))), True, False)
        self.enemy_tomato_img14 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,90))), True, False)
        self.enemy_tomato_img15 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,80))), True, False)
        self.enemy_tomato_img16 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,70))), True, False)
        self.enemy_tomato_img17 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,60))), True, False)
        self.enemy_tomato_img18 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,50))), True, False)
        self.enemy_tomato_img19 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,60))), True, False)
        self.enemy_tomato_img20 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,70))), True, False)
        self.enemy_tomato_img21 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,80))), True, False)
        self.enemy_tomato_img22 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,90))), True, False)
        self.enemy_tomato_img23 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))), True, False)
        self.enemy_tomato_img24 = pygame.transform.flip((pygame.transform.scale(pygame.image.load('Stuff/images/enemies/tomato/roll-01.png'), (100,100))), True, False)
        
        self.enemy_tomato_img_array_01 = [self.enemy_tomato_img1, self.enemy_tomato_img2, self.enemy_tomato_img3, self.enemy_tomato_img4, self.enemy_tomato_img5, self.enemy_tomato_img6, self.enemy_tomato_img7, self.enemy_tomato_img8, self.enemy_tomato_img9, self.enemy_tomato_img10, self.enemy_tomato_img11]  
         
        self.enemy_random = [self.enemy_ani_img_array_01, self.enemy_gourd_img_array_01, self.enemy_pumpkin_img_array_01, self.enemy_tomato_img_array_01]

        self.enemy_ani_img_array = random.choice(self.enemy_random)
        self.up = True
        self.down = False

        self.current_frame = 0
        self.last_updated = 0
        self.state = 'jump'


    def update(self,screen):
        screen.blit(self.cEnemy_img, self.cEnemy_img_rect)

        if self.cEnemy_img_rect.top <= 360:
            self.up = False
            self.down = True
        elif self.cEnemy_img_rect.top >= 460:
            self.up = True
            self.down = False

        if self.up:
            self.cEnemy_img_rect.top -= self.cEnemy_velocity
        elif self.down:
            self.cEnemy_img_rect.top += self.cEnemy_velocity
    
    #function definition for the enemy' jumping animation
    def enemyAnimation(self):
        now = pygame.time.get_ticks()

        if self.state == 'jump':
            if now - self.last_updated > 300: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.enemy_ani_img_array)
                self.cEnemy_img = self.enemy_ani_img_array[self.current_frame]
        self.move()
    
    def draw(self, screen):
        screen.blit(self.cEnemy_img, self.cEnemy_img_rect)
    
    def move(self):
        self.cEnemy_img_rect.x -= 6
        if self.cEnemy_img_rect.left < self.eOnBlock and self.cEnemy_img_rect.left < 800:
            self.down = True
            self.cEnemy_img_rect.top += self.cEnemy_velocity
        if self.cEnemy_img_rect.top >= 460:
            self.down = False
            self.cEnemy_img_rect.top = 1280/2 - 180