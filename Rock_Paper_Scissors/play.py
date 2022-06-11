import random
is_game = True
while is_game:
    user_action = input(
        "Enter a choice (R for rock, P for paper, S for scissors): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        is_game = False
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
            is_game = False
        else:
            print("Paper covers rock! You lose.")
            is_game = False
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
            is_game = False
        else:
            print("Scissors cuts paper! You lose.")
            is_game = False
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
            is_game = False
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("read the instruction carefully")
