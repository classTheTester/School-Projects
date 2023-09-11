import pygame as pygame

display_width = 900
display_height = 700

background_color = (34,139,34)
white = (250, 250, 250)
blue = (66, 135, 245)
black = (0,0,0)
green = (3, 158, 34)
red = (255,0,0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 35)
textfont = pygame.font.SysFont('Arial', 15)
game_end = pygame.font.SysFont('dejavusans', 40)
blackjack = pygame.font.SysFont('roboto', 70)
backCard = pygame.image.load("img/back.png")


SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

themeMusic = pygame.mixer.music.load("sounds/theEntertainer.mp3")
pygame.mixer.music.play(-1)


cardSound = pygame.mixer.Sound("sounds/cardFlip.mp3")
cardSound.set_volume(0.8)
  
screen=pygame.display.set_mode((800,600))
dealBool = True
background = pygame.image.load("img/background.jpg")
background = pygame.transform.scale(background,(800,600))
startBackground = pygame.image.load("img/startBackground.jpg")
startBackground = pygame.transform.scale(startBackground, (800, 600))
start = True
gameLoop = False





