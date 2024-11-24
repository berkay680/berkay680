import matplotlib.pyplot as plt
import seaborn as sns

# Evet ve Hayır verileri
cevaplar = ["Evet"] * 170 + ["Hayır"] * 830

# Veriyi bar grafiğiyle görselleştirme
cevap_sayilari = {"Evet": 170, "Hayır": 830}

# Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(cevap_sayilari.keys(), cevap_sayilari.values(), color=["green", "red"])
plt.title("Anket Sonuçları: Asgari Ücret Memnuniyeti", fontsize=14)
plt.ylabel("Kişi Sayısı", fontsize=12)
plt.xlabel("Cevaplar", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(cevap_sayilari.values(), labels=cevap_sayilari.keys(), autopct='%1.1f%%', colors=["green", "red"])
plt.title("Asgari Ücret Memnuniyetinin Yüzdesel Dağılımı", fontsize=14)
plt.show()

# Histogram (örnek için rastgele karışık liste)
import random
random.shuffle(cevaplar)  # Rastgele sıralı veri
cevap_numeric = [1 if cevap == "Evet" else 0 for cevap in cevaplar]  # 1: Evet, 0: Hayır

plt.figure(figsize=(8, 6))
sns.histplot(cevap_numeric, bins=2, kde=False, color="blue")
plt.title("Anket Sonuçları Histogramı", fontsize=14)
plt.xlabel("Cevaplar (1: Evet, 0: Hayır)", fontsize=12)
plt.ylabel("Kişi Sayısı", fontsize=12)
plt.xticks([0, 1], ["Hayır", "Evet"], fontsize=10)
plt.show()
