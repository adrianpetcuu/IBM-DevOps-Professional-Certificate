# 🧪 Practicing Test Driven Development (TDD)

## 📖 Introducere

**Test Driven Development (TDD)** este o metodologie de dezvoltare software în care scrierea testelor precede implementarea codului efectiv.  
Scopul este de a crea un ciclu continuu de feedback între **cerințe → teste → cod → validare**, reducând erorile și asigurând un design mai curat și modular.

TDD este un element esențial al DevOps și Agile, promovând calitatea, automatizarea și încrederea în livrări frecvente.

---

## 🔁 Ciclul TDD: Red – Green – Refactor

TDD urmează un ciclu simplu în trei pași:

| Pas | Descriere | Rezultat |
|-----|------------|-----------|
| 🔴 **Red** | Scrie un test care eșuează, deoarece funcționalitatea nu există încă. | Testul trebuie să fie *roșu* (fail). |
| 🟢 **Green** | Scrie codul minim necesar pentru ca testul să treacă. | Testul devine *verde* (pass). |
| 🟡 **Refactor** | Curăță codul și testele, fără a schimba comportamentul. | Codul devine mai clar și robust. |

> 💡 Scopul este **claritatea codului și acoperirea testelor**, nu doar trecerea testului.

---

## 🧱 Exemplu practic – Calculul ariei unui triunghi

### 1️⃣ Scriem testul (Red)
```python
# test_triangle.py
import unittest
from triangle import area_of_triangle

class TestTriangle(unittest.TestCase):
    def test_area(self):
        result = area_of_triangle(10, 5)
        self.assertEqual(result, 25)
```

La acest moment, funcția `area_of_triangle()` nu există, deci testul va eșua.

---

### 2️⃣ Implementăm codul minim (Green)
```python
# triangle.py
def area_of_triangle(base, height):
    return (base * height) / 2
```

Rulând testul:
```bash
pytest -v
```
Rezultat:
```
✅ Test passed
```

---

### 3️⃣ Refactorizare
După ce testul trece, verificăm dacă putem simplifica codul:
- Adăugăm validare pentru argumente.
- Adăugăm alte teste (valori negative, zero, etc.).

```python
def area_of_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return (base * height) / 2
```

Și un nou test:
```python
def test_invalid_input(self):
    with self.assertRaises(ValueError):
        area_of_triangle(-3, 4)
```

---

## 🧩 Avantajele TDD

| Beneficiu | Explicație |
|------------|-------------|
| 💡 **Claritate** | Forțează gândirea în termeni de cerințe verificabile. |
| 🔍 **Siguranță** | Codul este permanent testat și validat. |
| 🔄 **Design modular** | Fiecare componentă are un scop bine definit. |
| ⚙️ **Automatizare** | Poți rula sute de teste rapid. |
| 🚀 **Calitate constantă** | Previne regresiile și bug-urile ascunse. |

---

## 🧰 Unelte utile în TDD
| Tool | Scop |
|------|------|
| **unittest** | Framework standard de testare în Python |
| **pytest** | Framework avansat, ușor de extins |
| **nose2** | Runner pentru testare compatibil cu unittest |
| **coverage.py** | Măsoară acoperirea testelor |
| **factory_boy / Faker** | Generează date false pentru testare |

---

## ⚙️ Bune practici TDD

- Scrie **un test mic la un moment dat**.
- Nu scrie cod de producție fără un test care îl motivează.
- Menține testele **independente și clare**.
- Rulează testele la fiecare modificare (automatizat în pipeline).
- Refactorizează codul constant fără a schimba comportamentul.

---

## 🧠 Exemplu complet – Validare cont bancar

### Test
```python
def test_create_account():
    account = Account("John Doe", 100)
    assert account.name == "John Doe"
    assert account.balance == 100
```

### Cod
```python
class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.name = name
        self.balance = balance
```

### Test de eroare
```python
import pytest

def test_negative_balance():
    with pytest.raises(ValueError):
        Account("John", -10)
```

---

## 📈 Integrarea TDD în pipeline DevOps
1. **Commit code** → Trigger pipeline.  
2. **Run unit tests** (TDD).  
3. **Run integration & acceptance tests.**  
4. **Measure coverage** și raportare.  
5. **Deploy only if all tests pass.**

> 🔸 În IBM Cloud și Code Engine, aceste etape pot fi integrate automat în CI/CD pipelines.

---

## 📚 Resurse
- [Python Docs – unittest](https://docs.python.org/3/library/unittest.html)
- [RealPython – Test Driven Development](https://realpython.com/test-driven-development-of-a-django-restful-api/)
- IBM Skills Network – *Practicing Test Driven Development*

---

## ✅ Concluzie
TDD nu este doar o tehnică de testare, ci o **filozofie de design**.  
Prin ciclul Red–Green–Refactor, dezvoltatorii pot livra cod **curat, sigur și testabil**, menținând un ritm constant și o calitate ridicată în cadrul proceselor DevOps.
