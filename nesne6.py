class Personel:
    zam_orani = (1.05)

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"
        #print(f"Yeni personel tanımlandı: {isim} {soyisim}")

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)
        return self.maas

    def __repr__(self):
        # Bu özel fonksiyonumuzla sadece personel ismimizle tüm bilgilerine ulaşabiliriz
        return f"Personel:\n{self.isim}\n{self.soyisim}\n{self.maas}\n{self.eposta}"

    def __str__(self):
        return f"{self.tam_isim()} - {self.eposta}"

    def __add__(self, other):
        return f"{self.isim} + {other.isim} maaşlarının toplamı = {self.maas + other.maas}"



per_1 = Personel("Dean", "Winchester", 10000)
per_2 = Personel("Sam", "winchester",15000)

#print(per_1.__repr__())
# per_1 in tüm bilgileri gelir.

print(per_1.__add__(per_2))
# add metodunu bu şekilde kullanarak istediğimiz personellerin maaşlarını topladık









