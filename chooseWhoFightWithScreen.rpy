
screen ChooseWhoToFightWithScreen:
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        xsize 50*config.screen_width/100
        ysize 40*config.screen_height/100
        # https://www.renpy.org/doc/html/screen_actions.html
        $gridRows =  len(usableProtaganistAsideFromMain)/4 if len(usableProtaganistAsideFromMain)%2 ==0 else len(usableProtaganistAsideFromMain)/4 + 1
        text "Available party members" xalign 0.5
        grid 4 gridRows yoffset 50:
            spacing 10
            for member in usableProtaganistAsideFromMain:
                frame:
                    xpadding 0
                    ypadding 0
                    xsize 120
                    ysize 50
                    xalign 0.0
                    yalign 0.0
                    background Solid("#00000000")
                    textbutton "[member.name]" action [ ToggleSetMembership(protaganistsInThisFight, member) , Notify(member.name)] 
                    textbutton "{size=12}Status{/size}" action Show("StatusScreen", member=member) xalign 0.0 yalign 1.0
            if len(usableProtaganistAsideFromMain)%2 ==1:
                text ""
        textbutton "Done" xalign 1.0 yalign 1.0 action Jump("battle")

# name,speed, agile, defense, state, strength, magic, acc, resistance, level,max_hp,hp, max_mp, mp, element, attr, exp
screen StatusScreen(member=member):
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        xsize 70*config.screen_width/100
        ysize 60*config.screen_height/100
        
        text "___________________________" xalign 0.0
        text "[member.name]" xalign 0.5
        text "___________________________" xalign 1.0

        text "{size=12}Lvl: [member.level]{/size}" xalign 1.0 yoffset 30
        text "{size=12}Exp: [member.exp]/100{/size}" xalign 0.0 yoffset 30
        text "{size=12}Ele: [member.element]{/size}" xalign 0.5 yoffset 30 xoffset -40
        text "{size=12}Attr: {/size}" xalign 0.5 xoffset 20 yoffset 30
        $attrOffset = 50
        for i in member.attr:
            text "{size=12}[i]{/size}" xoffset attrOffset yoffset 30 xalign 0.5
            $attrOffset +=30

        text "{size=15}Max HP:    [member.max_hp]{/size}" yoffset 70 
        text "{size=15}Max MP:    [member.max_mp]{/size}" yoffset 110
        text "{size=15}Strength:   [member.strength]{/size}" yoffset 150
        text "{size=15}Magic:        [member.magic]{/size}" yoffset 190
        text "{size=15}Speed:        [member.speed]{/size}" yoffset 230

        text "{size=15}State:          [member.state]{/size}" yoffset 70 xoffset 150
        text "{size=15}Accuracy:      [member.acc]{/size}"  yoffset 110 xoffset 150
        text "{size=15}Agile:            [member.agile]{/size}" yoffset 150 xoffset 150
        text "{size=15}Defense:       [member.defense]{/size}" yoffset 190 xoffset 150
        text "{size=15}Resistance:   [member.resistance]{/size}" yoffset 230 xoffset 150
        textbutton "Back" xalign 1.0 yalign 1.0 action Hide("StatusScreen")
