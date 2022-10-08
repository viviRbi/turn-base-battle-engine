# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image white = Solid("#fff")
define p1 = Protaganist(name="Player",level=1, max_hp=12, hp=9, max_mp=8, mp=8, strength=3,element="Water", attack=0,attack_max=0, exp=90)


# The game starts here.

label start:
    scene bg room
    show eileen happy

    e "Hi, let's start the battle."

    jump battle

    return
