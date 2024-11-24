import random

# Toplam kişi sayısı
toplam_kisi = 1000

# Evet ve Hayır cevaplarının sayıları
evet_sayisi = 170
hayir_sayisi = toplam_kisi - evet_sayisi

# Cevapları oluştur
cevaplar = ["Evet"] * evet_sayisi + ["Hayır"] * hayir_sayisi

# Cevapları karıştır
random.shuffle(cevaplar)

# Cevapları txt dosyasına yazdır
with open("anket_sonuclari.txt", "w", encoding="utf-8") as dosya:
    for i, cevap in enumerate(cevaplar, 1):
        dosya.write(f"{i}. kişi: {cevap}\n")

print("Sonuçlar 'anket_sonuclari.txt' dosyasına kaydedildi.")
