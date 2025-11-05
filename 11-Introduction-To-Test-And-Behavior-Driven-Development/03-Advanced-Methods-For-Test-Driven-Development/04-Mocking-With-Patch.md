# 🧩 Mocking with Patch (Simularea cu Patch)

## 📖 Overview
**Patching** este o tehnică din `unittest.mock` care permite **înlocuirea temporară** a unei funcții, clase sau metode dintr-un modul în timpul rulării testelor.  
Scopul este de a izola unitatea testată de componentele externe și de a **controla comportamentul** dependențelor sale.

---

## ⚙️ Cum funcționează `patch`
`patch` înlocuiește obiectul specificat cu un **mock** doar în timpul testului, apoi îl restabilește la valoarea originală.

### Sintaxă de bază:
```python
from unittest.mock import patch

@patch('path.to.object')
def test_something(mock_object):
    # mock_object este mock-ul injectat automat
    ...
```
sau cu `with`:
```python
with patch('path.to.object') as mock_object:
    ...
```

---

## 🎯 Avantajele folosirii `patch`
- Nu modifică codul sursă.
- Înlocuiește temporar o dependență reală (ex: API, DB).
- Poți seta `return_value`, `side_effect`, sau `spec` pentru control total.
- Automat revine la starea originală după test.

---

## 🧪 Exemple practice

### 1️⃣ Patching o funcție
```python
# app/utils.py
def get_temperature():
    return 22

# app/weather.py
from app.utils import get_temperature

def is_hot():
    return get_temperature() > 25
```

Test:
```python
from unittest.mock import patch
from app.weather import is_hot

@patch('app.weather.get_temperature', return_value=30)
def test_is_hot(mock_temp):
    assert is_hot() is True
    mock_temp.assert_called_once()
```

> 🔹 Observă: am patch-uit `app.weather.get_temperature`, nu `app.utils.get_temperature`  
> pentru că în modulul `weather` a fost **importată** funcția `get_temperature`.  
> `patch` trebuie aplicat acolo unde obiectul este *folosit*, nu unde este *definit*.

---

### 2️⃣ Patching o clasă
```python
# app/payments.py
class Gateway:
    def charge(self, amount):
        return "success"

class PaymentService:
    def pay(self, amount):
        gateway = Gateway()
        return gateway.charge(amount) == "success"
```

Test:
```python
from unittest.mock import patch
from app.payments import PaymentService

@patch('app.payments.Gateway')
def test_payment(mock_gateway_class):
    mock_gateway = mock_gateway_class.return_value
    mock_gateway.charge.return_value = "success"

    service = PaymentService()
    assert service.pay(100) is True
    mock_gateway.charge.assert_called_once_with(100)
```

> 🔹 `mock_gateway_class` este mock-ul clasei `Gateway`, iar `mock_gateway_class.return_value`
> este instanța returnată când se face `Gateway()` în cod.

---

### 3️⃣ Patching folosind context manager
```python
from unittest.mock import patch

def test_patch_context_manager():
    with patch('module.function', return_value="mocked!") as mock_func:
        result = module.function()
        assert result == "mocked!"
        mock_func.assert_called_once()
```

---

## 🎭 Patching valori de întoarcere (return values)
Uneori vrem doar să controlăm ce returnează o funcție.

```python
@patch('services.api.call_api', return_value={"status": "ok"})
def test_api_call(mock_api):
    response = services.api.call_api()
    assert response["status"] == "ok"
```

### Cu efecte secundare (side effects)
```python
def raise_error():
    raise ValueError("Connection failed")

@patch('services.api.call_api', side_effect=raise_error)
def test_api_error(mock_api):
    with pytest.raises(ValueError):
        services.api.call_api()
```

---

## 💡 Cazuri tipice pentru patching
| Caz | Exemplu |
|-----|----------|
| Testarea unei funcții care apelează altă funcție | `@patch('app.module.helper_function')` |
| Simularea unei clase externe (DB, API) | `@patch('app.module.ExternalService')` |
| Înlocuirea unei variabile de configurare | `@patch('app.module.CONFIG', new="test_value")` |
| Evitarea apelurilor rețea | `@patch('requests.get')` |

---

## 🧱 Patch vs Mock
| Concept | Descriere |
|----------|------------|
| **Mock** | Creezi manual un obiect fals pentru a verifica comportamentul. |
| **Patch** | Înlocuiește automat o dependență reală cu un mock temporar. |

---

## 🧠 Bune Practici
- Aplică `patch` **acolo unde este folosit obiectul**, nu unde este definit.
- Dacă ai mai multe patch-uri, ordinea lor contează (de sus în jos în decorator).
- Evită patch-uri globale — folosește `with patch()` în testele scurte.
- Combină cu `autospec=True` pentru a valida numele și semnăturile metodelor.

---

## 📚 Resurse utile
- [Python Docs – unittest.mock.patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
- [RealPython – Understanding the Patch Decorator](https://realpython.com/python-mock-library/#patch)
- IBM Skills Network – *Mocking with Patch and Mock Objects*
