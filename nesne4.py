class Personel:
    personel_sayisi = 0
    zam_orani = (1.05)

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

        Personel.personel_sayisi += 1

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)
        return self.maas

    @classmethod
    # classmethod ile sınıfımızın içindeki değişkenimizi fonksiyon olarak çağırıp manüpüle edebiliyoruz.
    # cls parametremiz personel sınıfımızı temsil ediyor direk. cls.zam_orani sınıfımızın içindeki zam_orani değişkenimizi ifade ediyor.
    def zam_oranini_belirle(cls,oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f"Eski zam oranı: '{eski_oran}' güncellendi. Yeni oran: {cls.zam_orani}")

    @classmethod
    def from_string(cls,per_str):
        isim,soyisim,maas = per_str_1.split("-")
        return cls(isim, soyisim, maas)

    @staticmethod
    # staticmethod da sınıfımızın içindeki herhangibir nesneyi yada sınıf değişkenimizi argüman olarak vermiyoruz.
    # dışarıdan bir şeyler dahil ediyoruz.
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return "Haftasonu"
        else:
            return "Haftaiçi"



"""from datetime import datetime

bugun = datetime.now()"""



from datetime import datetime
bugun = datetime.now()

print(Personel.mesai_gunu(bugun))





per_1 = Personel("john","smith",10000)
per_2 = Personel("mary","smith",35000)


per_str_1 = "Sam-Winchester-40000"
per_str_2 = "Dean-Winchester-60000"
per_str_3 = "Boby-Singer-60000"



# yeni_per_1 = Personel.from_string("Sam-Winchester-40000")
#
# print(yeni_per_1.eposta)
# print(yeni_per_1.maas)












# isim, soyisim, maas = per_str_1.split("-")
#
# yeni_per_1 = Personel(isim,soyisim,maas)
#
# print(yeni_per_1.eposta)
# print(yeni_per_1.maas)

#Personel.zam_oranini_belirle(1.1)



