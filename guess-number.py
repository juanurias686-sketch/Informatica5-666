import random
def main():



        name = input("Whats your name?: ")
        dif = input("Select a dificult, Easy, Medium or Hard: ").title().strip()
        if dif == "Easy":
            print(f"Well,{name}, I am thinking of a number between 1 and 100")



        number = random.randint(1,100)
        guess = int(input("Take a guess: "))


        while guess != number:







                if guess > number:
                    print("You retard, too high")
                elif guess < number:
                    print("You retard, too low")



                guess = int(input("Try again: "))

                if guess == number:
                    print(f"Good job, {name} You guessed my number!")

                    break

























if __name__=="__main__":
    main()

