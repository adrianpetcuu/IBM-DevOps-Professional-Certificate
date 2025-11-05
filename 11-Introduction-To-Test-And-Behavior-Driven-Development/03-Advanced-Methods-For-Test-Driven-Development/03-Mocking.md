# 🧠 Mocking în Testare

## 📖 Overview
**Mocking** este o tehnică folosită în testarea automată pentru a **simula comportamentul unor obiecte sau funcții reale**.  
Scopul este de a izola unitatea de cod testată de dependențele externe (baze de date, API-uri, servicii etc.), permițând testarea logicii interne fără a executa efectiv acele dependențe.

---

## 🎯 De ce folosim Mocking?
- 🧩 **Izolare:** permite testarea unei componente fără a rula codul dependent.
- ⚙️ **Control:** poți specifica exact ce returnează funcțiile sau obiectele externe.
- ⚡ **Performanță:** testele rulează mult mai rapid (nu fac I/O real, rețea, DB etc.).
- 🧪 **Predictibilitate:** poți simula scenarii de eroare greu de reprodus în mod real.

---

## 🧰 Biblioteci de Mocking în Python
| Library | Description |
|----------|--------------|
| **`unittest.mock`** | Biblioteca standard Python pentru mocking și patching. |
| **`pytest-mock`** | Extensie pentru pytest care simplifică folosirea `mock`. |
| **`mocker` fixture (pytest)`** | Fixture integrată care oferă acces direct la `mock`. |

---

## 🧩 Exemple de bază

### 1️⃣ Mock simplu
```python
from unittest.mock import Mock

# Cream un obiect mock
mock_object = Mock()
mock_object.say_hello.return_value = "Salut, lume!"

# Apelăm metoda
print(mock_object.say_hello())   # -> "Salut, lume!"
```

### 2️⃣ Mock cu argumente
```python
mock = Mock()
mock.add_numbers.return_value = 42

result = mock.add_numbers(10, 20)
print(result)  # 42

# Verificăm dacă metoda a fost apelată
mock.add_numbers.assert_called_once_with(10, 20)
```

### 3️⃣ Mock într-un test real
```python
from unittest import TestCase
from unittest.mock import Mock

class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount):
        response = self.gateway.charge(amount)
        return response == "success"

class TestPaymentProcessor(TestCase):
    def test_payment_success(self):
        mock_gateway = Mock()
        mock_gateway.charge.return_value = "success"

        processor = PaymentProcessor(mock_gateway)
        assert processor.pay(100) is True
        mock_gateway.charge.assert_called_once_with(100)
```

---

## 🧱 Mocks vs Stubs vs Fakes
| Tip | Scop | Descriere |
|------|------|------------|
| **Mock** | Verifică interacțiuni | Înregistrează ce metode au fost apelate și cu ce argumente |
| **Stub** | Returnează date fixe | Nu înregistrează apeluri, doar returnează valori predefinite |
| **Fake** | Implementare simplificată | Rulează logică minimală, de ex. stocare în memorie |

---

## ⚙️ Mock vs Patch
- **Mock** → creezi manual un obiect fals.
- **Patch** → înlocuiești temporar o funcție, clasă sau modul în timpul testului.  
  (Patch-ul este explicat detaliat în fișierul următor: *Mocking With Patch*.)

---

## 🧪 Bune Practici
- Folosește `Mock()` doar când ai nevoie să **verifici comportamente**, nu doar rezultate.
- Testele trebuie să **rămână clare** – prea multe mocks pot ascunde logica reală.
- Evită mock-ul pentru **cod intern** (mockează doar dependențele externe).
- Folosește `spec=` pentru a preveni erori de nume de metode (vezi în *Mocking with Mock Objects*).

---

## 📚 Resurse
- [Python Docs – unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [RealPython: Mocking in Python](https://realpython.com/python-mock-library/)
- IBM Skills Network – *Introduction to Test and Behavior Driven Development*
