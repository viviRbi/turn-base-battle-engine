class TurnList:
    def __init__(self, protaganists =[], enemies=[], participants=[]):
        self.protaganists = protaganists
        self.enemies = enemies
        self.participants = participants
        decideTurn()
    #Sort party members and enemies by speed
    def decideTurn(self):
        p = self.protaganists + self.enemies
        sortedParticipants = sorted(p,key=lambda x: x.speed)
        self.participants=sortedParticipants