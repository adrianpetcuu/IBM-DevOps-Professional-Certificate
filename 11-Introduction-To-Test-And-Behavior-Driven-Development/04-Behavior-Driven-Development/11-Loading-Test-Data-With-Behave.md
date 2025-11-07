
# Încărcarea Datelor de Test în Behave (Loading Test Data with Behave)

## Introducere
În testarea automată, este esențial să poți folosi **date de test** realiste și consistente.  
Behave permite încărcarea și gestionarea acestor date într-un mod organizat și repetabil, folosind fișiere externe (JSON, CSV, YAML) sau chiar baze de date.

Folosirea datelor dinamice asigură că testele sunt flexibile, reutilizabile și independente de datele hardcodate în cod.

---

## Surse comune de date de test
1. **Fișiere JSON** – cele mai des folosite pentru structuri complexe.  
2. **Fișiere CSV** – utile pentru liste simple de valori.  
3. **Fișiere YAML** – ușor de citit, potrivite pentru configurări.  
4. **Baze de date** – pentru aplicații complexe sau testare de integrare.  

---

## Exemplu: Încărcarea datelor dintr-un fișier JSON

### 1. Structura fișierului
Creează un fișier numit `users.json` în folderul `features/data/`:

```json
[
  { "username": "testuser", "password": "12345" },
  { "username": "admin", "password": "admin123" }
]
```

### 2. Încărcarea datelor în fișierul `environment.py`
```python
import json

def before_all(context):
    with open('features/data/users.json') as file:
        context.users = json.load(file)
```

### 3. Folosirea datelor în fișierul de pași
```python
from behave import given, when, then

@given('utilizatorul se autentifică cu datele din fișier')
def step_impl_login_from_file(context):
    user = context.users[0]
    print(f"Autentificare cu utilizatorul: {user['username']}")
```

---

## Încărcarea datelor dintr-un fișier CSV

### 1. Structura fișierului
`data.csv`:
```
username,password
testuser,12345
admin,admin123
```

### 2. Încărcarea fișierului CSV
```python
import csv

def before_all(context):
    with open('features/data/data.csv', newline='') as file:
        reader = csv.DictReader(file)
        context.users = [row for row in reader]
```

### 3. Accesarea datelor
```python
@given('utilizatorul {index:d} este autentificat')
def step_impl(context, index):
    user = context.users[index]
    print(f"Login: {user['username']} - {user['password']}")
```

---

## Încărcarea datelor din YAML (opțional)

Dacă preferi un format mai lizibil, instalează biblioteca `pyyaml`:

```bash
pip install pyyaml
```

### Exemplu de fișier `config.yaml`
```yaml
url: https://example.com
users:
  - username: test1
    password: 1234
  - username: admin
    password: admin123
```

### Cod Python pentru încărcare
```python
import yaml

def before_all(context):
    with open('features/data/config.yaml') as file:
        context.config_data = yaml.safe_load(file)
```

---

## Accesarea datelor în scenarii
```gherkin
Scenario: Verificarea datelor de test
  Given datele de test au fost încărcate
  When aplicația le folosește pentru login
  Then testele rulează cu succes
```

```python
@given('datele de test au fost încărcate')
def step_impl(context):
    assert 'users' in context.config_data
    print("Datele de test au fost încărcate cu succes!")
```

---

## Recomandări bune de practică
✅ Păstrează fișierele de date într-un director dedicat (`features/data/`).  
✅ Nu hardcoda valori sensibile (parole, API keys) direct în teste.  
✅ Folosește `context` pentru a transmite datele între pași.  
✅ Curăță sau resetează datele la finalul testelor, dacă sunt dinamice.  

---

## Concluzie
Încărcarea datelor de test în Behave îți permite să creezi teste flexibile, clare și ușor de întreținut.  
Prin folosirea fișierelor externe, testele devin independente de cod și pot fi adaptate rapid pentru diferite seturi de date sau scenarii de testare.
