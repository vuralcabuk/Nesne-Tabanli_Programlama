class Personel:

    def __init__(self,isim,soyisim,maas):
        self.isim = isim.title() # GLOBAL
        self.soyisim = soyisim.title()
        self.maas = maas
        self.__zam_orani = 1.05 # PRİVATE
        # değişkenin başına __ iki tane alttan çizgi eklediğimizde dışarıda erişimi engelleriz buna kapsülleme denir.
        # def __zam_uygula(self) aynı şeyi fonksiyonada yapabiliriz.

    def getZamOrani(self):
        return self.__zam_orani
    # get ile zam oranına dışardan erişebiliyoz

    def setZamOrani(self,oran):
        # set ile dışardan müdahale ediyoruz
        self.__zam_orani = oran

    def zam_uygula(self):
        self.maas = int(self.maas * self.__zam_orani)



per_1 = Personel("Dean","Winchester",10000)

print(per_1.getZamOrani())
per_1.setZamOrani(oran=1.2)
# müdahale
print(per_1.getZamOrani())

#print(help(per_1))
#print(per_1.__dict__)




