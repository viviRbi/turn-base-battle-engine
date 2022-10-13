
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

screen StatusScreen(member=member):
    frame:
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        xsize 70*config.screen_width/100
        ysize 60*config.screen_height/100
        text "Name: [member.name]"
        text "Speed: [member.speed]" yoffset 40
        textbutton "Back" xalign 1.0 yalign 1.0 action Hide("StatusScreen")
