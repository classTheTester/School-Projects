import pygame
darkBlue = (49, 79, 152)
lightBlue = (16, 217, 219)
# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
WIDTH = 800
HEIGHT = 600
screen_size = (WIDTH, HEIGHT)
WHITE = (255,255,255)
white = (255, 255, 255)
PEACH = (243,144,15)
font = pygame.font.SysFont('Arial Black',27)

# Create the screen surface
screen = pygame.display.set_mode(screen_size)
def button(msg, x, y, w, h, initcol, aftercol, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, aftercol, (x, y, w, h))
        if click[0] == 1:
            if msg == "Deal":
                 player.money -= player.bet
            action()
    else:
        pygame.draw.rect(screen, initcol, (x, y, w, h))
    msg = font.render(msg, 1, white)
    screen.blit(msg, (x+20,y))


def typingGame():
    from typingGame import Game
    game = Game()
    game.run()
    

def spaceGame():
    from spaceGame import Game
    game = Game()
    game.run()

def draw():
    screen.fill((48, 221, 255)) #fill 2/3 screen
    topHalf = pygame.draw.rect(screen,PEACH,(0,0,2500,350)) 
    gameMessage = font.render('Welcome to RapidType! Please select below!',18,WHITE)
    gameMessageTwo = font.render('RapidType is the best way to improve your typing!',18,WHITE)
    ballMessage = font.render('Balloon Pop',10,WHITE)
    personMessage = font.render('Made by Zach, Edward, Yifan and Braden',18,WHITE)
    screen.blit(gameMessage,(20,75))
    screen.blit(gameMessageTwo,(40,185))
    screen.blit(personMessage,(150,425))
    timeButton = button("Play timed", WIDTH//2+10, HEIGHT//2-30, 190, 35, darkBlue, lightBlue, typingGame)
    spaceButton = button("Space", 100,HEIGHT//2-31,130,35, darkBlue, lightBlue, spaceGame)

    
# Game loop
gameLoop = True
while gameLoop:
    pygame.display.update()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()


    # Update the screen
    #pygame.display.flip()

# Quit the game
pygame.quit()
