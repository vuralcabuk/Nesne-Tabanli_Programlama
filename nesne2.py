class Personel:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
#sınıf içinde tanımladığımız bu fonksiyonu çağırarak istediğimiz kişinin tam adını otomatik olarak çekebiliyoruz.
# örn: print(per_1.tam_isim())

per_1 = Personel("john","smith",30000)
per_2 = Personel("mary","smith",35000)

print(Personel.tam_isim(per_1))
print(per_2.tam_isim())
#iki farklı çağrı yaptık



