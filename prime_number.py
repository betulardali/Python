num=int(input("enter a number: "))
is_Prime= True

if num==1:
    is_Prime=False

for i in range(2,num):
    if num%i==0:
        is_Prime=False
        break

if is_Prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
