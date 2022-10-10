label battle:

    call set_up

    ## logic here
    $ protaganists = [p1,p2]
    $ enemies = [skeleton_fire]
    $ turnList = TurnList(protaganists,enemies)
    $ turn = 1
    $ whoseTurn = turnList.participants[turn-1]



    call screen FightingScreen

    return

label nextTurn:
    if turn > len(turnList.participants):
        $whoseTurn =  turnList.participants[turn % len(turnList.participants)-1]
    else: 
        $ whoseTurn = turnList.participants[turn-1]
    return





