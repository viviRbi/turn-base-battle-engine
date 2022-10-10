screen FightingScreen:
    text "{size=14}Turn: [turn]{/turn}    [whoseTurn.name]'s turn"
    frame:
        xpadding 20
        ypadding 20
        xalign 0.0
        yalign 1.0
        xsize 30*config.screen_width/100
        ysize 25*config.screen_height/100
        frame:
            add Solid("#fff") 
            text "{color=#0000ffff}hero stats, face{/color}"
            xpadding 5
            ypadding 5
            xsize 80 
            ysize 80
        text "{size=14}Attr [p1.element]{/size}" yalign 1.0 xalign 0.0  ypos 110 xpos 0 
        text "HP   [p1.hp]/[p1.max_hp]" yalign 0.0 xalign 0.0 xpos 100
        text "MP   [p1.hp]/[p1.max_hp]" yalign 0.5 xalign 0.0 xpos 100
        text "Well rested" yalign 1.0 xalign 0.0 xpos 100
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 70*config.screen_width/100
        ysize 25*config.screen_height/100
        textbutton "Block" yalign 0.0 action Jump("blockAttack")
        textbutton "Flee" yalign 0.5 action Jump("fleeTheFight")
        textbutton "Attack" yalign 0.0 xoffset 90 action Show("attackSkill")
        textbutton "Item" yalign 0.5 xoffset 90 action Show("itemScreen")

screen AttackSkill:
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 50*config.screen_width/100
        ysize 25*config.screen_height/100
        # skill library then loop
        textbutton "Water Slash" yalign 0.0 action Hide("attackSkill"), Show("selectWhoToAttack")
        textbutton "Ice lance" yalign 0.5 action Show("selectWhoToAttack")
screen SelectWhoToAttack:
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 50*config.screen_width/100
        ysize 25*config.screen_height/100
        text "Select who to attack?" xalign 0 yalign 0

label blockAttack:
    call endTurn
    return

label endTurn:
    $ turn +=1
    "Blocked"
    call nextTurn
    call screen FightingScreen


    

