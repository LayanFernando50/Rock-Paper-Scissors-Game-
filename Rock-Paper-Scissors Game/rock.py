while True:
    user1 = input('Select your choice rock, paper, or scissors:')
    user2 = input('Select your choice rock, paper, or scissors:')

    print("Here are the Rules\n"
          "1: Rock beats Scissors\n"
          "2: Scissors beat Pape\n"
          "3: Paper beats Rock.\n"
          "4: If both players choose the same option, it’s a tie")

    if user1 == user2:
        print('declare a tie.')

    elif user1 == "rock":
        if user2 == "scissors":
            print('User 1 winds')

        else:
            print('User 2 wins')

    elif user1 == "scissors":
        if user2 == "paper":
            print('User 1 winds')

        else:
            print('User 2 winds')

    elif user1 == "paper":
        if user2 == "rock":
            print('User 1 winds')

        else:
            print('User 2 winds')

    replay = input('Do you want to play again Yes/No: ')

    if replay == "No":
        break
    else:
        print('Carry On')












