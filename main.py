import pygame

pygame.init()

# Screen
width = 1200
height = 800
current_screen = "MENU"

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


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Geometry Dash")

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

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

        if back_rect.collidepoint(mousepos):
            back_text = Sysfont.render("Back to Menu" , True , green)
            screen.blit(back_text,back_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_screen = "MENU"

        level_1 = Play_font.render("LEVEL 1" , True , white)
        level_1_rect = level_1.get_rect(center = (width/2 , height/2))
        screen.blit(level_1,level_1_rect)
        

    clock.tick(fps)
    pygame.display.update()
pygame.quit()