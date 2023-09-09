import random

choices = ("rock", "paper", "scissors")
defeators = ("paper", "scissors", "rock")

def generateRand(list):
    choice = random.choice(list)
    return choice 

def main():
    random.seed(None)
    print("Hey! Lets play rock, paper, scissors!\n")
    print("Do you want to choose Rock, Paper, Or Scissors? I promise my choice is random too!\n")

    while True:
        choice = input("Choice: ").lower()

        while True:
            try:
                tuple.index(choices, choice)
                break
            except ValueError:
                choice = input("oooops! that doesnt seem like a proper choice! Try again: ").lower()
                continue
        
        # get AIchoice
        AIchoice = generateRand(choices)
        print("I choose", AIchoice)
        
        # get the index
        index = tuple.index(choices, choice)

        if (choice == AIchoice):
            print("oooooo a Draw! What will you do now?")
        elif (defeators[index] == AIchoice):
            print("oooooo! you lose!")
        else:
            print("faiyaaaaa pasta! I lost")

        replay = input("Would you like to play again?[y/n] ").lower()

        while True:
            if (replay == "y"): break
            elif (replay == "n"): return
            else: replay = input("what was that?[y/n]")


if __name__ == "__main__":
    main()