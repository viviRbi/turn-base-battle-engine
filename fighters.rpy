'''
Atk = strength/magic + power of skills/weapon
Evade = speed + agile
Hit percent = acc +/- (raining, foggy spell or terrain) - opponent evade. Opponent use= minus. User use = +
Exp (when hit opp) = (opp level + my level) +12
Exp (opp killed) = [(opp level + my level)*2 + 35]
Dammage = Attack - Opp defense +- Buff/Debuff spell
Crit Damage = Attack x 2 - Opp defense
'''

init python:
    class Fighter:
        def __init__(self, name, speed, agile, defense, state, strength, magic, resistance, level=1,max_hp=10,hp=10, max_mp=4, mp=4, element="Normal", skills=[]):
            self.name = name
            self.speed = speed
            self.level = 1
            self.max_hp = max_hp
            self.agile = agile 
            self.defense = defense 
            self.state = state 
            self.strength = strength 
            self.magic = magic 
            self.resistance = resistance
            self.hp = hp
            self.max_mp = max_mp
            self.mp = mp
            self.element = element
            self.skills =skills

    class Protaganist (Fighter):
        def __init__(self, name, speed, agile, defense, state, strength, magic, resistance,level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal", skills=[], exp=0):
            Fighter.__init__(self,name,speed, agile, defense, state, strength, magic, resistance, level,max_hp,hp, max_mp, mp, element, skills)
            self.exp=exp
        def addExp(self,exp):
            self.exp += exp

    class Enemy(Fighter):
        def __init__(self, name, speed, agile, defense, state, strength, magic, resistance, defeatedEarnedExp, level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal", skills=[]):
            Fighter.__init__(self,name,speed, agile, defense, state, strength, magic, resistance,level,max_hp,hp, max_mp, mp,element, skills)
            self.defeatedEarnedExp = defeatedEarnedExp

    class Skill:
        def __init__(self, name, power, mp_cost, level_unlocked, acc, element="water", target="single", sfx=None, img=None, usable=False):
            self.name = name
            self.power = power
            self.mp_cost = mp_cost
            self.element = element
            self.sfx = sfx
            self.img = img
            self.target = target
            self.acc = acc
            self.level_unlocked = level_unlocked



