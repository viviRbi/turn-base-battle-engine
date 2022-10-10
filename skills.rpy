init python:
    class Skill:
        def __init__(self, name, power, mp_cost, level, acc, element="water", target="single", sfx=None, img=None):
            self.name = name
            self.power = power
            self.mp_cost = mp_cost
            self.element = element
            self.sfx = sfx
            self.img = img
            self.target = target
            self.acc = acc
            self.level = level
        def addSkill(self, char):
            if not self in char.skills:
                char.skills.append(self)
        def useSkill(self):
            global damage
            global mp_lost
            global atk_sfx
            global name_skill
            global skill_element
            mp_lost = self.mp_cost
            #atk_sfx = "audio/battle/skills/" + self.sfx + ".ogg"
            msg_skill = self.name
            skill_element = self.element

# name, power, mp_cost, level, acc, element="water", target="single", sfx=None, img=None

# Main char, only main char has lots of almost-non-combat skill
default liquification = Skill("Liquification", 0, 2, 1, 90, "water","single", "", "") # just to avoid hit 90%. 1st skill
default dashingBreeze = Skill("Dashing Breeze", 5, 6, 1, 80, "water", "single","", "") # 80% avoid hit (except if enemies too strong) plus deals some damage
default drowningBubble = Skill("Drowning Bubble", 0, 6, 1, 60, "water", "multiple","", "") # for easier to flee the scene
default waterBlast = Skill("Water Blast", 10, 8, 1, 90, "water", "single","", "") # single target attack
default whisperingSound = Skill("Whispering Sound", 0, 12, 1, 95, "water", "single","", "") # remove effect single
default dancingStorm = Skill("Dancing Storm", 10, 15, 1, 100, "water", "multiple","", "") # splash all enemies plus decreases all enemies accuracy by create Advection Fog
default oceanRhythm = Skill("Ocean Rhythm", 0, 20, 1, "water", 90, "multiple","", "") # remove effect all
default roaringTyphoon = Skill("Roaring Typhoon", 20, 25, 1, 100, "water", "single","", "") # single
default tiamatInferno = Skill("Tiamat Inferno", 35, 49, 1, 50, "water", "single","", "") # single
default ultimateSheild = Skill("UtimateSheild", 0, 100, 1, 100, "ice", "multiple","", "") # all member immunes for 1 attack. Cost lots of mana, better if cost all man of main char
default absFreezing = Skill("Absolute Freezing", 40, 70, 1, 100, "ice", "multiple","", "") # frozen effect, multiple final move of all element name abosulute something + fog to decrease all enermies acc

# Generic monster skills
default normalAttack = Skill("Normal Attack", 0, 2, 1,90, "normal", "row", "","")