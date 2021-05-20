import time
import random



class Market():


    urun_sayısı = 0
    calısan_sayısı = 0
    meyve = ["Muz", "Çilek", "Karpuz", "Kavun", "Elma"]
    meyve_miktar = [100,50,1000,500,2000]       # Kg Cinsinden Ağırlık
    meyve_fiyat = [12,10,3,2,5]                 # Kg Fiyatı



    sebze = ["Pırasa", "Patlıcan", "Domates", "Salatalık", "Biber", "Soğan"]
    sebze_miktar = [50,80,200,150,200,300]      # Kg Cinsinden Ağırlık
    sebze_fiyat = [7, 4, 3, 2, 5, 2]            # Kg Fiyatı


    et_reyonu = ["Dana Kıyma", "Antrikot", "Kuzu Kuşbaşı", "Paça"]
    et_reyonu_miktar = [300,120,500,200]          # Kg Cinsinden Ağırlık
    et_reyonu_fiyat = [50,80,45,20]               # Kg Fiyatı



    calısanlar = ["Ahmet","Hatice","Raziye","Furkan","Mahmut","Selin","Havva"]
    aktif_kullanıcı = 0


    @classmethod
    def toplam_aktif_kullanıcı(cls):              # Market sistemi içerisindeki toplam aktif kullanıcı sayısı

        return f"Toplam Aktif Kullanıcı Sayısı {cls.aktif_kullanıcı}"


    @classmethod
    def ürün_sayısı(cls):                      # Market içerisindeki toplam ürün sayısı

        Market.urun_sayısı = len(Market.meyve) + len(Market.sebze) + len(Market.et_reyonu)
        return f"Marketteki Toplam Ürün Sayısı {Market.urun_sayısı} tanedir."


    @classmethod
    def meyve_ürün_ekleme(cls,urun_adı,fiyat,miktar):      # Meyve reyonuna yeni getirtilen ürün methodu

        Market.meyve.append(urun_adı)
        Market.meyve_fiyat.append(fiyat)
        Market.meyve_miktar.append(miktar)

        return f"""Eklenen yeni meyve: {urun_adı}
                   Eklenen {urun_adı} miktarı: {miktar} Kg
                   {urun_adı} adlı meyvenin kg fiyatı: {fiyat} TL'dir."""


    @classmethod
    def meyve_fiyat_değiştirme(cls,urun_adı):                     # Reyonda bulunan meyvenin güncel fiyatını değiştirme methodu

        print(f"{urun_adı} ürününün güncel kg fiyatı: {Market.meyve_fiyat[Market.meyve.index(urun_adı)]}")

        yeni_fiyat = int(input(f"{urun_adı} ürünün yeni fiyatını giriniz:"))
        Market.meyve_fiyat[Market.meyve.index(urun_adı)] = yeni_fiyat

        return Market.meyve_fiyat[Market.meyve.index(urun_adı)]

    @classmethod
    def meyve_miktar_değiştirme(cls,urun_adı):          # Depoya yeni aktarılan ürün miktarının methodu

        print(f"{urun_adı} ürünününden toplam {Market.meyve_miktar[Market.meyve.index(urun_adı)]} kg bulunmaktadır.")
        yeni_miktar = int(input(f"Depoya aktarılan {urun_adı} ürününün miktarını(kg cinsinden) giriniz:"))
        Market.meyve_miktar[Market.meyve.index(urun_adı)] += yeni_miktar

        return Market.meyve_miktar[Market.meyve.index(urun_adı)]




    @property
    def meyve_ürün_bilgisi(cls):

        meyve_bilgi = list(zip(Market.meyve, Market.meyve_fiyat, Market.meyve_miktar))

        for a,s,d in meyve_bilgi:

            print(f"{a} meyvenin kg fiyatı {s} TL'dir. Depoda toplam {d} kg ürün bulunmaktadır." + "\n")

            if d < 20:

                print(f"{a} meyvenin kg fiyatı {s} TL'dir. Depoda toplam {d} kg ürün bulunmaktadaır.")
                print("")
                print(f"""{a} adlı ürünün miktarı azalmaktadır ! 
                                Lütfen yeni ürün tedarik edin !""")




    def __init__(self,isim,şifre):

        self.isim = isim
        self.şifre = şifre
        Market.aktif_kullanıcı +=1


    def çalışan_alma(self,kişi_sayısı):

        Market.calısan_sayısı += kişi_sayısı




market = Market()