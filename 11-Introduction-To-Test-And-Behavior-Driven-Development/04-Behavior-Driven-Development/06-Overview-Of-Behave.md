
# Prezentare generală a Behave

## Introducere
**Behave** este un framework Python pentru **Behavior Driven Development (BDD)** – Dezvoltare Bazată pe Comportament.  
Acesta permite dezvoltatorilor și testerilor să descrie comportamentul software-ului într-un limbaj simplu, ușor de înțeles, folosind sintaxa **Gherkin**.

## Concepte cheie
- **Fișiere de funcționalități (.feature)** – conțin scenarii scrise în format Gherkin (Given / When / Then).  
- **Fișiere de pași (steps/*.py)** – conțin funcțiile Python care implementează acțiunile descrise în fișierele `.feature`.  
- **Environment.py** – definește procesele de inițializare și finalizare (setup/teardown) pentru testele Behave.  
- **Fixtures** – ajută la gestionarea mediului și a resurselor înainte și după rularea testelor.  

---

## Sintaxa Gherkin
Gherkin oferă un format structurat și ușor de citit pentru definirea scenariilor de testare:

```gherkin
Feature: Funcționalitatea de autentificare
  Scenario: Autentificare reușită
    Given utilizatorul se află pe pagina de login
    When introduce date de autentificare valide
    Then este redirecționat către pagina de dashboard
```

---

## Implementarea pașilor (Steps Implementation)

```python
from behave import given, when, then

@given('utilizatorul se află pe pagina de login')
def pasul_utilizator_pe_pagina_de_login(context):
    context.browser.get("https://exemplu.com/login")

@when('introduce date de autentificare valide')
def pasul_introduce_date_valide(context):
    context.browser.find_element("id", "username").send_keys("testuser")
    context.browser.find_element("id", "password").send_keys("parola123")
    context.browser.find_element("id", "login-button").click()

@then('este redirecționat către pagina de dashboard')
def pasul_redirectionare_dashboard(context):
    assert "dashboard" in context.browser.current_url
```

---

## Hook-uri (Setup și Teardown)
Behave folosește **hook-uri** definite în fișierul `environment.py` pentru a gestiona resursele.

```python
def before_all(context):
    # Inițializează mediul de testare
    context.config.setup_logging()

def after_all(context):
    # Curăță resursele la final
    context.browser.quit()
```

---

## Beneficiile folosirii Behave
- Îmbunătățește colaborarea între dezvoltatori, testeri și părțile de business.  
- Produce **documentație vie**, ușor de înțeles și mereu actualizată.  
- Încurajează o definire clară a comportamentului software-ului înainte de implementare.  
- Automatizează testarea de acceptanță pe baza specificațiilor în limbaj natural.  

---

**Behave** conectează implementarea tehnică cu cerințele de business, asigurând claritate, calitate și trasabilitate între echipe.
