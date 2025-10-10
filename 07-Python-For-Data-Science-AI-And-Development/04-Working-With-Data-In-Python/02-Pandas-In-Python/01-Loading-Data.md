
# 📘 Loading Data with Pandas

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Încarci fișiere de date în Pandas DataFrame-uri.  
- Vizualizezi și înțelegi structura datelor încărcate.  
- Explorezi atributele și metodele principale ale unui DataFrame.  
- Salvezi datele din Pandas într-un fișier nou.  

## 🧠 Ce este Pandas?
**Pandas** este o bibliotecă Python foarte populară, folosită pentru **analiza și manipularea datelor**.  
Ea oferă două structuri principale de date:
- **`Series`** → un vector unidimensional (ca o coloană dintr-un tabel).  
- **`DataFrame`** → un tabel bidimensional, cu rânduri și coloane etichetate.  

Pandas permite lucrul ușor cu fișiere: CSV, Excel, JSON, SQL și HTML.

## 📥 Încărcarea datelor într-un DataFrame
```python
import pandas as pd
df = pd.read_csv("data.csv")
```

## 🔍 Explorarea datelor
```python
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
```

## 📊 Accesarea datelor
```python
print(df["CustomerName"])
print(df[["CustomerName", "CustomerCity"]])
print(df.loc[0, "CustomerCity"])
print(df.iloc[3])
```

## ✏️ Schimbarea indexului unui DataFrame
```python
new_index = ['a', 'b', 'c', 'd', 'e']
df.index = new_index
```

## 🔄 Filtrarea datelor
```python
filtered = df[df["TotalSales"] > 5000]
print(filtered)
```

## 💾 Salvarea datelor
```python
df.to_csv("new_data.csv", index=False)
```

## 🧩 Funcții Pandas frecvent folosite
| Funcție / Atribut         | Descriere |
|----------------------------|------------|
| `read_csv()` | Încarcă date dintr-un fișier CSV. |
| `head()` / `tail()` | Afișează primele / ultimele rânduri. |
| `shape` | Returnează dimensiunile (rânduri, coloane). |
| `columns` | Listează toate coloanele. |
| `info()` | Informații despre tipurile de date și valorile lipsă. |
| `describe()` | Statistici descriptive pentru coloane numerice. |
| `unique()` / `nunique()` | Valori unice / număr de valori unice dintr-o coloană. |
| `sort_values()` | Sortează DataFrame-ul după o coloană. |
| `to_csv()` | Salvează DataFrame-ul într-un fișier CSV. |

## 🧠 Concluzie
Prin folosirea bibliotecii **Pandas**, poți:
- încărca rapid date din fișiere CSV sau Excel,  
- le poți vizualiza, filtra și analiza,  
- și poți salva rezultatele într-un format nou.

Pandas este un instrument esențial pentru analiza datelor și este baza multor fluxuri de lucru în Data Science și Machine Learning.
