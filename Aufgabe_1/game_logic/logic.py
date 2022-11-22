def logicGame(playerOption, computerOption):
    """
    This function contains the game logic and what it returns when different options are picked
    :param playerOption: represents the input of the user
    :param computerOption: represents the random or automated input of computer
    :return: returns different numbers when different outcomes happen
    """
    if playerOption == computerOption:
        return 3

    match playerOption:
        case 1:
            """
            The player has chosen rock
            """
            if computerOption == 2:
                return 2
            return 1

        case 2:
            """
            The player has chosen paper
            """
            if computerOption == 3:
                return 2
            return 1

        case 3:
            """
            The player has chosen scissors
            """
            if computerOption == 1:
                return 2
            return 1