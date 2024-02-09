import pygame


class Tile:
    def __init__(self, character, x=0, y=0, width=0, height=0):
        self.character = character
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word_score = 1
        self.letter_score = 1
        self.DEFAULT_COLOR = (227, 207, 170)
        self.color = self.DEFAULT_COLOR
        self.remove = False
        self.selected = False
        self.previous_x = 0
        self.previous_y = 0

    def render(self, screen, font):
        text = self.character
        if (self.letter_score > 1 and self.character == ''):
            text = "{}".format(self.letter_score)
            if (self.letter_score == 2):
                self.color = pygame.Color('deepskyblue')
            elif (self.letter_score == 3):
                self.color = pygame.Color('blue')
        elif (self.word_score > 1 and self.character == ''):
            text = "{}".format(self.word_score)
            if (self.word_score == 2):
                self.color = pygame.Color('deeppink')
            elif (self.word_score == 3):
                self.color = pygame.Color('orange')
        elif (self.selected):
            self.color = pygame.Color('red')
        else:
            self.color = self.DEFAULT_COLOR
        # TODO
        # render each individual line of text instead of tile mult value
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        text_surface = font.render(text, False, (0, 0, 0))
        screen.blit(text_surface, (self.x + (self.width//2), self.y + (self.height//2)))

    def collision(self, mouse_x, mouse_y):
        return (self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height)

    def set_previous(self):
        self.previous_x = self.x
        self.previous_y = self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def reset_previous(self):
        self.x = self.previous_x
        self.y = self.previous_y

    def set_letter_score(self, value):
        self.letter_score = value

    def set_word_score(self, value):
        self.word_score = value
