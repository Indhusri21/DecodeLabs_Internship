to_do_list = []

def menu():
    print("----------TO-DO LIST----------")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. EDIT TASK")
    print("4. DELETE TASK")
    print("5. EXIT TASK")
    print("===============================")

while True:
    menu()
    try:
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    if choice == 1:
        new_task = input("New task: ")
        to_do_list.append(new_task)
        print("--NEW TASK CREATED SUCCESSFULLY--")

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


    elif choice==5:
        print("EXITING TASK")
        break

    else:
        print("Choose valid number from 1-5:")