#Создай собственный Шутер!
from random import randint
import time
from pygame import *

juchara = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,z):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,z))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 625:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx,self.rect.top,15,20,25)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global juchara 
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(70,630)
            juchara = juchara+1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
c = ''
spriter = Player('rocket.png',110,400,7,65,65) 
monsters = sprite.Group()
for i in range(1,6):
    abc = randint(1,5)
    if abc == 1 or abc == 2:
        c = 'ufo.png'
    elif abc == 3 or abc == 4:
        c = 'asteroid.png'
    monster = Enemy(c,randint(70,630),20,randint(1,3),75,45) 
    monsters.add(monster)
bullets = sprite.Group()

window = display.set_mode((700,500))
display.set_caption('Хохохо ес.exe')
background = transform.scale(image.load("galaxy.jpg"),(700,500))
game = True
finish = False
mixer.init()
firen = mixer.Sound('fire.ogg')
mixer.music.load('space.ogg')
mixer.music.play()
font.init()
font = font.SysFont('Arial', 40)
redqwe = 0
adeboP = font.render(
    'YOU WON!', True, (200, 200, 0)
)
proigrisH = font.render(
    'YOU LOSE!', True, (0, 205, 0)
)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                spriter.fire()
                firen.play()
    if not finish:
        window.blit(background, (0,0))
        propusheno = font.render('Пропущено:'+ str(juchara),1,(255,255,0))
        window.blit(propusheno,(10,10))
        cxore = font.render('Счёт'+ str(redqwe),1,(255,255,0))
        window.blit(cxore,(10,50))
        if sprite.spritecollide(spriter, monsters, False) or juchara >= 50:
            finish = True
            window.blit(proigrisH,(280,250))
        sdawe = sprite.groupcollide(monsters, bullets, True, True)            
        for i in sdawe:
            abc = randint(1,5)
            if abc == 1 or abc == 2:
                c = 'ufo.png'
            elif abc == 3 or abc == 4:
                c = 'asteroid.png'
            redqwe += 1
            monster = Enemy(c,randint(70,630),20,randint(1,3),75,45) 
            monsters.add(monster)
        if redqwe == 15:
            finish = True
            window.blit(adeboP,(280,250))
        spriter.reset()
        spriter.update()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
    display.update()
    