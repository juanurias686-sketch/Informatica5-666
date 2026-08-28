def main():
    print("Carniceria Chapala")

    rating = float(input("Rate Carniceria Chapala: "))


    if rating >= 4.5:
        print("Perfection")
    elif rating >= 4:
        print("Excelent")
    elif rating >= 3:
        print("Good")
    elif rating >= 2:
        print("fair")
    else:
        print("Poor")



if __name__=="__main__":
    main()
