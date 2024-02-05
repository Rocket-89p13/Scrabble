class Player:
    def __init__(self):
        self.rack = []
        self.score = 0
    
    def render(self, screen, font):
        for tile in self.rack:
            tile.render(screen, font)