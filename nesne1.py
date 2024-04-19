class Personel:
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"
#burada self'i nesnelerimize sistematik bir işleyiş katması için class yapımızın bize söylediği bir drektif olarak kullanıyoruz.
#bunun self yazması önemli değil herşey yazılabilir. önemli olan bu ilk parametrenin nesnelerimize kazandırdığı özellik ataması.
#isim = isim yazmasıda önemli değil ad = isim gibide bir değişken ataması yapabiliriz. fakat kullanımı zor olur.

per_1 = Personel(isim="john",soyisim="smith",maas=30000)
per_2 = Personel("mary","smith",35000)

print(per_1.isim)
print(per_1.soyisim)
print(per_1.maas)
print(per_1.eposta)
print()
print(per_2.isim)
print(per_2.soyisim)
print(per_2.maas)
print(per_2.eposta)


