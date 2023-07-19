import os

kayit_Sorgu = os.path.exists("saves")
if (kayit_Sorgu != True):
    os.mkdir("saves")


# İki değişken kayıt etme fonksiyonu
def tanx(kategori, isim):
            
            ### Bu kategori, sayısız ismi kayıt yapma imkanı sunar!
            if (kategori == "isim"):
                try:
                    bosisim = isim.strip()
                    # Bu şeilde özel isimde bir dosya oluştulur
                    dosya = open(f"saves/{bosisim}.txt", "w", encoding="utf-8")
                except FileExistsError:
                    print(" > Bu isimde daha önce bir dosya oluşturuldu!")
                else:
                    dosya.write(isim)
                    dosya.close()


            ## Bu kategori, yapay zeka gibi tek seferlik kullanılacak isimler için oluşturulmuştur, bu fonksiyon ile
            # oluşturulan isim değiştirilemez ve ana isim olarak kalır!
            elif (kategori == "tekisim"):
                try:
                    bosisim = isim.strip()
                    dosya = open("saves/tekisim.txt", "w", encoding="utf-8")
                except FileExistsError:
                    print(" > Bu isimde daha önce bir dosya oluşturuldu!")
                else:
                    dosya.write(isim)
                    dosya.close()
            else:
                print(" > Anlayamadım...")


# üç değişkenli veri kayıt etme # özel isimlerin verilerini kayıt ediyoruz durum,yas gibi
def cotx(kategori,isim,veri):
            # Belirteceğimiz özel isim hakkında durum bilgisi girilebilir
            if (kategori == "isimBilgi_durum"):
                bosisim = isim.strip()

                try:
                    newdosya = open(f"saves/{bosisim}durum.txt","w", encoding="utf-8")
                except FileExistsError:
                    print(" > Bu isimde daha önce bir dosya oluşturuldu!")
                else:
                    newdosya.write(veri)
                    newdosya.close()
            ## isimBilgi_yas kategorisi diye devam edebilir burası

            else:
                print(" > Anlayamadım...")
    


### iki değişkenli veri kayıt etme # tekisimin verisini kayıt ediyoruz durum,yas gibi
def secx(kategori,veri):
        # tekisim kategorisi için durum kayıt etme
        if (kategori == "tekisimBilgi_durum"):
            newdosya = open(f"saves/tekisimdurum.txt","w", encoding="utf-8")
            newdosya.write(veri)
            newdosya.close()
        ## tekisimBilgi_yas kategorisi diye devam edebilir burası

        else:
            print(" > Anlayamadım...")




# tek değişken çağırmalı # tekisimin verilerini okuma isim,durum,yas gibi
def sinx(kategori):

        if (kategori == "tekisim"):
            dosya = open("saves/tekisim.txt", "r", encoding="utf-8")
            tekisim = dosya.read()
            return tekisim.strip()

        elif (kategori == "tekisimBilgi_durum"):
            dosya = open(f"saves/tekisimdurum.txt", "r", encoding="utf-8")
            tekisimdurum = dosya.read()
            dosya.close()
            return tekisimdurum.strip()
        

        
        else:
            print(" > Anlayamadım...")





# iki değişken çağırmalı # özel isimleri verilerini okuyoruz isim,durum,yas gibi
def cosx(kategori,isim):
        bosisim = isim.strip()

        if (kategori == "isim"):
            dosya = open(f"saves/{bosisim}.txt", "r", encoding="utf-8")
            isim = dosya.read()
            return isim.strip()    


        elif (kategori == "isimBilgi_durum"):
            dosya = open(f"saves/{bosisim}durum.txt", "r", encoding="utf-8")
            isimdurum = dosya.read()
            return isimdurum.strip()
        


        else:
            print(" > Anlayamadım...")
        




   
