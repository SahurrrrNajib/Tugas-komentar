from flask import Flask, render_template, request
from wordcloud import WordCloud
import os

app = Flask(__name__)

# =========================
# KAMUS SENTIMEN
# =========================
positif = [
    "bagus", "baik", "mantap", "keren",
    "suka", "enak", "nyaman", "hebat"
]

negatif = [
    "jelek", "buruk", "gak jelas", "parah",
    "sampah", "ribet", "susah", "bosan",
    "malas", "error"
]

# =========================
# FUNGSI KLASIFIKASI
# =========================
def klasifikasi(text):
    text = text.lower()

    for kata in negatif:
        if kata in text:
            return "Kontra"

    for kata in positif:
        if kata in text:
            return "Pro"

    return "Netral"

# =========================
# ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    hasil_prediksi = []
    pro = kontra = netral = 0

    if request.method == "POST":
        komentar_input = request.form["komentar"]
        daftar = komentar_input.split("\n")

        for k in daftar:
            if k.strip() == "":
                continue

            hasil = klasifikasi(k)
            hasil_prediksi.append((k, hasil))

            if hasil == "Pro":
                pro += 1
            elif hasil == "Kontra":
                kontra += 1
            else:
                netral += 1

        # =========================
        # WORDCLOUD
        # =========================
        text = " ".join(daftar)

        if not os.path.exists("static"):
            os.makedirs("static")

        wc = WordCloud(width=800, height=400, background_color="white")
        wc.generate(text)
        wc.to_file("static/wordcloud.png")

    return render_template(
        "index.html",
        hasil_prediksi=hasil_prediksi,
        pro=pro,
        kontra=kontra,
        netral=netral
    )

# =========================
# RUN (WAJIB UNTUK RAILWAY)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)