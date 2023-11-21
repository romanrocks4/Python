import random

# This is creating the bounderies for the number guessing game
Lower = int(input("Enter lowest number to guess "))
Higher = int(input("Enter highest number to guess "))

# This is establishing the variables
Guess = 0
Counter = 0
Highscore_list = {}

menu = [
    "Romans number game!!",
    "1.Start",
    "2.See highscores",
    "3.Exit"
]

Game = True

# This adds the usser and their highscore to the highscore list
def add_user(Name, Counter):
    
    #Highscore_list.update({"Name": Name, "Counter": Counter})

    Highscore_list[Name] = Counter




while Game:
    # This is generating the the random number and printing the menu to choose from
    Number = random.randint(Lower, Higher)
    
    for menuItem in menu:
        print( menuItem )

    Choice = int(input("Enter your choice:"))

    if Choice == 1:
        # This is looping the game until the player guesses correct
        while ( Number != Guess):

           
            Guess = int(input("Enter your guess :"))
           # This is making sure the player does not guess outside of the number bounderies
            if Guess < Lower :
                print ("Please enter a number within the range")

            elif Guess > Higher :
                print ("Please enter number within the range")

            # This tells the player that their guess is incorrect and tells them if it is lower or higher than the correct guess
            elif Guess < Number :
                print ("your guess is too low")
                Counter = Counter + 1

            elif Guess > Number :
                print ("you guess is too high")
                Counter = Counter + 1

       # this tells the player that they have guessed correctly adds them to the highscore list and resets the guess and counter to 0
        Counter = Counter + 1
        print ("Congrats!! you did it in", Counter,"tries!!")
        
        Name = str(input("Enter your name:"))
        add_user(Name, Counter)

        Guess = 0
        Counter = 0
        Name = 0

    elif Choice == 2:
        # this prints the highscore list
        print (Highscore_list)

    # this ends the program
    elif Choice == 3:
        print ("Goodbye!!") 
        Game = False

    #this catches any invalid choices
    else:
        print("invaild! Pick 1 2 or 3")