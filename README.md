# MİLLÎ EĞİTİM BAKANLIĞI SINAVLI/SINAVSIZ OKUL BOŞ KONTENJAN VE SINAVLI OKUL TABAN PUAN BİLGİLERİ ALMA

Bu proje, Selenium ve Pandas kullanarak Python tabanlı bir web kazıma (scraping) aracıdır. e-Okul web sitesinden veri çekerek, bu verileri bir Excel dosyasına aktarmaktadır. Bu araç, kullanıcıların okul bilgilerini kolayca toplaması ve analiz etmesi için tasarlanmıştır.

## Özellikler
- e-Okul sisteminden kullanıcı girişine dayalı veri çekimi.
- Çekilen verilerin Excel dosyasına (`Nakil_Datasi.xlsx`) aktarılması.
- Farklı bölgeler ve okullar için konfigüre edilebilir.

### Gelecek Güncellemeler
- Her 10 dakikada bir otomatik veri çekimi.
- Öğrencinin durumuna göre açılacak kontenjan boşlukları için  otomatik e-posta bildirimleri.

Bu güncellemeler, ilerleyen sürümlerde eklenerek daha fazla kolaylık ve otomasyon sağlayacaktır.

## Gereksinimler

Projeyi çalıştırmadan önce, gerekli bağımlılıkların yüklendiğinden emin olun. `requirements.txt` dosyasında listelenen bağımlılıkları aşağıdaki komut ile yükleyebilirsiniz:

```bash
pip install -r requirements.txt
