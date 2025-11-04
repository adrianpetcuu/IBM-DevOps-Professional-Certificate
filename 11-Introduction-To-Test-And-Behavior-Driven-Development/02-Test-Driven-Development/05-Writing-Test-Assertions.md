# 🧪 Scrierea Aserțiunilor în Teste (Writing Test Assertions)

## 🔍 Ce este o aserțiune?

O **aserțiune** este o instrucțiune care verifică dacă rezultatul unui test este cel așteptat.  
Dacă expresia evaluată este `True`, testul trece; dacă este `False`, testul eșuează.

Aserțiunile sunt elementul central al testelor — ele decid dacă o funcționalitate funcționează corect sau nu.

---

## ⚙️ Aserțiuni în cadrul `unittest`

Biblioteca `unittest` oferă o gamă largă de metode de aserțiune pentru verificarea rezultatelor.

### Exemple de bază:

```python
import unittest

class TestMath(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)  # Verifică dacă 2+2 = 4

    def test_subtraction(self):
        self.assertNotEqual(5 - 3, 1)  # Verifică dacă 5-3 != 1

    def test_truth(self):
        self.assertTrue(10 > 5)

    def test_falsity(self):
        self.assertFalse(3 > 5)
```

---

## 🧩 Tipuri comune de aserțiuni

| Metodă | Descriere | Exemplu |
|---------|------------|----------|
| `assertEqual(a, b)` | Verifică dacă `a == b` | `self.assertEqual(sum([1,2,3]), 6)` |
| `assertNotEqual(a, b)` | Verifică dacă `a != b` | `self.assertNotEqual(10 - 5, 3)` |
| `assertTrue(expr)` | Verifică dacă expresia este `True` | `self.assertTrue(len([1,2]) == 2)` |
| `assertFalse(expr)` | Verifică dacă expresia este `False` | `self.assertFalse(0 > 1)` |
| `assertIsNone(x)` | Verifică dacă valoarea este `None` | `self.assertIsNone(None)` |
| `assertIsNotNone(x)` | Verifică dacă valoarea nu este `None` | `self.assertIsNotNone("text")` |
| `assertIn(a, b)` | Verifică dacă `a` este în `b` | `self.assertIn(2, [1,2,3])` |
| `assertNotIn(a, b)` | Verifică dacă `a` nu este în `b` | `self.assertNotIn(5, [1,2,3])` |
| `assertRaises(Error)` | Verifică dacă o excepție este ridicată | `with self.assertRaises(ValueError): int("abc")` |

---

## 🧠 Exemple de utilizare

### 1. Testare a valorilor numerice

```python
def test_multiplication(self):
    rezultat = 3 * 4
    self.assertEqual(rezultat, 12)
```

### 2. Testare a conținutului unui obiect

```python
def test_list_contains_value(self):
    valori = [10, 20, 30]
    self.assertIn(20, valori)
```

### 3. Testare a excepțiilor

```python
def test_division_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        rezultat = 10 / 0
```

---

## 🧩 Sad Path Testing

Un *sad path* este un scenariu în care lucrurile merg prost — adică testăm comportamentele așteptate în caz de eroare.  
De exemplu:

```python
def test_invalid_type(self):
    with self.assertRaises(TypeError):
        sum("123")  # sum nu poate procesa un string
```

👉 Scopul acestor teste este să se asigure că aplicația gestionează corect erorile, nu doar cazurile ideale.

---

## 🧾 Exemple complete

```python
import unittest

class TestAssertions(unittest.TestCase):

    def test_string_methods(self):
        self.assertTrue("HELLO".isupper())
        self.assertFalse("Hello".isupper())

    def test_value_comparisons(self):
        self.assertEqual(3 * 3, 9)
        self.assertNotEqual(2 + 2, 5)

    def test_check_membership(self):
        self.assertIn("a", "abc")
        self.assertNotIn("x", "abc")

    def test_raise_exception(self):
        with self.assertRaises(ValueError):
            int("abc")

if __name__ == "__main__":
    unittest.main()
```

---

## ✅ Concluzie

Aserțiunile sunt instrumentele care determină **dacă testele au trecut sau au eșuat**.  
Ele ajută la validarea logicii programului și la prevenirea introducerii de erori în codul existent.

> 💡 *Un test fără aserțiuni nu verifică nimic; aserțiunile sunt inima oricărui test.*
