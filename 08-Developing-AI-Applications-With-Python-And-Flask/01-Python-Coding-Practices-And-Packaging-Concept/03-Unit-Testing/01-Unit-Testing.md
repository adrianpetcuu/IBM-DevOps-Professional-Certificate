# ✅ Testare Unitară (Unit Testing) în Python

## 🔹 Ce este testarea unitară?
**Testarea unitară** verifică funcții/metode *izolat*, pentru a confirma că fiecare bucată mică de cod face exact ce trebuie. Scopul: cod **corect**, **sigur** și **ușor de modificat**.

---

## 🎯 De ce este importantă?
- Detectează bug-uri **devreme** (mai ieftin de reparat).
- Permite refactorizări fără frică (ai „plasa de siguranță”).
- Documentează comportamentul dorit al funcțiilor.
- Poate rula automat în CI/CD (GitHub Actions, Jenkins).

---

## 🧩 Termeni de bază
- **Unitate**: funcție, metodă, clasă.
- **Test case**: set de intrări + așteptări.
- **Test suite**: colecție de teste.
- **Fixture**: cod de inițializare/curățare pentru teste (ex.: `setUp`, `tearDown`).

---

## 🛠 Framework-uri populare
- **unittest** – inclus în Python, stil xUnit.
- **pytest** – concis, parametrare puternică, ecosistem bogat.
- **nose** (legacy) – nu mai este menținut.

---

## 📁 Organizare recomandată
```
project/
├─ src/
│  └─ mymath.py
└─ tests/
   ├─ test_mymath.py
   └─ conftest.py        # (pytest) fixtures comune
```
- Fisierele de test încep cu `test_` și conțin funcții/clase `Test*`.

---

## 🧪 Exemplu cu `unittest` (standard library)

**src/mymath.py**
```python
def square(x: int) -> int:
    return x * x

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b
```

**tests/test_mymath_unittest.py**
```python
import unittest
from src.mymath import square, divide

class TestMyMath(unittest.TestCase):
    def test_square_positive(self):
        self.assertEqual(square(3), 9)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_divide_ok(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
```
Rulare:
```bash
python -m unittest
# sau
python -m unittest tests/test_mymath_unittest.py -v
```

---

## 🧪 Exemplu cu `pytest` (concis și puternic)
Instalare:
```bash
pip install pytest
```
**tests/test_mymath_pytest.py**
```python
import pytest
from src.mymath import square, divide

def test_square_basic():
    assert square(4) == 16

@pytest.mark.parametrize("a,b,expected", [(9,3,3), (10,2,5), (5,2,2.5)])
def test_divide_param(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
```
Rulare:
```bash
pytest -q
```

---

## 📋 Aserțiuni uzuale

### `unittest.TestCase`
| Metodă | Exemplu |
|-------|---------|
| `assertEqual(a, b)` | `self.assertEqual(len(items), 3)` |
| `assertTrue(x)` / `assertFalse(x)` | `self.assertTrue(flag)` |
| `assertIs(a, b)` / `assertIsNone(x)` | `self.assertIsNone(result)` |
| `assertIn(a, b)` | `self.assertIn("id", data)` |
| `assertRaises(exc)` | `with self.assertRaises(ValueError): ...` |

### `pytest` (operator `assert`)
- `assert expr` – evaluează expresia și raportează dif-uri utile.
- `with pytest.raises(Exception): ...` – așteaptă excepții.
- `@pytest.mark.parametrize` – rulează același test cu mai multe seturi de date.

---

## 🧰 Fixtures (inițializare/curățare)
### `unittest`
```python
class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = connect_test_db()  # pregătește context
    def tearDown(self):
        self.conn.close()              # eliberează resursele
```
### `pytest`
```python
import pytest

@pytest.fixture
def temp_user():
    return {"id": 1, "name": "Ana"}

def test_user_fixture(temp_user):
    assert temp_user["id"] == 1
```

---

## 🕵️ Mocking (izolarea dependențelor)
```python
from unittest.mock import patch

def fetch_profile(user_id):
    # imaginează-ți că apelează o API externă
    ...

@patch("src.service.fetch_profile", return_value={"id": 1, "name": "Ana"})
def test_service_calls_api(mock_fetch):
    from src.service import user_greeting
    assert user_greeting(1) == "Hello, Ana!"
    mock_fetch.assert_called_once_with(1)
```

---

## 📈 Acoperire (coverage)
```bash
pip install coverage
coverage run -m pytest
coverage report -m
coverage html  # raport frumos în HTML
```

---

## 🔄 Integrare CI (ex. GitHub Actions)
`.github/workflows/tests.yml`
```yaml
name: tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest --maxfail=1 --disable-warnings -q
```

---

## 🧭 Bune practici
- Un test = **un singur comportament** verificat.
- Nume de teste **descriptive** (`test_divide_by_zero_returns_error`).
- Evită dependențele externe reale (folosește **mock** sau **fixtures**).
- Fă testele **deterministe** (fără timp real / rețea).
- Rulează testele în CI pe fiecare commit.
- Păstrează testele **rapide** (sub secunde).

---

## 🛠 Depanare rapidă
- Test „flaky”? → izolează sursa (random, timp, concurență).
- Importuri care eșuează? → verifică `PYTHONPATH` / structura pachetelor.
- Testele nu sunt descoperite? → numește fișierele `test_*.py` și funcțiile `test_*`.

---

## 📚 Resurse
- `unittest`: https://docs.python.org/3/library/unittest.html
- `pytest`: https://docs.pytest.org/
- `coverage.py`: https://coverage.readthedocs.io/
- Mocking: https://docs.python.org/3/library/unittest.mock.html

---

## ✅ Concluzie
Testarea unitară este baza calității software. Începe cu câteva teste simple, rulează-le la fiecare schimbare și integrează-le în CI. Vei câștiga viteză și încredere în codul tău.
