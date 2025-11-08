# Implementarea primilor pași în Behave

## Prezentare generală

După ce ai generat pașii (steps) cu Behave, următorul pas este
**implementarea lor** --- adică scrierea codului Python care dă viață
scenariilor definite în Gherkin.

Fiecare pas (`Given`, `When`, `Then`) trebuie asociat cu o funcție
Python corespunzătoare, care conține logica necesară pentru acel pas de
testare.

------------------------------------------------------------------------

## Structura unui pas Behave

Un pas Behave are următoarea structură de bază:

``` python
@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(context.base_url)
```

### Explicație:

-   `@given`, `@when`, `@then` sunt decoratori Behave care leagă o
    propoziție Gherkin de o funcție Python.
-   `context` este un obiect special Behave care stochează date și
    variabile comune între pași.
-   Logica din interiorul funcției reprezintă comportamentul efectiv ce
    trebuie testat.

------------------------------------------------------------------------

## Exemple de implementare

### 1️⃣ Pasul Given

``` python
@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(context.base_url)
```

➡️ *Inițializează pagina principală a aplicației.*

------------------------------------------------------------------------

### 2️⃣ Pasul When

``` python
@when('I set the "Pet Name" to "Fido"')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'pet_name')
    element.clear()
    element.send_keys('Fido')
```

➡️ *Simulează introducerea unui text într-un câmp HTML.*

------------------------------------------------------------------------

### 3️⃣ Pasul Then

``` python
@then('I should see the message "Success"')
def step_impl(context):
    element = context.driver.find_element(By.ID, 'flash_message')
    assert "Success" in element.text
```

➡️ *Verifică dacă mesajul „Success" apare pe pagină.*

------------------------------------------------------------------------

## Erori comune și coduri de stare Behave

  Culoare       Semnificație
  ------------- ------------------------------------------------
  🟢 Verde      Pas implementat și executat cu succes
  🔴 Roșu       Pasul a eșuat (test nereușit)
  🟡 Galben     Pasul este nedefinit (nu există implementare)
  🔵 Albastru   Pasul a fost omis (scenariul anterior a eșuat)

------------------------------------------------------------------------

## `NotImplementedError` în Behave

Dacă un pas este generat automat, dar încă nu are implementare, Behave
inserează implicit:

``` python
raise NotImplementedError("STEP: I am on the 'Home Page'")
```

🔹 Acest lucru indică un **pas implicit (default)** --- nu unul lipsă.\
🔹 Odată ce adaugi cod în locul acestei linii, pasul va fi considerat
implementat.

------------------------------------------------------------------------

## Sfaturi utile

-   Implementează **doar un pas odată**, apoi rulează testele din nou.\
-   Utilizează `context` pentru a transmite date între pași.\
-   Refactorizează pașii similari pentru a-i face reutilizabili.\
-   Rulează `behave -v` pentru a obține informații detaliate în consolă.

------------------------------------------------------------------------

## Concluzie

Prin implementarea corectă a pașilor Behave: - Scenariile Gherkin devin
teste automate funcționale. - Echipa poate verifica comportamentul
aplicației direct din limbaj natural. - Dezvoltarea devine mai
colaborativă, transparentă și sigură.
