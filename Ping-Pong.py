from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 160:
            self.rect.y += self.speed
            
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 160:
            self.rect.y += self.speed
       

racketka1 = Player ('', 30,200,4,50,150)
racketka2 = Player ('', 520,200,4,50,150)
Ping_ball = Gamesprite ('', 200,200,4,50,50)    
    
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ужас, а не Хобар')
background = Gamesprite('back.jpg', 0,0,0, win_width, win_height)

game = True
finish = False
clock = time.Clock()
FPS = 60

font1 = font.Font(None,35)
lose1 = font1.render('ПЕРВЫЙ ИГРОК ПРОИГРАЛ', True, (180,0,0))
font2 = font.Font(None,35)
lose3 = font2.render('ПЕРВЫЙ ИГРОК ПРОИГРАЛ', True, (180,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
       
    if finish != True:
        Ping_ball.rect.x += speed_x
        Ping_ball.rect.y += speed_y
        
        background.reset()
        
        racketka1.update_l()
        racketka2.update_r()
        
        racketka1.reset()
        racketka2.reset()
        Ping_ball.reset()
    
    if Ping_ball.rect.y > win_height-50
        or Ping_ball.rect.y < 0:
            speed_y *= -1
        
    if Ping_ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
        
    if Ping_ball.rect.x < 0:
        finish = True
        window.blit(lose2, (200,200))
    
    display.update()
    clock.tick(FPS)
