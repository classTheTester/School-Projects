import time
#testing
import pygame
pygame.init()
green = (0, 255, 0)
red = (149, 53, 83)
yellow = (255,255,0)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)


class Words():
    def __init__(self, word, xPos, yPos):
        self.time = 0
        self.accuracy = 0
        self.word = word
        self.wordLen = len(str(word))
        self.letterList = list(word)
        self.counter = -1
        self.xPos = xPos
        self.yPos = yPos
        self.listColour = [black] * self.wordLen
        self.wrongLetters = ""
        self.firstTime = 0
        self.letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    def backSpace(self):
        self.listColour[self.counter] = black
        if self.counter < 0:
            return True
        else:
            self.counter -= 1
    def initiateTime(self):
        self.firstTime = time.time()

    def checkCorrect(self, letterPressed):
        if self.counter < self.wordLen - 1:
            self.counter += 1
        if self.letterList[self.counter] == letterPressed:
            self.listColour[self.counter] = green
        elif self.letterList[self.counter] != letterPressed:
            self.listColour[self.counter] = red
            self.wrongLetters += self.letterList[self.counter]
        if self.counter == self.wordLen-1:
            return True

    def drawWord(self, surface, pointer):
        for i in range(len(self.word)):
            if i == self.counter + 1 and pointer:
                text = font.render(self.letterList[i], True, self.listColour[i], yellow)
            else:
                text = font.render(self.letterList[i], True, self.listColour[i])
            surface.blit(text, (self.xPos + 30*i, self.yPos))
    def inputData(self, accList, timeList, wrongLetterList):
        secondTime = time.time()
        self.time = secondTime - self.firstTime
        self.accuracy = (1-(len(self.wrongLetters)/self.wordLen))
        accList.append(self.accuracy); timeList.append(self.time); wrongLetterList.append(self.wrongLetters)    
    def indicateKeyboard(self, surface):
        rowLevel = 0
        if self.counter >= self.wordLen-1:
            pygame.draw.rect(surface, yellow, pygame.Rect(230, 530, 400, 60))
        else:
            letterIndex = self.letters.index(self.letterList[self.counter+1]) 
            if letterIndex >= 19:
                letterIndex -= 19
                rowLevel += 2
            elif letterIndex >= 10:
                letterIndex -= 10
                rowLevel += 1
            pygame.draw.rect(surface, yellow, pygame.Rect(110+(50*letterIndex)+20*rowLevel, 390+(50*rowLevel), 50, 40))





