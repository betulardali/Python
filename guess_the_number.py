from random import randint
x=randint(1,100)

counter=0

while(counter < 6):
    if counter==5:
            opt_1=int(input("Too many failed attempts. Please enter a number: new game (1), exit (0) "))
            if opt_1==1:
                continue
            
            elif opt_1==0:
                print("End of the game")
                break

    opt=(input("Please enter a number between 1 to 100: ( '0' for exit.) "))
    if opt=="0":
        print("End of the game")
        break

    else:
        
        if int(opt) < x:
            counter+=1
            print("Enter a bigger number. ")
            continue
        elif int(opt) > x:
            counter+=1
            print("Enter a smaller number. ")
            continue
        else:
             print("Correct guess!")
             break

    


       





