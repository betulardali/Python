import random
choices=["rock","paper","scissors"]
rock = choices[0]
paper = choices[1]
scissors = choices[2]
print("Welcome! (Enter '0' for exit) ")
counter_user=0
counter_pc=0

while True:
    choose=input("Rock, paper or scissors? ")
    pc_choose=random.choice(choices)

    if choose==rock:
        if pc_choose==rock:
            print("Choice of pc: rock")
            print("Result: Drawn\n")

        elif pc_choose==paper:
            print("Choice of pc: paper")
            print("Result: Defeated\n")
            counter_pc +=1

        else:
            print("Choice of pc: scissors")
            print("Result: Winning\n")
            counter_user+=1


    elif choose==paper:
        if pc_choose==paper:
            print("Choice of pc: paper")
            print("Result: Drawn\n")

        elif pc_choose==rock:
            print("Choice of pc: rock")
            print("Result: Winning\n")
            counter_user+=1

        else:
            print("Choice of pc: scissors")
            print("Result: Defeated\n")
            counter_pc+=1

    elif choose==scissors:
        if pc_choose==scissors:
            print("Choice of pc: scissors")
            print("Result: Drawn\n")

        elif pc_choose==paper:
            print("Choice of pc: paper")
            print("Result: Winning\n")
            counter_user+=1
        else:
            print("Choice of pc: rock")
            print("Result: Defeated\n")
            counter_pc+=1


    elif choose=="0":
        print("Game over!\n")
        sor=input("Do you wanna play again? : (Y/N) ")

        if sor=="Y" or sor=="y":
            print("Starting over.\n")
            continue
        elif sor=="N" or sor=="n":
            print("See you next time :)")
            break
        

    
    son=input("Choose one: '0' for exit, enter for continue.\n")
    if son=="0":
       # print(result.format(counter_pc,counter_user))
        result="\nFinal Result: Computer: {} User: {}\n"
        print(result.format(counter_pc,counter_user))
        print("Thanks for playing!")
        break
    else:
        continue

            

            