# 💾 Working With and Saving Data in Pandas

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Lucrezi cu date dintr-un DataFrame Pandas.  
- Selectezi, filtrezi și manipulezi coloane și rânduri.  
- Salvezi datele prelucrate în diverse formate de fișiere.  

## 🧠 Ce înseamnă lucrul cu date în Pandas?
După ce încarci un fișier într-un **DataFrame**, Pandas îți permite să vizualizezi, să modifici și să salvezi datele într-un mod foarte flexibil.  
Un DataFrame este similar cu un tabel din Excel — are rânduri, coloane și etichete.  

---

## 📊 Crearea unui DataFrame
```python
import pandas as pd

data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'CustomerName': ['John', 'Anna', 'Mike', 'Sara', 'David'],
    'TotalSales': [2000, 4000, 3000, 1500, 5000]
}

df = pd.DataFrame(data)
print(df)
```

---

## 🔍 Selectarea datelor dintr-un DataFrame

### Selectează o coloană
```python
print(df['CustomerName'])
```

### Selectează mai multe coloane
```python
print(df[['CustomerName', 'TotalSales']])
```

### Selectează rânduri folosind `loc[]` sau `iloc[]`
```python
print(df.loc[0])        # Rândul cu eticheta 0
print(df.iloc[2])       # Al treilea rând (index bazat pe poziție)
```

---

## ✏️ Adăugarea și modificarea coloanelor
```python
df['Region'] = ['East', 'West', 'South', 'North', 'East']
df['Discount'] = [5, 10, 7, 0, 3]

print(df)
```

### Actualizează valori dintr-o coloană
```python
df.loc[2, 'TotalSales'] = 3500
```

---

## 🔄 Filtrarea datelor
```python
filtered_df = df[df['TotalSales'] > 2500]
print(filtered_df)
```

### Filtrare multiplă
```python
filtered_df = df[(df['TotalSales'] > 2500) & (df['Region'] == 'East')]
```

---

## 🧮 Operații utile
```python
print(df.describe())     # Statistici generale
print(df.mean(numeric_only=True))   # Media coloanelor numerice
print(df['TotalSales'].max())       # Valoarea maximă
print(df['Region'].unique())        # Valorile unice dintr-o coloană
```

---

## 💾 Salvarea datelor

După procesare, poți salva DataFrame-ul în diferite formate:

### Salvează ca CSV
```python
df.to_csv('sales_data.csv', index=False)
```

### Salvează ca Excel
```python
df.to_excel('sales_data.xlsx', index=False)
```

### Salvează ca JSON
```python
df.to_json('sales_data.json')
```

### Salvează doar anumite coloane
```python
df[['CustomerName', 'TotalSales']].to_csv('customers_sales.csv', index=False)
```

---

## 📂 Încărcarea dintr-un fișier existent

### Citire CSV
```python
new_df = pd.read_csv('sales_data.csv')
print(new_df.head())
```

### Citire Excel
```python
excel_df = pd.read_excel('sales_data.xlsx')
print(excel_df.info())
```

---

## ⚙️ Modificarea indexului
Poți schimba etichetele rândurilor pentru o identificare mai clară:

```python
df.index = ['a', 'b', 'c', 'd', 'e']
print(df.loc['a'])
```

---

## 🧩 Funcții Pandas importante

| Funcție / Metodă | Descriere |
|------------------|------------|
| `read_csv()` | Încarcă date dintr-un fișier CSV. |
| `read_excel()` | Încarcă date dintr-un fișier Excel. |
| `to_csv()` | Salvează un DataFrame într-un fișier CSV. |
| `to_excel()` | Salvează un DataFrame într-un fișier Excel. |
| `to_json()` | Exportă datele în format JSON. |
| `loc[]` / `iloc[]` | Selectează date pe bază de etichete sau poziție. |
| `describe()` | Returnează statistici descriptive. |
| `unique()` | Returnează valorile unice dintr-o coloană. |

---

## 🧠 Concluzie
Prin acest laborator, ai învățat cum să:
- Creezi și manipulezi un DataFrame.  
- Filtrezi și selectezi date relevante.  
- Salvezi rezultatele în fișiere CSV, Excel sau JSON.  

📘 **Pandas** oferă o gamă largă de funcții care simplifică analiza datelor și pregătirea acestora pentru procesare ulterioară.

---