from datetime import datetime
def main():

    day = datetime.now().weekday()
    days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
    print(days [day])



    if day <= 4:
        print("Its a weekday")
        remaining = 5 - day
        print(f"{remaining} days remaining for weekend")
    elif day == 4:
        print("Its friday!")
        print("Just a day left until the weekend")
    else:
        print("Its weekend")




    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #print ("These are summer months")
    #print(months [5] )
   # print(months [6] )
   # print(months [7] )

    seasons = ["Winter", "Spring" , "Summer" , "Autunm"]

    month = datetime.now().month

    if month <= 2 or month == 12:
        season = 0

    elif month <= 5:
        season = 1

    elif month <= 8:
        season = 2

    else:
        season = 3

    print("It is", seasons[season])
    print("It is" , months[month-1])





if __name__=="__main__":
    main()
