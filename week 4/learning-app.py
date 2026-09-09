import random
def main():
    print("Welcome to this learning app")
    streak = 0
    message = ("You got a star ⭐")
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)



    print(f"Try to do this {n1}+{n2}")
    ans = int(input("Type your answer: "))

    while ans != n1 + n2:


        if ans != n1 + n2:
         print("Thats not the correct answer")

         ans = int(input("Try again: "))

         if ans == n1 + n2:
            print("You did it!")

        if ans == n1 + n2:
            print(f"{message}")


            break













if __name__=="__main__":
    main()
