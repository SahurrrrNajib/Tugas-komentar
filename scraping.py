from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# =========================
# SETTING CHROME
# =========================
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

# =========================
# AUTO DRIVER (NO ERROR)
# =========================
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# =========================
# LINK YOUTUBE (BISA LEBIH DARI 1)
# =========================
links = [
    "https://www.youtube.com/watch?v=DI6-4KzRTi8"
]

all_comments = set()

# =========================
# LOOP SETIAP VIDEO
# =========================
for link in links:
    print("\nAmbil dari:", link)
    driver.get(link)
    time.sleep(5)

    # scroll ke komentar
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(3)

    last_total = 0

    # =========================
    # SCROLL AMBIL KOMENTAR
    # =========================
    for i in range(30):
        comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")

        for c in comments:
            text = c.text.strip()
            if text != "":
                all_comments.add(text)

        print(f"Loop {i+1} | Total komentar: {len(all_comments)}")

        # scroll bawah
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

        # stop kalau tidak nambah
        if len(all_comments) == last_total:
            break
        last_total = len(all_comments)

# =========================
# SIMPAN CSV
# =========================
df = pd.DataFrame(list(all_comments), columns=["komentar"])
df.to_csv("komentar.csv", index=False, encoding='utf-8-sig')

print("\n✅ SELESAI")
print("Total komentar:", len(df))

driver.quit()