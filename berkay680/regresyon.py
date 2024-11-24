import pandas as pd
import numpy as np
import random
import statsmodels.api as sm

# Verileri oluşturma
cevaplar_memnuniyet = ["Evet"] * 170 + ["Hayır"] * 830
random.shuffle(cevaplar_memnuniyet)  # Rastgele sıralama
cevaplar_memnuniyet_numeric = [1 if cevap == "Evet" else 0 for cevap in cevaplar_memnuniyet]

cevaplar_zam_orani = ["%50"] * 460 + ["%30"] * 180 + ["%100"] * 360
random.shuffle(cevaplar_zam_orani)  # Rastgele sıralama
cevaplar_zam_orani_numeric = [50 if oran == "%50" else 30 if oran == "%30" else 100 for oran in cevaplar_zam_orani]

# Verilerin DataFrame'e aktarılması
data = {
    "Memnuniyet (Evet=1, Hayır=0)": cevaplar_memnuniyet_numeric[:1000],  # İlk 1000 kişi
    "Beklenen Zam Oranı (%)": cevaplar_zam_orani_numeric[:1000]  # İlk 1000 kişi
}

df = pd.DataFrame(data)

# Bağımsız ve bağımlı değişkenler
X = df["Memnuniyet (Evet=1, Hayır=0)"]
y = df["Beklenen Zam Oranı (%)"]

# X'e sabit terimi ekleyerek model oluşturma (statsmodels için gerekli)
X = sm.add_constant(X)

# Regresyon modelini oluşturma
model = sm.OLS(y, X).fit()

# Sonuçları yazdırma
print(model.summary())
