# Define the main function
#Make a txt file for the word
#make a function for the game
#create a variable inside the game function
#assign the txt function for the game function
#make an input to guess the word
#use len function to count the letters
#make a number of attempts
#make a while loop and an if to came back to the word
 #call the main function


import random
def main():

    words("hangwords.txt")

def words (file):
    with open(file) as hangwords:
        content = hangwords.read().splitlines()
    word1 = random.choice(content)
    print("This is your word: ")
    count = len(word1)
    content = ["_"] * count
    print(" ".join(content))

    while True:
        guess = input("Take a guess: ")

        if len(guess) == 1:
            break
        else:
            print("You retard")




if __name__=="__main__":
    main()
