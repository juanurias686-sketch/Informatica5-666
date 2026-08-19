def main():
    col=float(input("What do you have left in pesos?"))
    sol=float(input("What do you have left in soles?"))
    reais=float(input("What do you have left in reais?"))

    usd = (col * 0.0032) + (sol * 0.30) + (reais * 0.19)
    mxn = round(usd * 17.07, 2)

    print(f"USD: {round(usd , 2)}")
    print(f"MXN: {mxn}")

if __name__=="__main__":
    main()
