# Kitapların Ana Sınıfı
class Kitap:
    def __init__(self, kIsmi, sayfa, yazar):
        self.kIsmi = kIsmi
        self.sayfa = sayfa
        self.kTuru = "Genel Kitap"
        self.yazar = yazar

    def bilgileriGoster(self):
        print(f"Kitap Adı   : {self.kIsmi}")
        print(f"Kitap Yazarı: {self.yazar}")
        print(f"Sayfa Sayısı: {self.sayfa}")
        print(f"Kitap Türü  : {self.kTuru}")

# Basılı Kitap sınıfı    
class BasiliKitap(Kitap):
    def __init__(self, kIsmi, sayfa, yazar, adet):
        super().__init__(kIsmi, sayfa, yazar)
        self.kTuru = "E-Kitap"
        self.adet = adet

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(f"Adet        : {self.adet}")

    def oduncAl(self):
        if self.adet <= 0:
            print("Bu kitap envanterde mevcut değil.")
        else:
            self.adet -= 1
            print("Kitap ödünç alındı.")

    def iadeEt(self):
        self.adet += 1
        print("Kitap iade edildi.")
        

# E-Kitap sınıfı    
class EKitap(Kitap):
    def __init__(self, kIsmi, sayfa, yazar, boyut):
        super().__init__(kIsmi, sayfa, yazar)
        self.kiTuru = "E-Kitap"
        self.boyut = boyut

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(f"Dosya Boyutu: {self.boyut}")

# Kitap Ekleme Fonksiyonu
kitaplar = []
def kEkle():
    kIsmi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    sayfa = int(input("Sayfa sayısı: "))

    print("Tür seçiniz:")
    print("1- Basılı Kitap")
    print("2- E-Kitap")
    turSecimi = input("Seçim: ")
    if turSecimi == "1":
        adet = int(input("Adet: "))
        yeniKitap = BasiliKitap(kIsmi, sayfa, yazar, adet)
        kitaplar.append(yeniKitap)
        print("Kitap başarıyla eklendi.")
    elif turSecimi == "2":
        boyut = float(input("Dosya boyutu (MB): "))
        yeniKitap = EKitap(kIsmi, sayfa, yazar, boyut)
        kitaplar.append(yeniKitap)
        print("")
        print("Kitap başarıyla eklendi.")
        print("")
    else:
        print("")
        print("Geçersiz tür seçimi.")
        print("")

# Kitapları gösteren Fonksiyon
def kListele():
    if not kitaplar:
        print("")
        print("Kütüphanede hiç bir kitap yok.")
        print("")
    else:
        print("")
        print("--- KİTAPLAR ---")
        print("")
        for i, kitap in enumerate(kitaplar, start=1):
            print(f"Kitap No: {i}")
            print("")
            kitap.bilgileriGoster()
            print("")

# Kitap Ödünç Alma Fonksiyonu
def oduncAl():
    if not kitaplar:
        print("")
        print("Kütüphanede hiç bir kitap yok.")
        print("")
        return
    
    kListele()
    try:
        n = int(input("Ödünç alınacak kitap numarası: "))
        if n < 1 or n > len(kitaplar):
            print("Geçersiz kitap numarası.")
            return

        secilenKitap = kitaplar[n - 1]

        if isinstance(secilenKitap, BasiliKitap):
            secilenKitap.oduncAl()
        else:
            print("E-kitaplar ödünç alma işlemine uygun değildir.")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

# Kitap iade Etme Fonksiyonu
def iadeEt():
    if not kitaplar:
        print("")
        print("Kütüphanede hiç bir kitap yok.")
        print("")
        return
    
    kListele()
    try:
        n = int(input("İade edilecek kitap numarası: "))
        if n < 1 or n > len(kitaplar):
            print("")
            print("Geçersiz kitap numarası.")
            print("")
            return

        secilenKitap = kitaplar[n - 1]

        if isinstance(secilenKitap, BasiliKitap):
            secilenKitap.iadeEt()
        else:
            print("")
            print("E-kitaplar için iade işlemi gerekmez.")
            print("")
    except ValueError:
        print("")
        print("Lütfen geçerli bir sayı giriniz.")
        print("")

def menu():
    while True:
        print("Aşağıdaki İşlemlerin Birini seçin")
        print("1- Kitap Ekle")
        print("2- Kitapları Listele")
        print("3- Kitap Ödünç Al")
        print("4- Kitap İade Et")
        print("5- Çıkış")
        print("")

        secim = input("Seçim: ")

        if secim == "1":
            kEkle()
        elif secim == "2":
            kListele()
        elif secim == "3":
            oduncAl()
        elif secim == "4":
            iadeEt()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim yaptınız.")


menu()