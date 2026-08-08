to_do_list = []

def menu():
    print("\n========= TO-DO LIST =========")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. EDIT TASK")
    print("4. DELETE TASK")
    print("5. SEARCH TASK")
    print("6. COMPLETED TASK")
    print("7. EXIT TASK")
    print("===============================")

while True:
    menu()
    try:
        choice = int(input("Choose an option (1-7): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    if choice == 1:
        new_task = input("New task: ").strip()
        if new_task:
            to_do_list.append(new_task)
            print("--NEW TASK CREATED SUCCESSFULLY--")
        else:
            print("Task cannot be empty!")

    elif choice==2:
        if not to_do_list:
            print("YOUR TO-DO LIST IS EMPTY.")
        else:
            print("\nYOUR TASKS:")
            for index, item in enumerate(to_do_list, start=1):
                print(f"{index}. {item}")

    elif choice == 3:
        if not to_do_list:
            print("YOUR TO-DO LIST IS EMPTY. Nothing to edit.")
            continue
        print("1. RENAME\n2. EDIT TASK")
        option = int(input("Enter an option (1 / 2):"))
        
        if option==1 or option==2:
            print("\nYOUR TASKS:")
            for index, item in enumerate(to_do_list, start=1):
                print(f"{index}. {item}")

            edit_task_no = int(input("Enter task no to edit:"))
            task_no = edit_task_no - 1
            
            if 0 <= task_no < len(to_do_list):
                if option == 1:
                    new_name = input("Enter new task name:")
                    to_do_list[task_no] = new_name
                    print("--TASK NAME UPDATED SUCCESSFULLY!--")

                if option == 2:
                    extra_detail = input("Enter extra text to add: ")
                    to_do_list[task_no] = to_do_list[task_no] + " - " + extra_detail
                    print("--TASK EDITED SUCCESSFULLY!--")

    elif choice == 4:
        
        if not to_do_list:
            print("YOUR TO-DO LIST IS EMPTY.")
        else:
            print("\nYOUR TASKS:")
            for index, item in enumerate(to_do_list, start=1):
                print(f"{index}. {item}")

            del_no = int(input("Delete task no:"))
            del_num = del_no-1
            if 0 <= del_num < len(to_do_list) :
                delete = to_do_list.pop(del_num)
                print("--TASK DELETED SUCCESSFULLY.--")

    elif choice == 5:
        if not to_do_list:
            print("YOUR TO-DO LIST IS EMPTY.")
        else:
            search_word = input("Enter word to search: ")
            found = False
            
            print(f"\nSEARCH RESULTS FOR '{search_word}':")
            for index, item in enumerate(to_do_list, start=1):
                if search_word.lower() in item.lower():
                    print(f"{index}. {item}")
                    found = True
            
            if not found:
                print("No matching tasks found.")

    elif choice == 6:
        if not to_do_list:
            print("YOUR TO-DO LIST IS EMPTY.")
        else:
            print("\nYOUR TASKS:")
            for index, item in enumerate(to_do_list, start=1):
                print(f"{index}. {item}")

            comp_no = int(input("Enter task no to mark as completed:"))
            task_no = comp_no - 1
            if 0 <= task_no < len(to_do_list):
                to_do_list[task_no] = "[DONE] " + to_do_list[task_no]
                print("--TASK MARKED AS COMPLETED!--")

    elif choice==7:
        print("EXITING TASK")
        break

    else:
        print("Choose valid number from 1-7:")