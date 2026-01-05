import pygame
import random
import sys
import math
pygame.init()

from Stuff import FrameViewer
from Stuff import candyBoy
from Stuff import ally
from Stuff import enemy
from Stuff import blocks
from Stuff import score
from Stuff import level_key
from Stuff import startGame

f = FrameViewer.GameDisplay()
cBoy = candyBoy.CandyBoy()  #filename.classname
score = score.Topscore()

CLOCK = pygame.time.Clock()
FPS = 24

# Create a sprite group for the blocks
block_sprites = pygame.sprite.Group()
# Create a sprite group for the allies
ally_sprite = pygame.sprite.GroupSingle()
all_ally = pygame.sprite.Group()
# Create a sprite group for the enemies
enemy_sprite = pygame.sprite.GroupSingle()
all_enemy = pygame.sprite.Group()

# Create a sprite group for level key
keySprite = pygame.sprite.GroupSingle()
all_keys = pygame.sprite.Group()

def game_loop():
    print ("In Game Loop")
    # Initialize the time for block generation
    global next_block_time
    next_block_time = 0
    global LEVEL
    LEVEL = 1

    while True:
        global screen
        screen = f.drawDisplay()
        pygame.mixer.music.load('Stuff/sound/CandyLand.mp3')
        pygame.mixer.music.play(-1, 0.0)
        global SCORE
        SCORE = 0
        global ALLY_COUNT
        ALLY_COUNT = 0
        global ENEMY_COUNT
        ENEMY_COUNT = 0
        block_count = 0
        pauseTime = 0
        global TOTAL_SCORE
        TOTAL_SCORE = 0
        
        # define background scrolling variables (helpful tutorial: https://www.youtube.com/watch?v=MM98CvhPKiI)
        scroll = 0
        bg_speed = 5
        direction = 0
        panels = math.ceil(f.SCREEN_WIDTH / f.background_width) + 2 

        while True:
            # draw the scrolling background
            for i in range(0, panels):
                screen.blit(f.shareBackground(), (i * f.background_width + scroll - f.background_width, 0))

            # Check if it is time to generate a new block
            current_time = pygame.time.get_ticks()
            if current_time > next_block_time:

                # Generate a new block at a random height and add it to the block_sprites group
                cblock = blocks.Block(1280, random.randint(200, 420))
                block_sprites.add(cblock)
                block_count += 1
                block_left = cblock.rect.left
                #associate an ally with the block if condition is met
                if (block_count % 2) == 0:
                    left = cblock.rect.right + 100
                    top = 1280/2 - 180 + 100
                    #ally
                    ally_for_this_block = ally.Ally(left,top)
                    ally_sprite.add(ally_for_this_block)
                    all_ally.add(ally_for_this_block)
                    ALLY_COUNT += 1
                    #enemy
                    ENEMY_COUNT += 1
                    enemy_for_this_block = enemy.Enemy(left,top, block_left, ENEMY_COUNT)
                    enemy_sprite.add(enemy_for_this_block)
                    all_enemy.add(enemy_for_this_block)

                if (block_count % 3) == 0:
                    left = cblock.rect.left + 100
                    top = cblock.rect.top
                    #ally
                    ally_for_this_block = ally.Ally(left,top)
                    ally_sprite.add(ally_for_this_block)
                    all_ally.add(ally_for_this_block)
                    ALLY_COUNT += 1
                    #enemy
                    ENEMY_COUNT += 1
                    enemy_for_this_block = enemy.Enemy(left,top, block_left, ENEMY_COUNT)
                    enemy_sprite.add(enemy_for_this_block)
                    all_enemy.add(enemy_for_this_block)

                next_block_time = current_time + random.randint(5000, 10000)
            
            # Update block objects
            block_sprites.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        cBoy.up = True
                        cBoy.down = False
                        cBoy.jump = True
                        cBoy.hide = False
                    elif event.key == pygame.K_DOWN:
                        cBoy.down = True
                        cBoy.up = False
                        cBoy.jump = False
                        cBoy.hide = True
                    elif event.key == pygame.K_LEFT:
                        cBoy.left = True
                        direction = 1
                        cBoy.jump = False
                        cBoy.hide = False
                    elif event.key == pygame.K_RIGHT:
                        cBoy.right = True
                        direction = -1
                        cBoy.jump = False
                        cBoy.hide = False
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        cBoy.up = False
                        cBoy.down = True
                        cBoy.jump = False
                        cBoy.hide = False
                    elif event.key == pygame.K_DOWN:
                        cBoy.down = True
                        cBoy.up = False
                        cBoy.jump = False
                        cBoy.hide = False
                    elif event.key == pygame.K_LEFT:
                        cBoy.left = False
                        direction = 0
                        cBoy.jump = False
                        cBoy.hide = False
                    elif event.key == pygame.K_RIGHT:
                        cBoy.right = False
                        direction = 0
                        cBoy.jump = False
                        cBoy.hide = False
            
            block_sprites.draw(screen)
        
            # Check for collisions between CandyMan and the blocks
            for b in block_sprites:
                b_index = block_sprites.sprites().index(b)

                # detect collision between Candy Boy and the moving blocks and make him stop on the block
                detect_collision = cBoy.candyBoy_img_rect.colliderect(b.rect)
                if detect_collision:
                    cBoy.down = False
                    #check if Candy boy has reached the right edge of the block, if so, make it fall
                    if (cBoy.candyBoy_img_rect.right - 40) > b.rect.right:
                        cBoy.down = True
                        detect_collision = False
                
            # for each ally sprite
            for a in all_ally:
                detect_collision = cBoy.candyBoy_img_rect.colliderect(a.cAlly_img_rect)
                if detect_collision:
                    all_ally.remove(a)
                    SCORE += 1
                    if SCORE > 0 and SCORE % 5 == 0:
                        #LEVEL += 1
                        #key for the level change
                        L_key = level_key.LevelKey()
                        keySprite.add(L_key)
                        all_keys.add(keySprite)
                a.allyAnimation()
                a.draw(screen)
            
            # for each enemy sprite
            for e in all_enemy:
                detect_collision = cBoy.candyBoy_img_rect.colliderect(e.cEnemy_img_rect)
                if detect_collision:
                    all_enemy.remove(e)
                    pygame.mixer.music.pause()
                    pauseTime = current_time
                    sound = pygame.mixer.Sound('Stuff/sound/Celery.mp3')
                    sound.play()
                    SCORE -= 1
                if current_time - pauseTime > 500:
                    pygame.mixer.music.unpause()
                    
                e.enemyAnimation()
                e.draw(screen)
            
            # for making the key disappear on collision to go to next level
            for k in all_keys:
                detect_collision = cBoy.candyBoy_img_rect.colliderect(k.key_img_rect)
                if detect_collision:
                    all_keys.remove(k)
                    if LEVEL != 1:
                        TOTAL_SCORE = TOTAL_SCORE + SCORE
                    SCORE = 0
                    LEVEL += 1
                # k.keyAnimation()
                # k.draw(screen)
                k.update(screen)

            if LEVEL == 1:
                TOTAL_SCORE = SCORE

            if LEVEL >= 2 and SCORE >= 5:
                screenBackground = f.shareBackground()
                startGame.stop_game(screen, screenBackground)

            # scroll background with the character
            scroll += bg_speed * direction

            # reset scrolling bg
            if abs(scroll) >= f.background_width:
                scroll = 0

            #updating scores 
            score.currentScore(SCORE,screen)
            score.allyScore(ALLY_COUNT,screen)
            score.enemyScore(ENEMY_COUNT,screen)
            score.level_count(LEVEL, screen)
            score.totalScore(TOTAL_SCORE, screen)

            cBoy.update()
            cBoy.draw(screen)

            pygame.display.update()
            CLOCK.tick(FPS)