#LAB4
#PROBLEM1:Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız. 
isim=input("İSMİNİZİ GİRİNİZ:")
soyisim=input("SOY İSMİNİZİ GİRİNİZ:")
print("isim uzunluğu",len(isim))
print("soyisim uzunluğu",len(soyisim))

#PROBLEM2:edges = [(3, 4, 5), (5, 12, 13), (2, 15, 17), (5, 5, 5), (5, 5, 8), (1, 24, 25)]

#Bu listedeki üç sayıdan oluşan demetlerin (tuple) her birinin bir üçgen olup
#olmadığını ve hangi üçgen tipi olduğunu kontrol eden programı yazınız.
kenarlar =[(3,4,5),(5,12,13),(2,15,17),(5,5,5),(5,5,8),(1,24,25)]
for kenar in kenarlar:
    if kenar[0]+kenar[1]>kenar[2]and kenar[0]+kenar[2] > kenar[1] and kenar[1]+kenar[2]>kenar[0] :
        if kenar[0]==kenar[1]==kenar[2]:
         print(f"{kenar} bir eşkenar üçgendir")
         if kenar[0]==kenar[1] or kenar[1]==kenar[2] or kenar[0]==kenar[2]:
            print(f"{kenar} bir ikiz kenar üçgenir")
        if kenar[0]!= kenar[1]and kenar[0]!=kenar[2] and kenar[1]!=kenar[2]:
           print(f"{kenar} bir çeşit kenar üçgendir")    
    else:
       print(f"{kenar} bir üçgen değildir")       
     
#PROBLEM3:kullanıcıdan öğrenci adını ve üç sınav notunu girmesini isteyin.
#Kullanıcı 'q' tuşuna basana kadar bu işlemi tekrarlansın. Ardından,
#öğrenci not bilgilerini ekrana yazdırın, her öğrencinin adını,
#notlarını ve ortalama notunu gösteren programı yazınız.
ogrenciler=[]
while True:
    isim=input("isim giriniz:")
    ogrenciler.append(isim)
    if isim == "q" :
        break
    notlar=[]
    for i in range(3):
        not_gir = float(input(f"{isim} için {i+1}. notu giriniz:"))
        notlar.append(not_gir)
    ortalama= (notlar[0]+notlar[1]+notlar[2])/3
    for i in notlar:
     ogrenci_bilgisi={ 
        "ad": isim,
        "notlar":notlar,
         "ortalama": ortalama }
    print(ogrenci_bilgisi)       