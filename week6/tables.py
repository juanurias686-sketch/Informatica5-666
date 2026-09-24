def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))

    while True:

        times_table = input("Enter a number(1 to 10 or exit): ").lower().strip()


        if times_table == "exit":
            break


        elif times_table in valid_nums:
            maxvalue = int(input("Enter maximum value for the times table: "))


            print(f"Here is the {times_table} times table")


            for x in range(1,maxvalue + 1):
                answer = x * int(times_table)
                print(f"{x} times {times_table} is {answer}")
        else:
            print("Invalid command.")




















if __name__=="__main__":
    main()
