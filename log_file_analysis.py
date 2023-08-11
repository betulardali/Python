#check whether password match after request it.
#record all data (accurate and incorrect) to the list.


from datetime import datetime
import time
from termcolor import colored

counter=0
def correct():
    global counter
    counter+=1
    time=datetime.now()
    correct_name=colored(user_name,"black","on_green", attrs=["bold"])
    
    with open("log_file.txt","a",encoding="utf-8") as list:
        list.write(f"\n{counter}- User '{correct_name}' has logged in\nDETAILS: {time}\n")
    print(f"\nCorrect, welcome user '{correct_name}'\n")


def incorrect():
    global counter
    counter+=1
    time_2=datetime.now()
    wrong_name=colored(user_name,"red", "on_white",attrs=["bold"])
    with open("log_file.txt","a",encoding="utf-8") as list:
        list.write(f"\n{counter}- User '{wrong_name}' has entered wrong password\nDETAILS: {time_2}\n")

    print(f"\nUser '{wrong_name}' entered wrong password!\n")


def display():
    with open("log_file.txt","r",encoding="utf-8") as file:
        print(file.read())


def remove():
    with open("log_file.txt","w",encoding="utf-8"):
        print("\nClean as your heart :)\nAll data has been deleted!\n")



while True:
   
    pick=int(input(f"{1}-Enter new data\n{2}-Display the log file\n{3}-Remove all data\n{4}-Exit\n"))

    if pick==1:
        user_name=input("\nUser Name: ")
        user_password=(input("Password: "))
        password="123abc+"
        print("Checking...")
        time.sleep(1)

        if user_password == password:
            correct()
        else:
            incorrect()
            

    elif pick==2:
        display()

    elif pick==3:
        remove()
    
    else:
        print("Closing...")
        break


   

   


    