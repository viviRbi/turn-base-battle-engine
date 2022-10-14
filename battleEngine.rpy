init python: 
    # perfom deep copy of a randome obj in enemyTypeList (user input). 
    # Deep copy = new object generated with same value of the copy class
    # if not copy, it'll create a loop of last value instead of randomly picked value. 
    # Ex: print i object from 1-8, it will print 8 eight times
    import copy
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

    class EnemiesGenerator:
            def __init__(self,enemiesTypeList, enemiesList):
                self.enemiesTypeList = enemiesTypeList
                self.enemiesList = enemiesList
                self.generateEnemies()
            def generateEnemies(self):
                self.enemiesList=[]
                numberOfPartyMembers= len(protaganistsInThisFight)
                numberOfMonsters = renpy.random.randint(numberOfPartyMembers+1, numberOfPartyMembers*3)
                for i in range(1, numberOfMonsters):

                    # get the monster type from list
                    if(len(self.enemiesTypeList ) >1):
                        diceMonsterChosenType = copy.deepcopy(self.enemiesTypeList[renpy.random.randint(0,len(enemiesTypeList )-1)])
                    else:
                        diceMonsterChosenType = copy.deepcopy(self.enemiesTypeList[0])
                    # get all possible elements it can have
                    possibleEleList = diceMonsterChosenType.possibleEle.keys()
                    # get element for the monster from its possible element
                    diceEle = possibleEleList[renpy.random.randint(0,len(possibleEleList)-1)]
                    diceMonsterChosenType.element = elementList[diceEle[0]][0]
                    diceMonsterChosenType.name += str(i)  
                    # attrList = diceEle[1].keys()
                    # randomAttr = attrList[renpy.random.randint(0,len(attrList)-1)]
                    # diceMonsterChosenType.attr = randomAttr
                    # add the generaed monster to the list
                    self.enemiesList.append(diceMonsterChosenType)   
            def addToEnemiesList(self):
                for i in self.enemiesList:
                    enemiesList.append(i)



