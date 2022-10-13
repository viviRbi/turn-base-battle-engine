label chooseWhoToFightWith:
    "Who will join this fight with you?"
    call screen ChooseWhoToFightWithScreen
    return

label battle:
    ## logic here
    "Let's go!"
    call setup
    call screen FightingScreen
    return

label setup:
    $ protaganists = protaganistsInThisFight
    $ enemies = [skeleton_fire]
    $ turnList = TurnList(protaganists,enemies)
    $ turn = 1
    $ whoseTurn = turnList.participants[turn-1]

    python:
        for skill in main.skills:
            if main.level >= skill.level_unlocked:
                skill.usable = True





