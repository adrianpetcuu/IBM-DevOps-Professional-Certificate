# 🧩 Anatomia unui Test Case

## 🔍 Ce este un Test Case?

Un **test case** (caz de test) reprezintă **unitatea de bază a testării automate**.  
El definește un set de condiții, pași și rezultate așteptate prin care verificăm dacă o porțiune de cod funcționează corect.

În Python, un test case este de obicei o **metodă** dintr-o **clasă derivată din `unittest.TestCase`**.

---

## 🧱 Structura unui Test Case

Un test case tipic conține următoarele elemente:

1. **Setarea mediului de test (`setUp`)**  
   Creează obiectele și datele necesare înainte de rularea testului.

2. **Execuția codului de testat**  
   Apelează funcția sau metoda pe care dorim să o verificăm.

3. **Aserțiunile (`assert` methods)**  
   Verifică dacă rezultatul real corespunde celui așteptat.

4. **Curățarea mediului (`tearDown`)**  
   Elimină datele temporare sau închide conexiuni după terminarea testului.

---

## 🧠 Exemplu de Test Case în Python

```python
import unittest
from calculator import adunare

class TestCalculator(unittest.TestCase):
    "Exemplu simplu de test case"

    def setUp(self):
        "Pregătește mediul de test"
        self.a = 10
        self.b = 5

    def test_adunare_corecta(self):
        "Testează funcția de adunare"
        rezultat = adunare(self.a, self.b)
        self.assertEqual(rezultat, 15)   # verifică dacă rezultatul este corect

    def tearDown(self):
        "Curăță mediul de test"
        del self.a
        del self.b

if __name__ == '__main__':
    unittest.main()
```

🔹 **Explicație:**  
- `setUp()` rulează automat înainte de fiecare test.  
- `tearDown()` rulează după fiecare test.  
- `assertEqual()` verifică dacă rezultatul obținut este cel așteptat.

---

## 🧩 Metode comune de aserțiune în `unittest`

| Metodă | Descriere | Exemplu |
|---------|------------|----------|
| `assertEqual(a, b)` | Verifică dacă `a == b` | `self.assertEqual(2 + 2, 4)` |
| `assertNotEqual(a, b)` | Verifică dacă `a != b` | `self.assertNotEqual(3 * 3, 8)` |
| `assertTrue(x)` | Verifică dacă expresia este `True` | `self.assertTrue(5 > 3)` |
| `assertFalse(x)` | Verifică dacă expresia este `False` | `self.assertFalse(2 > 5)` |
| `assertIsNone(x)` | Verifică dacă valoarea este `None` | `self.assertIsNone(None)` |
| `assertIsNotNone(x)` | Verifică dacă valoarea nu este `None` | `self.assertIsNotNone(7)` |
| `assertRaises(Error)` | Verifică dacă o excepție este ridicată | `with self.assertRaises(ValueError): func()` |

---

## 🧩 Organizarea claselor de test

Testele sunt grupate în **clase** pentru a menține claritatea și izolarea logică a codului:

```python
class TestUserCreation(unittest.TestCase):
    def test_create_user(self): ...
    def test_invalid_email(self): ...

class TestUserDeletion(unittest.TestCase):
    def test_delete_user(self): ...
```
➡️ Fiecare clasă reprezintă o unitate logică de testare pentru o componentă a aplicației.

---

## ⚙️ Rularea testelor

Pentru a rula toate testele definite:
```bash
python -m unittest discover -v
```
sau pentru un fișier specific:
```bash
python -m unittest test_calculator.py -v
```

---

## ✅ Concluzie

Un **test case** este nucleul procesului de testare automată.  
Prin structurarea clară a testelor — cu pași de inițializare, execuție, validare și curățare — putem:
- asigura stabilitatea codului,
- detecta rapid regresii,
- și menține o bază de testare clară și ușor de extins.

> 💡 *Un test bun este mic, clar, izolat și verifică o singură funcționalitate.*
