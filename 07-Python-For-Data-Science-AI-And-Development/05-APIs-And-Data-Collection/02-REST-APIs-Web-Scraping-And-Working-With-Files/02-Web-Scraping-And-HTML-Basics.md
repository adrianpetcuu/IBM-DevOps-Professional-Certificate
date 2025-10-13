# 🕸️ Web Scraping & HTML Basics (în Python)

Acest ghid practic te învață **bazele HTML** și **cum să faci web scraping** în Python în mod **etic, robust și scalabil** — folosind `requests`, `BeautifulSoup` și, când e nevoie, `Selenium`.

---

## 🎯 Obiective
După parcurgere vei putea:
- Înțelege structura unui document **HTML** (tag-uri, atribute, DOM).
- Extrage date cu **CSS Selectors** și **XPath**.
- Trimite cereri HTTP cu **`requests`** și gestionezi **headere, timeouts, retries, sesiuni**.
- Parsezi pagini cu **BeautifulSoup** sau **lxml**.
- Navighezi **pagination**, descarci imagini/fișiere și salvezi datele în **CSV/JSON**.
- Cunoști regulile de **etică & legalitate** (robots.txt, TOS, rate limiting).

---

## 🧱 1) HTML — noțiuni de bază

Un document HTML este format din **tag-uri** (ex: `<div>`, `<a>`, `<p>`) care pot avea **atribute** (ex: `class`, `id`, `href`).

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Exemplu</title>
  </head>
  <body>
    <h1 class="title">Titlul paginii</h1>
    <a href="/produs/123" data-price="49.90">Vezi produs</a>
    <ul id="items">
      <li class="item">Element 1</li>
      <li class="item">Element 2</li>
    </ul>
  </body>
</html>
```

**DOM** (Document Object Model) = arborele elementelor HTML.  
Extragerea datelor se face selectând elemente din DOM după **tag**, **clasă**, **id** etc.

---

## 🎯 2) Selectori — CSS & XPath

### CSS Selectors (ușor de folosit cu BeautifulSoup)
- `h1` – toate h1-urile
- `.item` – toate elementele cu clasa `item`
- `#items` – elementul cu id `items`
- `ul#items > li.item` – li cu clasa `item` doar copii direcți ai lui `ul#items`
- `a[href^="/produs/"]` – link-uri a căror `href` începe cu `/produs/`

### XPath (puternic cu lxml/Selenium)
- `//h1` – toate h1-urile
- `//*[@id="items"]/li[@class="item"]` – li cu clasa `item` sub id `items`
- `//a[starts-with(@href, '/produs/')]` – link-uri cu href ce începe cu `/produs/`
- `string(//h1)` – textul din primul h1

---

## 🌐 3) HTTP Requests în scraping

### De ce să folosești `requests` cu grijă
- Setează **`timeout`** pentru a nu bloca programul.
- Folosește **`Session()`** pentru conexiuni reutilizabile (mai rapid).
- Adaugă **User-Agent** pentru a mima un browser real.
- Respectă **rate limiting** (sleep între cereri).

```python
import time
import requests

BASE = "https://exemplu.tld"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/127.0 Safari/537.36"
}

with requests.Session() as s:
    s.headers.update(headers)
    for page in range(1, 4):
        url = f"{BASE}/catalog?page={page}"
        resp = s.get(url, timeout=15)
        resp.raise_for_status()
        print(f"[{resp.status_code}] {url}")
        time.sleep(1.0)  # respectare rate limiting
```

---

## 🍜 4) Parsare HTML cu BeautifulSoup

```python
from bs4 import BeautifulSoup

html = """
<ul id="items">
  <li class="item">Element 1</li>
  <li class="item">Element 2</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

# prin tag
print([li.text for li in soup.find_all("li")])

# după clasă
print([li.text for li in soup.select("li.item")])

# după id + copil
ul = soup.select_one("ul#items")
print([li.get_text(strip=True) for li in ul.select("> li.item")])
```

### Extrage atribute
```python
html = '<a href="/produs/123" data-price="49.90">Vezi produs</a>'
soup = BeautifulSoup(html, "html.parser")
a = soup.select_one("a")
print(a["href"], a.get("data-price"))
```

---

## ⚡ 5) Parsare rapidă cu lxml (XPath)

```python
from lxml import html as lhtml

doc = lhtml.fromstring("""
<ul id="items">
  <li class="item">Element 1</li>
  <li class="item">Element 2</li>
</ul>
""")

items = doc.xpath('//*[@id="items"]/li[@class="item"]/text()')
print(items)  # ['Element 1', 'Element 2']
```

---

## 🔁 6) Pagination + extragere listă detalii

Exemplu generic pentru listă → intră pe fiecare pagină de detaliu:

```python
import time
import csv
import requests
from bs4 import BeautifulSoup

BASE = "https://exemplu.tld"
OUT = "produse.csv"
headers = {"User-Agent": "Mozilla/5.0 ..."}

def parse_list(html):
    soup = BeautifulSoup(html, "html.parser")
    # Link-uri către produsele individuale
    links = [a["href"] for a in soup.select("a.product-card[href]")]
    # Normalizează link-urile relative
    return [l if l.startswith("http") else BASE + l for l in links]

def parse_detail(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("h1.product-title").get_text(strip=True)
    price = soup.select_one(".price .amount").get_text(strip=True)
    sku = soup.select_one("[data-sku]").get("data-sku")
    return {"title": title, "price": price, "sku": sku}

with requests.Session() as s, open(OUT, "w", newline="", encoding="utf-8") as f:
    s.headers.update(headers)
    writer = csv.DictWriter(f, fieldnames=["title", "price", "sku"])
    writer.writeheader()

    for page in range(1, 4):
        list_url = f"{BASE}/catalog?page={page}"
        r = s.get(list_url, timeout=15); r.raise_for_status()
        for url in parse_list(r.text):
            rd = s.get(url, timeout=15); rd.raise_for_status()
            data = parse_detail(rd.text)
            writer.writerow(data)
            time.sleep(0.8)
        time.sleep(1.0)

print(f"Scris în {OUT}")
```

---

## 🧲 7) Descărcat imagini / fișiere

```python
import os, pathlib, requests

IMG_URL = "https://exemplu.tld/img/produs123.jpg"
IMG_DIR = pathlib.Path("imagini"); IMG_DIR.mkdir(exist_ok=True)

with requests.get(IMG_URL, stream=True, timeout=20) as r:
    r.raise_for_status()
    dest = IMG_DIR / os.path.basename(IMG_URL)
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
print("Salvat:", dest)
```

---

## 🧪 8) Când ai nevoie de Selenium (și alternative)

Folosește **Selenium** dacă:
- Site-ul **încarcă conținutul dinamic** (JS) și nu există endpoint JSON ușor de chemat.
- Trebuie să **simulezi interacțiuni** (click, scroll, login 2FA).

Exemplu minim cu Selenium (Chrome headless):

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless=new")
driver = webdriver.Chrome(options=opts)

try:
    driver.get("https://exemplu.tld")
    h1 = driver.find_element(By.CSS_SELECTOR, "h1.title").text
    print(h1)
finally:
    driver.quit()
```

**Alternative mai rapide** (când se poate):  
- Caută **endpoint-uri XHR/JSON** în DevTools → apelează-le direct cu `requests`.  
- Folosește **Playwright** (mai rapid/stabil decât Selenium în unele scenarii).

---

## 🧱 9) Robusteză: retries, timeouts, proxies, anti-bot

### Retries + backoff
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers["User-Agent"] = "Mozilla/5.0 ..."
resp = session.get("https://exemplu.tld", timeout=15)
```

### Proxies & User-Agent rotation
- Folosește **liste de user-agents** și **proxy rotativ** pentru protecție anti-bot.
- Nu abuza — vezi secțiunea de etică.

---

## 💾 10) Salvare date (CSV, JSON, Parquet)

```python
import csv, json

rows = [{"title": "Produs A", "price": "49.90"}, {"title": "Produs B", "price": "79.00"}]

# CSV
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

# JSON
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
```

Pentru volume mari → **Parquet** (pandas + pyarrow).

---

## 📐 11) Etică, Legal și Bune Practici

- **Respectă `robots.txt`** (ex: `https://site.tld/robots.txt`) și **Termenii & Condițiile** site-ului.
- **Nu supraîncarcă** serverele. Folosește `time.sleep()`, `rate limiting`, `If-Modified-Since` / `ETag`.
- **Identifică-te** politicos prin User-Agent (ex.: include e-mailul tău, dacă e potrivit).
- **Nu colecta date personale** fără bază legală (GDPR/consimțământ).
- **Cache local** pentru a evita cereri repetate.
- Dacă există **API oficial**, **folosește-l** în locul scraping-ului.

---

## 🧰 12) Debugging & DevTools (Chrome/Firefox)
- Inspectează elementele (Right click → Inspect).
- Tab-ul **Network** → vezi cereri XHR, endpoints JSON, headere, cookies.
- **Copy selector** / **Copy XPath** pe elementul dorit.
- Înțelege **lazy-loading** (scroll pentru încărcare).

---

## ✅ Checklist de proiect
- [ ] Verificat `robots.txt` + TOS
- [ ] Definite țintele (ce câmpuri extrag?)
- [ ] Stabilit selecții CSS/XPath rezistente
- [ ] Adăugat `Session()`, `timeout`, `retries`, `backoff`
- [ ] Rate limiting + random delay
- [ ] Salvat în format potrivit (CSV/JSON/DB)
- [ ] Loguri & erori tratate
- [ ] Testat pe eșantion, apoi rulat în batch

---

## 📚 Resurse utile
- **BeautifulSoup**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **lxml**: https://lxml.de/
- **Requests**: https://requests.readthedocs.io/
- **Selenium**: https://www.selenium.dev/documentation/
- **Playwright**: https://playwright.dev/python/
- **XPath Cheatsheet**: https://devhints.io/xpath

---

> **Concluzie:** Începe cu `requests` + `BeautifulSoup` pentru site-uri statice, treci la **XPath/lxml** pentru viteză și la **Selenium/Playwright** doar când conținutul e încărcat dinamic. Respectă regulile de bună conduită și construiește parseri rezistenți la schimbări.
