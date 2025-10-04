# 🔢 Python Data Types — Tipuri de date de bază

## 📘 Tipurile de date fundamentale în Python

În Python, cele mai utilizate tipuri de date sunt:

### 🔹 `int` — Numere întregi
Reprezintă valori numerice fără zecimale.  
Exemple: `5`, `-12`, `1000`  
Sunt utilizate pentru operații aritmetice și numărare.

### 🔹 `float` — Numere reale (zecimale)
Reprezintă valori numerice cu parte fracționară.  
Exemple: `3.14`, `-2.5`, `0.99`  
Folosite pentru calcule științifice sau financiare.

### 🔹 `str` — Șiruri de caractere
Reprezintă textul, delimitat de ghilimele simple sau duble: `'text'` sau `"text"`.  
Exemple: `"Python"`, `'Salut lume'`

### 🔹 `bool` — Valori logice
Reprezintă adevărul unei expresii logice:  
- `True` (adevărat)  
- `False` (fals)  
Sunt folosite în condiții și expresii logice.

---

## 🔄 Conversii între tipuri (Type Casting)

Python permite conversia valorilor între tipuri diferite folosind funcții predefinite:

| Funcție | Descriere | Exemplu |
|----------|------------|----------|
| `int()` | convertește la întreg | `int("5") → 5` |
| `float()` | convertește la număr zecimal | `float("3.14") → 3.14` |
| `str()` | convertește la text | `str(10) → "10"` |
| `bool()` | convertește la valoare booleană | `bool(0) → False`, `bool(1) → True` |

> 💬 *Conversiile sunt utile pentru procesarea datelor în diferite formate și pentru interacțiunea dintre funcții care așteaptă tipuri specifice.*
