# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define testI =[]
define e = Character("Eileen")
image white = Solid("#fff")

## ----------------------------------------------------------------- Skills
# Main char, only main char has lots of almost-non-combat skill
define liquification = Skill(name="Liquification",     power=0, mp_cost=2,     unlocked_atLevel=1, acc=90, element="water",target="single", sfx="", img="") # just to avoid hit 90%. 1st skill
define dashingBreeze = Skill(name="Dashing Breeze",    power=5, mp_cost=6,     unlocked_atLevel=5, acc=80,  element="water", target="single",sfx="", img="") # 80% avoid hit (except if enemies too strong) plus deals some damage
define drowningBubble = Skill(name="Drowning Bubble",  power=0, mp_cost=6,     unlocked_atLevel=10, acc=60,  element="water", target="multiple",sfx="", img="") # for easier to flee the scene
define waterBlast = Skill(name="Water Blast",          power=10, mp_cost=8,    unlocked_atLevel=14, acc=90, element="water",  target="single",sfx="", img="") # single target attack
define whisperingSound = Skill(name="Whispering Sound",power=0, mp_cost=12,    unlocked_atLevel=16, acc=95,  element="water", target="single",sfx="", img="") # remove effect single
define dancingStorm = Skill(name="Dancing Storm",      power=10, mp_cost=15,   unlocked_atLevel=18, acc=100,  element="water", target="multiple",sfx="", img="") # splash all enemies plus decreases all enemies accuracy by create Advection Fog
define oceanRhythm = Skill(name="Ocean Rhythm",        power=0, mp_cost=20,    unlocked_atLevel=22, acc=25,  element="water", target="multiple",sfx="", img="") # remove effect all
define roaringTyphoon = Skill(name="Roaring Typhoon",  power=20, mp_cost=25,   unlocked_atLevel=26, acc=100, element="water", target="single",sfx="", img="") # single
define tiamatInferno = Skill(name="Tiamat Inferno",    power=35, mp_cost=49,   unlocked_atLevel=30, acc=50,  element="water", target="single",sfx="", img="") # single
define ultimateSheild = Skill(name="UtimateSheild",    power=0, mp_cost=100,   unlocked_atLevel=35, acc=100,  element="ice", target="multiple",sfx="", img="") # all member immunes for 1 attack. Cost lots of mana, better if cost all man of main char
define absFreezing = Skill(name="Absolute Freezing",   power=40, mp_cost=70,   unlocked_atLevel=40, acc=100,  element="ice", target="multiple",sfx="", img="") # frozen effect, multiple final move of all element name abosulute something + fog to decrease all enermies acc

## ------------------------------------------------------------------- Status dictionary
define status = {
    'wr': 'Well Rested', 
    't': 'Tired',
    'p':'Poison',
    'f': ' Freeze',
    'n': 'Normal'
}

## ------------------------------------------------------------------- Terrain Type dictionary
# buff = Attk +, Acc+, Speed +

# foggy buff water, air. Decreases earth and especially fire
# dought buff fire, light decrease water
# swamp buff dark, earth decreases fire air
# storm buff water, thunder, air, dark debuff fire
# day buff light decreases dark and vice versa
# fight in temple buff light
# snow debuff fire, air
# full moon buff water decrease earth

define terrain = {

}


## ------------------------------------------------------------------- Each char skills
define mainSkills = [liquification, dashingBreeze, drowningBubble, waterBlast, whisperingSound, dancingStorm, oceanRhythm, roaringTyphoon, tiamatInferno, ultimateSheild, absFreezing]
define rivalSkills = [liquification, dashingBreeze, drowningBubble, waterBlast, whisperingSound]

## ------------------------------------------------------------------- Characters
## Good (understable motivation), Priority, Realistic (true to normal life exp), Consistent

#name, speed, agile, defense, state, strength, magic, resistance,level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal", skills=[], exp=0
# Player choose gender. Good at agile and speed at first, later expert in water magic. 
# Trickster/theFool/Explorer archtype, who later become the Magician archtype
##---- Water. 
define main = Protaganist(name="Main", speed = 15, agile=10, defense=5, acc=8, strength=3, magic=14, resistance=14, level=1, 
speedGrowth = 90, agileGrowth=70, defenseGrowth=10, accGrowth=50, strengthGrowth=5, magicGrowth=85, resistanceGrowth=50, maxHpGrowth=100, maxMpGrowth=110,
state = status['wr'],max_hp=24, hp=24, max_mp=15, mp=15, element=elementList["w"][0], skills=mainSkills, exp=90)

# Archtype Orphan/OutCast/Hero. His quest is to capture main char. Eventhough his archtype is Hero, he was in the wrong side of battle field
##---- Void. 67777777Later become sword master type (1 sword)
define rival = Protaganist(name="Rival",speed = 13, agile=4, defense=8, acc=13, strength=10, magic=1, resistance=3, level=1, 
speedGrowth = 20, agileGrowth=10, defenseGrowth=70, accGrowth=30, strengthGrowth=70, magicGrowth=10, resistanceGrowth=8, maxHpGrowth=110, maxMpGrowth=50,
state = status['n'], max_hp=30, hp=30, max_mp=8, mp=8 ,element=elementList["v"][0], attr=[elementList["v"][1]["v"]], skills=rivalSkills, exp=0)

# Archtype Innocent/Caregiver/theLover. Her grandma archtype is theMother/theSage ##---- Light.
# Live alone with her grandma watching over the 3 pyramid and the temple. Used to often play with main char when they are young even though he forget her at first.
define nana = Protaganist(name="Nana",speed = 10, agile=5, defense=1, acc=7, strength=0, magic=13, resistance=10, level=1, 
speedGrowth = 30, agileGrowth=30, defenseGrowth=10, accGrowth=20, strengthGrowth=10, magicGrowth=100, resistanceGrowth=50, maxHpGrowth=30, maxMpGrowth=130,
state = status['wr'], max_hp=24, hp=24, max_mp=22, mp=22 ,element=elementList["v"][0], attr=[elementList["v"][1]["l"]], skills=rivalSkills, exp=0)

# Archtype theLoyalist/Outlaw. Gan means steel/theBoldOne in Mongolian. Dog eat dog style. Can kill without feeling guity, no concept of empathy, but listen to main char. Not kill anymore since main char told him not to
##---- Fire. Can also use smoke skills at first. Later plasma. Rare case: 2 attr
define gan = Protaganist(name="Gan",speed = 4, agile=4, defense=16, acc=5, strength=13, magic=1, resistance=0, level=1, 
speedGrowth = 7, agileGrowth=5, defenseGrowth=40, accGrowth=20, strengthGrowth=100, magicGrowth=5, resistanceGrowth=30, maxHpGrowth=130, maxMpGrowth=20,
state=status['t'], max_hp=36, hp=36, max_mp=4, mp=4 ,element=elementList["f"][0], attr=[elementList["f"][1]["m"]], skills=rivalSkills, exp=0)

# Archtype theMystic/Caregiver(but doesn't want anyone to know) -> detached, cold, frigid and mean at first but had a warm heart. The only demi human alive
##---- Air.
define sabrina = Protaganist(name="Sabrina",speed = 8, agile=4, defense=6, acc=11, strength=5, magic=8, resistance=13, level=1, 
speedGrowth = 30, agileGrowth=20, defenseGrowth=20, accGrowth=30, strengthGrowth=15, magicGrowth=30, resistanceGrowth=30, maxHpGrowth=60, maxMpGrowth=120,
state=status['t'], max_hp=28, hp=28, max_mp=9, mp=9 ,element=elementList["a"][0], attr=[elementList["a"][1]["d"]],skills=rivalSkills, exp=0)

# Archtype theHuntress/FemaleFatal. Laughs when shooting, enjoy fighting. Poised
# Looks very confident and cool. Brigid means 'exalted one' from Old Irish
##---- Thunder.
define brigid = Protaganist(name="Brigid",speed = 13, agile=5, defense=10, acc=9, strength=8, magic=6, resistance=9, level=1, 
speedGrowth = 25, agileGrowth=10, defenseGrowth=50, accGrowth=40, strengthGrowth=70, magicGrowth=70, resistanceGrowth=40, maxHpGrowth=30, maxMpGrowth=20,
state=status['n'], max_hp=26, hp=26, max_mp=12, mp=12 ,element=elementList["a"][0], attr=[elementList["a"][1]["h"]], skills=rivalSkills, exp=0)

# Archtype Underdog/Maiden/Damsel. Dark past. Aria means melody. In Rival's troop of twenty people looking to capture main char.
##---- Earth (moist). Rare case: Cold(Metal) weapon manipulation (metal shoot out from earth to formed into metal weapon)
define aria = Protaganist(name="Aria",speed = 7, agile=2, defense=6, acc=7, strength=10, magic=1, resistance=2, level=1, 
speedGrowth = 30, agileGrowth=5, defenseGrowth=60, accGrowth=40, strengthGrowth=50, magicGrowth=10, resistanceGrowth=50, maxHpGrowth=80, maxMpGrowth=50,
state = status['n'],max_hp=30, hp=30, max_mp=8, mp=8 ,element=elementList["e"][0], attr=[elementList["e"][1]["c"]],skills=rivalSkills, exp=0)

# Archtype theMagician/Alchemist/Jester -> like to troll. Ex: Level up when main char level up, learn new skills when main char does. Not appear in last battle. Out of battle with reason 'Tired' when hp becomes 0 but seems un-damaged and looks well
# Loner and Lazy archtype also, the only demon still alive, live alone in a ruin castle. But when travel together, he turns to a troll, but also a mentor/guidance. If ending with no one, he will guide main char to the legandary Blue Mage's path
##---- Dark (debuff). Super high in Magic, MP, Agile, HP, Acc. Low in the rest
define demonKing = Protaganist(name="Rick",speed = 10, agile=8, defense=7, acc=8,strength=6, magic=9, resistance=3, level=1, 
speedGrowth = 40, agileGrowth=40, defenseGrowth=40, accGrowth=50, strengthGrowth=5, magicGrowth=70, resistanceGrowth=50, maxHpGrowth=50, maxMpGrowth=50,
state = status['t'],max_hp=32, hp=32, max_mp=8, mp=8 ,element=elementList["v"][0], attr=[elementList["v"][1]["d"]],skills=rivalSkills, exp=0)

#### ---------- should be empty when in game (when game start)
define usableProtaganistAsideFromMain = [rival, nana, gan, sabrina, brigid, aria, demonKing]
#### Group party members in a fight. Here it'll save previous choice
default protaganistsInThisFight = [main]

## ------------------------------------------------------------------- Monsters
define skeleton = Enemy(name = "Skeleton", speed = 8, agile=6, defense=4, strength=5, magic=8, resistance=5, acc=6, 
speedGrowth = 40, agileGrowth=40, defenseGrowth=60, accGrowth=10, strengthGrowth=50, magicGrowth=80, resistanceGrowth=60, maxHpGrowth=80, maxMpGrowth=90,
state= status['n'], level=1, max_hp=12, hp=12, max_mp=0, mp=0, element=elementList["a"][0], attr=[elementList["a"][1]["d"]])

define bandit = Enemy(name = "Bandit", speed = 8, agile=6, defense=4, strength=5, magic=8, resistance=5, acc=6, 
speedGrowth = 40, agileGrowth=40, defenseGrowth=60, accGrowth=10, strengthGrowth=50, magicGrowth=80, resistanceGrowth=60, maxHpGrowth=80, maxMpGrowth=90,
state= status['n'], level=1, max_hp=12, hp=12, max_mp=0, mp=0, element=elementList["a"][0], attr=[elementList["a"][1]["d"]])

define enemiesTypeList = [skeleton]
define enemiesList = [skeleton]

## ------------------------------------------------------------------- Protaganist default team



# The game starts here.

label start:
    scene moon: 
        zoom 0.5
        yoffset -100

    call chooseWhoToFightWith
    call battle

    return
