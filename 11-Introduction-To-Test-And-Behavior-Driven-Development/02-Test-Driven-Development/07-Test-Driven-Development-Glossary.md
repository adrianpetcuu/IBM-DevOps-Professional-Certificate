# 📘 Glosar și Concepte – Test Driven Development (TDD)

## 🧩 Termeni și definiții

| **Termen** | **Definiție** |
|-------------|---------------|
| **CD** | *Continuous Delivery* – procesul de livrare continuă a codului în producție, automatizat și testat. |
| **CI** | *Continuous Integration* – integrarea continuă a codului, prin care schimbările sunt testate automat pentru a evita conflictele. |
| **Code coverage** | Procentul de cod care este executat în timpul rulării testelor automate. |
| **Doctest** | Unealtă care permite scrierea testelor direct în docstring-uri sau comentarii din cod. |
| **Nose** | Un test runner care permite adăugarea de culoare, formatare și rapoarte în rezultatele testelor. |
| **Peek** | Comandă folosită pentru a vizualiza elementul din vârful stivei fără a-l elimina. |
| **Pinocchio** | Plugin care adaugă culoare rezultatelor testelor. |
| **Pop** | Comandă care elimină un element din stivă. |
| **Push** | Comandă care adaugă (împinge) un element într-o stivă. |
| **Pytest** | Framework de testare Python care oferă un număr nelimitat de funcții `setup` și `teardown`, simplificând testarea. |
| **PyUnit** | Cunoscut și ca `unittest`. Este framework-ul de testare standard inclus în Python. |
| **Red/Green/Refactor** | Denumirea ciclului TDD: scrii un test care eșuează (*red*), adaugi codul minim pentru a-l face să treacă (*green*), apoi refactorizezi codul pentru a-l îmbunătăți. |
| **RSpec** | Framework foarte popular pentru Ruby, disponibil și pentru Python. |
| **setUpModule()** | Se execută o singură dată înaintea tuturor testelor dintr-un modul Python (fișier). |
| **Stack** | Structură de date care funcționează pe principiul *LIFO* (Last In, First Out). |
| **tearDownModule()** | Se execută o singură dată după terminarea tuturor testelor dintr-un modul. |
| **Test assertion** | Instrucțiune care verifică dacă o condiție este adevărată sau falsă; determină trecerea sau eșecul testului. |
| **Test Driven Development (TDD)** | Metodologie de dezvoltare în care testele unitare ghidează designul codului. Menține atenția pe modul în care codul va fi folosit și pe rezultatele așteptate. |
| **Test fixtures** | Sunt folosite pentru a stabili o stare inițială cunoscută înainte și după rularea testelor. |
| **unittest** | Framework-ul implicit de testare în Python (PyUnit). |
| **xUnit series** | Familie de framework-uri pentru TDD: JUnit (Java), PyUnit (Python), NUnit (.NET), Embunit (C/C++). |

---

## 🧪 Test Driven Development (TDD)

### 🔁 Workflow-ul Red/Green/Refactor
TDD urmează un ciclu iterativ de trei pași:
1. ✳️ **Red:** Scrie un test care eșuează pentru codul dorit.  
2. ✅ **Green:** Scrie suficient cod pentru ca testul să treacă.  
3. 🧹 **Refactor:** Îmbunătățește codul păstrând testele verzi.

---

## ⏱️ Avantajele TDD

- Economisește timp în dezvoltare.  
- Asigură că aplicația funcționează conform așteptărilor.  
- Fiecare schimbare este verificată prin teste automate.  
- Permite integrarea într-un pipeline DevOps complet automatizat.  

> 💡 *Într-un pipeline DevOps, toate testele trebuie automatizate pentru a permite livrarea continuă (CD).*

---

## 🧰 Framework-uri și unelte populare pentru TDD

| **Categorie** | **Framework-uri / Exemple** |
|----------------|-----------------------------|
| Testare unitară | PyUnit (unittest), Pytest |
| Testare bazată pe documentație | Doctest |
| Testare stil BDD | RSpec |
| Test runner | Nose |
| Alte framework-uri TDD | Jasmine (JavaScript), Mocha (Node.js), SimpleTest (PHP) |

---

## 🧩 Diferențe importante

- `PyUnit` și `Pytest` sunt cele mai folosite framework-uri pentru testare în Python.  
- `Doctest` și `RSpec` sunt alte opțiuni populare.  
- `Nose` poate adăuga culoare, rapoarte de acoperire a codului și listări ale testelor lipsă.  
- Poți rula testele TDD din Bash folosind:  
  ```bash
  python -m unittest
  ```  
  sau  
  ```bash
  nosetests
  ```
- `Nose` oferă funcționalități extinse față de `unittest`, cum ar fi colorarea rezultatelor și măsurarea code coverage-ului.

---

## 🧠 Concepte esențiale

- **Framework-urile de testare** simplifică procesul de scriere, organizare și execuție a testelor.  
- **Aserțiunile (assertions)** verifică dacă rezultatul unui test corespunde celui așteptat.  
- În Python, poți folosi fie funcția `assert()`, fie metodele de aserțiune oferite de PyUnit (ex: `assertEqual`, `assertTrue`).

---

## 🌞 Happy Paths și 😞 Sad Paths

- **Happy Path:** verifică dacă o funcție returnează rezultatele pozitive așteptate.  
- **Sad Path:** testează comportamentul în caz de erori sau excepții (de exemplu, input invalid sau lipsa datelor).  

> ⚙️ *Sad paths sunt esențiale pentru a te asigura că aplicația gestionează corect erorile fără a se bloca.*

---

## 🧱 Test Fixtures

Test fixtures definesc starea inițială a mediului de testare. Ele pot:
- crea date de test,  
- configura mock objects,  
- încărca baze de date temporare,  
- și curăța mediul după rularea testelor.

### Niveluri de fixture:
1. **Module** – inițializează resurse o singură dată pentru întregul modul de test.  
2. **Test Case** – rulează înainte și după fiecare caz de test.  
3. **Test** – gestionează detaliile specifice fiecărui test individual.  

---

> 💡 *În concluzie, TDD este o metodologie ce ghidează designul codului prin testare continuă, asigurând calitatea, stabilitatea și încrederea în produsul final.*
