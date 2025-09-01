# 🎭 Behavior-Driven Development (BDD)

**Behavior-Driven Development (BDD)** este o extensie a TDD care pune accent pe **comportamentul aplicației** din perspectiva utilizatorului final.  
În loc să scriem doar teste tehnice, BDD folosește **scenarii clare și ușor de înțeles** pentru a descrie cum ar trebui să funcționeze sistemul.

---

## 🔹 Principii cheie BDD
- Pune accent pe **colaborarea dintre business, dezvoltatori și testeri**.  
- Specificațiile sunt scrise într-un limbaj natural (ușor de înțeles și de non-tehnici).  
- Exemplele de utilizare sunt transformate în **teste automatizate**.  
- Se concentrează pe **“ce face sistemul”**, nu pe **“cum este implementat”**.  

---

## 🔹 Limbajul Gherkin
BDD folosește adesea limbajul **Gherkin** pentru a scrie scenarii:  

- **Given** – contextul inițial (situația de pornire).  
- **When** – acțiunea efectuată de utilizator sau sistem.  
- **Then** – rezultatul așteptat.  

### Exemplu:
```gherkin
Feature: Autentificare utilizator
  Scenario: Autentificare cu succes
    Given utilizatorul este pe pagina de login
    When introduce un nume de utilizator valid și o parolă validă
    Then este redirecționat către pagina principală
```

## 🔹 Beneficiile BDD

- Îmbunătățește **comunicarea între echipe** (business ↔ dev ↔ QA).  
- Specificațiile devin **documentație vie**.  
- Reduce **ambiguitatea în cerințe**.  
- Asigură că software-ul livrează **valoare reală pentru utilizatori**.  
- Susține **testarea automată** și **integrarea continuă (CI/CD)**.  

---

## 🔹 Diferențe TDD vs. BDD

| Caracteristică      | TDD                         | BDD                               |
|----------------------|-----------------------------|-----------------------------------|
| **Focus**            | Teste unitare (cod)         | Comportament (business + user)    |
| **Limbaj**           | Cod (JUnit, NUnit, etc.)    | Natural (Gherkin)                 |
| **Public țintă**     | Dezvoltatori                | Dezvoltatori, Testeri, Business   |
| **Beneficiu principal** | Calitate tehnică         | Claritate și aliniere pe business |

---

## ✅ Concluzie

**BDD transformă cerințele de business în teste automate** și conectează echipa tehnică cu stakeholderii non-tehnici.  
Este un pas natural după **TDD**, aducând **claritate, colaborare și valoare reală** în procesul DevOps.
