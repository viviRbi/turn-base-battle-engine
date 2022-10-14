label chooseWhoToFightWith:
    python:
        main.increaseStatsMultipleLevel(30)
        rival.increaseStatsMultipleLevel(30)
        nana.increaseStatsMultipleLevel(30)
        gan.increaseStatsMultipleLevel(30)
        sabrina.increaseStatsMultipleLevel(30)
        brigid.increaseStatsMultipleLevel(30)
        aria.increaseStatsMultipleLevel(30)
        demonKing.increaseStatsMultipleLevel(30)
    "Who will join this fight with you?"
    call screen ChooseWhoToFightWithScreen
    return

label battle:
    ## logic here
    "Let's go!"
    call setup
    call screen FightingScreen
    # for each exp >= 100, congrats level up then call increaseStatsEachLevel method
    return

label setup:
    $enemiesList=[]
    $ protaganists = protaganistsInThisFight
    call generateEnemies
    $ enemies = enemiesList
    $ turnList = TurnList(protaganists,enemiesList)
    $ turn = 1
    $ whoseTurn = turnList.participants[turn-1]

    python:
        for skill in main.skills:
            if main.level >= skill.unlocked_atLevel:
                skill.usable = True

label generateEnemies:
    $enemiesGenerator = EnemiesGenerator(enemiesTypeList,[])
    $enemiesList = enemiesGenerator.enemiesList
    return


    



