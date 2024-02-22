#LAB1:
#PROBLEM1:Kısa ve uzun kenarı girilen dikdörtgenin alanını ve çevresini hesaplayan program.
kisakenar=int(input("Kisa kenar uzunluğu giriniz:"))
uzunkenar=int(input("Uzun kenar uzunluğunu giriniz:"))
alan=kisakenar*uzunkenar
cevre=2*(kisakenar+uzunkenar)
print("CEVRE:",cevre,"ALAN:",alan)

#PROBLEM 2:Yarıçapı verilen çemberin alanını hesaplayan programı Python dilinde kodlayınız. (pi = 3,14)
yaricap=float(input("Yaricapi giriniz:"))
pisayisi=3.14
alan=pisayisi*yaricap**2
print("CEMBERİN ALANI:",alan)

#PROBLEM 3 : Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan programı kodlayınız.
gunsayisi=int(input("Sayi giriniz:"))
yil=gunsayisi//360
ay=(gunsayisi-(yil*360))//30
print("Girilen gün sayisi:",yil,"yıl",ay,"aydır")

#Problem 4 :100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz.
notunuz = int(input("Notunuzu giriniz:"))

if 85 <= notunuz <= 100:
    print("5 LİK SİSTEM NOTUNUZ 5")
elif 70 <= notunuz < 85:
    print("5 LİK SİSTEM NOTUNUZ 4")
elif 55 <= notunuz < 70:
    print("5 LİK SİSTEM NOTUNUZ 3")
elif 45 <= notunuz < 55:
    print("5 LİK SİSTEM NOTUNUZ 2")
else:
    print("5 LİK SİSTEM NOTUNUZ 1")


#PROBLEM 5 :Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran programın kodunuz yazınız.
sayi = int(input("3 basamaklı bir sayı giriniz:"))

birler = sayi % 10
onlar = (sayi // 10) % 10
yüzler = sayi // 100

print("Girdiğiniz sayının birler basamağı:", birler)
print("Girdiğiniz sayının onlar basamağı:", onlar)
print("Girdiğiniz sayının yüzler basamağı:", yüzler)
   
#PROBLEM 6:Bir ürünün alış fiyatı, vergi ve kâr oranlarını kullanılarak satış fiyatını hesaplayan programı kodlayınız.
alis_fiyati = float(input("Ürünün alış fiyatını giriniz: "))
vergi_orani = float(input("Vergi oranını giriniz (% cinsinden): "))
kar_orani = float(input("Kar oranını giriniz (% cinsinden): "))

vergi_miktari = alis_fiyati * (vergi_orani / 100)
kar_miktari = alis_fiyati * (kar_orani / 100)

satis_fiyati = alis_fiyati + vergi_miktari + kar_miktari

print("Ürünün satış fiyatı:", satis_fiyati)
