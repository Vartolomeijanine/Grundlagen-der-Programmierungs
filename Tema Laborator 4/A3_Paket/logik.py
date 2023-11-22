def S_S_P_Cases(human_choice, computer_choice):

    if not human_choice == computer_choice:
        if human_choice == "Stein" and computer_choice == "Schere":
            return 1
        elif human_choice == "Stein" and computer_choice == "Papier":
            return 2
        elif human_choice == "Schere" and computer_choice == "Papier":
            return 1
        elif human_choice == "Schere" and computer_choice == "Stein":
            return 2
        elif human_choice == "Papier" and computer_choice == "Stein":
            return 1
        elif human_choice == "Papier" and computer_choice == "Schere":
            return 2
    else:
        return 0


def S_S_P_Reset(human_score, computer_score):
    
    human_score = 0
    computer_score = 0