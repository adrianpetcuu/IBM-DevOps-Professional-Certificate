
# Scrierea Fișierelor de Pași (Writing Step Files)

## Introducere
În cadrul framework-ului **Behave**, fișierele de pași (*Step Files*) conțin codul Python care implementează acțiunile descrise în scenariile din fișierele `.feature`.

Aceste fișiere leagă textul din pașii Gherkin (Given / When / Then) de funcțiile Python care execută logica propriu-zisă a testului.

---

## Structura unui fișier de pași

Toate fișierele de pași se află, de regulă, într-un folder numit `steps/`.
Exemplu de structură de proiect:

```
my_project/
│
├── features/
│   ├── login.feature
│   └── steps/
│       └── login_steps.py
└── environment.py
```

---

## Importarea modulelor Behave

Pentru a crea pașii, importăm decoratoarele **@given**, **@when**, și **@then** din biblioteca `behave`:

```python
from behave import given, when, then
```

Aceste decoratoare definesc legătura dintre textul din fișierul `.feature` și codul Python corespunzător.

---

## Exemplu complet de fișier Step

```python
from behave import given, when, then

@given('utilizatorul este pe pagina de login')
def step_impl_user_on_login_page(context):
    context.browser.get("https://example.com/login")

@when('introduce date de autentificare valide')
def step_impl_user_enters_valid_credentials(context):
    context.browser.find_element("id", "username").send_keys("testuser")
    context.browser.find_element("id", "password").send_keys("password123")
    context.browser.find_element("id", "login-button").click()

@then('este redirecționat către dashboard')
def step_impl_user_redirected(context):
    assert "dashboard" in context.browser.current_url
```

---

## Reutilizarea pașilor

Behave permite reutilizarea pașilor între scenarii, atâta timp cât textul pașilor este identic.

Exemplu:
```gherkin
Scenario: Login reușit
  Given utilizatorul este pe pagina de login
  When introduce date de autentificare valide
  Then este redirecționat către dashboard

Scenario: Logout reușit
  Given utilizatorul este pe pagina de login
  When introduce date de autentificare valide
  Then este redirecționat către dashboard
```
→ Toți pașii pot fi implementați în același fișier `steps.py`, fără duplicare.

---

## Parametrizarea pașilor

Pașii pot primi argumente dinamice. Exemple:

### 1. Cu text simplu
```gherkin
When utilizatorul introduce parola "secret123"
```
```python
@when('utilizatorul introduce parola "{parola}"')
def step_impl_enter_password(context, parola):
    context.browser.find_element("id", "password").send_keys(parola)
```

### 2. Cu expresii regulate
```gherkin
Given utilizatorul are {numar:d} încercări rămase
```
```python
@given('utilizatorul are {numar:d} încercări rămase')
def step_impl_attempts_left(context, numar):
    context.remaining_attempts = numar
```

---

## Organizarea fișierelor de pași

Recomandări:
- Creează câte un fișier `steps_*.py` pentru fiecare funcționalitate majoră.  
- Păstrează pașii clari, scurți și specifici.  
- Evită codul duplicat.  
- Folosește funcții de utilitate comune pentru logica repetitivă.

---

## Gestionarea erorilor și aserțiunilor

Poți valida comportamentul aplicației folosind `assert` sau `unittest`:

```python
@then('un mesaj de eroare apare pe ecran')
def step_impl_error_message(context):
    message = context.browser.find_element("id", "error").text
    assert message == "Date invalide"
```

---

## Integrarea cu Selenium

Pașii pot folosi **Selenium WebDriver** pentru interacțiunea cu aplicația web:

```python
from selenium import webdriver

@given('browserul este deschis')
def step_impl_browser_open(context):
    context.browser = webdriver.Chrome()

@then('browserul este închis')
def step_impl_close_browser(context):
    context.browser.quit()
```

---

## Concluzie
Fișierele de pași din Behave sunt inima testelor BDD — ele transformă scenariile în acțiuni reale, automatizate.  
Prin folosirea decoratoarelor `@given`, `@when`, `@then`, putem lega specificațiile scrise în limbaj natural de codul executabil, oferind claritate, trasabilitate și testare complet automatizată.
