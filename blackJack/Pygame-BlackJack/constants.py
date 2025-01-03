import os
import pygame as pygame

# Set up paths relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))

# Helper function to construct paths
def resource_path(relative_path):
    return os.path.join(script_dir, relative_path)

# Screen dimensions and colors
display_width = 900
display_height = 700

background_color = (34, 139, 34)
white = (250, 250, 250)
blue = (66, 135, 245)
black = (0, 0, 0)
green = (3, 158, 34)
red = (255, 0, 0)
light_slat = (119, 136, 153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)

pygame.init()

# Fonts
font = pygame.font.SysFont("Arial", 35)
textfont = pygame.font.SysFont("Arial", 15)
game_end = pygame.font.SysFont("dejavusans", 40)
blackjack = pygame.font.SysFont("roboto", 70)

# Load assets
backCard = pygame.image.load(resource_path("img/back.png"))

SUITS = ["C", "S", "H", "D"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

themeMusic = pygame.mixer.music.load(resource_path("sounds/theEntertainer.mp3"))
pygame.mixer.music.play(-1)

cardSound = pygame.mixer.Sound(resource_path("sounds/cardFlip.mp3"))
cardSound.set_volume(0.8)

# Screen setup
screen = pygame.display.set_mode((800, 600))

dealBool = True
background = pygame.image.load(resource_path("img/background.jpg"))
background = pygame.transform.scale(background, (800, 600))
startBackground = pygame.image.load(resource_path("img/startBackground.jpg"))
startBackground = pygame.transform.scale(startBackground, (800, 600))

start = True
gameLoop = False
