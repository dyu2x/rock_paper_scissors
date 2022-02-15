import random
options = ['Rock', 'Paper', 'scissors']

def scores():
    print(f"\nPlayer's score is {my_score}")
    print(f"AI's score is {ai_score}")


def end():
    end_game = input("\nPress Q to quit, any keys to continue :")
    print("")
    if end_game == "q" or end_game == "Q":
        print("Closing game...")
        exit()


print(f"\n\nLet's play {options[0]}, {options[1]}, and {options[2]}")

while True:

    ai_score = 0
    my_score = 0

    best_of = input("Best of: ")
    print("")
    winning_score = (int(best_of) // 2) + 1

    while ai_score < winning_score and my_score < winning_score:
        ai_hand = random.choice(options)

        print(f"1. {options[0]}")
        print(f"2. {options[1]}")
        print(f"3. {options[2]}")
        print(f"Q to Exit")
        print("")

        while True:
            my_hand = input((f"{options[0]}, {options[1]}, {options[2]}, shoot: "))
            if my_hand == "1" or my_hand.lower() == options[0].lower():
                my_hand = options[0]
                break
            if my_hand == "2" or my_hand.lower() == options[1].lower():
                my_hand = options[1]
                break
            if my_hand == "3" or my_hand.lower() == options[2].lower():
                my_hand = options[2]
                break
            if my_hand == "Q" or my_hand == "q":
                print("Closing program...")
                exit()
            else:
                print("Unknown hand.")
        print(f"\nYou chose {my_hand}")
        print(f"Computer chose {ai_hand}")

        while True:
            if ai_hand == my_hand:
                print("it's a tie!")
                scores()
                break
            if ai_hand == options[0] and my_hand == options[1]:
                my_score = my_score + 1
                print("Player won")
                scores()
                break
            if ai_hand == options[0] and my_hand == options[2]:
                ai_score = ai_score + 1
                print("AI won")
                scores()
                break
            if ai_hand == options[1] and my_hand == options[0]:
                ai_score = ai_score + 1
                print("AI won")
                scores()
                break
            if ai_hand == options[1] and my_hand == options[2]:
                my_score = my_score + 1
                print("player won")
                scores()
                break
            if ai_hand == 'scissors' and my_hand == options[0]:
                my_score = my_score + 1
                print("player won")
                scores()
                break
            if ai_hand == options[2] and my_hand == options[1]:
                ai_score = ai_score + 1
                print("AI won")
                scores()
                break
    if ai_score > my_score:
        print('AI won!')
        end()
    else:
        print('You won!')
        end()
