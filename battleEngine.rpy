init python: 
    class TurnList:
        def __init__(self, protaganists =[], enemies=[], participants=[]):
            self.protaganists = protaganists
            self.enemies = enemies
            self.participants = participants
            self.decideTurn()
        #Sort party members and enemies by speed
        def decideTurn(self):
            p = self.protaganists + self.enemies
            sortedParticipants = sorted(p,key=lambda x: x.speed, reverse = True)
            self.participants=sortedParticipants

# Random Number Generator
label dice_roll:
    $ d_crit_percentage = renpy.random.randint(1, 10)
    return

