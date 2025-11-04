# 🧪 Test Driven Development (TDD) și Behavior Driven Development (BDD)

## 💡 Introducere

Test Driven Development (TDD) și Behavior Driven Development (BDD) sunt metodologii moderne de dezvoltare software  
care pun **testarea în centrul procesului de programare**.  
Ambele promovează scrierea codului de calitate, reducerea erorilor și o mai bună colaborare în echipă.

---

## ⚙️ Ce este Test Driven Development (TDD)

**TDD (Dezvoltarea Condusă de Teste)** este o abordare în care testele sunt scrise **înainte** de codul propriu-zis.  
Scopul este ca fiecare funcționalitate să fie confirmată de un test automat care validează comportamentul corect.

### 🔁 Ciclul TDD — „Red → Green → Refactor”

1. **Red (Roșu):** Scrii un test care eșuează (funcționalitatea nu este încă implementată).  
2. **Green (Verde):** Scrii codul minim necesar pentru ca testul să treacă.  
3. **Refactor:** Optimizezi codul păstrând toate testele verzi (valide).

### 🧩 Beneficiile TDD
- Asigură că fiecare linie de cod este verificată automat.  
- Permite detectarea rapidă a erorilor.  
- Încurajează un design modular și curat.  
- Oferă documentație implicită prin teste.  
- Reduce riscul de regresii la modificări ulterioare.

### 📘 Exemplu simplu (Python)

```python
# test_calculator.py
import unittest
from calculator import adunare

class TestCalculator(unittest.TestCase):
    def test_adunare(self):
        self.assertEqual(adunare(2, 3), 5)

# calculator.py
def adunare(a, b):
    return a + b
```

---

## 🤝 Ce este Behavior Driven Development (BDD)

**BDD (Dezvoltarea Condusă de Comportament)** extinde principiile TDD, concentrându-se pe **comportamentul aplicației** din perspectiva utilizatorului final.  
Este o metodologie colaborativă ce implică dezvoltatori, testeri și stakeholderi pentru a defini comportamentele dorite într-un limbaj comun.

### 🗣️ Limbajul Gherkin
BDD utilizează un limbaj simplu și descriptiv numit **Gherkin**, care definește comportamentele prin *scenarii*.

```gherkin
Feature: Autentificare utilizator
  As a user
  I want to log into the system
  So that I can access my dashboard

  Scenario: Login reușit
    Given utilizatorul este pe pagina de login
    When introduce credențiale valide
    Then este redirecționat către dashboard
```

### 🧩 Beneficiile BDD
- Clarifică cerințele înainte de implementare.  
- Creează o punte între echipele tehnice și non-tehnice.  
- Asigură că software-ul se comportă conform așteptărilor utilizatorului.  
- Menține testele sincronizate cu cerințele de business.  
- Permite automatizarea scenariilor de acceptanță.

### ⚙️ Exemple de instrumente
| Limbaj | Framework-uri BDD |
|--------|--------------------|
| Python | `behave`, `pytest-bdd` |
| Java   | `Cucumber`, `JBehave` |
| JavaScript | `Cypress`, `Jest`, `Cucumber.js` |

---

## 🔗 TDD vs BDD

| Caracteristică | TDD | BDD |
|-----------------|-----|-----|
| **Focalizare** | Corectitudinea codului | Comportamentul sistemului |
| **Scris de** | Dezvoltatori | Dezvoltatori, testeri, stakeholderi |
| **Limbaj** | Tehnic (cod de test) | Natural (scenarii Gherkin) |
| **Scop** | Cod funcțional și fără erori | Funcționalități conforme cerințelor de business |
| **Rezultat** | Teste unitare | Teste de acceptanță / comportament |

---

## 🧠 Cum se completează TDD și BDD

- **TDD** te ajută să scrii cod curat, corect și testabil.  
- **BDD** te ajută să construiești software care corespunde nevoilor reale ale utilizatorilor.  
- Împreună, asigură atât **calitatea internă** cât și **alinierea externă** a aplicației.  

Exemplu de flux combinat:
1. Definirea comportamentului în Gherkin (BDD).  
2. Scrierea testelor unitare conform comportamentului (TDD).  
3. Implementarea codului până când toate testele trec.  
4. Validarea comportamentului final automatizat.

---

## 🧭 Concluzie

- **TDD** garantează că software-ul funcționează corect la nivel de cod.  
- **BDD** garantează că software-ul oferă comportamentul dorit de utilizatori.  
- Împreună, oferă o abordare completă de dezvoltare orientată pe **calitate, claritate și colaborare**.  
- Adoptarea TDD și BDD duce la un proces de dezvoltare mai sigur, mai previzibil și mai eficient.

> 💬 „TDD verifică dacă software-ul funcționează. BDD verifică dacă software-ul face ceea ce trebuie.”
