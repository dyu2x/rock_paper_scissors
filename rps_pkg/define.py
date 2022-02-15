def scores(ai_score, my_score):
    print(f"\nPlayer's score is {my_score}")
    print(f"AI's score is {ai_score}")

def end():
    end_game = input("\nPress Q to quit, any keys to continue :")
    print("")
    if end_game == "q" or end_game == "Q":
        print("Closing game...")
        exit()