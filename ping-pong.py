from pygame import*
w = 1200
h = 800

class GameSprite(sprite.Sprite):
    def __init__(self,player_speed,player_image,w,h,x,y):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def move_WS(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > -30:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 580:
            self.rect.y += self.speed
    
    def move_arrows(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > -30:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 580:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
finish = False
window = display.set_mode((w,h))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('background.jpg'), (w,h))
clock = time.Clock()
ping = Player(5,'wall.png', 40,200,1050,100)
pong = Player(5,'wall.png', 40,200,50,100)
ball = GameSprite(10, 'ball.png', 50,50,600,400)
font.init()
font = font.Font(None,50)
game_over = font.render('GAME OVER!', True, (0,0,0))
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > h-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(ping, ball) or sprite.collide_rect(pong, ball):
            speed_x *= -1
        if ball.rect.x < 0 or ball.rect.x > 1200:
            window.blit(game_over,(500,400))
            finish = True
        ping.move_arrows()
        pong.move_WS()
        ping.reset()
        pong.reset()
        ball.reset()
        clock.tick(90)
        display.update()
        
