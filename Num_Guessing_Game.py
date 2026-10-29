import random as r

start = 1
end = 10
attempts = 5

games_played = 0
games_won = 0
games_lost = 0
best_score = 0

while True:
    print("<==========================================================================================>")
    print("WELCOME TO WORLD OF NUMBER GUESSING GAME")
    print("<==========================================================================================>")
    print("1 -> PLAY")
    print("2 -> SETTINGS")
    print("3 -> HOW TO PLAY")
    print("4 -> ACHIEVEMENT")
    print("5 -> EXIT")
    print("<==========================================================================================>")

    try:
        ch = int(input("Enter your Choice: "))
    except:
        print("Invalid Input!")
        continue

    if ch == 1:

        print("<==========================================================================================>")
        print("NUMBER GUESSING GAME")
        print("<==========================================================================================>")

        try:
            rounds = int(input("Enter how many times you want to play: "))

            if rounds <= 0:
                print("Enter a valid number!")
                continue

        except:
            print("Invalid Input!")
            continue

        for i in range(1,rounds+1):

            num = r.randint(start, end)
            won = False

            print("<==========================================================================================>")
            print("ROUND", i)
            print("Guess a number between", start, "and", end)
            print("You have", attempts, "attempts")
            print("<==========================================================================================>")

            for j in range(1, attempts+1):

                try:
                    choice = int(input("Enter your number: "))
                except:
                    print("Enter a valid number!")
                    continue

                if choice == num:

                    print()
                    print("You Won!!!")

                    score = attempts - j + 1
                    print("Score:", score)

                    games_won += 1
                    won = True

                    if score > best_score:
                        best_score = score

                    break

                elif choice < num:

                    print("Too Low!")
                    print("Attempts left:", attempts - j)

                else:

                    print("Too High!")
                    print("Attempts left:", attempts - j)

            if won == False:

                print("<==========================================================================================>")
                print("You Lost!!!")
                print("Correct number:", num)

                games_lost += 1

            games_played += 1

            if i < rounds:

                ch2 = input("Want to Continue (Y/N): ")

                if ch2.upper() != "Y":
                    break

        input("Press ENTER to return to Main Menu...")


    elif ch == 2:

        while True:

            print("<==========================================================================================>")
            print("SETTINGS")
            print("<==========================================================================================>")
            print("1 -> EASY")
            print("2 -> MEDIUM")
            print("3 -> HARD")
            print("4 -> BACK")
            print("<==========================================================================================>")

            choice = input("Enter your choice: ")

            if choice == "1":

                start = 1
                end = 10
                attempts = 5

                print("Difficulty set to EASY")

            elif choice == "2":

                start = 1
                end = 50
                attempts = 5

                print("Difficulty set to MEDIUM")

            elif choice == "3":

                start = 1
                end = 100
                attempts = 3

                print("Difficulty set to HARD")

            elif choice == "4":

                break

            else:

                print("Invalid Choice!")


    elif ch == 3:

        print("<==========================================================================================>")
        print("HOW TO PLAY")
        print("<==========================================================================================>")

        print("1. Select PLAY from the Main Menu.")
        print("2. Enter the number of rounds.")
        print("3. Computer will generate a random number.")
        print("4. Enter your guessed number.")
        print("5. Too Low means your guess is smaller.")
        print("6. Too High means your guess is greater.")
        print("7. Guess correctly to win.")
        print("8. Use all attempts and you lose.")

        input("Press ENTER to return to Main Menu...")


    elif ch == 4:

        print("<==========================================================================================>")
        print("ACHIEVEMENTS")
        print("<==========================================================================================>")

        print("Games Played  :", games_played)
        print("Games Won     :", games_won)
        print("Games Lost     :", games_lost)
        print("Best Score      :", best_score)
        

        print("<==========================================================================================>")

        if games_won >= 1:
            print("First Win")

        if games_won >= 5:
            print("5 Wins")

        if games_won >= 10:
            print("Number Master")

        if games_won == 0:
            print("No achievements yet")
        input("Press ENTER to return to Main Menu...")


    elif ch == 5:
        print("<==========================================================================================>")
        print("Thank You For Playing!")
        print("Good Bye!")
        break


    else:
        print("<==========================================================================================>")
        print("Invalid Choice!")
        print("Please select 1 to 5.")
