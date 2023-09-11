# import pygame module in this program
from classes import *
white = (255, 255, 255)
black = (0,0,0)
totalLetters = 0
mistakes = 0
wrongLetterList = []
accList = []
timeList = []
font = pygame.font.Font('freesansbold.ttf', 32)
import pygame
import json
scoreText = open("scores.txt", 'a')
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
 
# assigning values to X and Y variable
X = 800
Y = 600
timeList = []
accuracyList = []
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font

 
# create a text surface object,
# on which text is drawn on it.

words = ['thewiseman', 'thefool', 'thedog', 'jkjkjkjk', 'falling', 'what', 'fjfjfjfjfjfjfj']
listClass = []
wordsCounter = 0
gameLoop = True
scoreLoop = False
def createClasses(words):
    for i in range(len(words)):
        if i == 0:
            wordUsed = Words(words[i],0, i)
        else:
            wordUsed = Words(words[i],len(words[i-1]), i)
        listClass.append(wordUsed)
createClasses(words)
# create a rectangular object for the
# text surface object
 
# set the center of the rectangular object.
 
# infinite loop
userList = []
def scoreDraw():
    display_surface.fill(white)
    if len(userList) > 0:
        for i in range(len(userList)):
            text = font.render(userList[i], True, black)
            display_surface.blit(text, (10 +30*i,185))
        
def redraw():
    yVal = 20
    display_surface.fill(white)
    for i in range(len(listClass)):
        if i == wordsCounter:
            listClass[i].drawWord(display_surface, True)
        else:
            listClass[i].drawWord(display_surface, False)

while scoreLoop:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                scoreJson = {"name": ''.join(userList), "score": 0}
                test = json.dumps(scoreJson)
                scoreText.write(test)
                scoreText.close()
            else:
                userList.append(pygame.key.name(event.key))
    scoreDraw()

listClass[0].initiateTime()
while gameLoop:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                wordsCounter += 1
            elif keys[pygame.K_BACKSPACE]:
                if listClass[wordsCounter].backSpace() and wordsCounter > 0:
                    wordsCounter -= 1
            elif listClass[wordsCounter].checkCorrect(pygame.key.name(event.key),wrongLetterList, accuracyList, timeList):
                wordsCounter += 1
                if wordsCounter != len(words):
                    listClass[wordsCounter].initiateTime()
                print(wrongLetterList)
                if wordsCounter == len(words):
                    words = [a for a in wrongLetterList if a != ""]
                    if len(words) == 0:
                        print("timeList", timeList, "accuracyList", accuracyList, "wrongLetters", wrongLetterList)
                        gameLoop = False
                    else:
                        wordsCounter = 0
                        wrongLetterList.clear()
                        listClass.clear()
                        createClasses(words)
                    


    redraw()
