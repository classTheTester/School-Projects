from blackjack_classes import *
from constants import *
from math import sqrt
import pygame, time
pygame.init()
def startScreen():
     screen.blit(startBackground, (0,0))
     startText = blackjack.render("Press space to play!", 0, white)
     screen.blit(startText, (250, 550))
     pygame.display.update()

def loseScreen():
    lose = True
    while lose:
        screen.blit(background, (0,0))
        if dealer.money <= 0:
            endText = blackjack.render("You win!", 0, blue)
            screen.blit(endText, (250, 250))
        if player.money <= 0:
            endText = blackjack.render("You lose!", 0, dark_red)
            screen.blit(endText, (250, 250))
        endText2 = font.render("Press space to play again!", 0, white)
        screen.blit(endText2, (200, 300))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            deck = Deck()
            player.newGame()
            dealer.newGame()
            play.deal()
            lose = False
        pygame.display.update()

        
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
    pygame.display.update()



while start:
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            start = False
        # act upon mouse events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
             gameLoop = True
             start = False
        startScreen()

        
class Play:
         

    def hit():
        #The class has a function that returns whether or not the dealer busts or gets blackjack or vice versa
        #The function is called when the player hits the space with the play object, in which case, the game would use transfer the bet accordingly
        #This will be added for every combination in the final game through the function. Global will be removed when everything is transfered into the classes file

        play.draw("player")
        player.hit()
        redraw_screen()
        if player.handValue > 21:
            play.personWin("dealer")
        elif player.handValue == 21:
            play.personWin("player")
        #Used to indicate who one with a conditional, "null" shows nothing
    def hold():
        #While loop that makes continues to hit the dealer and redraw the screen to show it. If a person loses, the results variable is changed
        #The screen will be redrawed so the message will show, then change the variable to not show it again.
        #Global variable will be changed when the class play class is moved into the classes file (when it is complete)
        #For each of the events, the game will call the deal function which is in the same play class
        global dealBool
        dealBool = False
        redraw_screen()
        while True:
            if dealer.handValue > 21:
                play.personWin("player")
                break
            #Checks whether the dealer hand value is greater than 17 (since it can't hit if it is greater than 17, then checks if it is greater than than the player's and the dev has not busted)
            elif dealer.handValue >= 17 and dealer.handValue <= 21:
                if dealer.handValue > player.handValue:
                    play.personWin("dealer")
                else:
                    play.personWin("player")
                break
            elif dealer.handValue == 21:
                play.personWin("dealer")
                break
            else:
                play.draw("dealer")
                dealer.hit()
                redraw_screen()
                
    def bettingSystem():
        #Betting system which has a circle act as a slider by staying at the same y value, but its x value is equal to the user cursor
        betX = 150
        mouseHold = True
        while True:
             mouseX, mouseY = pygame.mouse.get_pos()
             percentage = (betX-150)/1.5
             playerBet = round(percentage*player.money/100)
             if mouseHold:
                 if mouseX > 300:
                     betX = 300
                 elif mouseX < 150:
                     betX = 150
                 else:
                    betX = mouseX
                    
             for event in pygame.event.get():
                    #Checks if user x's out the window
                    if event.type == pygame.QUIT:
                        betMenu = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if distance(mouseX, mouseY, betX, 300) < 10:
                            mouseHold = True
                        elif distance(mouseX, mouseY, betX, 300) > 10:
                            mouseHold = False
             keys = pygame.key.get_pressed()
             #Sets the bet variables
             if keys[pygame.K_RETURN] and playerBet > 0:
                 if playerBet > dealer.money:
                     playerBet = dealer.money
                 player.bet = playerBet
                 dealer.bet = playerBet
                 redraw_screen()
                 break
    
             pygame.time.delay(25)
             screen.fill(green)
             pygame.draw.line(screen, white, (150,300), (300, 300), 5)
             pygame.draw.circle(screen, white, (betX, 300), 10)
             percentage = (betX-150)/1.5
             betPercentage = textfont.render((str(round(percentage))+ "%"), 1, white)
             playerBet = round(percentage*player.money/100)
             #Calculates the percentage by subtracting the x value by 150 (since the line starts at 150) and dividing it by 300 (the line is 150 px long and starts at 150 px)\
             #The percentage is then multiplied by the total money.
             #This will be changed to betting with chips
             playerBetText = textfont.render("Bet Value: $" + str(playerBet), 1, white)
             screen.blit(betPercentage, (betX-10, 275))
             screen.blit(playerBetText, (150, 200))
             enterStatement = blackjack.render("Press enter to lock in bet", 0, white)
             screen.blit(enterStatement, (75, 10))
             pygame.display.update()

             

                    

        
    def deal():
        global dealBool
        dealBool = False
        player.handList.clear()
        player.cardPic.clear()
        dealer.handList.clear()
        dealer.cardPic.clear()
        play.draw("player")
        player.hit()
        play.draw("dealer")
        dealer.hit()
        play.draw("player")
        player.hit()
        play.draw("dealer")
        dealer.hit()
        dealBool = True
        redraw_screen()
        
    def draw(person):
        coor = [50,150]
        if person == "player":
            for i in range(15):
                screen.blit(backCard, coor)
                coor[0] += 20
                coor[1] += 5
                pygame.display.update()
                time.sleep(0.03)
                redraw_screen()
            
        elif person == "dealer":
            for i in range(7):
                screen.blit(backCard, coor)
                coor[0] += 20
                pygame.display.update()
                time.sleep(0.03)
                redraw_screen()
                
    def personWin(person):
        if person == "dealer":
            player.fundsUpdate("lose")
            dealer.fundsUpdate("win")
            dealerWin = blackjack.render("Dealer won!", 1, dark_red)
            screen.blit(dealerWin, (350,100))
            pygame.display.update()
            time.sleep(2.5)
            if player.money > 0 and dealer.money > 0:
                play.deal()
        elif person == "player":
            player.fundsUpdate("win")
            dealer.fundsUpdate("lose")
            playerWin = blackjack.render("Player won!", 1, blue)
            screen.blit(playerWin, (350,500))
            pygame.display.update()
            time.sleep(2.5)
            if dealer.money > 0 and player.money > 0:
                play.deal()
        
        

play = Play
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
    

def redraw_screen():
    #Loads the different types of hud
    betAmount = textfont.render(("Bet: $" + str(player.bet)), 1, white)
    playerScore = textfont.render(("Player money: $" + str(player.money)), 1, white)
    playerHand = textfont.render(("Hand Value: " + str(player.handValue)), 1, white)
    dealerScore = textfont.render(("dealer money: $" + str(dealer.money)), 1, white)
    dealerHand = textfont.render(("Hand Value: " + str(dealer.handValue)), 1, white)
    screen.blit(background,(0,0))
    #Checks if the player holds, if so, would blit the hand value of the dealer
    if not dealBool:
        screen.blit(dealerHand, (50, 50))
    screen.blit(playerScore, (10, 300))
    screen.blit(playerHand, (50, 380))
    screen.blit(dealerScore, (10, 130))
    screen.blit(betAmount, (450, 300))
    
    screen.blit(backCard, (10, 150))
    player.drawCards(screen)
    dealer.drawCards(screen, dealBool)
    pygame.display.update()

        
        
        
#Deals the cards initially using the method
play.deal()
while gameLoop:
     button("Deal", 650, 150, 100, 50, black, dark_slat, play.deal)
     button("Hit", 650, 225, 100, 50, black, dark_slat, play.hit)
     button("Hold", 650, 300, 100, 50, black, dark_slat, play.hold)
     button("Bet", 650, 375, 100, 50, black, dark_slat, play.bettingSystem)
     if len(deck.cards) <= 0:
          deck.build()
    #All the keys are hotkeyed to the different functions in the play class.
     for event in pygame.event.get():
            #Checks if user x's out the window
            if event.type == pygame.QUIT:
                gameLoop = False
     if dealer.money < 0 or player.money < 0:
         loseScreen()

pygame.quit()
            
        
    
