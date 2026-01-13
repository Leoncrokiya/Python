import pygame
pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("My Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

shotsound = pygame.mixer.Sound("hit.mp3")
hitsound = pygame.mixer.Sound("hit.mp3")
music = pygame.mixer.music.load("music.mp3")

pygame.mixer.music.play(-1)

score = 0

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))  
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5", 1, (0, 0, 255))

        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()

        i = 0

        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 100
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 0, 255), (self.hitbox[0], self.hitbox[1] - 20, 50 - (1 * (100 - self.health)), 10))

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
                
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                # self.x += self.vel
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
                self.walkCount = 0
                # self.x += self.vel

    def hit(self):
        if self.health > 0:
            self.health -= 10
        else:
            self.visible = False
        print("hit")
        
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render("Score:" + str(score), 1, (0, 0, 255))
    win.blit(text, (350, 10))
    guy.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
        
    pygame.display.update()

font = pygame.font.SysFont("comicsans", 30, True)
guy = player(200, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shots = 0
bullets = []
run = True
while run:
    clock.tick(27)
    
    if goblin.visible == True:
        if guy.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and guy.hitbox[1] + guy.hitbox[3] > goblin.hitbox[1]:
            if guy.hitbox[0] + goblin.hitbox[2] > goblin.hitbox[0] and guy.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                guy.hit()
                # shotsound.play()
                # hitsound.play()
                score -= 5
                # bullets.pop(bullets.index(bullets))

    if shots > 0:
        shots += 1

    if shots > 3:
        shots = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitsound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and shots == 0:
        shotsound.play()
        if guy.left:
            facing = -1
            
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(guy.x + guy.width // 2), round(guy.y + guy.height // 2), 6, (0, 255, 255), facing))
        
        shots = 1

    
    if keys[pygame.K_LEFT] and guy.x > guy.vel:
        guy.x -= guy.vel
        guy.left = True
        guy.right = False
        guy.standing = False

    elif keys[pygame.K_RIGHT] and guy.x < 500 - guy.width - guy.vel:
        guy.x += guy.vel
        guy.right = True
        guy.left = False
        guy.standing = False
        
    else:
        guy.standing = True
        guy.walkCount = 0
        
    if not (guy.isJump):
        if keys[pygame.K_UP]:
            guy.isJump = True
            guy.right = False
            guy.left = False
            guy.walkCount = 0
            
    else:
        if guy.jumpCount >= -10:
            neg = 1
            if guy.jumpCount < 0:
                neg = -1
            guy.y -= (guy.jumpCount ** 2) * 0.5 * neg
            guy.jumpCount -= 1
            
        else:
            guy.isJump = False
            guy.jumpCount = 10
        
    redrawGameWindow()
            
pygame.quit()