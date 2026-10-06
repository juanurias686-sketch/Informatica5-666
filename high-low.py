def main():

    def highest(a, b):


        if a > b:
            print(f"The highest number entered is A {a}")
        else:
            print(f"The highest number entered is B {b}")


    num1 = float(input("Enter A value: "))
    num2 = float(input("Enter B value: "))


    highest(num1, num2)




    def lowest(a, b, c):


            if a < b < c:
                print(f"The lowest number entered is A {a}")
            elif b < a < c:
                print(f"The lowest number entered is B {b}")
            else:
                 print(f"The lowest number entered is C {c}")


    num1 = float(input("Enter A value: "))
    num2 = float(input("Enter B value: "))
    num3 = float(input("Enter C value: "))


    lowest(num1, num2, num3)

















if __name__=="__main__":
    main()
