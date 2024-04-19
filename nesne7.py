class Personel:
    zam_orani = (1.05)

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim.title()
        self.maas = maas
    @property
    # @propert dekoratörümüz ile fonksiyonlarımıza print(per_1.isim) gibi nesneye erişir gibi erişebiliriz.
    # normalde bu fonksiyonumuza print(per_1.eposta()) şeklinde erişebiliyorduk
    def eposta(self):
        return f"{self.isim.lower()}.{self.soyisim.lower()}@firmam.com"

    @property
    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    @tam_isim.setter
    # burada bir üstteki tam_isim fonksiyonumuzu manüpüle ediyoruz. nesnemizin tam isminide per_1.tam_isim = "Alper AKBAŞ"
    # olarak değiştirebiliyoruz. üstteki fonksiyonumuz ayrıca orda olmalı çünkü onun işi sadece tam isim kontrolü yapmak
    # ilişkili iki fonksiyonumuzunda olması gereklidir.
    def tam_isim(self,ad):
        isim, soyisim = ad.split(' ')
        self.isim = isim
        self.soyisim = soyisim

    @tam_isim.deleter
    # üstteki setter dekoratörünün tersi olarak deleter dekoratörüde silme işi yapar
    # ' del per_1.tam_isim ' bu şekilde kullanabiliriz.
    def tam_isim(self):
        print("Değişkenler Silindi")
        self.isim = None
        self.soyisim = None




per_1 = Personel("Dean","Winchester",10000)

print("___________")
per_1.tam_isim = "Alper AKBAŞ"
print(per_1.isim)
print(per_1.eposta)
print(per_1.tam_isim)

del per_1.tam_isim
print(per_1.tam_isim)








