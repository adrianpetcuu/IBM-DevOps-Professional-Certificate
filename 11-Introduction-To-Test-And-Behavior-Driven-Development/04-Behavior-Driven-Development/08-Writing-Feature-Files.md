
# Scrierea Fișierelor Feature (Writing Feature Files)

## Introducere
În cadrul **Behavior Driven Development (BDD)**, fișierele **Feature** sunt esențiale.  
Ele descriu comportamentul așteptat al aplicației într-un limbaj natural, ușor de înțeles de către toți membrii echipei: dezvoltatori, testeri și stakeholderi.

Behave folosește fișiere `.feature` scrise în **Gherkin**, un limbaj structurat care definește comportamentul software-ului prin scenarii de testare.

---

## Structura unui fișier Feature

Un fișier `.feature` are o structură clară și standardizată:

```gherkin
Feature: Autentificare utilizator
  Ca utilizator înregistrat
  Vreau să mă pot autentifica
  Pentru a-mi accesa contul personal

  Scenario: Autentificare reușită
    Given utilizatorul este pe pagina de login
    When introduce date de autentificare valide
    Then este redirecționat către dashboard
```

### Explicație:
- **Feature:** descrie funcționalitatea testată.  
- **Scenario:** definește un caz concret de testare.  
- **Given:** setează starea inițială (contextul).  
- **When:** descrie acțiunea efectuată.  
- **Then:** validează rezultatul așteptat.  

---

## Exemple cu mai multe scenarii

Un fișier `.feature` poate conține mai multe scenarii:

```gherkin
Feature: Autentificare utilizator

  Scenario: Autentificare reușită
    Given utilizatorul este pe pagina de login
    When introduce date valide
    Then este redirecționat către dashboard

  Scenario: Autentificare eșuată
    Given utilizatorul este pe pagina de login
    When introduce o parolă greșită
    Then apare un mesaj de eroare "Date invalide"
```

Acest format permite testarea diferitelor comportamente ale aceleiași funcționalități.

---

## Scenarii parametrizate cu Example Tables

Poți testa mai multe combinații de date folosind **Scenario Outline**:

```gherkin
Scenario Outline: Autentificare cu combinații diferite
  Given utilizatorul este pe pagina de login
  When introduce <username> și <password>
  Then rezultatul este <rezultat>

  Examples:
    | username  | password  | rezultat                |
    | admin     | 12345     | redirecționare reușită |
    | testuser  | greșit    | mesaj de eroare         |
```

Behave va rula acest scenariu de câte ori există o combinație în tabel.

---

## Comentarii și claritate

Poți adăuga comentarii pentru a explica pașii din fișierele `.feature`:

```gherkin
# Acest scenariu verifică loginul reușit
Scenario: Autentificare corectă
  Given utilizatorul este pe pagina de login
  When introduce date valide
  Then este redirecționat către dashboard
```

Comentariile încep cu `#` și sunt ignorate la rulare.

---

## Recomandări pentru fișierele Feature
✅ Scrie scenarii scurte, clare și centrate pe comportament.  
✅ Folosește același limbaj pentru toți pașii (consistență).  
✅ Evită detaliile tehnice – descrie doar comportamentul observabil.  
✅ Organizează fișierele `.feature` pe module sau funcționalități.  

---

## Concluzie
Fișierele **Feature** sunt puntea dintre echipele tehnice și non-tehnice.  
Ele documentează clar comportamentul aplicației, servesc ca teste automate și asigură o înțelegere comună a cerințelor software.
