# 🧩 Exemplu de Behavior Driven Development (BDD)

## 🧠 Introducere

Pentru a înțelege mai bine cum funcționează **Behavior Driven Development (BDD)** în practică, să analizăm un exemplu complet de implementare.  
Acest exemplu demonstrează cum echipa definește comportamentul așteptat al aplicației, îl exprimă în limbaj **Gherkin**, și apoi îl automatizează cu ajutorul codului de testare.

---

## 🧱 Scenariul: Autentificarea utilizatorului

### 🔹 Cerință de business:
> „Ca utilizator, vreau să mă pot autentifica folosind numele de utilizator și parola, astfel încât să pot accesa contul meu.”

---

## 🧩 1️⃣ Definirea comportamentului în Gherkin

```gherkin
Feature: User login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid username and password
    Then the system redirects the user to the dashboard

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters an incorrect password
    Then the system displays an error message "Invalid credentials"
```

👉 Acest fișier poate fi salvat ca `login.feature`.  
El descrie **două comportamente** distincte ale aplicației — unul pozitiv (happy path) și unul negativ (sad path).

---

## ⚙️ 2️⃣ Implementarea codului de testare

Fiecare pas din fișierul `.feature` este legat de o funcție Python, numită *step definition*.  
De exemplu, folosind framework-ul **Behave**:

```python
# features/steps/login_steps.py

from behave import given, when, then
from my_app import login_system

@given('the user is on the login page')
def step_user_on_login_page(context):
    context.page = login_system.open_login_page()

@when('the user enters a valid username and password')
def step_user_enters_valid_credentials(context):
    context.response = login_system.login("john_doe", "correct_password")

@when('the user enters an incorrect password')
def step_user_enters_invalid_credentials(context):
    context.response = login_system.login("john_doe", "wrong_password")

@then('the system redirects the user to the dashboard')
def step_user_redirected(context):
    assert context.response == "dashboard"

@then('the system displays an error message "Invalid credentials"')
def step_error_message(context):
    assert context.response == "Invalid credentials"
```

---

## 🧩 3️⃣ Executarea testelor BDD

După definirea fișierului `.feature` și a pașilor, rularea testelor se face cu comanda:

```bash
behave
```

Rezultatul va afișa:
```
Feature: User login
  Scenario: Successful login with valid credentials  PASSED
  Scenario: Unsuccessful login with invalid credentials  PASSED
```

✔️ Dacă ambele scenarii trec, știm că funcționalitatea de autentificare se comportă corect.

---

## 🧠 4️⃣ Beneficii demonstrate în exemplu

| Beneficiu | Cum se aplică în exemplu |
|------------|--------------------------|
| **Claritate** | Toți membrii echipei pot citi și înțelege scenariile Gherkin |
| **Trasabilitate** | Fiecare cerință de business are teste automate asociate |
| **Documentație vie** | Fișierul `.feature` servește ca document actualizat automat |
| **Testare completă** | Sunt acoperite atât cazurile pozitive, cât și cele negative |

---

## 💡 Concluzie

Acest exemplu arată cum **BDD transformă cerințele de business în teste automate**, ușor de înțeles și întreținut.  
Prin definirea clară a comportamentelor și colaborarea între echipe, se obține:
- cod de calitate superioară,  
- teste relevante,  
- și un produs care se comportă exact așa cum așteaptă utilizatorul final.

> **Behavior Driven Development = claritate, colaborare și comportament verificabil.**
