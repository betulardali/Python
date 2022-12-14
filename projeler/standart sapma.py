#Rastgele belirlenen 7 tane sayının standart sapmasını bulma


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

ort=(num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7) / 7
#tam sayı şeklinde istersek; ort=int((num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7) / 7)
print("Aritmetik ortalama: ",ort)

#standart sapma= veri sayısı n olan bir kümede; her bir sayı aritmetik ortalamadan çıkarılır ve kareleri alınır, kareler toplanıp n-1 'e bölünür, son olarak karekök alınır.
s_1=ort-num_1
s_1*=s_1
print("1.sayinin karesi: ",s_1)
s_2=ort-num_2
s_2*=s_2
print("2.sayinin karesi: ",s_2)
s_3=ort-num_3
s_3*=s_3
print("3.sayinin karesi: ",s_3)
s_4=ort-num_4
s_4*=s_4
print("4.sayinin karesi: ",s_4)
s_5=ort-num_5
s_5*=s_5
print("5.sayinin karesi: ",s_5)
s_6=ort-num_6
s_6*=s_6
print("6.sayinin karesi: ",s_6)
s_7=ort-num_7
s_7*=s_7
print("7.sayinin karesi: ",s_7)

sum= s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7
print("Kareler toplami: ",sum)

sapma= sum / 6
import math
standart_sapma=math.sqrt(sapma)
#tam sayı şeklinde bulmak istersek; standart_sapma=int(math.sqrt(sapma))
print("Standar sapma: ",standart_sapma)



