def main():
    print("Welcome to the times table quiz")

    # Ask for the times table
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))

            if 1 <= times_table <= 10:
                break
            else:
                print("Invalid command. Enter a number between 1 and 10.")

        except ValueError:
            print("Invalid command. Enter a number between 1 and 10.")

    # Ask for the maximum value
    while True:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))

            if max_value > 0:
                break
            else:
                print("Invalid command. Enter a positive number.")

        except ValueError:
            print("Invalid command. Enter a number.")

    max_value += 1

    print(f"Here is your quiz on the {times_table} times table")

    score = 0

    # Quiz
    for x in range(1, max_value):
        correct_answer = x * times_table

        print(f"{x} times {times_table} is ...")

        while True:
            try:
                user_answer = int(input("Answer: "))
                break
            except ValueError:
                print("Invalid answer. Enter a number.")

        if user_answer == correct_answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")

    print(f"Quiz finished! You got {score} out of {max_value - 1} correct.")


if __name__ == "__main__":
    main()
