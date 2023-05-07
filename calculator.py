

numbers=[]
counter=int(input("How many numbers you want to calculate?: "))
i=0
while i<counter:

    num=int(input("Enter the numbers(by one by): "))
    numbers.append(num)
    i+=1


def sum():
    result_1=0
    for m in numbers:
        result_1 += m

    print(("\nSum of the numbers is '{}' ").format(result_1))


def sub():
    result_2=numbers[0]
    for m in numbers:
        result_2 -= m

    result_2+=numbers[0]
    print(("\nSubstratction of the numbers is '{}' ").format(result_2))
   
   
def multi():
    result_3=1
    for m in numbers:
        result_3 *= m
    print(("\nMultiplication of the numbers is '{}' ").format(result_3))


def div():      # only for two numbers
    result_4=0
    result_4= numbers[0] / numbers[1]
    print(("\nDivision of he numbers is '{}' ").format(result_4))




print("\nChoose the operation\n")
choices=int(input(" summation(1), substraction(2), multiplication(3), division(4): " ))
if choices==1:
    sum()

elif choices==2:
    sub()

elif choices==3:
    multi()

elif choices==4:
    div()

else:
    print("Wrong choice!")
















