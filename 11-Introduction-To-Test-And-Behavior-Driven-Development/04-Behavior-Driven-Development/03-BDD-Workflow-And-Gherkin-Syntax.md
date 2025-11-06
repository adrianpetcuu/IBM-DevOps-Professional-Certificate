# 🔄 BDD Workflow și Sintaxa Gherkin

## 🧠 Introducere

**Behavior Driven Development (BDD)** este o abordare colaborativă de dezvoltare software care pune accent pe **definirea comportamentului aplicației** din perspectiva utilizatorului final.  
Procesul se bazează pe scenarii clare, exprimate într-un **limbaj comun și ușor de înțeles**, numit **Gherkin**.

---

## ⚙️ Fluxul de lucru (BDD Workflow)

Fluxul de lucru BDD combină comunicarea dintre echipe, testarea automată și implementarea codului.  
Procesul are de obicei următorii pași:

### 1️⃣ Descoperirea (Discovery)
- Echipa (dezvoltatori, testeri, analiști de business) discută despre comportamentele dorite.
- Se stabilesc **cerințele de business** în termeni de comportament, nu de implementare.
- Exemplele concrete se definesc împreună, pentru a evita ambiguitățile.

### 2️⃣ Formularea (Formulation)
- Exemplele definite sunt convertite în **scenarii BDD** folosind **sintaxa Gherkin**.
- Scenariile sunt scrise într-un limbaj natural, dar formal, care poate fi rulat ca test automat.

### 3️⃣ Automatizarea (Automation)
- Scenariile scrise în Gherkin sunt legate de codul real prin funcții denumite **step definitions**.
- Testele automate validează dacă implementarea se comportă conform specificațiilor.

---

## 🧩 Sintaxa Gherkin

**Gherkin** este limbajul folosit pentru a descrie comportamentele aplicației într-un format lizibil pentru oameni și calculatoare.

### 🔹 Structura de bază

```gherkin
Feature: Login functionality

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard
```

### 🔹 Cuvinte-cheie principale

| Cuvânt cheie | Descriere |
|---------------|-----------|
| **Feature** | O funcționalitate majoră a aplicației |
| **Scenario** | O situație concretă care testează un comportament |
| **Given** | Contextul inițial (starea sistemului) |
| **When** | Acțiunea efectuată de utilizator sau sistem |
| **Then** | Rezultatul așteptat după acțiune |
| **And / But** | Condiții suplimentare în același pas |

---

## 💡 Exemple suplimentare

### ✅ Scenariu de căutare

```gherkin
Feature: Search functionality

  Scenario: Searching for an existing product
    Given the user is on the home page
    When the user searches for "laptop"
    Then the system displays a list of laptops
    And the list contains at least one result
```

### ❌ Scenariu de căutare fără rezultate

```gherkin
Scenario: Searching for a product that does not exist
  Given the user is on the home page
  When the user searches for "spaceship"
  Then the system shows a message "No results found"
```

---

## 🧱 Legătura între Gherkin și cod

Fiecare pas din scenariul Gherkin este asociat cu o funcție în cod (numită *step definition*).  
De exemplu, în Python (folosind **Behave**):

```python
from behave import given, when, then

@given('the user is on the login page')
def step_user_on_login_page(context):
    context.browser.get("https://example.com/login")

@when('the user enters valid credentials')
def step_user_enters_credentials(context):
    context.browser.login("user", "password")

@then('the user is redirected to the dashboard')
def step_user_redirected(context):
    assert context.browser.current_url == "https://example.com/dashboard"
```

---

## 🚀 Avantajele Gherkin și BDD Workflow

- **Claritate** — scenariile pot fi citite de oricine din echipă.  
- **Trasabilitate** — fiecare cerință are teste automate asociate.  
- **Colaborare** — toți actorii (business, QA, dev) contribuie la definirea comportamentului.  
- **Calitate** — comportamentele sunt validate înainte ca implementarea să fie finalizată.

---

## 🧩 Pe scurt

> **BDD Workflow** = Colaborare + Comunicare + Testare automată  
> **Gherkin** = Limbaj comun pentru descrierea comportamentului aplicației

Prin folosirea BDD și Gherkin, echipele pot livra software de înaltă calitate, construit corect și în acord cu așteptările utilizatorului final.
