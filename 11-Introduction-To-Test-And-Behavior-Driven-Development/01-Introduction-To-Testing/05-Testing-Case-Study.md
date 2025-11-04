# 📐 Studiu de caz: Testarea unei funcții pentru calculul ariei unui triunghi

## 💡 Introducere

Acest studiu de caz simplu ilustrează modul în care principiile **Test Driven Development (TDD)** pot fi aplicate pentru a dezvolta și testa o funcție Python care calculează aria unui triunghi.  
Exemplul evidențiază importanța scrierii testelor înaintea implementării efective și verificarea cazurilor de eroare.

---

## 🎯 Scopul

Să dezvoltăm o funcție care calculează aria unui triunghi cunoscând **baza** și **înălțimea**, urmând pașii TDD:  
1. Scrierea unui test care eșuează.  
2. Implementarea funcției minime pentru ca testul să treacă.  
3. Refactorizarea codului.  

Formula matematică utilizată este:  
\[ aria = \frac{baza \times înălțimea}{2} \]

---

## 🧪 Pasul 1: Scrierea testelor (Red Phase)

Creăm mai întâi un fișier de test, fără ca funcția să existe încă.

```python
# test_triangle_area.py
import unittest
from triangle import calculeaza_aria_triunghiului

class TestTriangleArea(unittest.TestCase):
    def test_arie_corecta(self):
        rezultat = calculeaza_aria_triunghiului(10, 5)
        self.assertEqual(rezultat, 25.0)

    def test_valori_negative(self):
        with self.assertRaises(ValueError):
            calculeaza_aria_triunghiului(-3, 6)

    def test_valori_zero(self):
        with self.assertRaises(ValueError):
            calculeaza_aria_triunghiului(0, 5)

if __name__ == "__main__":
    unittest.main()
```

🟥 În acest punct, testele **eșuează**, deoarece funcția `calculeaza_aria_triunghiului()` nu există încă.

---

## 🧠 Pasul 2: Implementarea funcției (Green Phase)

Scriem funcția simplă care trece testele.

```python
# triangle.py

def calculeaza_aria_triunghiului(baza, inaltime):
    if baza <= 0 or inaltime <= 0:
        raise ValueError("Baza și înălțimea trebuie să fie valori pozitive.")
    return (baza * inaltime) / 2
```

✅ După rularea testelor cu `pytest` sau `unittest`, toate testele ar trebui să treacă.

---

## 🧹 Pasul 3: Refactorizare

Dacă testele sunt verzi, putem îmbunătăți lizibilitatea codului fără a schimba comportamentul.

```python
def calculeaza_aria_triunghiului(baza: float, inaltime: float) -> float:
    """
    Calculează aria unui triunghi pe baza lungimii bazei și a înălțimii.
    Ridică ValueError pentru valori negative sau zero.
    """
    if baza <= 0 or inaltime <= 0:
        raise ValueError("Baza și înălțimea trebuie să fie pozitive și nenule.")
    return (baza * inaltime) / 2
```

---

## 🧾 Cazuri de Test Relevante

| Caz de test | Intrare (baza, înălțime) | Rezultat așteptat | Observație |
|--------------|---------------------------|------------------|-------------|
| Caz valid | (10, 5) | 25.0 | Calcul corect |
| Baza negativă | (-3, 6) | Eroare (`ValueError`) | Input invalid |
| Înălțime zero | (8, 0) | Eroare (`ValueError`) | Input invalid |
| Numere reale | (7.5, 3.2) | 12.0 | Calcul corect cu zecimale |

---

## 🔁 Legătura cu TDD

Acest exemplu demonstrează clar ciclul **TDD**:
1. **Red** — testele eșuează inițial.  
2. **Green** — codul minim face testele să treacă.  
3. **Refactor** — codul este îmbunătățit păstrând testele verzi.  

TDD ajută la:
- scrierea unui cod curat și sigur,  
- prevenirea erorilor logice,  
- validarea funcționalității pas cu pas.

---

## 🧭 Concluzie

- Scrierea testelor înaintea codului reduce semnificativ numărul de bug-uri.  
- TDD promovează o dezvoltare disciplinată și previzibilă.  
- Testarea chiar și a funcțiilor simple (ca aria unui triunghi) construiește o bază solidă pentru aplicații complexe.

> 💬 „Un cod fără teste este doar o ipoteză că funcționează.”
