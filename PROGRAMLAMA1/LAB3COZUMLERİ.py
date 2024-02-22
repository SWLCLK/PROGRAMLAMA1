#LAB3
#PROBLEM1 :1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
for sayi in range(1, 101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print(sayi)

#PROBLEM2:Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
sayi = int(input("Bir sayı giriniz: "))

tek_toplam = 0
cift_toplam = 0

for i in range(1, sayi + 1):
    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i

print("Girilen sayıya kadar olan tek sayıların toplamı:", tek_toplam)
print("Girilen sayıya kadar olan çift sayıların toplamı:", cift_toplam)


#PROBLEM3:parola=input("PAROLA GİRİNİZ:")
list=["ö","ç","ş","ı","ğ","ü","i"]
for karakter in list:
    if karakter in list:
     print("TÜRKÇE KAREKTER KULLANMAYINIZ") 
     break
    if karakter not in list:
       print("PAROLANIZ UYGUN")
       break

 #PROBLEM4:Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.
# İlk sayıyı kullanıcıdan alalım ve en küçük sayı olarak atayalım
en_kucuk = int(input("1. sayıyı giriniz: "))

# Kalan 4 sayı için döngü kullanalım
for i in range(2, 6):
    sayi = int(input(f"{i}. sayıyı giriniz: "))  # Kullanıcıdan diğer sayıları alalım
    if sayi < en_kucuk:
        en_kucuk = sayi  # Eğer alınan sayı en küçükse, en küçük değeri güncelleyelim

print("En küçük sayı:", en_kucuk)
 
#PROBLEM5:1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.
for sayi in range(10, 0, -1):
    print(sayi)
 