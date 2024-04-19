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



class Yazilimci(Personel):
    # burada farklı özelliklere sahip çalışanlar için bir sınıf oluşturduk. fakat bu çalışanlarında bir çok özelliği
    # Personel sınıfımızdakilerle aynı olacak. o yüzden biz kısaca ilk sınıfımızdan komple özellikleri miras alıyoruz
    # ve ordaki özelliklerin dışında eklemek istediğimiz özellikleri buraya özgün şekilde yazabilmiş oluyoruz.
    zam_orani = 1.1

    def __init__(self,isim,soyisim,maas,prog_dili):
        # buradaki sınıfımızda, ilk çalışan init fonksiyomuzda farklı bir özellik olmasını istiyoruz. fakat biz init
        # fonksiyonuna ekleme yaparsak miras aldığımız sınıfımızın init fonksiyonu geçersiz olacaktır.
        # o yüzden miras almak istediğimiz özellikleri belirtmeliyiz __init__ içinde
        super().__init__(isim,soyisim,maas)
        # pratik bir şekilde Personel sınıfının nesnelerinide miras alıyoruz tekrar
        #print(f"Yeni personel yazılımcı kategorisine taşındı: {self.isim} {self.soyisim}")
        self.prog_dili = prog_dili
        # sonra buraya özgün nesnemizi oluşturuyoruz.




class Mudur(Personel):

    def __init__(self,isim,soyisim,maas,personeller = None):
        super().__init__(isim,soyisim,maas)
        if personeller is None:
            self.personeller = []
        else:
            self.personeller = personeller

    def personel_ekle(self,per):
        if per not in self.personeller:
            self.personeller.append(per)

    def personel_cikar(self,per):
        if per in self.personeller:
            self.personeller.remove(per)

    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e += 1
            print(e,per.tam_isim())





yaz_1 = Yazilimci("Dean","Winchester",10000,"python")
yaz_2 = Yazilimci("Sam","Winchester",35000,"java")
#yazılımcı sınıfından iki kişiyi işe aldık ve bilgilerini kaydederek nesne oluşturmuş olduk.
mdr_1 = Mudur("John","Wick",50000,[yaz_1])
# aynı şekilde müdür sınıfından nesne oluşturduk. tabi bu sınıfların birbirinden farklı özellikleri var.




#print(isinstance(yaz_1,Yazilimci))
# isinstance() fonksiyonu ile biz doğrulama işlemi yapıyoruz. örneğin burada yaz_1, Yazılımcı sınıfından mı üretilmiş
# onu kontrol ettik ilerde nesnelerimizin nerden türediğini sorgulamak için kullanabiliriz.

# print(issubclass(Mudur, Yazilimci))
# print(issubclass(Yazilimci, Mudur))
# print(issubclass(Yazilimci,Personel))
# Yazılımcı Personelden mi türemiş onu kontrol ettik True



