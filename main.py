import photo
import pygame
window = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()
background_img = pygame.image.load("photo/background.jpg")
background_img = pygame.transform.scale(background_img,[700,500])


class BaseSprite():
    def __init__(self,x,y,texture,speed,w,h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture,[w,h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
    def draw(self,window):
        window.blit(self.texture, self.hitbox)

class Hero(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x = self.hitbox.x - self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        if keys[pygame.K_w]:
            self.hitbox.y = self.hitbox.y - self.speed
class Wall():
    def __init__(self,x,y,color,w,h):
        self.hitbox = pygame.Rect(x,y,w,h)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.hitbox)





pygame.init()



cyborg_png = pygame.image.load("photo/cyborg.png")
cyborg_png = pygame.transform.scale(cyborg_png,[50,50])

hero = Hero(250, 250, "photo/hero.png", 2, 50, 50)
Walls = [

    Wall (118,0,[250,0,0],10,400),
    Wall (214,50,[250,0,0],10,450),
    Wall (308,0,[250,0,0],10,251),
    Wall (308,321,[250,0,0],10,300),
    Wall (396,0,[250,0,0],10,50),
    Wall (396,100,[250,0,0],10,300),
Wall (396,450,[250,0,0],10,50)

]



treasure_png = pygame.image.load("photo/treasure.png")
treasure_png = pygame.transform.scale(treasure_png,[50,50])
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    hero.update()

    window.fill([123,123,123])

    window.blit(background_img,[0,0])
    window.blit(cyborg_png,[0,0])
    hero.draw(window)
    for Wall in Walls:
        Wall.draw(window)
    window.blit(treasure_png,[450,370])
    pygame.display.flip()
    clock.tick(60)
