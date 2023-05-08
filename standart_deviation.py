#Calculating standart deviation of random 7 numbers


#import random
#sayi=random.randint(1,100)

from random import randint     
num_1=randint(1,100)
num_2=randint(1,100)
num_3=randint(1,100)
num_4=randint(1,100)
num_5=randint(1,100)
num_6=randint(1,100)
num_7=randint(1,100)
print(num_1 , num_2 , num_3, num_4 , num_5 , num_6 , num_7)

mean=(num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7) / 7
#if we want to make it integer; ort=int((num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7) / 7)
print("arithmetic mean:  ",mean)

#let's say we have an array that has n elements. To find standart deviation, we substract every number from arithmetic mean by one by and take square of them. And then we sum all squares and take divison by n-1. Finally we take square root.

s_1=mean-num_1
s_1*=s_1
print("Square of num1: ",s_1)

s_2=mean-num_2
s_2*=s_2
print("Square of num2: ",s_2)

s_3=mean-num_3
s_3*=s_3
print("Square of num3: ",s_3)

s_4=mean-num_4
s_4*=s_4
print("Square of num4: ",s_4)

s_5=mean-num_5
s_5*=s_5
print("Square of num5: ",s_5)

s_6=mean-num_6
s_6*=s_6
print("Square of num6: ",s_6)

s_7=mean-num_7
s_7*=s_7
print("Square of num7: ",s_7)


sum= s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7
print("Sum of squares: ",sum)

deviation= sum / 6
import math
standart_deviation=math.sqrt(deviation)
#integer >>  standart_sapma=int(math.sqrt(sapma))
print("Standart deviation: ",standart_deviation)



