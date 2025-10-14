# 🕸️ Web Scraping în Python – Ghid Complet

## 📖 Introducere

**Web scraping** este procesul de colectare automată a datelor din paginile web.  
Într-o lume dominată de informație, web scraping-ul oferă o metodă eficientă de extragere a datelor nestructurate (HTML, XML) și transformarea lor într-un format structurat (CSV, JSON, Excel, baze de date).

---

## 🌍 Cum funcționează Web Scraping-ul

Când accesezi o pagină web, browserul tău trimite o cerere HTTP către serverul site-ului. Serverul răspunde cu un fișier HTML care conține tot conținutul paginii — text, linkuri, imagini, tabele etc.  
Prin web scraping, folosim programe Python pentru a:
1. **Descărca** conținutul HTML (cu `requests` sau `urllib`)
2. **Analiza** structura HTML (cu `BeautifulSoup` sau `lxml`)
3. **Extrage** informațiile dorite (titluri, tabele, linkuri etc.)
4. **Salva** datele într-un format util (CSV, JSON, Pandas DataFrame)

---

## 🧠 Noțiuni de bază HTML

Pentru a face scraping eficient, trebuie să înțelegi structura HTML.

### 🔹 Exemple de elemente HTML:
```html
<html>
  <head><title>Pagina mea</title></head>
  <body>
    <h1>Bun venit!</h1>
    <p id="intro">Aceasta este o pagină exemplu.</p>
    <a href="https://www.example.com">Apasă aici</a>
  </body>
</html>
```

### 🔸 Elemente importante:
- `<tag>` → indică începutul unui element HTML
- `</tag>` → indică sfârșitul elementului
- `<a href="...">` → definește un **link**
- `<p>` → definește un **paragraf**
- `<table>` → definește un **tabel**

---

## 🧰 Biblioteci Python pentru Web Scraping

### 1️⃣ **Requests**
Folosită pentru a descărca conținutul unei pagini web.

```python
import requests

url = "https://www.example.com"
response = requests.get(url)

print(response.status_code)  # 200 înseamnă succes
print(response.text[:500])   # primele 500 caractere din HTML
```

### 2️⃣ **BeautifulSoup**
Folosită pentru analizarea și extragerea datelor din HTML.

```python
from bs4 import BeautifulSoup
import requests

url = "https://www.example.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title)               # titlul paginii
print(soup.find_all('p'))       # toate paragrafele
print(soup.find('a')['href'])   # primul link
```

### 3️⃣ **Pandas**
Poate extrage direct tabele HTML în DataFrame-uri.

```python
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
tables = pd.read_html(url)
df = tables[0]
print(df.head())
```

### 4️⃣ **Selenium**
Folosită pentru a controla un browser (ex. Chrome, Firefox). Poate accesa pagini dinamice generate de JavaScript.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

print(driver.title)
driver.quit()
```

### 5️⃣ **Scrapy**
Framework avansat pentru crawling și colectare de date la scară mare.

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}
```

---

## ⚙️ Bune practici și etică în Web Scraping

✅ Respectă **termenii și condițiile** site-ului.  
✅ Verifică fișierul `robots.txt` (ex. `https://site.com/robots.txt`).  
✅ Nu trimite cereri prea frecvent (folosește `time.sleep()` între cereri).  
✅ Nu copia sau redistribui conținut protejat de drepturi de autor.  
✅ Identifică-te clar în antetul HTTP (ex. `User-Agent`).

---

## 🚨 Erori comune și soluții

| Problemă | Cauză | Soluție |
|-----------|--------|----------|
| `403 Forbidden` | Site-ul blochează cererile automate | Adaugă un User-Agent în header |
| `NoneType` la `find()` | Elementul nu există în HTML | Verifică cu `print(soup.prettify())` |
| Pagina nu se încarcă complet | Conținut dinamic (JavaScript) | Folosește Selenium în loc de Requests |
| Datele sunt într-un iframe | Pagina conține alte URL-uri | Accesează direct linkul iframe-ului |

Exemplu de User-Agent:

```python
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
requests.get(url, headers=headers)
```

---

## 🧼 Curățarea și procesarea datelor extrase

După scraping, datele pot fi „murdare”. Poți folosi:

```python
import pandas as pd

df['col'] = df['col'].str.strip()          # elimină spațiile
df['col'] = df['col'].str.replace('$','')  # elimină caractere inutile
df.dropna(inplace=True)                    # elimină valorile lipsă
```

---

## 🏁 Concluzie

Web Scraping este o tehnică esențială pentru analiștii și dezvoltatorii de date.  
Prin combinarea bibliotecilor Python — `requests`, `BeautifulSoup`, `pandas`, `selenium` — putem transforma internetul într-o sursă vastă de informații structurate.  
Totuși, este important să practicăm **scraping responsabil și etic**, pentru a respecta drepturile de autor și stabilitatea serverelor.

---
