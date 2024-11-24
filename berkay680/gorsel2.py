import matplotlib.pyplot as plt
import seaborn as sns
import random

# Zam oranları ve kişi sayıları
zam_oranlari = {
    "%50": 460,
    "%30": 180,
    "%100": 360
}

# Veriyi hazırlama
cevaplar = []
for oran, kisi_sayisi in zam_oranlari.items():
    cevaplar.extend([oran] * kisi_sayisi)

# Veriyi karıştır (isteğe bağlı)
random.shuffle(cevaplar)

# Bar Chart (Çubuk Grafik)
plt.figure(figsize=(8, 6))
plt.bar(zam_oranlari.keys(), zam_oranlari.values(), color=["blue", "orange", "green"])
plt.title("Anket Sonuçları: Beklenen Zam Oranları", fontsize=14)
plt.ylabel("Kişi Sayısı", fontsize=12)
plt.xlabel("Zam Oranları", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Pie Chart (Pasta Grafiği)
plt.figure(figsize=(8, 8))
plt.pie(zam_oranlari.values(), labels=zam_oranlari.keys(), autopct='%1.1f%%', colors=["blue", "orange", "green"])
plt.title("Beklenen Zam Oranlarının Yüzdesel Dağılımı", fontsize=14)
plt.show()

# Histogram (Zam oranlarının sıklık dağılımı için)
zam_numeric = [50 if oran == "%50" else 30 if oran == "%30" else 100 for oran in cevaplar]

plt.figure(figsize=(8, 6))
sns.histplot(zam_numeric, bins=3, kde=False, color="purple")
plt.title("Anket Sonuçları Histogramı: Beklenen Zam Oranları", fontsize=14)
plt.xlabel("Zam Oranı (%)", fontsize=12)
plt.ylabel("Kişi Sayısı", fontsize=12)
plt.xticks([30, 50, 100], ["%30", "%50", "%100"], fontsize=10)
plt.show()
