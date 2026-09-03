import random
def main():





        name = input("Whats your name?: ")
        guess = float(input (f"Well,{name}, I am thinking of a number between 1 and 100 Take a guess: "))
        number = random.randint(1,100)

        while guess != number:

        if guess >= number:
              print("You retard, too high")
        elif guess <= number:
              print("You retard, too low")





if __name__=="__main__":
    main()

