class Tale:
    def __init__(self, color, is_solid = False, is_player = False, is_victory = False, x = 0, y = 0):
        self.x = x
        self.y = y
        self.color = color
        self.is_solid = is_solid
        self.is_player = is_player
        self.is_victory = is_victory
        self.width = 50
        self.height = 50
        self.is_visited = False

    def __repr__(self):
        return(f"({self.x}, {self.y})")

LIGHT_GRAY = (60,64,66)
DARK_GREY = (32,33,36)
LIGHT_PINK = (255,179,255)
DARK_PINK = (234,128,252)
WHITE_1 = (255,255,255)
WHITE_2 = (185,185,185)