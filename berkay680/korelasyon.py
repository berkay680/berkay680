import pandas as pd
import numpy as np
import random

# Soru 1: Asgari ücretten memnuniyet verileri
cevaplar_memnuniyet = ["Evet"] * 170 + ["Hayır"] * 830
random.shuffle(cevaplar_memnuniyet)  # Rastgele sıralama
cevaplar_memnuniyet_numeric = [1 if cevap == "Evet" else 0 for cevap in cevaplar_memnuniyet]

# Soru 2: Beklenen zam oranı verileri
cevaplar_zam_orani = ["%50"] * 460 + ["%30"] * 180 + ["%100"] * 360
random.shuffle(cevaplar_zam_orani)  # Rastgele sıralama
cevaplar_zam_orani_numeric = [50 if oran == "%50" else 30 if oran == "%30" else 100 for oran in cevaplar_zam_orani]

# Verilerin birleştirilmesi
data = {
    "Memnuniyet (Evet=1, Hayır=0)": cevaplar_memnuniyet_numeric[:1000],  # İlk 1000 kişi
    "Beklenen Zam Oranı (%)": cevaplar_zam_orani_numeric[:1000]  # İlk 1000 kişi
}

df = pd.DataFrame(data)

# Korelasyon analizleri
pearson_corr = df["Memnuniyet (Evet=1, Hayır=0)"].corr(df["Beklenen Zam Oranı (%)"], method="pearson")
spearman_corr = df["Memnuniyet (Evet=1, Hayır=0)"].corr(df["Beklenen Zam Oranı (%)"], method="spearman")
kendall_corr = df["Memnuniyet (Evet=1, Hayır=0)"].corr(df["Beklenen Zam Oranı (%)"], method="kendall")

# Sonuçları yazdırma
print(f"Pearson Korelasyon Katsayısı: {pearson_corr:.2f}")
print(f"Spearman Korelasyon Katsayısı: {spearman_corr:.2f}")
print(f"Kendall Korelasyon Katsayısı: {kendall_corr:.2f}")

# Korelasyon matrisini görselleştirme
import seaborn as sns
import matplotlib.pyplot as plt

# Korelasyon matrisi
corr_matrix = df.corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.show()
