import pygame

pygame.init()

# Screen
width = 1200
height = 800
current_screen = "MENU"
ground_y = height - 100

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

# Cube
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

    def jump(self):
        if self.is_ground == True:
            self.vy = self.jump_force
            self.is_ground = False

    def physics(self):
        self.vy += self.gravity
        self.y += self.vy
        self.rect.y = self.y

    def update(self,ground_y):
        self.physics()
        if self.y >= ground_y - self.height:
            self.y = ground_y - self.height
            self.vy = 0
            self.is_ground = True

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

    def reset(self):
        self.vx = 0
        self.vy = 0
        self.y = ground_y - self.height
        self.is_ground = True

cube = Cube()

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

    if current_screen == "MENU":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        play_text = Play_font.render("PLAY" , True , white)
        play_rect = play_text.get_rect(center = (width / 2 , height / 2))
        screen.blit(play_text,play_rect)

        logo_text = logo_font.render("GEOMETRY DASH" , True , white)
        logo_rect = logo_text.get_rect(center= (width / 2 , height / 2 - 200))
        screen.blit(logo_text,logo_rect)

        if play_rect.collidepoint(mousepos):
            play_text = Play_font.render("PLAY" , True , green)
            screen.blit(play_text,play_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen = "PLAY"

    elif current_screen == "PLAY":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        back_text = Sysfont.render("Back to Menu" , True , white)
        back_rect = back_text.get_rect(center = (width / 2 , height - 100))
        screen.blit(back_text,back_rect)

        level_1 = Play_font.render("LEVEL 1" , True , white)
        level_1_rect = level_1.get_rect(center = (width//2 , height//2))
        screen.blit(level_1,level_1_rect)

        next_lvl = Sysfont.render("next lvl ==>" , True , white)
        next_lvl_rect = next_lvl.get_rect(bottomleft = (width - 150 , height//2))
        screen.blit(next_lvl,next_lvl_rect)

        if next_lvl_rect.collidepoint(mousepos):
            next_lvl = Sysfont.render("next lvl ==>" , True , green)
            screen.blit(next_lvl,next_lvl_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        if level_1_rect.collidepoint(mousepos):
            level_1 = Play_font.render("LEVEL 1" , True , green)
            screen.blit(level_1,level_1_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen = "LEVEL1"

        if back_rect.collidepoint(mousepos):
            back_text = Sysfont.render("Back to Menu" , True , green)
            screen.blit(back_text,back_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen = "MENU"

    elif current_screen == "LEVEL1":
        screen.fill(black)

        cube.update(ground_y)
        cube.draw(screen)
                    
    clock.tick(fps)
    pygame.display.update()
pygame.quit()