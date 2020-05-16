import pygame
from random import randint
import math
import datetime
import time
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mario Run!")

def round_up(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.ceil(n * multiplier) / multiplier

class Mario(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('mario.png'), (60, 80))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.velocity = 0

    def update(self):
        if self.rect.bottom >= 440:
            self.velocity = 0
            self.rect.bottom = 440
            if keys[pygame.K_UP]:
                self.velocity = 24
        self.velocity -= 2
        self.rect.move_ip((0, -self.velocity))

    def die(self, death):
        if death == True:
            self.velocity = 30
            self.image = pygame.transform.scale(pygame.image.load('dies.png'), (70, 70))
            self.image.set_colorkey(WHITE)
        self.velocity -= 2
        self.rect.move_ip((0, -self.velocity))

class CMario(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('cmario.png'), (80, 60))
        self.image.set_colorkey(WHITE)


        self.rect = self.image.get_rect()

        self.velocity = 0

        
class Shell(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        rand = randint(0, 2)
        if rand == 0:
            self.image = pygame.transform.scale(pygame.image.load('shell.png'), (60, 45))
        elif rand == 1:
            self.image = pygame.transform.scale(pygame.image.load('bshell.png'), (60, 45))
        elif rand == 2:
            self.image = pygame.transform.scale(pygame.image.load('rshell.png'), (60, 45))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.velocity = 0
        
    def update(self):
        self.rect.move_ip((-self.velocity, 0))
        if self.rect.right <= 0:
            self.kill()


class DShell(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        rand = randint(0, 1)
        if rand == 0:
            self.image = pygame.transform.scale(pygame.image.load('goomba.png'), (70, 70))
        if rand == 1:
            self.image = pygame.transform.scale(pygame.image.load('koopa.png'), (60, 80))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.velocity = 0
        
    def update(self):
        self.rect.move_ip((-self.velocity, 0))
        if self.rect.right <= 0:
            self.kill()

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        rand = randint(0, 1)
        if rand == 0:
            self.image = pygame.transform.scale(pygame.image.load('arrow.png'), (60, 15))
        elif rand == 1:
            self.image = pygame.transform.scale(pygame.image.load('bullet.png'), (60, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.velocity = 0
        
    def update(self):
        self.rect.move_ip((-self.velocity, 0))
        if self.rect.right <= 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        rand = randint(0, 2)
        if rand == 0:
            self.image = pygame.transform.scale(pygame.image.load('cloud.png'), (100, 70))
        elif rand == 1:
            self.image = pygame.transform.scale(pygame.image.load('dcloud.png'), (170, 70))
        elif rand == 2:
            self.image = pygame.transform.scale(pygame.image.load('tcloud.png'), (260, 70))
        self.image.set_colorkey(WHITE) 
        self.rect = self.image.get_rect()
        self.velocity = 0
        

    def update(self):
        self.rect.move_ip((-self.velocity, 0))
        if self.rect.right <= 0:
            self.kill()
        
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(loops= -1)
BG = pygame.transform.scale(pygame.image.load('download.png'), (800, 500))
BG.set_colorkey(WHITE)
BGrect = BG.get_rect()
BGrect.x = 0
BGrect.y = 0
mario = Mario()
mario.rect.x = 90
mario.rect.y = 360
CREATEOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(CREATEOBSTACLE, 3500)
CREATECLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(CREATECLOUD, 3000)
all_sprites = pygame.sprite.Group()
all_clouds = pygame.sprite.Group()
cmario = CMario()
cmario.rect.x = 90
cmario.rect.y = 380
clock = pygame.time.Clock()
carryOn = True
velocity = 15
font = pygame.font.Font('mariofont.ttf', 30)
now = datetime.datetime.now()
stand = True
crouch = False
while carryOn:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                carryOn=False
        if event.type == CREATEOBSTACLE:
            ram = randint(0, 7)
            if ram < 3:
                new_cactus = Shell()
                new_cactus.velocity = round_up(velocity, 1)
                new_cactus.rect.left = 700
                new_cactus.rect.bottom = 440
                all_sprites.add(new_cactus)
            elif ram > 2 and ram < 6:
                new_cactus = DShell()
                new_cactus.velocity = round_up(velocity, 1)
                new_cactus.rect.left = 700
                new_cactus.rect.bottom = 440
                all_sprites.add(new_cactus)
            elif ram > 5:
                ramd = randint(0, 3)
                new_cactus = Projectile()
                new_cactus.velocity = round_up(velocity, 1)
                new_cactus.rect.left = 700
                new_cactus.rect.bottom = 370
                all_sprites.add(new_cactus)
            rand = randint(700, 2000)
            pygame.time.set_timer(CREATEOBSTACLE, rand)
        if event.type == CREATECLOUD:
            veloc = randint(1, 3)
            ycor = randint(0, 150)
            new_cloud = Cloud()
            new_cloud.velocity = veloc
            new_cloud.rect.x = 700
            new_cloud.rect.y = ycor
            all_clouds.add(new_cloud)
            rund = randint(2500, 3500)
            pygame.time.set_timer(CREATECLOUD, rund)
    screen.fill(WHITE)
    screen.blit(BG, BGrect)
    if not keys[pygame.K_DOWN] or mario.rect.bottom < 440:
        mario.update()
        screen.blit(mario.image, mario.rect)
        stand = True
        crouch  =False
    elif keys[pygame.K_DOWN] and mario.rect.bottom >= 440:
        screen.blit(cmario.image, cmario.rect)
        stand = False
        crouch = True
    if stand == True and mario.rect.bottom < 440:
        mario.image = pygame.transform.scale(pygame.image.load('jmario.png'), (70, 80))
        mario.rect.x = 80
    elif stand == True and mario.rect.bottom >= 440:
        mario.image = pygame.transform.scale(pygame.image.load('mario.png'), (60, 80))
        mario.rect.x = 90
    for sprite in all_sprites:
        sprite.update()
        screen.blit(sprite.image, sprite.rect)
    newnow = datetime.datetime.now()
    diff = newnow-now
    if diff.seconds >= 4:
        text = font.render(str(diff.seconds - 4) + str(diff.microseconds)[0], True, BLACK)
    else:
        text = font.render('00', True, BLACK)
    score = str(diff.seconds - 4) + str(diff.microseconds)[0]
    textRect = text.get_rect()
    textRect.x = 0
    textRect.y = 0
    screen.blit(text, textRect)
    for sprite in all_clouds:
        sprite.update()
        screen.blit(sprite.image, sprite.rect)
    if pygame.sprite.spritecollideany(mario, all_sprites) and stand == True:
        carryOn = False
    elif pygame.sprite.spritecollideany(cmario, all_sprites) and crouch == True:
        carryOn = False
    pygame.display.update()
    velocity += 0.003
    clock.tick(30)
pygame.mixer.music.stop()
pygame.mixer.music.load('dies.wav')
pygame.mixer.music.play()
death = 1
click = pygame.time.Clock()
while True:
    screen.blit(BG, BGrect)
    screen.blit(text, textRect)
    if death == 1:
        mario.die(True)
    else:
        mario.die(False)
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
    for sprite in all_clouds:
        screen.blit(sprite.image, sprite.rect)   
    screen.blit(mario.image, mario.rect)
    pygame.display.update()
    death += 1
    if mario.rect.top >= 500:
        break
    click.tick(30)
time.sleep(1.7)
now = datetime.datetime.now()
while True:
    screen.fill(BLACK)
    gmov = font.render("GAME OVER", True, WHITE)
    gmovrect = gmov.get_rect()
    gmovrect.x = 210
    gmovrect.y = 230
    scor = font.render("SCORE:" + score, True, WHITE)
    scorect = scor.get_rect()
    scorect.x = 210
    scorect.y = 180
    newnow = datetime.datetime.now()
    screen.blit(gmov, gmovrect)
    screen.blit(scor, scorect)
    if (newnow - now).seconds >= 4:
        break
    pygame.display.update()
pygame.mixer.music.stop()
time.sleep(0.5)
pygame.quit()
