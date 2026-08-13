def main():
    # planet = input("Planet:")

    # # Separation
    # print("Hello", planet)

    # # Concatenation
    # print("Hello " + planet)

    # #Formated Strings
    # print(f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().
    adjetive = input("say an adjetive: ").strip()
    goal = input("A goal you would like to achieve: ").strip().

    print(f"Hello, {name}!", end="\n\n")

    print("This is yor story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today I will finally {goal}.")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today I will finally {goal}.".upper())






if __name__=="__main__":
    main()
