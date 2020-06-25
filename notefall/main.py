import pygame, sys, os
 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('notefall')
gameWindow = pygame.display.set_mode((960, 720), pygame.FULLSCREEN)
 
font = pygame.font.SysFont(None, 60)
btnfont = pygame.font.SysFont(None, 30)

gameBg = pygame.image.load(os.path.join("assets", "imgmedia", "homescreen_bg.jpg"))
gameBg = pygame.transform.scale(gameBg, (960, 720))
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(gameBg, (0, 0)) 
        draw_text('notefall', font, (28, 30, 150), gameWindow, 120, 360)
 
        mx, my = pygame.mouse.get_pos()
        
        playBtn = pygame.Rect(580, 200, 200, 50)
        optionsBtn = pygame.Rect(580, 300, 200, 50)
        exitBtn = pygame.Rect(580, 400, 200, 50)
        if playBtn.collidepoint((mx, my)):
            if click:
                game()
        if optionsBtn.collidepoint((mx, my)):
            if click:
                options()
        if exitBtn.collidepoint((mx, my)):
            if click:
                exitGame()
        pygame.draw.rect(gameWindow, (122, 113, 247), playBtn)
        pygame.draw.rect(gameWindow, (122, 113, 247), optionsBtn)
        pygame.draw.rect(gameWindow, (122, 113, 247), exitBtn)
        
        playTxt = btnfont.render('Play', True, (0, 0, 0))
        gameWindow.blit(playTxt, (655, 215))
        optionTxt = btnfont.render('Options', True, (0, 0, 0))
        gameWindow.blit(optionTxt, (635, 315))
        exitTxt = btnfont.render('Exit', True, (0, 0, 0))
        gameWindow.blit(exitTxt, (655, 415))

 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    
    while running:
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(gameBg, (0, 0)) 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        gameWindow.fill((255, 255, 255))
        gameWindow.blit(gameBg, (0, 0)) 
 
        draw_text('options', font, (28, 30, 150), gameWindow, 80, 80)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

def exitGame():
    pygame.quit()
 
main_menu()