def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))
        ala = True
        while ala:
            try:

                times_table = input("Enter a number(1 to 10 or exit): ").lower().strip()
                ala = False
            except ValueError:
                print("Invalid")


    alan = True
    while alan:

        try:
            maxvalue = int(input("Enter maximum value for the times table: "))
            ala = False
        except ValueError:
                print("Invalid")




                print(f"Here is the {times_table} times table")


                for x in range(1,maxvalue + 1):
                    answer = x * int(times_table)
                    int(input(f"{x} times {times_table} is.....: "))







if __name__=="__main__":
    main()
