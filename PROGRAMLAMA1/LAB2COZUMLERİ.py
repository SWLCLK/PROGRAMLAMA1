#LAB2
#PROBLEM 1:Kullanıcının girdiği bir sayının hem 2'ye hemde 3'e bölünebilme durumunu kontrol eden programı kodlayınız.
sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 0 and sayi % 3 == 0:
    print("Girdiğiniz sayı hem 2'ye hem de 3'e bölünebilir.")
else:
    print("Girdiğiniz sayı hem 2'ye hem de 3'e bölünemez.")


#PROBLEM 2 :Problem Bir kredi kartından 2000 TL üzeri alış veriş yapıldığında 100 TLhediye puan, 1000 TL ve üzeri alış veriş yapıldığında 50 TLhediye puan, 1000 TL’nin altında alış veriş yapıldığında 10 TL hediye puan kazanılmaktadır. Klavyeden girilen harcama tutarına
#göre hediye puanı yazan problemin Python kodlarını yazın.
harcama_tutari = float(input("Harcama tutarını giriniz: "))
if harcama_tutari >= 2000:
    hediye_puani = 100
elif harcama_tutari >= 1000:
    hediye_puani = 50
else:
    hediye_puani = 10

print("Aldığınız hediye puanı:", hediye_puani)

#PROBLEM 3:Bir internet satış sitesi alışveriş tutarı 50 TL’nin üzerindeki her kargoyu bedava veriyarına ise 7 TL ilave edilerek, ekrana kargo ücretini ve toplam tutarı yazdırın.
alisveris_tutari = float(input("Alışveriş tutarını giriniz (TL): "))

if alisveris_tutari > 50:
    kargo_ucreti = 0
else:
    kargo_ucreti = 7

toplam_tutar = alisveris_tutari + kargo_ucreti

print("Kargo ücreti:", kargo_ucreti, "TL")
print("Toplam tutar:", toplam_tutar, "TL")

#PROBLEM4:Bir kişiye ait cinsiyet, boy ve kilo bilgilerini alarak aşağıdaki şartlara göre kişinin ideal kiloda olup olmadığını, ideal kiloda değilse kaç kilo alması veya kaç kilo vermesi gerektiğini bulan Python kodunu oluşturunuz. İdeaLKİLO Bayanlarda: Boy-110, Erkeklerde: Boy-108
cinsiyet= str(input("CİNSİYETİ GİRİNİZ :"))
boy= float(input("BOYUNUZU GİRİNİZ:"))
kilo=float(input("KİLONUZU GİRİNİZ:"))
kadın_ideal_kilo= boy-110
erkek_ideal_kilo=boy-108
if cinsiyet== str("kadın") and kilo== kadın_ideal_kilo:
    print("İDEAL KİLODASINIZ")
if cinsiyet== str("kadın") and kilo> kadın_ideal_kilo:
    print(kilo-kadın_ideal_kilo,"KİLO VERMELİSİNİZ")    
if cinsiyet== str("kadın") and kilo< kadın_ideal_kilo:
    print(kadın_ideal_kilo - kilo,"KİLO ALMALISINIZ")    
if cinsiyet== str("erkek")and kilo== erkek_ideal_kilo:
    print("İDEAL KİLODASINIZ")  
if cinsiyet== str("erkek")and kilo>erkek_ideal_kilo:
    print(kilo-erkek_ideal_kilo,"KİLO VERMELİSİNİZ")
if cinsiyet== str("erkek")and kilo<erkek_ideal_kilo:
    print(erkek_ideal_kilo-kilo,"KİLO ALMALISINIZ")


#PROBLEM5:Kullanıcıya Python ya da Java programlama dillerini ve İngilizce dilini bilip bilmediğini soran, Python ya da Javadan birini biliyorsa ve İngilizce dilini biliyorsa “İş alım süreciniz olumlu geçti”, değilse “Aranan pozisyona nitelikleriniz uymamaktadır.” mesajı veren Python kodunu oluşturunuz.
programlama_dili = input("Python ya da Java programlama dillerinden hangisini biliyorsunuz? ").lower()
ingilizce_bilgisi = input("İngilizce dilini biliyor musunuz? (Evet/Hayır) ").lower()

if (programlama_dili == "python" or programlama_dili == "java") and ingilizce_bilgisi == "evet":
    print("İş alım süreciniz olumlu geçti.")
else:
    print("Aranan pozisyona nitelikleriniz uymamaktadır.")


#PROBLEM6:Klavyeden, girilen ay bilgisine göre kuzey yarım kürede hangi mevsimin yaşandığını ekrana yazdıran Python kodunu oluşturunuz.
ay_bilgisi= input("AY GİRİNİZ:")
if ay_bilgisi in ["OCAK","ARALIK","ŞUBAT"] :
    print("KUZEY YARIM KÜREDE KIŞ YAŞANMAKTADIR.")
if ay_bilgisi in ["EYLÜL","EKİM","KASIM"]:
    print("KUZEY YARIM KÜREDE SONBAHAR YAŞANMAKTADIR.")
if ay_bilgisi in ["HAZİRAN","TEMMUZ", "AĞUSTOS"]:
    print("KUZEY YARIM KÜREDE YAZ YAŞANMAKTADIR.")
if ay_bilgisi in [ "MART","NİSAN","MAYIS"]:
    print("KUZEY YARIM KÜREDE İLKBAHAR YAŞANMAKTADIR.")    

#PROBLEM7:Kullanıcının girdiği üç sayı arasındaki en küçük çift sayıyı bulun veya eğer hiç çift sayı yoksa bir mesaj yazdırın.
    sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))

cift_sayilar = []

if sayi1 % 2 == 0:
    cift_sayilar.append(sayi1)
if sayi2 % 2 == 0:
    cift_sayilar.append(sayi2)
if sayi3 % 2 == 0:
    cift_sayilar.append(sayi3)

if len(cift_sayilar) > 0:
    en_kucuk_cift_sayi = min(cift_sayilar)
    print("Girdiğiniz sayılar arasındaki en küçük çift sayı:", en_kucuk_cift_sayi)
else:
    print("Girdiğiniz sayılar arasında çift sayı bulunmamaktadır.")
