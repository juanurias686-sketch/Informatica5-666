def main():
    not_validated = True #initialization
    number = [1,2,3,4,5,6,7,8,9,10]

    while not_validated: #condition
        try:
            int(input("Enter a number between 1 and 10: "))

            if not_validated in number:
                print("Correct answer")
                break

        except ValueError:

            print("You must enter a number between 1 and 10")






if __name__=="__main__":
    main()

