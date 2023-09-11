import pygame
import json
pygame.init()
from gameClasses import *
class Game:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = (0, 0, 255)
        self.totalLetters = 0
        self.mistakes = 0
        self.wrongLetterList = []
        self.accList = []
        self.timeList = []
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font2 = pygame.font.Font('freesansbold.ttf', 45)
        self.X = 800
        self.Y = 600
        self.keyboardImg = pygame.image.load("keyboard.png")
        self.display_surface = pygame.display.set_mode((self.X, self.Y))
        pygame.display.set_caption('Show Text')
        self.words = ['yes', 'no', 'random', 'words', 'jkjkj', 'please', 'damn']
        self.level = 0 #need to add a function that can take a user difficulty level and string together random words from the dedicated level list (to make another list)
        self.listClass = []
        self.wordsCounter = 0
        self.endList = False
        self.gameLoop = True
        self.scoreLoop = True
        self.userList = []
        self.nameSaved = False
        self.score = 0
        self.rawWPM = 0
        self.accuracy = 0

    def createClasses(self):
        xSpace = 0
        ySpace = 50
        for i in range(len(self.words)):
            wordUsed = Words(self.words[i], xSpace, ySpace)
            self.listClass.append(wordUsed)
            if xSpace + 30 * len(self.words[i]) + 40 < 600:
                xSpace += 30 * len(self.words[i]) + 50
            else:
                ySpace += 50
                xSpace = 0

    def scoreDraw(self, username):
        self.display_surface.fill(self.white)
        text = self.font.render("Please enter a username (max 15 letters)", True, self.black)
        text2 = self.font.render(
            "Your score " + str(self.score) + " wpm" + "(raw WPM: " + str(self.rawWPM) + " accuracy: " + str(
                round(100 * self.accuracy)) + "%)", True, self.black)
        self.display_surface.blit(text, (50, 140))
        self.display_surface.blit(text2, (20, 80))
        if len(self.userList) > 0:
            text = self.font.render(''.join(self.userList), True, self.black)
            self.display_surface.blit(text, (50, 185))
            if self.nameSaved:
                text = self.font.render("Username is saved!", True, self.blue)
                self.display_surface.blit(text, (50, 230))

    def redraw(self):
        yVal = 20
        self.display_surface.fill(self.white)
        self.display_surface.blit(self.keyboardImg, (0, 300))
        if len(self.listClass) - 1 > 0:
            self.listClass[self.wordsCounter].indicateKeyboard(self.display_surface)
        for i in range(len(self.listClass)):
            if i == self.wordsCounter:
                self.listClass[i].drawWord(self.display_surface, True)
            else:
                self.listClass[i].drawWord(self.display_surface, False)

    def scoreScreen(self):
        keyList = []
        topList = []
        readInfo = open("scores.txt", "r")
        readDict = json.load(readInfo)
        for i in readDict:
            keyList.append(int(i))
        for j in range(5):
            topList.append(max(keyList))
            keyList.remove(max(keyList))
        topList = [str(a) for a in topList]
        return topList, readDict

    def drawScoreScreen(self):
        topList, dic = self.scoreScreen()
        self.display_surface.fill(self.white)
        textWPM = self.font2.render("WPM:", True, self.black)
        textUsername = self.font2.render("Username:", True, self.black)
        self.display_surface.blit(textWPM, (630, 0))
        self.display_surface.blit(textUsername, (30, 0))
        for i in range(len(topList)):
            text = self.font.render((str(i + 1) + ".) " + dic.get(topList[i])), True, self.black)
            text2 = self.font.render(str(topList[i]), True, self.black)
            self.display_surface.blit(text, (30, 150 + 100 * i))
            self.display_surface.blit(text2, (630, 150 + 100 * i))

    def run(self):
        self.createClasses()
        self.listClass[0].initiateTime()

        while self.gameLoop:
            self.redraw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        if self.endList:
                            self.endList = False
                            self.listClass[self.wordsCounter].inputData(self.accList, self.timeList, self.wrongLetterList)
                            self.wordsCounter += 1
                            if self.wordsCounter == len(self.words):
                                totalTime = sum(self.timeList)
                                self.rawWPM = round((60 / totalTime) * len(self.words))
                                self.accuracy = sum(self.accList) / len(self.words)
                                self.score = round(self.rawWPM * self.accuracy)
                                self.gameLoop = False
                                self.words = [a for a in self.wrongLetterList if a != ""]
                                if len(self.words) == 0:
                                    self.gameLoop = False
                            else:
                                self.listClass[self.wordsCounter].initiateTime()
                    elif keys[pygame.K_BACKSPACE]:
                        if self.listClass[self.wordsCounter].backSpace() and self.wordsCounter > 0:
                            self.wordsCounter -= 1
                    elif self.listClass[self.wordsCounter].checkCorrect(pygame.key.name(event.key)):
                        if self.wordsCounter < len(self.words) - 1:
                            self.listClass[self.wordsCounter + 1].initiateTime()
                        self.endList = True

        scoreScreenBool = False
        while self.scoreLoop:
            pygame.display.update()
            for event in pygame.event.get():
                if not scoreScreenBool:
                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            if len(self.userList) > 0:
                                self.nameSaved = True
                                readInfo = open("scores.txt", "r")
                                readDict = json.load(readInfo)
                                readDict[str(self.score)] = ''.join(self.userList)
                                readInfo.close()
                                writingInfo = open("scores.txt", "w")
                                dumpingInfo = json.dumps(readDict)
                                writingInfo.write(dumpingInfo)
                                writingInfo.close()
                        elif keys[pygame.K_RETURN]:
                            scoreScreenBool = True
                        elif keys[pygame.K_BACKSPACE]:
                            if len(self.userList) > 0:
                                self.userList.pop()
                        else:
                            if len(self.userList) <= 15:
                                self.userList.append(pygame.key.name(event.key))
                        self.scoreDraw(''.join(self.userList))
                else:
                    self.drawScoreScreen()
