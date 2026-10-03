def main():
    name = input("Enter your name: ")

    print(f"Welcome {name} to the times table quiz")


    while True:
        try:
            times_table = int(input("Enter Enter a number(1 to 10): "))

            if 1 <= times_table <= 10:
                break
            
            else:
                print("The number should be between 1 and 10")

        except ValueError:
            print("You MUST enter a number between 1 and 10")


    while True:
        try:
            max_value = int(input("Enter the max value for the times table: "))

            if max_value > 0:
                break
            else:
                print("The number should be positive")

        except ValueError:
            print("You MUST enter a number")

    max_value += 1

    print(f"Here is your test on the {times_table} times table")

    score = 0


    for i in range(1, max_value):
        correct_answer = i * times_table

        print(f"{i} times {times_table} is ...")

        while True:
            try:
                user_answer = int(input("Answer: "))
                break
            except ValueError:
                print("It should be a NUMBER")

        if user_answer == correct_answer:
            print("Correct")
            score += 1
        else:
            print("You retard")

    print(f"Quiz finished! You got {score} out of {max_value - 1} nice job")


if __name__ == "__main__":
    main()
