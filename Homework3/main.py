class TersCevir:
    def __init__(self, metin):
        yeniMetin = ""
        for n in range(len(metin)):
            yeniMetin += metin[len(metin) - n - 1]
        self.metin = yeniMetin

    def __str__(self):
        return self.metin
    
class SezarSifreleme:
    def __init__(self, metin, otelemeMiktari):
        tersMetin = str(TersCevir(metin))
        yeniMetin = ""
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
        alfabeUpper = alfabe.upper()
        for i in tersMetin:
            if i in alfabe:
                yeniMetin += alfabe[(alfabe.find(i) + otelemeMiktari) % len(alfabe)]
            elif i in alfabeUpper:
                yeniMetin += alfabeUpper[(alfabeUpper.find(i) + otelemeMiktari) % len(alfabeUpper)]
            else:
                yeniMetin += i 
                
        self.metin = yeniMetin

    def __str__(self):
        return self.metin

class Cozucu:
    def __init__(self, metin):
        tersMetin = ""
        yeniMetin = ""
        alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
        alfabeUpper = alfabe.upper()
        print("\tTers Metin\tDüz Metin \n------------------------------------------------")
        for j in range(len(alfabeUpper)):
            for i in metin:
                if i in alfabe:
                    tersMetin += alfabe[(alfabe.find(i) - j) % len(alfabe)]
                elif i in alfabeUpper:
                    tersMetin += alfabeUpper[(alfabeUpper.find(i) - j) % len(alfabeUpper)]
                else:
                    tersMetin += i 

            yeniMetin = str(TersCevir(tersMetin))
            print(f"key{j}:\t{tersMetin}\t{yeniMetin}")
            tersMetin = ""
            

    


metin = input("Şifrelemek istediğiniz metni girin:")
otelemeMiktari  = input("Şifre anahtarı girin:")
print(TersCevir(metin))
sifreliMetin = SezarSifreleme(metin, int(otelemeMiktari))
print(sifreliMetin)
Cozucu(str(sifreliMetin))

