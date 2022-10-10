init python:
    class Fighter:
        def __init__(self, name, speed, level=1,max_hp=10,hp=10, max_mp=4, mp=4, element="Normal",strength=0,attack=0,attack_max=0, skills=[]):
            self.name = name
            self.speed = speed
            self.level = 1
            self.max_hp = max_hp
            self.hp = hp
            self.max_mp = max_mp
            self.mp = mp
            self.element = element
            self.strength = strength
            self.attack = strength + renpy.random.randint(-4,4)
            self.attack_max = strength + strength*60/100 + renpy.random.randint(-4,8)
            self.skills =skills

    class Protaganist (Fighter):
        def __init__(self, name, speed, level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal",strength=0,attack=0,attack_max=0, skills=[], exp=0):
            Fighter.__init__(self,name,speed, level,max_hp,hp, max_mp, mp,element,strength,attack,attack_max, skills)
            self.exp=exp
            if(exp >=100):
                self.level +=1
                self.strength += renpy.random.randint(0,4)
        def addExp(self,exp):
            self.exp += exp

label set_up:
$ skeleton_fire = Fighter(name = "Fire Skeleton", speed=12, level=1, max_hp=12, hp=12, max_mp=0, mp=0, element="Mist",strength=2, attack=5,attack_max=10)
return

# Random Number Generator
label dice_roll:
$ d_crit_percentage = renpy.random.randint(1, 10)
return