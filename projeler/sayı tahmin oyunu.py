from random import randint
x=randint(1,100)

sayac=0

while(sayac < 6):
    if sayac==5:
            secim_1=int(input("Cok fazla basarisiz giris yaptiniz. Tekrar oynamak icin (1), cikmak icin (0) tuslayiniz. "))
            if secim_1==1:
                continue
            
            elif secim_1==0:
                print("Oyundan ciktiniz!")
                break

    secim=(input("Lutfen 1 ile 100 arasinda bir deger girin: (Cikis icin (0) tuslayiniz.) "))
    if secim=="0":
        print("Oyundan ciktiniz!")
        break

    else:
        
        if int(secim) < x:
            sayac+=1
            print("Daha buyuk bir sayi giriniz. ")
            continue
        elif (secim) > x:
            sayac+=1
            print("Daha kucuk bir sayi giriniz. ")
            continue
        else:
             print("Dogru tahmin ettiniz!")
             break

    


       





