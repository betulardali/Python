import random
secenek=["tas","kagit","makas"]
tas = secenek[0]
kagit = secenek[1]
makas = secenek[2]
print("Oyuna hosgeldiniz! Çikmak için (0) tuslayin.")
kullanici_sayac=0
pc_sayac=0
while True:
    secim=input("tas mi, kagit mi, makas mi? ")
    pc_secim=random.choice(secenek)

    if secim==tas:
        if pc_secim==tas:
            print("Bilgisayar secimi: tas")
            print("Sonuc: Berabere\n")

        elif pc_secim==kagit:
            print("Bilgisayar secimi: kagit")
            print("Sonuc: Kaybettiniz\n")
            pc_sayac+=1

        else:
            print("Bilgisayar secimi: makas")
            print("Sonuc: Kazandiniz\n")
            kullanici_sayac+=1

    elif secim==kagit:
        if pc_secim==kagit:
            print("Bilgisayar secimi: kagit")
            
            print("Sonuc: Berabere\n")
        elif pc_secim==tas:
            print("Bilgisayar secimi: tas")
            print("Sonuc: Kazandiniz\n")
            kullanici_sayac+=1
        else:
            print("Bilgisayar secimi: makas")
            print("Sonuc: Kaybettiniz\n")
            pc_sayac+=1

    elif secim==makas:
        if pc_secim==makas:
            print("Bilgisayar secimi: makas")
            print("Sonuc: Berabere\n")
        elif pc_secim==kagit:
            print("Bilgisayar secimi: kagit")
            print("Sonuc: Kazandiniz\n")
            kullanici_sayac+=1
        else:
            print("Bilgisayar secimi: tas")
            print("Sonuc: Kaybettiniz\n")
            pc_sayac+=1


    elif secim=="0":
        print("Oyundan ciktiniz!\n")
        sor=input("Tekrar oynamak istiyor musunuz? : (E/H) ")

        if sor=="E" or sor=="e":
            print("Oyun bastan basliyor.\n")
            continue
        elif sor=="H" or sor=="h":
            print("Oyun kapatiliyor.")
            break
        

    sonuc="Son durum: Bilgisayar: {} Kullanici: {}\n"
    print(sonuc.format(pc_sayac,kullanici_sayac))
    son=input("Cikmak için 0, devam etmek icin enter tusunu kullaniniz.\n")
    if son=="0":
        print(sonuc.format(pc_sayac,kullanici_sayac))
        print("Oynadiginiz icin tesekkurler!")
        break
    else:
        continue

            

            