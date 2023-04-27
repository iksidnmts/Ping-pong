from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 640:
            self.rect.x += self.speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 640:
            self.rect.x += self.speed

mw_width = 700
mw_height = 500
mw = display.set_mode((mw_width, mw_height))
display.set_caption('Ping-pong')

backgr_color = (171, 205, 239) 
mw.fill(backgr_color)

ball = Player('ball.jpg', 400, 200, 6, 50, 50)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.reset()

    display.update()
    clock.tick(FPS)