# Utilizarea Substituției de Variabile în Behave

## Prezentare generală

În Behave, **substituția de variabile** îți permite să reutilizezi pași
Gherkin și să-i faci mai flexibili.\
În loc să scrii pași diferiți pentru fiecare valoare, poți introduce
**variabile între ghilimele** care vor fi transmise funcției Python
corespunzătoare.

Această tehnică face scenariile mai **generice, clare și
reutilizabile**.

------------------------------------------------------------------------

## Exemplu simplu

### Fișier `.feature`

``` gherkin
Feature: Căutare animal de companie

  Scenario: Căutare dinamică
    Given I am on the "Home Page"
    When I set the "Pet Name" to "Fido"
    Then I should see the message "Success"
```

### Fișier `steps/web_steps.py`

``` python
@when('I set the "{element_name}" to "{value}"')
def step_impl(context, element_name, value):
    element_id = "pet_" + element_name.lower().replace(" ", "_")
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(value)
```

------------------------------------------------------------------------

## Explicație

-   `{element_name}` și `{value}` sunt **variabile dinamice** definite
    în pașii Gherkin.\
-   Ele sunt transmise automat funcției Python ca **parametri**.\
-   Astfel, poți folosi același pas pentru a introduce **orice câmp** și
    **orice valoare**.

------------------------------------------------------------------------

## Beneficii

✅ Reutilizare mai mare a pașilor\
✅ Scenarii mai scurte și mai clare\
✅ Reducerea duplicării codului\
✅ Parametrii dinamici pot fi extrași din fișiere, baze de date sau
tabele Gherkin

------------------------------------------------------------------------

## Exemplu extins

``` gherkin
Scenario: Căutare multiplă
    Given I am on the "Home Page"
    When I set the "Pet Name" to "Fido"
    And I set the "Pet Type" to "Dog"
    Then I should see "Fido" in the results
```

``` python
@then('I should see "{pet_name}" in the results')
def step_impl(context, pet_name):
    element = context.driver.find_element(By.ID, 'search_results')
    assert pet_name in element.text
```

➡️ Acum testul va funcționa pentru **orice nume** introdus în Gherkin.

------------------------------------------------------------------------

## Substituție cu Tabele de Date

Behave permite, de asemenea, transmiterea datelor prin tabele:

``` gherkin
Scenario: Adăugare de animale multiple
    Given I am on the "Home Page"
    When I add the following pets:
      | Pet Name | Pet Type |
      | Fido     | Dog      |
      | Kitty    | Cat      |
      | Leo      | Lion     |
```

### Implementare în Python

``` python
@when('I add the following pets:')
def step_impl(context):
    for row in context.table:
        name = row["Pet Name"]
        pet_type = row["Pet Type"]
        # aici poți apela o funcție care adaugă fiecare animal
        print(f"Adding {name} ({pet_type})")
```

------------------------------------------------------------------------

## Bune practici

-   Evită codul duplicat --- folosește variabile în pașii Gherkin.\
-   Numește variabilele clar și consecvent (`"{nume}"`, `"{valoare}"`).\
-   Testează substituțiile folosind valori diferite pentru același pas.\
-   Ține cont de sensibilitatea la majuscule în string-uri.

------------------------------------------------------------------------

## Concluzie

Substituția de variabile este o parte esențială din **Behavior Driven
Development (BDD)**.\
Prin folosirea ei: - Scenariile devin mai flexibile și mai ușor de
întreținut.\
- Poți acoperi mai multe cazuri de test cu mai puțin cod.\
- Testele devin mai aproape de limbajul natural al utilizatorilor.
