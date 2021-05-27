class Player():
    def __init__(self, nome = None):
        self.nome = nome
        self.score = 0
        
    def loseScore(self, player):
        self.score = 0
    def addScore(self, player, score):
        self.score = score
