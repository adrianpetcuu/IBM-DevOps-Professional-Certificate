# 🏭 Factories & Fakes (Fabrici și Obiecte False) în Testare

## 📖 Overview
În testarea automată, **Factories** (fabrici) și **Fakes** (obiecte false) sunt tehnici care ne ajută să creăm rapid **date/obiecte realiste** fără a depinde de resurse externe (API-uri, DB reale).  
Acestea accelerează TDD, reduc fragilitatea testelor și fac scenariile **deterministe**.

---

## 🧰 Ce sunt „Factories”?
O **Factory** este un utilitar care construiește instanțe de modele/DTO-uri cu **valori implicite valide**.  
În Python, cea mai populară unealtă este **`factory_boy`**, adesea folosită cu **`Faker`** pentru date credibile.

### Avantaje
- Elimină duplicarea codului de inițializare în teste
- Asigură **valori valide** by default (mai puține erori triviale)
- Creează rapid colecții mari de obiecte pentru scenarii/performanță
- Se integrează ușor cu ORM-uri (SQLAlchemy, Django ORM)

### Exemplu: `AccountFactory` (SQLAlchemy)
```python
# factories/__init__.py
import factory
from faker import Faker
from models.account import Account

fake = Faker()

class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    name = factory.LazyAttribute(lambda _: fake.first_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    phone_number = factory.LazyAttribute(lambda _: fake.msisdn())
    disabled = False
```
Utilizare în teste:
```python
def test_create_many_accounts(db_session):
    accounts = [AccountFactory() for _ in range(5)]
    for a in accounts:
        a.create()
    assert len(Account.all()) == 5
```

> 💡 `factory_boy` are și strategia `build()` (nu salvează) vs `create()` (persistă automat pentru unele ORM). Pentru modele simple cu metode custom (`create()`), apelăm explicit.

---

## 🎭 Ce sunt „Fakes”?
Un **Fake** este o implementare simplificată, *funcțională*, care **înlocuiește** o dependență reală scumpă sau greu de folosit în teste (ex: un API, o coadă de mesaje, un repo pe disc).  
Spre deosebire de *Mocks* (care verifică interacțiuni) sau *Stubs* (care doar returnează valori), **Fake-ul conține logică minimală** și se comportă ca un înlocuitor ușor.

### Când folosim Fakes?
- Vrem să rulăm testele **fără rețea / fără DB** reală
- Avem nevoie de **performanță** (mii de teste rapide)
- Dorim determinism (fără latențe sau intermitențe)

### Exemplu Fake Repository
```python
class FakeAccountRepo:
    def __init__(self):
        self._store = {}
        self._next_id = 1

    def add(self, account):
        account.id = self._next_id
        self._store[account.id] = account
        self._next_id += 1
        return account

    def get(self, account_id):
        return self._store.get(account_id)

    def all(self):
        return list(self._store.values())
```

---

## 🧪 Mocks vs Stubs vs Fakes – pe scurt
| Tip | Ce este | Când îl folosesc |
|-----|---------|-------------------|
| **Mock** | Obiect dublură care **verifică interacțiuni** (ce metode au fost apelate și cum) | Când ne interesează contractul/colaborarea |
| **Stub** | Obiect care **returnează valori** predefinite | Când vrem să controlăm rezultatele dependenței |
| **Fake** | Implementare **funcțională, simplificată** a dependenței | Când vrem logică minimală fără resurse externe |
| **Factory** | Utilitar de **creare de obiecte valide** | Când vrem date/obiecte consistente rapid |

---

## ⚙️ Integrare cu `pytest`
### Fixture pentru contextul aplicației + DB in-memory
```python
# tests/conftest.py
import os, sys, pytest
from models import app, db

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

@pytest.fixture(scope="session", autouse=True)
def app_context():
    app.config.update(TESTING=True, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:")
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    yield
    db.drop_all()
    ctx.pop()
```
### Folosirea unei fabrici în teste
```python
from factories import AccountFactory
from models.account import Account

def test_account_factory_creates_valid_accounts():
    a = AccountFactory()
    a.create()
    assert isinstance(a, Account)
    assert len(Account.all()) == 1
```

---

## 🧪 Generarea de date realiste cu `Faker`
```python
from faker import Faker
fake = Faker()
fake.name()         # 'Ana Pop'
fake.email()        # 'ana.pop@example.com'
fake.msisdn()       # '40724567890'
fake.date()         # '2025-09-21'
```
> Pentru teste **deterministe**, fixează seed-ul: `Faker.seed(1234)`.

---

## 🚦 Best Practices
- **Păstrează fabricile aproape de modele** (ușor de găsit/actualizat).
- **Valori implicite valide** în fabrică; suprascrie în test doar ce ai nevoie.
- **Seed pentru Faker** în testele unde contează stabilitatea.
- **Nu abuza de mocks**; preferă **fakes** când poți rula logică simplă offline.
- **Curăță DB** între teste (fixtures `setUp/tearDown` sau `pytest` fixtures).

---

## 🔗 Instalare rapidă
```bash
pip install factory_boy Faker
```

---

## 🧾 Rezumat
- **Factories** → creează obiecte valide, rapid, cu date plauzibile (ex: `AccountFactory`).  
- **Fakes** → înlocuitori funcționali, simpli, pentru dependențe reale (ex: repo în memorie).  
- Combinate, duc la **teste rapide, deterministe și ușor de întreținut** – perfect pentru TDD.

