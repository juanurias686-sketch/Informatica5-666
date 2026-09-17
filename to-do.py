def main():

    tasks = []
    command = ""


    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ")

        if command == "exit":
                    break


        elif command == "add":
            new_task = input ("Enter new task: ")
            tasks.append(new_task)
            




        elif command == "complete":
            complete = input("Enter complete task: ")
            tasks.remove(complete)











if __name__=="__main__":
    main()
