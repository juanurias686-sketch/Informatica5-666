def main():
    print("Binary to Decimal Converter")
    print("The purpose of this program is to make you known the value of a binary code in understandable numbers" )
    bin = input("Type a binary code: ")
    bin_to_dec(bin)





def bin_to_dec(num):
    dec = 0
    size = len(num)

    for i in range(size):

        bit = int(num[size - 1 - i])
        dec += bit * (2 ** i)

    print(f" The binary code {num} in decimal: {dec}")














if __name__=="__main__":
    main()
