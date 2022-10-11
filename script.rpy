# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image white = Solid("#fff")

## ----------------------------------------------------------------- Skills
# Main char, only main char has lots of almost-non-combat skill
define liquification = Skill(name="Liquification",     power=0, mp_cost=2,     level_unlocked=1, acc=90, element="water",target="single", sfx="", img="") # just to avoid hit 90%. 1st skill
define dashingBreeze = Skill(name="Dashing Breeze",    power=5, mp_cost=6,     level_unlocked=5, acc=80,  element="water", target="single",sfx="", img="") # 80% avoid hit (except if enemies too strong) plus deals some damage
define drowningBubble = Skill(name="Drowning Bubble",  power=0, mp_cost=6,     level_unlocked=10, acc=60,  element="water", target="multiple",sfx="", img="") # for easier to flee the scene
define waterBlast = Skill(name="Water Blast",          power=10, mp_cost=8,    level_unlocked=14, acc=90, element="water",  target="single",sfx="", img="") # single target attack
define whisperingSound = Skill(name="Whispering Sound",power=0, mp_cost=12,    level_unlocked=16, acc=95,  element="water", target="single",sfx="", img="") # remove effect single
define dancingStorm = Skill(name="Dancing Storm",      power=10, mp_cost=15,   level_unlocked=18, acc=100,  element="water", target="multiple",sfx="", img="") # splash all enemies plus decreases all enemies accuracy by create Advection Fog
define oceanRhythm = Skill(name="Ocean Rhythm",        power=0, mp_cost=20,    level_unlocked=22, acc=25,  element="water", target="multiple",sfx="", img="") # remove effect all
define roaringTyphoon = Skill(name="Roaring Typhoon",  power=20, mp_cost=25,   level_unlocked=26, acc=100, element="water", target="single",sfx="", img="") # single
define tiamatInferno = Skill(name="Tiamat Inferno",    power=35, mp_cost=49,   level_unlocked=30, acc=50,  element="water", target="single",sfx="", img="") # single
define ultimateSheild = Skill(name="UtimateSheild",    power=0, mp_cost=100,   level_unlocked=35, acc=100,  element="ice", target="multiple",sfx="", img="") # all member immunes for 1 attack. Cost lots of mana, better if cost all man of main char
define absFreezing = Skill(name="Absolute Freezing",   power=40, mp_cost=70,   level_unlocked=40, acc=100,  element="ice", target="multiple",sfx="", img="") # frozen effect, multiple final move of all element name abosulute something + fog to decrease all enermies acc

## ------------------------------------------------------------------- Status dictionary
define status = {
    'wr': 'Well Rested', 
    't': 'Tired',
    'p':'Poison',
    'f': ' Freeze',
    'n': 'Normal'
}

## ------------------------------------------------------------------- Each char skills
define mainSkills = [liquification, dashingBreeze, drowningBubble, waterBlast, whisperingSound, dancingStorm, oceanRhythm, roaringTyphoon, tiamatInferno, ultimateSheild, absFreezing]
define rivalSkills = [liquification, dashingBreeze, drowningBubble, waterBlast, whisperingSound]

## ------------------------------------------------------------------- Charactera
#name, speed, agile, defense, state, strength, magic, resistance,level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal", skills=[], exp=0
define main = Protaganist(name="Main", speed = 25, agile=10, defense=5, state= status['wr'], strength=3, magic=25, resistance=20,level=8, max_hp=12, hp=12, max_mp=8, mp=8, element="Wfdgf", skills=mainSkills, exp=90)
define rival = Protaganist(name="Friend",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
define skeleton_fire = Enemy(name = "Fire Skeleton", speed = 8, agile=6, defense=4, state= status['n'], strength=5, magic=8, resistance=5, defeatedEarnedExp =5, level=1, max_hp=12, hp=12, max_mp=0, mp=0, element="Mist")




# The game starts here.

label start:
    scene bg room
    show eileen happy

    e "Hi, let's start the battle."

    call battle

    return
