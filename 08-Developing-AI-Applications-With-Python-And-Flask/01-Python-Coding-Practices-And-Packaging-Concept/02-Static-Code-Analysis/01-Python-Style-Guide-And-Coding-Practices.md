
# 🐍 Ghid de stil Python și bune practici de programare

## 🔹 Descriere generală

Acest document oferă o prezentare a regulilor de **stil Python (PEP 8)** și a **bunelor practici de programare**, pentru a te ajuta să scrii cod clar, lizibil și ușor de întreținut.  
Respectarea acestor standarde este esențială în proiectele individuale și de echipă.

---

## 🧱 1. Convenții generale de stil (PEP 8)

### ✅ Nume de variabile, funcții și clase

| Tip element | Stil recomandat | Exemplu |
|--------------|----------------|----------|
| Variabile | `snake_case` | `user_name`, `total_price` |
| Funcții | `snake_case` | `get_user_data()` |
| Clase | `PascalCase` | `UserProfile`, `DataModel` |
| Constante | `UPPER_CASE` | `MAX_RETRIES`, `API_URL` |

---

### ✅ Spații și indentare
- Indentarea standard: **4 spații per nivel** (nu tab-uri).
- Lasă **o linie goală** între funcții și **două linii goale** între clase.
- Pune **un spațiu înainte și după** operatori:
  ```python
  total = price * quantity
  ```

---

### ✅ Linii și comentarii
- O linie de cod nu trebuie să depășească **79 de caractere**.
- Folosește comentarii **clare și scurte**, doar unde e necesar.
- Folosește **docstring-uri** pentru a descrie scopul funcțiilor:
  ```python
  def calculate_area(radius):
      """Returnează aria unui cerc cu raza dată."""
      return 3.14 * radius ** 2
  ```

---

## 🧩 2. Bune practici în Python

### 🔸 Scrie cod lizibil și curat
- Evită nume vagi de variabile (`x`, `data`) — folosește denumiri descriptive.  
- Împarte codul în funcții mici și logice.  
- Nu repeta codul — aplică principiul **DRY (Don’t Repeat Yourself)**.

### 🔸 Respectă principiul EAFP („Easier to Ask Forgiveness than Permission”)
În loc să verifici tot timpul dacă o operație e validă, folosește `try/except`:
```python
try:
    value = my_dict["key"]
except KeyError:
    value = None
```

### 🔸 Folosește f-string pentru formatarea textelor
```python
name = "Ana"
print(f"Bun venit, {name}!")
```

### 🔸 Respectă structura de bază a unui program Python
```python
def main():
    print("Program principal")

if __name__ == "__main__":
    main()
```

---

## ⚙️ 3. Organizarea fișierelor și modulelor

Structură recomandată:
```
project/
│
├── main.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── tests/
    └── test_helpers.py
```

- Fiecare modul (`.py`) trebuie să aibă un scop clar.  
- Include un fișier `__init__.py` în fiecare folder pentru a-l face un pachet Python.  
- Denumește testele conform convenției `test_*.py`.

---

## 🧠 4. Tipuri de comentarii și documentare

| Tip | Scop | Exemplu |
|------|-------|----------|
| Inline | Explică o linie de cod | `x = 10  # valoare implicită` |
| Block | Explică o secțiune de cod | `# Calculează media notelor` |
| Docstring | Descrie funcții/clase/module | `"""Returnează suma."""` |

---

## 🔍 5. Analiza codului și verificarea stilului

### 🔸 PyLint
Instrument pentru analiza statică a codului. Verifică erorile de sintaxă, stil și bune practici.
```bash
pylint myscript.py
```

### 🔸 Black
Formatează automat codul Python după regulile PEP 8.
```bash
black myproject/
```

### 🔸 Flake8
Verifică erorile de stil, indentare și linii prea lungi.
```bash
flake8 myproject/
```

---

## 🧾 6. Exemple de bune practici

### ❌ Greșit:
```python
def calc(a,b):return a*b
```

### ✅ Corect:
```python
def calculate_area(length, width):
    """Returnează aria unui dreptunghi."""
    return length * width
```

---

## 🧩 7. Alte recomandări utile

- Folosește **type hints** pentru claritate:
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```
- Tratează erorile în mod controlat (nu folosi `except:` fără tip de excepție).
- Scrie teste unitare pentru funcțiile critice.
- Evită importurile wildcard (`from module import *`).

---

## 📚 Resurse utile

- [PEP 8 – Python Style Guide](https://peps.python.org/pep-0008/)  
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)  
- [PyLint Documentation](https://pylint.readthedocs.io/)  
- [Black – Code Formatter](https://black.readthedocs.io/)  

---

## ✅ Concluzie

Urmând aceste reguli și practici, vei scrie cod **mai clar, mai sigur și mai profesionist**.  
Respectarea PEP 8 și utilizarea instrumentelor de analiză statică fac parte dintr-un proces modern de dezvoltare software.

---
