# 🧰 Test Fixtures în Test Driven Development

## 🔍 Ce este un Test Fixture?

Un **test fixture** reprezintă **mediul pregătit pentru rularea testelor** — adică datele, obiectele și condițiile necesare pentru ca un test să se execute corect și repetabil.

Scopul unui *fixture* este de a asigura că fiecare test:
- pornește dintr-o stare controlată,
- nu este influențat de alte teste,
- și lasă mediul curat după terminare.

---

## ⚙️ De ce sunt importante test fixtures?

Fără *fixtures*, testele pot deveni **instabile** sau pot da rezultate diferite la fiecare rulare.  
Prin folosirea lor, ne asigurăm că fiecare test:

- are **date coerente și previzibile**,
- nu modifică starea globală a sistemului,
- și poate fi rulat oricând, independent de alte teste.

---

## 🧠 Exemple de Test Fixtures în `unittest`

În Python, cele mai comune metode pentru definirea *fixtures* sunt:

- `setUp()` – rulează **înainte de fiecare test**.
- `tearDown()` – rulează **după fiecare test**.
- `setUpClass()` și `tearDownClass()` – rulează **o singură dată** înainte și după toate testele din clasă.

---

### 🔹 Exemplu de bază

```python
import unittest

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("🔧 Creare conexiune la baza de date...")
        cls.db = {"users": []}

    @classmethod
    def tearDownClass(cls):
        print("🧹 Închidere conexiune la baza de date...")
        del cls.db

    def setUp(self):
        print("🧩 Pregătire date pentru test...")
        self.db["users"].clear()
        self.db["users"].append({"id": 1, "name": "Ana"})

    def tearDown(self):
        print("🧽 Curățare după test...")
        self.db["users"].clear()

    def test_add_user(self):
        print("✅ Test: adăugare utilizator")
        self.db["users"].append({"id": 2, "name": "Ion"})
        self.assertEqual(len(self.db["users"]), 2)

    def test_remove_user(self):
        print("✅ Test: ștergere utilizator")
        self.db["users"].pop()
        self.assertEqual(len(self.db["users"]), 0)

if __name__ == "__main__":
    unittest.main()
```

---

## 🧩 Explicație

| Metodă | Când se apelează | Scop |
|---------|------------------|------|
| `setUpClass()` | O singură dată, înainte de toate testele | Inițializează resurse globale (ex: conexiuni DB) |
| `setUp()` | Înainte de fiecare test individual | Creează datele necesare pentru acel test |
| `tearDown()` | După fiecare test individual | Curăță mediul testului curent |
| `tearDownClass()` | O singură dată, după toate testele | Eliberează resursele globale |

---

## 🧩 Fixtures în `pytest`

`pytest` oferă un sistem mai flexibil de fixtures, bazat pe decoratori.

### Exemplu:
```python
import pytest

@pytest.fixture
def lista_utilizatori():
    print("🔧 Inițializare listă utilizatori...")
    return ["Ana", "Ion"]

def test_add_user(lista_utilizatori):
    lista_utilizatori.append("Maria")
    assert len(lista_utilizatori) == 3

def test_clear_users(lista_utilizatori):
    lista_utilizatori.clear()
    assert lista_utilizatori == []
```

🔹 **Avantaje în pytest:**
- Fixture-urile pot fi partajate între mai multe fișiere.
- Pot avea diferite niveluri de scop: `function`, `class`, `module`, `session`.
- Se pot combina și reutiliza foarte ușor.

---

## ✅ Cele mai bune practici

1. 🧩 **Menține testele izolate** – fiecare test ar trebui să aibă propriile date.
2. 🔁 **Curăță mediul după rulare** – pentru a evita efecte între teste.
3. ⚙️ **Reutilizează fixture-urile** – pentru a evita duplicarea codului.
4. 💾 **Folosește baze de date temporare sau in-memory** (ex: `sqlite:///:memory:`).
5. 🧱 **Definește clar resursele globale și cele locale**.

---

## ✅ Concluzie

*Test fixtures* sunt elemente esențiale ale testării automate — ele garantează că fiecare test rulează în condiții controlate și previzibile.  
Prin configurarea și curățarea automată a mediului de test, acestea cresc fiabilitatea și repetabilitatea întregului proces TDD.

> 💡 *Un test curat începe și se termină în același loc — fără a lăsa urme în mediul de execuție.*
