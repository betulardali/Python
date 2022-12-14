#Listeden seçilen şeklin kullanıncın isteğine göre alanını veya çevresini bulma

sekiller=["daire","eskenar ucgen","kare","dikdortgen"]
print(sekiller)
istenilen_sekil=input("Islem yapmak istediginiz sekli üstteki listeden seciniz (islemler cm cinsindendir): ")

while True:

    if istenilen_sekil =="daire" or istenilen_sekil=="Daire":
        pi=3.14
        r=int(input("Dairenin yaricapini giriniz: "))
        islem=input("Alan bulmak icin (1) çevre bulmak için (2) tuslayiniz: ")

        
        if islem=="1":
            alan=pi*r*r
            alan_daire="Yaricapi {} cm olan dairenin alani {} cm^2 dir."
            print(alan_daire.format(r,alan))
            break

        elif islem=="2":
            cevre=2*pi*r
            daire_cevre="Yaricapi {} cm olan dairenin cevresi {} cm'dir."
            print(daire_cevre.format(r,cevre))
            break

        else:
            print("Gecersiz islem!")
            break


    elif istenilen_sekil=="kare" or istenilen_sekil=="Kare":
        a=int(input("Karenin bir kenar uzunlugunu giriniz: "))

        islem=input("Alan bulmak icin (1) çevre bulmak için (2) tuslayiniz: ")
        if islem=="1":
            alan=a*a
            alan_kare="Bir kenari {} cm olan karenin alanı {} cm^2 dir."
            print(alan_kare.format(a,alan))
            break
        
        elif islem==2:
            cevre=4*a
            cevre_kare="Bir kenari {} cm olan karenin çevresi {} cm'dir."
            print(cevre_kare.format(a,cevre))
            break

        else:
            print("Gecersiz islem!")
            break


    elif istenilen_sekil=="dikdortgen" or istenilen_sekil=="Dikdortgen":
        uzun=int(input("Dikdortgenin uzun kenarini giriniz: "))
        kisa=int(input("Dikdörtgenin kisa kenarini giriniz: "))
        islem=input("Alan bulmak icin (1) çevre bulmak için (2) tuslayiniz: ")

        if islem=="1":
            alan=uzun*kisa
            alan_d="Uzun kenari {} cm kisa kenari {} olan dikdortgenin alani {}  cm^2 dir."
            print(alan_d.format(uzun,kisa,alan))
            break

        elif islem==2:
            cevre=2*(uzun+kisa)
            cevre_d="Uzun kenari {} cm kisa kenari {} olan dikdortgenin cevresi {}  cm'dir."
            print(cevre_d.format(uzun,kisa,cevre_d))
            break

        else:
            print("Gecersiz islem!")
            break


    elif istenilen_sekil=="eskenar ucgen" or istenilen_sekil==" Eskenar Ucgen":
        kenar=int(input("Ucgenin bir kenar uzunlugunu giriniz: "))
        alan= 0.43*kenar              #(√3 / 4)*kenar 
        islem=input("Alan bulmak icin (1) çevre bulmak için (2) tuslayiniz: ")

        if islem=="1":
            alan_u="Ucgenin alani {} cm^2 dir."
            print(alan_u.format(alan))
            break

        if islem=="2":
            cevre=3*kenar
            print("Ucgenin cevresi {} cm'dir.".format(cevre))
            break

        else:
            print("Gecersiz islem!")
            break
        
    else:
        print("Listede olmayan bir sekil sectiniz!\n")
        print(sekiller)
        print("Lutfen listeden bir sekil seciniz: ")
        istenilen_sekil=input()
        continue

        


 


