
import random

oyuncular = {
  "oyuncu1" : {
    "isim" : "Oyuncu1",
    "ugurluSayi" : random.randint(1,6),
    "bulunduguKutu" : 0,
    "surpriz": False
  },
  "oyuncu2" : {
    "isim" : "Oyuncu2",
    "ugurluSayi" : random.randint(1,6),
    "bulunduguKutu" : 0,
    "surpriz": False
  },
  "oyuncu3" : {
    "isim" : "Oyuncu3",
    "ugurluSayi" : random.randint(1,6),
    "bulunduguKutu" : 0,
    "surpriz": False
  },
  "oyuncu4" : {
    "isim" : "Oyuncu4",
    "ugurluSayi" : random.randint(1,6),
    "bulunduguKutu" : 0,
    "surpriz": False
  },
}

#Sürpriz kutucuk
while True:
    surprizKutucuk = input("Sürpriz kutucuğu belirleyin (2 basamaklı sayı): ")
    if surprizKutucuk.isdigit():
        surprizKutucuk = int(surprizKutucuk)
        if 10 <= surprizKutucuk <= 99:
            break
    print("Lütfen 10 ile 99 arasında 2 basamaklı bir sayı girin.")

print(f"Sürpriz kutucuğu {surprizKutucuk} olarak belirlendi.")

kazanan = None

#Ugurlu Sayilari Ekrana Yazmak
for x, obj in oyuncular.items():
    print(f"{x}'ın uğurlu sayısı: {obj['ugurluSayi']}" )

#Oyun
def zar_at(oyuncu, basamakSayisi):
    global kazanan
    #Oynayanin belirlenmesi
    print("")
    print(f"======================  Oynayan: {oyuncu['isim']}   ======================")
    print("")

    #İlk Atış
    print(f"Atılan zarın karşılığı: {basamakSayisi}")
    print(f"{oyuncu['isim']} {basamakSayisi} basamak ilerledi.")
    oyuncu["bulunduguKutu"] = oyuncu["bulunduguKutu"] + basamakSayisi
    print(f"{oyuncu['isim']}'nun bulunduğu kutucuk: {oyuncu['bulunduguKutu']}")
    #Ceza
    if oyuncu["bulunduguKutu"] % 11 == 0 and oyuncu["bulunduguKutu"] < 100:
        print(f"{oyuncu['isim']}'nun bulunduğu kutucuğun 1. ve 2. basamağı aynı olduğu için, ceza olarak 5 adım geriye gönderildi.")
        oyuncu["bulunduguKutu"] = oyuncu["bulunduguKutu"] - 5
        print(f"{oyuncu['isim']}'nun bulunduğu kutucuk: {oyuncu['bulunduguKutu']}")

    #Sürpriz kutucuğa gelenlerin tespiti
    if oyuncu["bulunduguKutu"] == int(surprizKutucuk) and oyuncu["surpriz"] == False:
        print(f"Tebrikler! Sürpriz kutucuğa geldin, oyun sonuna kadar zarı 2 kez atma hakkını kazandın.")
        oyuncu["surpriz"] = True
    
    #Kazan oyuncu belirlenmesi
    if oyuncu["bulunduguKutu"] >= 100:
        print(f"{oyuncu['isim']} Kazandı!🎉")
        print("")
        kazanan = oyuncu
    elif basamakSayisi == oyuncu["ugurluSayi"]:
        print(f"Tebrikler! Zarın değeri {oyuncu['isim']}'nun uğurlu sayısına eşit geldiği için tekrar zarı atma hakkını kazandın.")
        yeniZar = random.randint(1,6)
        zar_at(oyuncu, yeniZar)


while kazanan == None:
    for x in oyuncular:
        if kazanan == None:
            zar = random.randint(1,6)
            zar_at(oyuncular[x], zar)
        else:
            break
        #Sürpriz kutucuğa gelenlerin tekrar zarı atmaları
        if oyuncular[x]["surpriz"] and kazanan == None:
            print("Sürpriz kutucuğa geldiğin için tekrar zarı atma hakkını kazandın.")
            yeniZar = random.randint(1,6)
            zar_at(oyuncular[x], yeniZar)


