class Personel:

    personel_sayisi = 0
    zam_orani = (1.05)

# zam oranını sınıf değişkeni olarak burada bu şekilde yazmış oluyoruz. Bu değişkenimiz nesneler arasında değişmeden,
# kullanabileceğimiz ve güncellemek için kolayca ulaşabileceğimiz bir veri yapısını oluşturmuş oluyor.
# bizim bu zam_orani değişkenimize ulaşmamızın iki yolu var. 1. si Personel.zam_orani, 2. si self.zam_orani yani bu
# sınıf değişkenimize ya Personel sınıfı üzerinden yada sınıfımızdaki nesnelere atfettiğimiz self parametresi üzerinden erişebiliriz.

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

        Personel.personel_sayisi += 1
#bu sınıfımızdan her yaratılan personel için öncelik olarak init fonksiyonumuz çalışacak. o yüzden sınıfımız içindeki
# personel_sayisi değişkenimizi 1 arttırması için Personel.personel_sayisi += 1 değişkenimizi bu init fonksiyonumuza yazdık

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)



per_1 = Personel("john","smith",30000)
per_2 = Personel("mary","smith",35000)



from pprint import pprint


#pprint(per_1.__dict__)
"""{'eposta': 'john.smith@firmam.com',
 'isim': 'john',
 'maas': 30000,
 'soyisim': 'smith'}"""
# Aslında pythonda herşey zaten objeden oluşur. Arka planda pythonın her bir değişkeni sözlük yapısında olduğu gibi okuduğunu görebiliyoruz.

#per_1.zam_orani = 1.1
# Burada sınıfımız içinde oluşturduğumuz zam_orani = 1.05 sınıf değişkenimize erişip manüpüle ediyoruz.

"""_______________Manüpüleden sonra_____________"""

#pprint(per_1.__dict__)
"""{'eposta': 'john.smith@firmam.com',
 'isim': 'john',
 'maas': 30000,
 'soyisim': 'smith',
 'zam_orani': 1.1}"""
print(per_1.maas)
per_1.zam_uygula()
print(per_1.maas)



