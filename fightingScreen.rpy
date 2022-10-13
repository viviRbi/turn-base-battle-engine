screen FightingScreen:
    text "{size=14}Turn: [turn]{/size}    [whoseTurn.name]'s turn "
    $pos = 30
    # show list of hero team top left vertically
    for i in protaganistsInThisFight:
        $pos +=51
        frame:
            xalign 0.0
            yalign 0.0
            xsize 160
            ysize 50
            yoffset pos
            background Solid("#101000")
            text "{size=14}[i.name] {/size} "
            text "{size=9}[i.state] {/size} " yalign 1.0
            text "{size=14}HP: [i.hp]/[i.max_hp] {/size}" xoffset 60
            text "{size=14}MP: [i.mp]/[i.max_mp] {/size}" xoffset 60 yalign 1.0
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
            text "{size=14}Lvl [whoseTurn.level] [whoseTurn.element]{/size}" yalign 1.0 xalign 0.0  ypos 110 xpos 0 
            text "HP   [whoseTurn.hp]/[whoseTurn.max_hp]" yalign 0.0 xalign 0.0 xpos 100
            text "MP   [whoseTurn.mp]/[whoseTurn.max_mp]" yalign 0.5 xalign 0.0 xpos 100
            text "[whoseTurn.state]" yalign 1.0 xalign 0.0 xpos 100
        frame:
            xpadding 40
            ypadding 20
            xalign 1.0
            yalign 1.0
            xsize 70*config.screen_width/100
            ysize 25*config.screen_height/100
            textbutton "Block" yalign 0.0 action Jump("blockAttack")
            textbutton "Item" yalign 0.5 action Show("ItemScreen")
            textbutton "Flee" yalign 1.0 action [Hide("AttackSkillScreen"), Jump("fleeTheFight")]
            textbutton "Attack" yalign 0.0 xoffset 90 action Jump("endTurn")
            textbutton "Skills" yalign 0.5 xoffset 90 action ToggleScreen("AttackSkillScreen")
    else:
        frame:
            xpadding 0
            ypadding 0
            xalign 0.0
            yalign 1.0
            background Solid("#00000000")
            xsize config.screen_width
            ysize 25*config.screen_height/100 
            
            imagebutton:
                xalign 0.0
                yalign 1.0
                xsize config.screen_width
                focus_mask None
                idle "gui/textbox.png"
                action Jump("enemyAttack")
            text "[whoseTurn.name] attacks." yalign 0.3 xalign 0.5 


screen AttackSkillScreen:
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 50*config.screen_width/100
        ysize 25*config.screen_height/100
        # skill library then loop
        python:
            usableSkills = []
            for skill in whoseTurn.skills:
                if whoseTurn.level >= skill.level_unlocked:
                    usableSkills.append(skill)
        $gridRows =  len(usableSkills)/2 if len(usableSkills)%2 ==0 else len(usableSkills)/2 + 1
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True
            grid 2 gridRows:
                for skill in usableSkills:
                    textbutton "[skill.name]" action Hide("attackSkill"), Show("SelectWhoToAttackScreen")
                if len(usableSkills)%2 ==1:
                    text ""
            

screen SelectWhoToAttackScreen:
    frame:
        xpadding 40
        ypadding 20
        xalign 1.0
        yalign 1.0
        xsize 50*config.screen_width/100
        ysize 25*config.screen_height/100
        text "Select who to attack?" xalign 0 yalign 0
        textbutton "Back" action Hide("SelectWhoToAttackScreen") xalign 0 yalign 0.5

label blockAttack:
    "[whoseTurn.name] blocked the attack."
    call endTurn
    return

label fleeTheFight:
    "[whoseTurn.name] flee the fight."
    "Game reset"
    show white 
    pause .5
    hide white
    call chooseWhoToFightWith

label enemyAttack:
    "[whoseTurn.name] use ABC skill on ABC. ABC lost 10 hp"
    call endTurn
    return

label endTurn:
    $ turn +=1
    call nextTurn
    call screen FightingScreen
    return

label nextTurn:
    if turn > len(turnList.participants):
        $whoseTurn =  turnList.participants[turn % len(turnList.participants)-1]
    else: 
        $ whoseTurn = turnList.participants[turn-1]
    return


    

