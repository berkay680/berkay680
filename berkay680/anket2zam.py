import random

# Toplam kişi sayısı
toplam_kisi = 1000

# Zam oranlarına göre kişi sayıları
zam_oranlari = {
    "%50": 460,
    "%30": 180,
    "%100": 360
}

# Cevapları oluştur
cevaplar = []
for oran, kisi_sayisi in zam_oranlari.items():
    cevaplar.extend([oran] * kisi_sayisi)

# Cevapları karıştır
random.shuffle(cevaplar)

# Cevapları txt dosyasına yazdır
with open("zam_oranlari_anketi.txt", "w", encoding="utf-8") as dosya:
    for i, cevap in enumerate(cevaplar, 1):
        dosya.write(f"{i}. kişi: {cevap}\n")

print("Sonuçlar 'zam_oranlari_anketi.txt' dosyasına kaydedildi.")
