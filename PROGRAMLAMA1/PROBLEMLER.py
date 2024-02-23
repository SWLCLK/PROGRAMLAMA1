#Girilen 5 sayının ortalamasını bulan program?
liste = []
for i in range(5):
    sayi = int(input("sayi giriniz:"))
    liste.append(sayi)

toplam = 0
for sayi in liste:
    toplam += sayi

ortalama = toplam / len(liste)

print("Girilen 5 sayının ortalaması:", ortalama)

#Girilen 5 sayı içerisindeki minimum ve maksimum değerleri bulan program?
sayilar=[]
for i in range(5):
    sayi=int(input("sayi girin:"))
    sayilar.append(sayi)
minsayi=min(sayilar)
maxsayi=max(sayilar)
print("min değer",minsayi,"max değer",maxsayi)

#N’e kadar tek sayıları yazdıran program?
liste=[]
n=int(input("deger girin:"))
for i in range(n):
    if i%2==1:
       liste.append(i)
print(liste)

#Girilen sayının tam bölenlerini bulan program?
tambolen=[]
sayi=int(input("sayi girin:"))
for i in range(1,sayi+1):
    if sayi%i==0:
       tambolen.append(i)
print(tambolen) 

#   a**b  yi açık hesaplayan program?
taban=int(input("taban degeri girin:"))
us=int(input("us degeri girin:"))
usalma=taban**us
print("cevap:",usalma)

#n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?
tektoplam=0
ciftcarpim=1
n=int(input("sayi girin:"))
for i in range (1,n):
    if i%2==0:
        ciftcarpim*=i
    if i%2==1:
        tektoplam+=i
print("cift carpım:",ciftcarpim,"tek toplam:",tektoplam)

#Girilen sayının faktöriyelini hesaplayan program?
sayi=int(input("sayi girin:"))
fak=1
for i in range (1,sayi+1):
    fak*=i
print("faktoriyel deger:",fak)

#Girilen n adet sayı içerisinden pozitif, negatif ve sıfır sayısının kaçar adet tekrarlandığını bulan program?
n = int(input("Kaç adet sayı gireceksiniz? "))
pozitif_sayi = 0
negatif_sayi = 0
sifir_sayi = 0

for i in range(n):
    sayi = float(input("sayi girin:"))
    if sayi > 0:
        pozitif_sayi += 1
    elif sayi < 0:
        negatif_sayi += 1
    else:
        sifir_sayi += 1

print("Girilen sayılar arasında",pozitif_sayi,"tane pozitif", negatif_sayi," negatif",sifir_sayi, " adet sıfır sayısı bulunmaktadır.")

#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?
ilk_eleman = float(input("Serinin ilk elemanını girin: "))
toplam_eleman_sayisi = int(input("Toplam eleman sayısını girin: "))
artis_degeri = float(input("Artış değerini girin: "))

seri_toplami = 0
for i in range(toplam_eleman_sayisi):
    seri_toplami += ilk_eleman
    ilk_eleman += artis_degeri

print("Serinin toplamı:", seri_toplami)

# Girilen bir sayının asal olup olmadığını bulunuz?
sayi=int(input("sayi gir:"))
for i in range(2,sayi):
    if sayi%i==0:
        print("sayı asal degil")
        break
    else:
        print("sayı asaldır.")
        break

# Girilen sayının basamak değerleri çarpımını bulunuz?
sayi = int(input("Bir sayı girin: "))
carpim = 1
while sayi > 0:
    basamak = sayi % 10
    carpim *= basamak
    sayi //= 10
print("Girilen sayının basamak değerleri çarpımı:", carpim)
# Girilen sayının basamak sayısını ekrana yazdıran program?
sayi = int(input("Bir sayı girin: "))
if sayi < 0:
    sayi *= -1

basamak_sayisi = len(str(sayi))
print("Girilen sayının basamak sayısı:", basamak_sayisi)

# Girilen cümleyi tersten yazdırın? 
cumle = input("Bir cümle girin: ")
tersten = cumle[::-1]
print("Cümlenin tersi:", tersten)


