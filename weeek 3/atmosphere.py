def main():
        layer = input("Descent atmosphere layer: ")
        if layer == "Exosphere":
            print("Your altittude will be between 700–10,000 km")


        elif layer == "Thermosphere":
            print("Your alttitude will be between 85–700 km")

        elif layer == "Mesosphere":
            print("Your alttitude will be between 50–85 km")

        elif layer == "Stratosphere":
            print("Your alttitude will be between 12–50 km")
        elif layer == "Troposphere":
            print("Your alttitude will be between 0–12 km")
        else:
            print("Invalid option")


        altitude = float(input("Enter exact alttitude: "))
        if altitude >= 700:
                (print(altitude - 700 /  2, "Total descent time"))

        elif altitude >= 85:
                     print(altitude - 85 /  0.5 , "Total descent time")
        elif altitude >= 50:
                    print(altitude - 50 /  0.2 , "Total descent time")
        elif altitude >= 12:
                    print(altitude - 12 /  0.075, "Total descent time")
        elif altitude > 0:
                    print(altitude * 1000 /  20 , "Total descent time")

















if __name__=="__main__":
    main()
