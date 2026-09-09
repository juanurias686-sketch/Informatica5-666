import time
def main():
    r = 0

    while r == 0:
        p = input("Have you read the scriptures?: ").strip().lower()
        if p=="no":
            print("Time to read the scriptures")
            time.sleep(1)
            print("Program continues after 24 hours....")
            time.sleep(24*60*60)
            print("Program continues after another 24 hours.")
            r += 1
        elif p == "yes":
            print("Good Job")
            break


if __name__=="__main__":
    main()
