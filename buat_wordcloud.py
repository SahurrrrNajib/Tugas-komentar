import pandas as pd

import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("komentar.csv")

# =========================
# GABUNG SEMUA KOMENTAR
# =========================
text = " ".join(df["komentar"].astype(str))

# =========================
# BUAT WORDCLOUD
# =========================
wc = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(text)

# =========================
# TAMPILKAN
# =========================
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.title("WordCloud Komentar YouTube")
plt.show()

# =========================
# SIMPAN GAMBAR
# =========================
wc.to_file("wordcloud.png")

print("✅ WordCloud berhasil dibuat!")