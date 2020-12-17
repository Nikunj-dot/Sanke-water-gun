print("Welcome to number guessing game")
n = 18
number_of_guesses = 1
print("Number of guesses is only till 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number: \n"))
    if guess_number<18:
        print("you entered smaller number, please input greater number.\n")
    elif guess_number>18:
        print("you have entered greater number, please input smaller number")
    else:
        print("you won\n")
        print(number_of_guesses, "no.guesses he took to finish.")
        break
        print("9= number_of_guesses", "no. of guesses left")
        if(number_of_guesses>9):
            print("Game over")