import pandas as pd

# BACA DATA
df = pd.read_csv("komentar.csv")

# KAMUS SENTIMEN (SUDAH DIPERLUAS 🔥)
positif = [
    "bagus", "baik", "setuju", "mantap", "keren",
    "suka", "membantu", "enak", "nyaman",
    "hebat", "luar biasa", "top", "oke", "recommended"
]

negatif = [
    "buruk", "jelek", "gak jelas", "ga jelas",
    "tidak jelas", "parah", "sampah", "cringe",
    "aneh", "gagal", "ribet", "susah",
    "capek", "pusing", "bosan", "malas",
    "tidak suka", "ga suka", "gak suka",
    "lemot", "error", "gangguan", "jelek banget"
]

# FUNGSI KLASIFIKASI
def klasifikasi(text):
    text = str(text).lower()

    # PRIORITAS NEGATIF DULU
    for kata in negatif:
        if kata in text:
            return "Kontra"

    for kata in positif:
        if kata in text:
            return "Pro"

    return "Netral"

# PROSES ANALISIS
df["sentimen"] = df["komentar"].apply(klasifikasi)

# HASIL
hasil = df["sentimen"].value_counts()

print("\n=== HASIL ANALISIS SENTIMEN ===")
print(hasil)

# SIMPAN HASIL
df.to_csv("hasil_sentimen.csv", index=False)