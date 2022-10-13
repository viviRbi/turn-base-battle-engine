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

## ------------------------------------------------------------------- Characters
#name, speed, agile, defense, state, strength, magic, resistance,level=1,max_hp=10,hp=4,max_mp=4,mp=4, element="Normal", skills=[], exp=0
# Player choose gender. Good at agile and speed at first, later expert in water magic. 
# Trickster/theFool/Explorer archtype, who later become the Magician archtype
define main = Protaganist(name="Main", speed = 25, agile=10, defense=5, state= status['wr'], strength=3, magic=25, resistance=20,level=8, max_hp=12, hp=12, max_mp=8, mp=8, element="Water", skills=mainSkills, exp=90)
# Archtype Orphan/OutCast/Hero. His quest is to capture main char. Eventhough his archtype is Hero, he was in the wrong side of battle field
define rival = Protaganist(name="Rival",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype Innocent/Caregiver/theLover. Her grandma archtype is theMother/theSage
# Live alone with her grandma watching over the 3 pyramid and the temple. Used to often play with main char when they are young even though he forget her at first.
define nana = Protaganist(name="Nana",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype theLoyalist/Outlaw. Gan means steel/theBoldOne in Mongolian. Dog eat dog style. Can kill without feeling guity, no concept of empathy, but listen to main char. Not kill anymore since main char told him not to
define gan = Protaganist(name="Gan",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype theMystic/Caregiver(but doesn't want anyone to know) -> detached, cold, frigid and mean at first but had a warm heart. The only demi human alive
define sabrina = Protaganist(name="Sabrina",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype theHuntress/FemaleFatal. Laughs when shooting, enjoy fighting. Poised
# Looks very confident and cool. Brigid means 'exalted one' from Old Irish
define brigid = Protaganist(name="Brigid",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype Underdog/Maiden/Damsel. Dark past. Aria means melody. In Rival's troop of twenty people looking to capture main char.
define aria = Protaganist(name="Aria",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
# Archtype theMagician/Alchemist/Jester -> like to troll. Ex: Level up when main char level up, learn new skills when main char does. Not appear in last battle. Out of battle with reason 'Tired' when hp becomes 0 but seems un-damaged and looks well
# Loner archtype also, the only demon still alive, live alone in a ruin castle. But when travel together, he turns to a troll, but also a mentor/guidance. If ending with no one, he will guide main char to the legandary Blue Mage's path
define demonKing = Protaganist(name="Rick",speed = 7, agile=4, defense=20, state = status['t'], strength=20, magic=3, resistance=3, level=14, max_hp=12, hp=9, max_mp=8, mp=8 ,element="Fire", skills=rivalSkills, exp=0)
#### should be empty when in game (when game start)
define usableProtaganistAsideFromMain = [rival, nana, gan, sabrina, brigid, aria, demonKing]
#### Group party members in a fight. Here it'll save previous choice
default protaganistsInThisFight = [main]

## ------------------------------------------------------------------- Monsters
define skeleton_fire = Enemy(name = "Fire Skeleton", speed = 8, agile=6, defense=4, state= status['n'], strength=5, magic=8, resistance=5, defeatedEarnedExp =5, level=1, max_hp=12, hp=12, max_mp=0, mp=0, element="Mist")

## ------------------------------------------------------------------- Protaganist default team



# The game starts here.

label start:
    scene bg room
    show eileen happy

    e "Hi, let's start the battle."

    call chooseWhoToFightWith
    call battle

    return
