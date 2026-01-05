# helpful tutorial: https://www.youtube.com/watch?v=qPnKIbrVnJk

import pygame

from Stuff import FrameViewer

f = FrameViewer.GameDisplay()

class CandyBoy:
    velocity = 10
    
    def __init__(self):
        print ("I'm init of CandyBoy")
        self.down = True
        self.up = False
        self.left = False
        self.right = False
        self.facing_left = False
        self.jump = False
        self.hide = False
        self.load_frames()

        self.hero_start_image = self.hero_idle_array_right[0]
        self.candyBoy_img = pygame.transform.scale(self.hero_start_image, (145, 145))

        self.candyBoy_img_rect = self.candyBoy_img.get_rect()
        self.candyBoy_img_rect.left = f.SCREEN_WIDTH/3
        self.candyBoy_img_rect.top = 422      #1280/2 - 170
        self.current_frame = 0
        self.last_updated = 0
        self.state = 'idle'

    def load_frames(self): # load all animation images
        self.hero_run_01 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (1).png'), (150,150))
        self.hero_run_02 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (2).png'), (150,150))
        self.hero_run_03 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (3).png'), (150,150))
        self.hero_run_04 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (4).png'), (150,150))
        self.hero_run_05 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (5).png'), (150,150))
        self.hero_run_06 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (6).png'), (150,150))
        self.hero_run_07 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (7).png'), (150,150))
        self.hero_run_08 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/run/Run (8).png'), (150,150))

        self.hero_run_array_right = [self.hero_run_01, self.hero_run_02, self.hero_run_03, self.hero_run_04, self.hero_run_05, self.hero_run_06, self.hero_run_07, self.hero_run_08]

        self.hero_run_array_left = []
        for frame in self.hero_run_array_right:
            self.hero_run_array_left.append(pygame.transform.flip(frame, True, False))

        self.hero_idle_01 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (1).png'), (150,150))
        self.hero_idle_02 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (2).png'), (150,150))
        self.hero_idle_03 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (3).png'), (150,150))
        self.hero_idle_04 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (4).png'), (150,150))
        self.hero_idle_05 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (5).png'), (150,150))
        self.hero_idle_06 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (6).png'), (150,150))
        self.hero_idle_07 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (7).png'), (150,150))
        self.hero_idle_08 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (8).png'), (150,150))
        self.hero_idle_09 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (9).png'), (150,150))
        self.hero_idle_10 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/idle/Idle (10).png'), (150,150))

        self.hero_idle_array_right = [self.hero_idle_01, self.hero_idle_02, self.hero_idle_03, self.hero_idle_04, self.hero_idle_05, self.hero_idle_06, self.hero_idle_07, self.hero_idle_08, self.hero_idle_09, self.hero_idle_10]

        self.hero_idle_array_left = []
        for frame in self.hero_idle_array_right:
            self.hero_idle_array_left.append(pygame.transform.flip(frame, True, False))

        self.hero_jump_01 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (1).png'), (150,150))
        self.hero_jump_02 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (2).png'), (150,150))
        self.hero_jump_03 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (3).png'), (150,150))
        self.hero_jump_04 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (4).png'), (150,150))
        self.hero_jump_05 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (5).png'), (150,150))
        self.hero_jump_06 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (6).png'), (150,150))
        self.hero_jump_07 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (7).png'), (150,150))
        self.hero_jump_08 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (8).png'), (150,150))
        self.hero_jump_09 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (9).png'), (150,150))
        self.hero_jump_10 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (10).png'), (150,150))
        self.hero_jump_11 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (11).png'), (150,150))
        self.hero_jump_12 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/jump/Jump (12).png'), (150,150))

        self.hero_jump_array_right = [self.hero_jump_01, self.hero_jump_02, self.hero_jump_03, self.hero_jump_04, self.hero_jump_05, self.hero_jump_06, self.hero_jump_07, self.hero_jump_08, self.hero_jump_09, self.hero_jump_10, self.hero_jump_11, self.hero_jump_12]
        
        self.hero_jump_array_left = []
        for frame in self.hero_jump_array_left:
            self.hero_jump_array_left.append(pygame.transform.flip(frame, True, False))

        self.hero_crouch_01 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/hide/Slide (1).png'), (150,150))
        self.hero_crouch_02 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/hide/Slide (2).png'), (150,150))
        self.hero_crouch_03 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/hide/Slide (3).png'), (150,150))
        self.hero_crouch_04 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/hide/Slide (4).png'), (150,150))
        self.hero_crouch_05 = pygame.transform.scale(pygame.image.load('Stuff/images/hero/hide/Slide (5).png'), (150,150))

        self.hero_crouch_array_right = [self.hero_crouch_01, self.hero_crouch_02, self.hero_crouch_03, self.hero_crouch_04, self.hero_crouch_05]
        
        self.hero_crouch_array_left = []
        for frame in self.hero_crouch_array_left:
            self.hero_crouch_array_left.append(pygame.transform.flip(frame, True, False))

    def set_state(self):
        self.state = 'idle'

        if self.right:
            self.state = 'right'
        elif self.left:
            self.state = 'left'
        elif self.jump:
            self.state = 'jump'
        elif self.hide:
            self.state = 'crouch'

        # print (self.state)

    def animate(self):
        now = pygame.time.get_ticks()

        if self.state == 'idle':
            if now - self.last_updated > 100: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hero_idle_array_right)
                if self.facing_left:
                    self.candyBoy_img = self.hero_idle_array_left[self.current_frame]
                elif not self.facing_left:
                    self.candyBoy_img = self.hero_idle_array_right[self.current_frame]

        elif self.state == 'jump':
            if now - self.last_updated > 100: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hero_jump_array_right)
                if self.state == "left":
                    self.candyBoy_img = self.hero_jump_array_left[self.current_frame]
                elif self.state == "right":
                    self.candyBoy_img = self.hero_jump_array_right[self.current_frame]

        elif self.state == 'crouch':
            if now - self.last_updated > 100: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hero_crouch_array_right)
                if self.state == "left":
                    self.candyBoy_img = self.hero_crouch_array_left[self.current_frame]
                elif self.state == "right":
                    self.candyBoy_img = self.hero_crouch_array_right[self.current_frame]

        else:
            if now - self.last_updated > 100: # controls the speed at which each animation frame is cycled
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.hero_run_array_right)
                if self.state == "left":
                    self.candyBoy_img = self.hero_run_array_left[self.current_frame]
                elif self.state == "right":
                    self.candyBoy_img = self.hero_run_array_right[self.current_frame]
                
    def update(self):

        if self.up:
            self.candyBoy_img_rect.top -= 10
        if self.down and self.candyBoy_img_rect.top < 422:
            self.candyBoy_img_rect.bottom += 10

        self.set_state()
        self.animate()

    def draw(self, screen):
        screen.blit(self.candyBoy_img, self.candyBoy_img_rect)