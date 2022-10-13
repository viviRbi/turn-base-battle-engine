label chooseWhoToFightWith:
    "Who will join this fight with you?"
    call screen ChooseWhoToFightWithScreen
    return

label battle:
    ## logic here

    $ protaganists = protaganistsInThisFight
    $ enemies = [skeleton_fire]
    $ turnList = TurnList(protaganists,enemies)
    $ turn = 1
    $ whoseTurn = turnList.participants[turn-1]

    python:
        for skill in main.skills:
            if main.level >= skill.level_unlocked:
                skill.usable = True

    call screen FightingScreen
    return

label nextTurn:
    if turn > len(turnList.participants):
        $whoseTurn =  turnList.participants[turn % len(turnList.participants)-1]
    else: 
        $ whoseTurn = turnList.participants[turn-1]
    return





