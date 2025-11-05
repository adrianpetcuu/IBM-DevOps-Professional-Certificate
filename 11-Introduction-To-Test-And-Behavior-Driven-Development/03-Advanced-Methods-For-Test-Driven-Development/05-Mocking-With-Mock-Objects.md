# 🧱 Mocking with Mock Objects

## 📖 Overview
**Mock Objects** sunt obiecte false (simulate) care imită comportamentul obiectelor reale, dar fără a executa logica reală.  
Sunt folosite pentru a **verifica interacțiunile** dintre componente și pentru a izola codul testat de dependențele sale externe.

---

## 🎯 Scopul folosirii Mock Objects
- 🔍 Testează **comportamentul** unei funcții sau clase — ce metode sunt apelate și cu ce parametri.  
- 🚀 Înlocuiește componente scumpe sau greu de controlat (API-uri, baze de date, sisteme externe).  
- 🧩 Asigură că logica principală reacționează corect la rezultate simulate.

---

## 🧰 Crearea Mock Objects în Python
Mock Objects pot fi create folosind biblioteca standard `unittest.mock`.

### Exemplu simplu:
```python
from unittest.mock import Mock

mock_obj = Mock()
mock_obj.method.return_value = 42

assert mock_obj.method() == 42
mock_obj.method.assert_called_once()
```

---

## 🧠 Exemple de utilizare

### 1️⃣ Verificarea apelurilor către o dependență
```python
from unittest.mock import Mock

class EmailService:
    def send(self, to, message):
        print(f"Sending '{message}' to {to}")

class NotificationManager:
    def __init__(self, email_service):
        self.email_service = email_service

    def notify(self, user_email, message):
        self.email_service.send(user_email, message)

def test_notification_manager():
    mock_email = Mock()
    manager = NotificationManager(mock_email)

    manager.notify("ana@example.com", "Salut!")

    mock_email.send.assert_called_once_with("ana@example.com", "Salut!")
```

✅ Testul confirmă că metoda `send()` a fost apelată exact o dată, cu parametrii corecți.

---

### 2️⃣ Simularea valorilor de întoarcere
```python
mock_service = Mock()
mock_service.get_data.return_value = {"status": "ok"}

result = mock_service.get_data()
assert result["status"] == "ok"
mock_service.get_data.assert_called_once()
```

---

### 3️⃣ Folosirea `side_effect` pentru a simula excepții
```python
from unittest.mock import Mock

mock_api = Mock()
mock_api.connect.side_effect = ConnectionError("Unable to connect")

try:
    mock_api.connect()
except ConnectionError as e:
    assert str(e) == "Unable to connect"
```

---

## 🧩 Autospec și Validarea Interfeței
Când un mock are `autospec=True`, acesta copiază **semnătura exactă** a obiectului real.  
Astfel, poți preveni erorile de scriere sau apeluri inexistente.

```python
from unittest.mock import create_autospec

class Database:
    def insert(self, record): pass

mock_db = create_autospec(Database)
mock_db.insert({"id": 1})

# mock_db.invalid_call()  # Va genera o eroare pentru că metoda nu există
```

> 💡 Folosește `spec` sau `autospec=True` pentru a face mock-ul mai sigur și realist.

---

## 🧱 Comparativ între tipurile de Mock
| Tip | Descriere | Când se folosește |
|------|------------|------------------|
| **Mock** | Obiect fals care poate fi configurat liber | Când vrem să simulăm metode sau atribute fără restricții |
| **MagicMock** | Extinde `Mock` cu suport pentru operatori (`__len__`, `__getitem__`, etc.) | Când testăm clase complexe (cu iterare, context etc.) |
| **create_autospec()** | Creează mock-uri care respectă semnăturile reale | Când vrem siguranță că apelurile sunt corecte |

---

## 🧪 Exemple combinate

### Cu `MagicMock`
```python
from unittest.mock import MagicMock

mock_list = MagicMock()
mock_list.__len__.return_value = 5

assert len(mock_list) == 5
```

### Cu `spec` (imită o clasă reală)
```python
from unittest.mock import Mock

class Calculator:
    def add(self, x, y): pass

mock_calc = Mock(spec=Calculator)
mock_calc.add.return_value = 10

assert mock_calc.add(5, 5) == 10
mock_calc.add.assert_called_once_with(5, 5)
```

> 🔹 Dacă ai încerca `mock_calc.subtract(1, 2)`, testul ar eșua, pentru că metoda nu există în `Calculator`.

---

## 🧪 Când să folosești Mock Objects
| Situație | Recomandare |
|-----------|--------------|
| Testezi o funcție dependentă de alt obiect | Creează un `Mock` pentru acel obiect |
| Vrei să verifici dacă o metodă a fost apelată | Folosește `assert_called_*` |
| Ai nevoie de valori specifice | Setează `return_value` sau `side_effect` |
| Vrei să copiezi interfața unei clase reale | Folosește `spec` sau `autospec=True` |

---

## ⚙️ Principalele metode utile
| Metodă | Descriere |
|---------|-----------|
| `assert_called()` | Verifică dacă metoda a fost apelată cel puțin o dată |
| `assert_called_once()` | Verifică dacă metoda a fost apelată exact o dată |
| `assert_called_with(*args)` | Verifică parametrii ultimului apel |
| `reset_mock()` | Resetează istoricul apelurilor |
| `side_effect` | Permite simularea excepțiilor sau valorilor dinamice |

---

## 📚 Resurse utile
- [Python Docs – unittest.mock.Mock](https://docs.python.org/3/library/unittest.mock.html#mock-objects)
- [Real Python – Mocking in Python](https://realpython.com/python-mock-library/)
- IBM Skills Network – *Mocking with Patch and Mock Objects*

---

## 🧾 Concluzie
Mock Objects sunt instrumente esențiale în testarea unitară modernă.  
Ele permit testarea izolată a componentelor, verificarea comportamentului și simularea dependențelor fără efecte secundare reale.

> 🔸 Împreună cu `patch()` și `spec`, mock-urile formează baza testelor fiabile și rapide în TDD.
