def main():

    tasks = []
    command = ""


    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ")
        if command == "add":
            new_task = input ("Enter new task: ")
            tasks.append(new_task)

        elif command == "complete":
            complete = int(input("Select completed task (starting from 0): " ))
            tasks.remove({complete})
            print(tasks)




if __name__=="__main__":
    main()
