class Player:
    def __init__(self):
        self.rack = []
        self.rack_start_pos = (0,0)
        self.rack_direction = 0
        self.score = 0
    
    def render(self, screen, font):
        for tile in self.rack:
            if(tile is not None):
                tile.render(screen, font)