import os
import pygame
import random
from constants import *

# Helper function to construct paths relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    return os.path.join(script_dir, relative_path)

class Deck:
    def __init__(self):
        self.cards = []
        # Sets the "deck" by using a for loop for the card values and suits
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                # Putting both the suits and ranks together
                # Done so it can be loaded into the main game with another string concatenation
                self.cards.append([value, suit])
        # Randomizes the card deck each time
        random.shuffle(self.cards)
        return self.cards


class Dealer(object):
    def __init__(self, bet, sound):
        self.money = 1000
        self.cardPic = []
        self.handValue = 0
        self.handList = []
        self.bet = bet
        self.sound = sound

    def fundsUpdate(self, condition):
        if condition == "win":
            self.money += self.bet
        elif condition == "lose":
            self.money -= self.bet

    def count(self):
        self.handValue = 0
        aceCount = 0
        for value in self.handList:
            if value == "A":
                aceCount += 1
            elif value in "JQK":
                self.handValue += 10
            else:
                value = int(value)
                self.handValue += value
        for i in range(aceCount):
            # Checks to see if an ace would make the hand greater than 21, if so, changes the value to 1
            if self.handValue + 11 > 21:
                self.handValue += 1
            else:
                self.handValue += 11

    def hit(self):
        # Appends the first "card" in the deck and only its value.
        self.handList.append(deck.cards[0][0])
        # Appends the cardPic list with the files by adding the value and suit with each other
        card_path = resource_path(f"img/{deck.cards[0][0]}{deck.cards[0][1]}.png")
        self.cardPic.append(card_path)
        # Removes the first card
        deck.cards.pop(0)
        # Each hit, it uses the count method to calculate the hand.
        self.count()
        self.sound.play()

    def drawCards(self, surface, dealBool):
        dealerPicList = []
        index = 250

        for i in range(len(self.cardPic)):
            card = pygame.image.load(self.cardPic[i])
            dealerPicList.append(card)

        for j in range(len(dealerPicList)):
            surface.blit(dealerPicList[j], (index, 50))
            if dealBool:
                surface.blit(backCard, (350, 50))
            index += 100

    def newGame(self):
        self.money = 1000
        self.cardPic = []
        self.handValue = 0
        self.handList = []


class Player(Dealer):
    def drawCards(self, surface):
        index = 250
        playerPicList = []
        for i in range(len(self.cardPic)):
            card = pygame.image.load(self.cardPic[i])
            playerPicList.append(card)

        for j in range(len(playerPicList)):
            surface.blit(playerPicList[j], (index, 400))
            index += 100


# Initialize instances
dealer = Dealer(100, cardSound)
player = Player(100, cardSound)
deck = Deck()
