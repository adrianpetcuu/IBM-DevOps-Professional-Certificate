# 📂 Lucrul cu Diferite Formate de Fișiere în Python

## 📘 Introducere

În Python, lucrul cu fișiere este esențial pentru prelucrarea și stocarea datelor. Limbajul oferă suport complet pentru formate precum **CSV**, **JSON**, **XLSX (Excel)** și **XML**.  
Prin intermediul bibliotecilor `pandas`, `json`, `openpyxl` și `xml.etree.ElementTree`, putem citi, analiza și scrie fișiere în multiple formate.

---

## 📄 1. Lucrul cu fișiere CSV

CSV (Comma-Separated Values) este unul dintre cele mai comune formate pentru schimbul de date tabulare.

### 🔹 Citirea unui fișier CSV

```python
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/.../addresses.csv"
df = pd.read_csv(filename)
print(df.head())
```

### 🔹 Redenumirea coloanelor

```python
df.columns = ['Prenume', 'Nume', 'Adresă', 'Oraș', 'Stat', 'Cod']
print(df.columns)
```

### 🔹 Accesarea rândurilor și coloanelor

```python
print(df.loc[0])                 # primul rând
print(df.loc[[0,1,2], 'Prenume']) # primele 3 valori din coloana "Prenume"
```

### 🔹 Salvarea datelor într-un CSV

```python
df.to_csv('date_noi.csv', index=False)
```

---

## 🧾 2. Lucrul cu fișiere JSON

JSON (JavaScript Object Notation) este un format ușor de citit de oameni și mașini. Este utilizat frecvent în API-uri și schimb de date.

### 🔹 Crearea și scrierea unui fișier JSON

```python
import json

persoana = {
    "prenume": "Andrei",
    "nume": "Popescu",
    "varsta": 30,
    "adresa": {
        "strada": "Str. Libertății 21",
        "oras": "București",
        "cod_postal": "010203"
    }
}

with open("persoana.json", "w") as f:
    json.dump(persoana, f, indent=4)
```

### 🔹 Citirea unui fișier JSON

```python
with open("persoana.json", "r") as f:
    data = json.load(f)
print(data["adresa"]["oras"])
```

---

## 📊 3. Lucrul cu fișiere Excel (XLSX)

Python permite citirea și scrierea fișierelor Excel folosind biblioteca `pandas` împreună cu `openpyxl`.

### 🔹 Citirea unui fișier Excel

```python
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/.../file_example_XLSX_10.xlsx"
df = pd.read_excel(filename)
print(df.head())
```

### 🔹 Scrierea unui fișier Excel

```python
df.to_excel("rezultate.xlsx", index=False)
```

### 🔹 Transformări rapide cu `transform()`

```python
import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=['a', 'b', 'c'])
df = df.transform(func=lambda x: x + 10)
print(df)
```

---

## 🧩 4. Lucrul cu fișiere XML

XML (eXtensible Markup Language) este un format bazat pe tag-uri, utilizat pentru structuri ierarhice de date.

### 🔹 Crearea unui fișier XML

```python
import xml.etree.ElementTree as ET

angajat = ET.Element('angajat')
detalii = ET.SubElement(angajat, 'detalii')
ET.SubElement(detalii, 'nume').text = 'Ionescu'
ET.SubElement(detalii, 'prenume').text = 'Maria'
ET.SubElement(detalii, 'varsta').text = '29'

tree = ET.ElementTree(angajat)
tree.write('angajat.xml')
```

### 🔹 Citirea unui fișier XML

```python
tree = ET.parse('angajat.xml')
root = tree.getroot()

for elem in root.iter():
    print(elem.tag, ":", elem.text)
```

---

## 🔄 5. Conversii între formate

Python permite conversia ușoară între formate de fișiere.

### 🔸 CSV → JSON
```python
df = pd.read_csv("date.csv")
df.to_json("date.json", orient="records", indent=4)
```

### 🔸 Excel → CSV
```python
df = pd.read_excel("fisier.xlsx")
df.to_csv("fisier.csv", index=False)
```

### 🔸 JSON → DataFrame
```python
import json
with open("persoana.json", "r") as f:
    data = json.load(f)
df = pd.DataFrame([data])
print(df)
```

---

## ⚙️ 6. Bune practici

✅ Folosește `with open()` pentru a închide automat fișierele.  
✅ Verifică encoding-ul (UTF-8, ISO-8859-1) pentru fișiere text.  
✅ Manipulează excepțiile (`try...except`) la citirea fișierelor.  
✅ Normalizează datele (șterge spațiile, convertește la tipuri corecte).  
✅ Evită fișierele mari în memorie — lucrează pe bucăți (`chunksize`).

---

## 🚨 7. Erori frecvente

| Problemă | Cauză | Soluție |
|-----------|--------|----------|
| `UnicodeDecodeError` | Fișierul are un alt encoding | Specifică `encoding="utf-8"` |
| `FileNotFoundError` | Calea fișierului e greșită | Verifică path-ul complet |
| `ValueError` în `read_excel()` | Format invalid | Instalează `openpyxl` |
| `json.decoder.JSONDecodeError` | Structură JSON invalidă | Verifică ghilimelele și parantezele |

---

## 🏁 Concluzie

Manipularea fișierelor este una dintre abilitățile de bază ale unui programator Python.  
Prin utilizarea corectă a bibliotecilor standard și `pandas`, putem:

- Citi, analiza și exporta date din surse diferite  
- Converti între formate (CSV ↔ JSON ↔ Excel ↔ XML)  
- Integra aceste date în aplicații web, baze de date și proiecte de analiză

📘 **Python transformă orice tip de fișier într-o sursă accesibilă de informație.**

---

