#add tasks to the "to do list"
#mark the ones that accomplished as "marked as done" >>> you can also use "termcolor" module
#remove tasks user wants


counter=0
def add():
    global counter
    while True:
        to_do=input("Enter the task: ")
        counter+=1
        with open("to_do_list.txt","a",encoding="utf-8") as list:
            list.write(f"\n{counter}: {to_do}")

        choose=int(input(f"\n{1}-Keep adding tasks\n{2}-Main menu\n"))
        if choose==1:
             continue
        else: break


def mark():
    from termcolor import colored
    number=input("Enter task number you want to mark: ").strip()
    with open("to_do_list.txt", "r", encoding="utf-8") as list:
            lines = list.readlines()
            modified=[]

            for line in lines:
                 line_task_number=line.split(":")[0].strip()  # Extract the task number from each line
                 if number==line_task_number:
                      marked_task=colored(line.strip(),"black","on_green",attrs=["bold"])  # Mark the task as done using termcolor
                      modified.append(f"{marked_task}\n")
                 else:
                    modified.append(line)


    with open("to_Do_list.txt", "w", encoding="utf-8") as list:
            list.writelines(modified)
    print(f"Task '{number}' marked as done!")        


def remove():
    delete=input("Enter task number you want to delete: ").strip()
    with open("to_do_list.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if delete not in line]
            print(f"Task '{delete}' has been removed!")

    with open("to_do_list.txt", "w", encoding="utf-8") as file:
            file.writelines(modified_lines)

def display():
     with open("to_do_list.txt","r",encoding="utf-8") as list:
        print(list.read())
     

while True:
    opt=int(input(f"\n{1})Add a new task\n{2})Mark as done\n{3})Remove a task\n{4})Display whole list\n{5})Exit\n"))

    if opt==1:
        add()
    elif opt==2:
        mark()
    elif opt==3:
        remove()
    elif opt==4:
        display()
    else:
        print("Closing...")
        break
