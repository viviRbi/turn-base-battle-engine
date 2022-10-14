'''
Atk = Strength/Magic + power of AttackSkills +/- (raining, foggy spell or terrain) 
Combo Magic Strength Atk = (Magic + Strength)/2 + power of skills
Evade = speed + agile
Double attack percent = player speed - opponent speed
Hit percent = acc*2 + skill acc percentage +/- (raining, foggy spell or terrain)  18+ 50
Exp (when hit opp) = (opp level + my level) +12
Exp (opp killed) = [(opp level + my level)*2 + 35]
Damage = Attack - Opp defense +- Buff/Debuff spell
Crit percentage = crit percentage from AttackSkill + (player agile + speed)/2 - enemy agile
Crit Damage = Attack x 2 - Opp defense
State effect evade = agile +/- (raining, foggy spell or terrain)
Block percentage = defense/res + agile*2 + acc - opponent acc*2
                   9 +13*2 + 9 18+26 - 5= 44 -5 = 39%
'''
## ------------------------------------------------------------------- Elemental Type dictionary
#### Use definition of Aristotle-element
#   Element also had:  hot versus cold, moist versus dry

# attribute of element can decide which skill to use too. Like Water-Cold can use ice skills + water skills, Water-Steam can use Steam skills + water skills

define elementList = {
    "v": ["Aether",{"l":"Light", "d": "Dark", "v": "Void"}],  ## Light ------- Dark
    "f": ["Fire", {"h": "Hot", "m":"Moist"}],  # Hot-Plasma ------------ Moist-Smoke
    "w": ["Water", {"c": "Cold", "d":"Dry"}],   # Cold-Ice ------ Dry-Steam 
    "e": ["Earth", {"c": "Cold", "m":"Moist"}],   # Cold-Metal -------- Moist-Plant, Swam 
    "a": ["Air", {"h": "Hot", "d":"Dry"}]   # Hot-Thunder -------- Dry-Aurora (illusion, breathe control, aurora partical) https://en.wikipedia.org/wiki/Aurora
}

init python:
    class Fighter:
        def __init__(self, name, speed, agile, defense, state, strength, magic, acc, resistance,speedGrowth, agileGrowth, defenseGrowth, strengthGrowth, magicGrowth, accGrowth, resistanceGrowth,maxHpGrowth, maxMpGrowth, level, max_hp=10, hp=10, max_mp=4, mp=4, element="Water", attr=["None"], skills=[]):
            self.name = name
            self.speed = speed
            self.agile = agile 
            self.speedGrowth = speedGrowth
            self.level = level
            self.max_hp = max_hp
            self.maxHpGrowth = maxHpGrowth
            self.agileGrowth = agileGrowth 
            self.defense = defense 
            self.defenseGrowth = defenseGrowth 
            self.state = state 
            self.strength = strength 
            self.strengthGrowth = strengthGrowth 
            self.magic = magic
            self.magicGrowth = magicGrowth 
            self.acc = acc
            self.accGrowth = accGrowth
            self.attr = attr
            self.resistance = resistance
            self.resistanceGrowth = resistanceGrowth
            self.hp = hp
            self.max_mp = max_mp
            self.maxMpGrowth = maxMpGrowth
            self.mp = mp
            self.element = element
            self.skills =skills
        def increaseStatsMultipleLevel(self,level):
            while self.level < level:
                self.speed += abs((self.speed/100 * self.speedGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1)) 
                self.strength += abs((self.strength/100 * self.strengthGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1))
                self.magic += abs((self.magic/100 * self.magicGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1))
                self.acc += abs((self.acc/100 * self.accGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,2))
                self.defense += abs((self.defense/100 * self.defenseGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1))
                self.resistance += abs((self.resistance/100 * self.resistanceGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1))
                self.agile += abs((self.agile/100 * self.agileGrowth) + renpy.random.randint(0,1) -renpy.random.randint(0,1))
                self.max_hp += abs(((self.max_hp/100 * self.maxHpGrowth) + renpy.random.randint(0,5) -renpy.random.randint(0,5)))
                self.max_mp += abs(((self.max_mp/100 * self.maxMpGrowth) + renpy.random.randint(0,5) -renpy.random.randint(0,5)))
                self.level +=1

    class Protaganist (Fighter):
        def __init__(self, name, speed, agile, defense, state, strength, magic, acc, resistance,speedGrowth, agileGrowth, defenseGrowth, strengthGrowth, magicGrowth, accGrowth, resistanceGrowth,maxHpGrowth, maxMpGrowth, level,max_hp=10,hp=4,max_mp=4,mp=4,element="Water", attr=["None"], skills=[], exp=0):
            Fighter.__init__(self,name,speed, agile, defense, state, strength, magic, acc, resistance,speedGrowth, agileGrowth, defenseGrowth, strengthGrowth, magicGrowth, accGrowth, resistanceGrowth,maxHpGrowth, maxMpGrowth, level,max_hp,hp, max_mp, mp, element, attr, skills)
            self.exp=exp
        def addExp(self,exp):
            self.exp += exp
        def increaseStatsEachlevel(self):
            self.speed += abs(self.speed/100 * self.speedGrowth + renpy.random.randint(-1, 2))
            self.strength += abs(self.strength/100 * self.strengthGrowth + renpy.random.randint(-1, 2))
            self.magic += abs(self.magic/100 * self.magicGrowth + renpy.random.randint(-1, 2))
            self.acc += abs(self.acc/100 * self.accGrowth + renpy.random.randint(-1, 2))
            self.defense += abs(self.defense/100 * self.defenseGrowth + renpy.random.randint(-1, 2))
            self.resistance += abs(self.resistance/100 * self.resistanceGrowth + renpy.random.randint(-1, 2))
            self.agile += abs(self.agile/100 * self.agileGrowth + renpy.random.randint(-1, 2))
            self.max_hp += abs(self.max_hp/100 * self.maxHpGrowth + renpy.random.randint(-20, 50))
            self.max_mp += abs(self.max_mp/100 * self.maxMpGrowth + renpy.random.randint(-20, 50))
            self.level +=1

    class Enemy(Fighter):
        def __init__(self, name, speed, agile, defense, state, strength, magic, acc, resistance,speedGrowth, agileGrowth, defenseGrowth, strengthGrowth, magicGrowth, accGrowth, resistanceGrowth,maxHpGrowth, maxMpGrowth,level,max_hp=10,hp=4,max_mp=4,mp=4, element="Water", attr=["None"], skills=[], possibleEle=elementList):
            Fighter.__init__(self,name,speed, agile, defense, state, strength, magic, resistance, acc, speedGrowth, agileGrowth, defenseGrowth, strengthGrowth, magicGrowth, accGrowth, resistanceGrowth,maxHpGrowth, maxMpGrowth,level,max_hp,hp, max_mp, mp,element, attr, skills)
            self.possibleEle = possibleEle

    class Skill:
        def __init__(self, name, power, mp_cost, unlocked_atLevel, acc, element="water", target="single", sfx=None, img=None, usable=False):
            self.name = name
            self.power = power
            self.mp_cost = mp_cost
            self.element = element
            self.sfx = sfx
            self.img = img
            self.target = target
            self.acc = acc
            self.unlocked_atLevel = unlocked_atLevel



