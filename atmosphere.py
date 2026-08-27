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


    altitude = int(input("Enter exact alttitude: "))
    








if __name__=="__main__":
    main()
