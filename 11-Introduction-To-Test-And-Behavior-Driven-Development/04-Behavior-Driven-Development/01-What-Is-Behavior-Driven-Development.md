# 🧠 Ce este Behavior Driven Development (BDD)

## 🔍 Definiție

**Behavior Driven Development (BDD)** este o metodologie de dezvoltare software derivată din **Test Driven Development (TDD)**.  
Scopul său principal este de a face procesul de dezvoltare mai **colaborativ**, **clar** și **orientat spre comportamentul așteptat** al aplicației.

BDD se concentrează pe **cum ar trebui să se comporte sistemul din perspectiva utilizatorului final**, nu doar pe implementarea codului.

---

## ⚙️ Principiul de bază

În loc să scrii testele înainte de cod (ca în TDD), în BDD scrii **scenarii de comportament** exprimate în limbaj natural, pe care apoi le transformi în teste automate.

Astfel, toți participanții la proiect (dezvoltatori, testeri, analiști de business) pot înțelege și valida comportamentul sistemului.

---

## 🧩 Limbajul Gherkin

BDD folosește un limbaj simplu, numit **Gherkin**, pentru a descrie comportamentele aplicației prin scenarii logice.  
Acest limbaj folosește o structură standard:

```gherkin
Feature: Login functionality

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard
```

👉 Acest scenariu descrie **comportamentul dorit** al aplicației într-un mod clar, lizibil și ușor de automatizat.

---

## 🧱 Elemente cheie în BDD

| Element | Descriere |
|----------|------------|
| **Feature** | O funcționalitate a sistemului (ex: autentificare, căutare, plată) |
| **Scenario** | Un caz concret de utilizare a funcționalității |
| **Given** | Contextul inițial (starea sistemului înainte de acțiune) |
| **When** | Acțiunea efectuată de utilizator sau de sistem |
| **Then** | Rezultatul așteptat al acțiunii |

---

## 💬 Beneficiile BDD

- Claritate și înțelegere comună între echipe (dev, test, business)  
- Documentație vie, sincronizată cu codul  
- Teste automate direct derivate din specificații  
- Reducerea neînțelegerilor și a comportamentelor neprevăzute  
- Creșterea calității și încrederii în produs

---

## ⚡ Exemple de framework-uri BDD populare

| Limbaj | Framework-uri BDD |
|---------|-------------------|
| **Python** | Behave, pytest-bdd |
| **JavaScript** | Cucumber.js, Jasmine |
| **Java** | Cucumber, JBehave |
| **Ruby** | RSpec, Cucumber |

---

## 🧠 Diferența între TDD și BDD

| Aspect | TDD | BDD |
|---------|-----|-----|
| Focus | Testarea codului | Testarea comportamentului |
| Limbaj | Tehnic (unit tests) | Natural (Gherkin) |
| Scris de | Dezvoltatori | Dezvoltatori + Testeri + Business |
| Scop | Asigurarea corectitudinii codului | Confirmarea comportamentului corect al sistemului |

---

## 🧩 Pe scurt

> **BDD = TDD + limbaj comun + colaborare.**

Behavior Driven Development ajută echipa să **vorbească aceeași limbă** și să se concentreze pe ceea ce contează cel mai mult:  
💡 *comportamentul aplicației din perspectiva utilizatorului.*
