screen FightingScreen:
    text "{size=14}Turn: [turn]{/turn}    [whoseTurn.name]'s turn  [main.skills[0]]" # 
    if type(whoseTurn) == Protaganist:
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
            text "{size=14}Attr [whoseTurn.element]{/size}" yalign 1.0 xalign 0.0  ypos 110 xpos 0 
            text "HP   [whoseTurn.hp]/[whoseTurn.max_hp]" yalign 0.0 xalign 0.0 xpos 100
            text "MP   [whoseTurn.hp]/[whoseTurn.max_hp]" yalign 0.5 xalign 0.0 xpos 100
            text "Well rested" yalign 1.0 xalign 0.0 xpos 100
        frame:
            xpadding 40
            ypadding 20
            xalign 1.0
            yalign 1.0
            xsize 70*config.screen_width/100
            ysize 25*config.screen_height/100
            textbutton "Block" yalign 0.0 action Jump("blockAttack")
            textbutton "Item" yalign 0.5 action Show("itemScreen")
            textbutton "Flee" yalign 1.0 action Jump("fleeTheFight")
            textbutton "Attack" yalign 0.0 xoffset 90 action Jump("endTurn")
            textbutton "Skills" yalign 0.5 xoffset 90 action Show("attackSkill")
    else:
        frame:
            xpadding 0
            ypadding 0
            xalign 0.0
            yalign 1.0
            background Solid("#00000000")
            xsize config.screen_width
            ysize 25*config.screen_height/100 
            
            #image "gui/textbox.png" xsize config.screen_width ysize 50 xalign 0.0 yalign 1.0
            imagebutton:
                xalign 0.0
                yalign 1.0
                xsize config.screen_width
                focus_mask None
                idle "gui/textbox.png"
                action Jump("enemyAttack")
            text "[whoseTurn.name] attacks." yalign 0.3 xalign 0.5 


screen attackSkill:
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 50*config.screen_width/100
        ysize 25*config.screen_height/100
        # skill library then loop

        for skill in main.skills:
            textbutton "[skill.name]" yalign 0.0 xalign 0.0 action Hide("attackSkill"), Show("selectWhoToAttack")
        

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
    "[whoseTurn.name] blocked the attack."
    call endTurn
    return

label enemyAttack:
    "[whoseTurn.name] use ABC skill on ABC. ABC lost 10 hp"
    call endTurn
    return

label endTurn:
    $ turn +=1
    call nextTurn
    call screen FightingScreen
    return


    

