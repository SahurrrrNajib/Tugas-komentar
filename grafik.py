import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hasil_sentimen.csv")

data = df["sentimen"].value_counts()

plt.figure()
data.plot(kind='bar')
plt.title("Grafik Sentimen Komentar YouTube")
plt.xlabel("Sentimen")
plt.ylabel("Jumlah")

plt.show()