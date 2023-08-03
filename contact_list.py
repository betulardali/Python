def new_contact():
    name=input("\nName: ")
    surname=input("Surname: ")
    number=int(input("Phone Number (0XXXXXXXXXX): "))

    with open("contact_list.txt","a",encoding="utf-8") as list:
        print(("New contact has been created!").center(10,"*"))
        list.write(f"\nPerson: {name} {surname}, Number: {number}\n")



def contact_list():
    with open("contact_list.txt","r",encoding="utf-8") as list:
        print(list.read())


def delete():
    deleting=input("Contact name you want to delete: ").strip()
    with open("contact_list.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if deleting not in line]
            print(f"Person '{deleting}' has been removed!")

    with open("contact_list.txt", "w", encoding="utf-8") as file:
            file.writelines(modified_lines)



while True:
    choose=int(input(f"\n{1}-Create new contact\n{2}-Display contact list\n{3}-Delete contact\n{4}-Exit\n"))

    if choose==1:
        new_contact()

    elif choose==2:
        contact_list()

    elif choose==3:
        delete()

    else: break