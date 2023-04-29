import saves as save

# Kullanacağımız değişkenler
isim = "Burak"
main = "Makima"
durum = "Üzgün"
durum2 = "Yapayzeka gibi hissediyo"

save.tanx("isim",isim) # özel isim kayıt ediyoruz
save.tanx("tekisim",main) # tek yapayzekanın kullanacağı isimi kayıt ediyoruz

save.cotx("isimBilgi_durum",isim,durum) # belirttiğimiz özel isime durum bilgisi ekliyoruz
save.secx("tekisimBilgi_durum", durum2) # tekisime durum bilgisi ekliyoruz



tekisim_name = save.sinx("tekisim") # tekisimin adını çekiyoruz
tekisim_durum = save.sinx("tekisimBilgi_durum") # tekisimin durum bilgisini çekiyoruz

özelisim_name = save.cosx("isim",isim) # özelisimin ismini çekiyoruz
özelisim_durum = save.cosx("isimBilgi_durum",isim) # özelisimin durumunu çekiyoruz

print(tekisim_name,tekisim_durum,özelisim_name,özelisim_durum)

