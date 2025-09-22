# Im not sure that we haven't done some of the things I used in this lab submission, but this is how I would solve the problem.
# I am a senior Computer Science student, with a lot of experience in Python (my internship this summer was almost 90% programming 
# # in Python) but am taking this class to satisfy a certificate, and like the refresher on the earlier-on techniques. 


tasks = []
def display(tasklist):
    i = 1
    for task in tasklist:
        print(f"{i}. {task}\n")
        i += 1 
        
listStart = input("Would you like to start a list of your tasks? (y/n): ")
if listStart == "y":
    task = input("Enter the task you'd like to accomplish: ")
    tasks.append(task)
    print(f"Added {task} to your list!\n")
    while True:
        choice = input("At this point, you can do any of the following: \n"
                       "1. Add a new task \n"
                       "2. Mark a task as done/Remove it from the list \n"
                       "3. Display the list. \n"
                       "4. Quit \n"
                       "Which would you like to accomplish? (i.e. 1,2,3,4): \n")
        if choice == "1":
            task = input("Enter the task you'd like to accomplish: ")
            tasks.append(task)
            print(f"Added {task} to your list!\n")
        elif choice == "2":
            finished = input("Enter the task you wish to mark as complete: (case sensitive!!!)")
            if finished in tasks:
                tasks.remove(finished)
                print(f"Removed {finished} from your list.\n")
            else:
                print("Task you provided does not match with a task in the list... printing list and Re-prompting ...")
                display(tasks)
        elif choice == "3":
            display(tasks) 
        elif choice == "4":
            print("Goodbye!")
            break
        else: # no valid input
            print("Please select one of the four provided options. Re-prompting ...")
            