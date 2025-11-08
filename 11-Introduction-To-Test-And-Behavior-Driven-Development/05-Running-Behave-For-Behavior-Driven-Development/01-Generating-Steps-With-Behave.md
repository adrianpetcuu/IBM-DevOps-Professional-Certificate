# Generarea pașilor cu Behave

## Prezentare generală

**Behave** este un cadru de testare bazat pe principiul Behavior-Driven
Development (BDD). Acesta permite scrierea testelor în limbaj natural
(Gherkin), astfel încât toți membrii echipei --- dezvoltatori, testeri
sau analiști --- să poată înțelege comportamentul dorit al aplicației.

------------------------------------------------------------------------

## Cum funcționează generarea pașilor

Când rulezi un fișier `.feature` care conține pași Gherkin (`Given`,
`When`, `Then`), dar fără implementare Python corespunzătoare, Behave
generează automat fragmente de cod pentru acei pași, pe care le poți
copia și completa ulterior.

### Exemplu

``` gherkin
Feature: Căutare animal de companie

  Scenario: Căutare cu succes
    Given I am on the "Home Page"
    When I set the "Pet Name" to "Fido"
    And I click the "Search" button
    Then I should see the message "Success"
```

La rulare, Behave va afișa în consolă codul lipsă:

``` python
@given('I am on the "Home Page"')
def step_impl(context):
    raise NotImplementedError("STEP: I am on the 'Home Page'")
```

### Explicație

-   `@given`, `@when`, `@then` sunt **decoratori** specifici Behave.\
-   Fiecare decorare marchează un **pas Gherkin**.\
-   Funcția `step_impl(context)` este punctul de intrare al
    implementării.\
-   Linia `raise NotImplementedError` apare până când adaugi logica
    reală a testului.

------------------------------------------------------------------------

## Codurile de culoare Behave

  Culoare       Semnificație
  ------------- ---------------------------------------------
  🟢 Verde      Pas implementat și executat cu succes
  🔴 Roșu       Pasul a eșuat (a generat o eroare)
  🟡 Galben     Pasul este nedefinit (nu are cod Python)
  🔵 Albastru   Pasul a fost omis (un pas anterior a eșuat)

------------------------------------------------------------------------

## Pașii pentru implementare

1.  Rulează `behave` pentru a genera automat pașii lipsă.\
2.  Copiază fragmentele din consolă în fișierele Python din folderul
    **steps/**.\
3.  Înlocuiește linia `raise NotImplementedError(...)` cu logica
    efectivă.\
4.  Rulează din nou testele până când toate etapele sunt verzi.

------------------------------------------------------------------------

## Bună practică

Scrie pașii tăi într-un mod **generic și reutilizabil**, pentru a evita
duplicarea codului și pentru a face scenariile mai clare.
