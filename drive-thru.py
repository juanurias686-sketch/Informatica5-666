def main():



    welcome()

    food = input("Choose one thing from the menu from 1 to 5: ")
    get_item(food)



def welcome():

    print("Welcome, here is the menu")
    print("1. Cheeseburger")
    print("2. Fries")
    print("4. Ice Cream")
    print("5. Cookie")


def get_item(food):

    if food == "1":
        print("🍔")
    elif food == "2":
        print("🍟")
    elif food == "3":
        print("🥤")
    elif food == "4":
        print("🍦")
    elif food == "5":
        print("🍪")















if __name__=="__main__":
    main()
