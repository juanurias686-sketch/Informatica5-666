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
    attempts = 10
    with open(file) as hangwords:
        content = hangwords.read().splitlines()
    word1 = random.choice(content)
    hint = ["_"] * len(word1)
    incorrect_letters = []

    while attempts > 0:
        print("Current word:", " ".join(hint) )


        while True:
            guess = input("Take a guess: ")

            if len(guess) == 1:
                break
            else:
                print("You retard")
        if guess in word1 and guess not in hint:
            for i in range(len(word1)):
                if word1[i] == guess:
                    hint[i] = guess
            print("Great guess")
        elif guess in hint:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
        if guess not in incorrect_letters:
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word1)
        if attempts == 0 and "_" in hint:
            print("No attempts left 💀 The word was:", word1)











if __name__=="__main__":
    main()
