def main():

    not_validated = True #initialization

    while not_validated: #condition
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1 and number <= 10:
                print("Success!")
                not_validated = False
            else:
                print("You must enter a number between 1 and 10")
                
        except ValueError:

            print("You must enter a number between 1 and 10")

if __name__=="__main__":
    main()

