import pygame

pygame.init()

# Screen
width = 1200
height = 800
current_screen = "MENU"
ground_y = height - 100
scroll_speed = 10
previous_screen = ""

# Animation
rect_x = 0
transition = False
transition_speed = 40

# Frame Per Second
fps = 60
clock = pygame.time.Clock()

# Color
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

# Font
Sysfont = pygame.font.SysFont(None,30)
Play_font = pygame.font.SysFont(None,70)
logo_font = pygame.font.SysFont(None,100)

# Menu

# PLay
lvl_select = "1"

# OOP

class Block:
    def __init__(self,x,y):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.color = blue
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.speed = scroll_speed

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x <= -self.width:
            self.x = width
            self.rect.x = self.x
            

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,5)

blocks = [
    Block(width,ground_y - 100),
    Block(width + 50,ground_y - 100),
    Block(width + 100 , ground_y - 100)
]

class Spike:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = width - 100
        self.y = ground_y - self.height
        self.color = red
        self.speed = scroll_speed
        self.rect_width = 10
        self.rect_height = 30
        self.hitbox_x = self.x + 20
        self.hitbox_y = self.y + 10
        self.rect = pygame.Rect(self.hitbox_x,self.hitbox_y,
                                self.rect_width,self.rect_height)

    def update(self):
        self.x -= self.speed
        self.hitbox_x = self.x + 20
        self.rect.x = self.hitbox_x
        if self.x <= -self.width:
            self.x = width + 300
            self.hitbox_x = self.x + 20
            self.rect.x = self.hitbox_x 

    def draw(self,screen):
        pygame.draw.polygon(screen,
                            self.color,
                            [(self.x + self.width // 2 , self.y ),
                             (self.x, self.y + self.height),
                             (self.x + self.width , self.y + self.height),
                             ]
        )
    def reset(self):
        self.x = width - 100
        self.hitbox_x = self.x + 20
        self.rect.x = self.hitbox_x

spike = Spike()

class Cube:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = width // 2 - 200
        self.y = ground_y - self.height        
        self.vx = 0
        self.vy = 0
        self.gravity = 1
        self.jump_force = -20
        self.is_ground = True
        self.rect = pygame.Rect(self.x , self.y , self.width , self.height)
        self.color = green
        self.old_x = self.x
        self.old_y = self.y
        self.is_dead = False

    def jump(self):
        if self.is_ground == True:
            self.vy = self.jump_force
            self.is_ground = False
            
    def update(self,ground_y,blocks,spike):
        self.old_x = self.x
        self.old_y = self.y
        self.vy += self.gravity
        self.y += self.vy
        self.rect.y = self.y        
        if self.y >= ground_y - self.height:
            self.y = ground_y - self.height
            self.vy = 0
            self.is_ground = True
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if (self.old_y + self.height) <= block.rect.top:
                    self.y = block.rect.top - self.height
                    self.vy = 0
                    self.is_ground = True
                    self.rect.y = self.y
                    break
                else:
                    self.is_dead = True

            elif self.rect.colliderect(spike.rect):
                self.is_dead = True

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

    def reset(self):
        self.vx = 0
        self.vy = 0
        self.y = ground_y - self.height
        self.is_ground = True
        self.is_dead = False

cube = Cube()

class Ship:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = width // 2 - 200
        self.y = height // 2       
        self.vx = 0
        self.vy = 0
        self.gravity = 1
        self.fly_force = -1.5
        self.rect = pygame.Rect(self.x , self.y , self.width , self.height)
        self.color = green
        self.old_x = self.x
        self.old_y = self.y
        self.is_dead = False

    def fly(self):
        self.vy += self.fly_force
        if self.vy < -8:
            self.vy = -8

    def update(self):
        self.old_y = self.y
        self.vy += self.gravity
        if self.vy > 8:
            self.vy = 8
        self.y += self.vy
        self.rect.y = self.y

        for block in blocks:
            if self.rect.colliderect(block.rect):
                if (self.old_y + self.height) <= block.rect.top:
                    self.y = block.rect.top - self.height
                    self.vy = 0
                elif self.old_y >= block.rect.bottom:
                    self.y = block.rect.bottom + 10
                    self.vy = 0
                else:
                    self.is_dead = True

            elif self.rect.colliderect(spike.rect):
                self.is_dead = True

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

    def reset(self):
        self.vx = 0
        self.vy = 0
        self.y = height // 2
        self.old_y = self.y
        self.is_dead = False

ship = Ship()
        
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Geometry Dash")

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    cube.jump()
            if event.key == pygame.K_SPACE:
                if current_screen == "DEAD":
                    cube.reset()
                    spike.reset()
                    ship.reset()
                    blocks = [
                                Block(width,ground_y - 50),
                                Block(width + 50,ground_y - 50),
                                Block(width + 100 , ground_y - 50)
                            ]
                    current_screen = previous_screen

        if event.type == pygame.MOUSEBUTTONDOWN:

            if play_rect.collidepoint(event.pos):
                current_screen = "PLAY"

            elif level_1_rect.collidepoint(event.pos):
                current_screen = "LEVEL1"

            elif level_2_rect.collidepoint(event.pos):
                current_screen = "LEVEL2"

            elif back_rect.collidepoint(event.pos):
                current_screen = "MENU"
                rect_x = 0

            elif next_lvl_rect.collidepoint(event.pos):
                transition = True

    if current_screen == "MENU":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        play_text = Play_font.render("PLAY" , True , white)
        play_rect = play_text.get_rect(center = (width / 2 , height / 2))
        screen.blit(play_text,play_rect)

        logo_text = logo_font.render("GEOMETRY DASH" , True , white)
        logo_rect = logo_text.get_rect(center= (width / 2 , height / 2 - 200))
        screen.blit(logo_text,logo_rect)

    elif current_screen == "PLAY":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        back_text = Sysfont.render("Back to Menu" , True , white)
        back_rect = back_text.get_rect(center = (width / 2 , height - 100))
        screen.blit(back_text,back_rect)

        level_1 = Play_font.render("LEVEL 1" , True , white)
        level_1_rect = level_1.get_rect(center = (width//2 + rect_x , height//2))
        screen.blit(level_1,level_1_rect)

        level_2 = Play_font.render("LEVEL 2" , True , white)
        level_2_rect = level_2.get_rect(center = (width//2 + width + rect_x , height//2))
        screen.blit(level_2,level_2_rect)

        next_lvl = Sysfont.render("next lvl ==>" , True , white)
        next_lvl_rect = next_lvl.get_rect(bottomleft = (width - 150 , height//2))
        screen.blit(next_lvl,next_lvl_rect)

        if transition:
            rect_x -= transition_speed
            if rect_x <= -width:
                transition = False

    elif current_screen == "DEAD":

        dead_text = logo_font.render("GAME OVER" , True , red)
        dead_rect = dead_text.get_rect(center = (width / 2 , height / 2))
        screen.blit(dead_text,dead_rect)

        restart = Sysfont.render("Press SPACE to restart" , True , white)
        restart_rect = restart.get_rect(center = (width / 2 , height / 2 + 50))
        screen.blit(restart,restart_rect)

    elif current_screen == "LEVEL1":
        screen.fill(black)

        previous_screen = "LEVEL1"

        for block in blocks:
            block.update()

        spike.update()
        spike.draw(screen)

        cube.update(ground_y,blocks,spike)
        cube.draw(screen)

        for block in blocks:
            block.draw(screen)

        if cube.is_dead:
            current_screen = "DEAD"
      
    elif current_screen == "LEVEL2":
        screen.fill(black)

        previous_screen = "LEVEL2"

        for block in blocks:
            block.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ship.fly()
        ship.update()
        ship.draw(screen)

        spike.update()
        spike.draw(screen)

        for block in blocks:
            block.draw(screen)

        if ship.is_dead:
            current_screen = "DEAD"

    clock.tick(fps)
    pygame.display.update()
pygame.quit()