import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Chrome'un ayarlarını yapıyoruz
options = Options()
options.add_experimental_option("detach", True)  # Tarayıcıyı kapatmadan bırak

# WebDriver'ı başlatıyoruz
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Hedef URL'yi açıyoruz
driver.get("https://e-okul.meb.gov.tr/OrtaOgretim/OKL/OOK06006.aspx")
driver.maximize_window()  # Tarayıcı penceresini tam boyut yapıyoruz

# Genel Müdürlük seçimini yapıyoruz
driver.find_element(By.CSS_SELECTOR, "span").click()
time.sleep(2)  # Bekleme süresi
driver.find_element(By.CSS_SELECTOR, ".active-result:nth-child(6)").click()  # İlgili Genel Müdürlük seçimi

# İl seçimi
driver.find_element(By.CSS_SELECTOR, "#ddlIl_chosen span").click()
time.sleep(2)  # Bekleme süresi
istanbul_option = driver.find_element(By.XPATH, "//li[@class='active-result' and text()='İSTANBUL']")  # Burada 'İSTANBUL' dışında başka bir il seçmek için ismi değiştirin
istanbul_option.click()  # İstanbul ilini seçiyoruz

# İlçe seçimi
driver.find_element(By.CSS_SELECTOR, "#ddlIlce_chosen span").click()
time.sleep(2)  # Bekleme süresi
driver.find_element(By.CSS_SELECTOR, ".active-result:nth-child(42)").click()  # Bu 42. değer sizin için farklı olabilir, lütfen uygun olanı seçin

# Okul seçimi
driver.find_element(By.CSS_SELECTOR, "#ddlOkul_chosen span").click()
time.sleep(2)  # Bekleme süresi

# İlgili okul adını girin
school_name = 'Büyükyalı Mesleki ve Teknik Anadolu Lisesi'  # Burada okul adını kendinize göre değiştirin
school_option = driver.find_element(By.XPATH, f"//li[contains(text(), '{school_name}')]")  # Okul seçimi
school_option.click()  # Seçilen okulu tıklıyoruz

# Listele butonuna basıyoruz
driver.find_element(By.ID, "btnGiris").click()  # 'Listele' butonuna basıyoruz

# Tablo verilerinin yüklenmesi için bekliyoruz
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "dgListeDOGM")))  # Tablo yüklendiğinde bekleme

# Tablo verilerini alıyoruz
table = driver.find_element(By.ID, "dgListeDOGM")  # Tabloyu buluyoruz
rows = table.find_elements(By.TAG_NAME, "tr")  # Tablodaki tüm satırları alıyoruz

# Başlık ve veri listelerini başlatıyoruz
header_texts = []
data = []

# Başlıkları çıkarıyoruz
headers = rows[0].find_elements(By.TAG_NAME, "td")  # İlk satır başlıklardır
header_texts = [header.text for header in headers]  # Başlıkları listeye ekliyoruz

# Her bir veri satırını çıkarıyoruz
for row in rows[1:]:  # Başlık satırını atlıyoruz
    cells = row.find_elements(By.TAG_NAME, "td")  # Satırdaki hücreleri alıyoruz
    cell_texts = [cell.text for cell in cells]  # Hücre metinlerini alıyoruz
    data.append(cell_texts)  # Satır verilerini listeye ekliyoruz

# Elde edilen verilerle bir DataFrame oluşturuyoruz
df = pd.DataFrame(data, columns=header_texts)

# DataFrame'i bir Excel dosyasına yazıyoruz
output_file = "Nakil_Datasi.xlsx"  # Çıktı dosyasının adı
df.to_excel(output_file, index=False, engine='openpyxl')  # DataFrame'i Excel dosyasına yazıyoruz

print(f"Veriler başarıyla {output_file} dosyasına yazıldı.")  # Başarı mesajı

# Temizlik: tarayıcıyı kapatıyoruz
driver.quit()  # Tarayıcıyı kapat
