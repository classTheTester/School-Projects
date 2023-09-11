import pygame
from random import randint, randrange

pygame.init()

class Game:
    def __init__(self):
        self.HEIGHT = 600
        self.WIDTH = 800
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.WHITE = (255, 255, 255)
        pygame.display.set_caption("Balloon Pop Game")
        self.font = pygame.font.SysFont('Arial Black', 40)
        self.ufo_image = pygame.image.load('items/result.png')
        self.background_image = pygame.image.load('items/space.jpg')
        self.ufo_image = pygame.transform.scale(self.ufo_image, (self.ufo_image.get_width() // 8, self.ufo_image.get_height() // 8))
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))
        pygame.mixer.music.load('items/music.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
        self.sound = pygame.mixer.Sound('items/sound.mp3')
        self.sound.set_volume(0.5)
        self.difficulty = self.selectDifficulty()
        if self.difficulty == 1:
            self.speed = 1
            self.number = -20
        elif self.difficulty == 2:
            self.speed = 2
            self.number = -6
        else:
            self.speed = 3
            self.number = -6
        self.numberOfBalloons = randint(50, 70)
        self.balloonList = []
        for _ in range(self.numberOfBalloons):
            balloon = self.Balloon(
                self.surface, self.WIDTH, self.HEIGHT, self.speed, self.number,
                self.ufo_image, self.font, self.WHITE
            )
            self.balloonList.append(balloon)
        self.score, self.fly = 0, 0
        self.exitFlag = False

    def selectDifficulty(self):
        self.surface.fill(self.WHITE)
        text = self.font.render('Select Difficulty:', 1, (0,0,0))
        self.surface.blit(text, (300, self.HEIGHT//2 - 50))
        text1 = self.font.render('1. Easy', 1, (0,0,0))
        self.surface.blit(text1, (350, self.HEIGHT//2))
        text2 = self.font.render('2. Medium', 1, (0,0,0))
        self.surface.blit(text2, (350, self.HEIGHT//2 + 50))
        text3 = self.font.render('3. Hard', 1, (0,0,0))
        self.surface.blit(text3, (350, self.HEIGHT//2 + 100))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode == '1':
                        return 1
                    elif event.unicode == '2':
                        return 2
                    elif event.unicode == '3':
                        return 3

    def endScreen(self):
        self.surface.fill(self.WHITE)
        text = self.font.render('Game Over! Your score is ' + str(self.score), 1, (0,0,0))
        self.surface.blit(text, (300, self.HEIGHT//2))
        pygame.display.update()

    def showScore(self):
        text1 = self.font.render('Popped:' + str(self.score), 1, (0,0,0), self.WHITE)
        self.surface.blit(text1, (0,0))
        text2 = self.font.render('Flown away:' + str(self.fly), 1, (0,0,0), self.WHITE)
        self.surface.blit(text2, (self.WIDTH-300, 0))

    def redraw(self):
        self.surface.blit(self.background_image, (0, 0))
        self.showScore()
        for i in self.balloonList: 
            i.draw()
        pygame.draw.line(self.surface, (0,0,0), (0, self.HEIGHT * 1 / 4), (self.WIDTH, self.HEIGHT * 1 / 4), 2)
        pygame.display.update()

    def run(self):
        while not self.exitFlag:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    self.exitFlag = True  
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key).upper()
                    balloons_to_pop = []
                    for balloon in self.balloonList:
                        if balloon.letter == key and balloon.balloonVisible:
                            balloons_to_pop.append(balloon)
                    if balloons_to_pop:
                        self.sound.play()
                        balloon_to_pop = balloons_to_pop[0]
                        for balloon in balloons_to_pop:
                            if balloon.balloonY > balloon_to_pop.balloonY:
                                balloon_to_pop = balloon
                        self.score = balloon_to_pop.pop(key, self.score)
            for i in self.balloonList:
                self.fly += i.moveDown()
            if self.fly + self.score == self.numberOfBalloons:
                self.exitFlag = True
            self.redraw()
            pygame.time.delay(60)
        self.endScreen()
        pygame.time.delay(2000)
        pygame.quit()

    class Balloon():
        def __init__(self, surface, WIDTH, HEIGHT, speed, number, ufo_image, font, color):
            self.surface = surface
            self.WIDTH = WIDTH
            self.HEIGHT = HEIGHT
            self.ufo_image = ufo_image
            self.font = font
            self.color = color
            self.balloonX = randrange(60, self.WIDTH-60, 50)
            self.balloonY = randrange(number * self.HEIGHT / 5, self.HEIGHT * 2 / 5, 50)
            self.balloonR  = randint(30, 40)
            self.balloonSPEED = speed
            self.balloonVisible = True
            self.value = randint(0, 25)
            self.letter = chr(self.value + 65)

        def draw(self):
            if self.balloonVisible:
                self.surface.blit(self.ufo_image, (self.balloonX, self.balloonY))
                text = self.font.render(self.letter, True, self.color)
                text_rect = text.get_rect(center=(self.balloonX + self.ufo_image.get_width() / 2, self.balloonY + self.ufo_image.get_height() / 2))
                self.surface.blit(text, text_rect)

        def moveDown(self):
            if self.balloonVisible:
                self.balloonY += self.balloonSPEED
                if self.balloonY > self.HEIGHT + 100:
                    self.balloonVisible = False
                    return True
            return False

        def pop(self, key, score):
            if self.balloonVisible and key == self.letter and self.balloonY > 0:
                self.balloonVisible = False
                return score + 1
            return score

game = Game()
game.run()
