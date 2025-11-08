# Lucrul cu Context în Behave

## Prezentare generală

În Behave, obiectul **`context`** este un element esențial care
acționează ca un **container partajat de date** între pașii de testare
(`Given`, `When`, `Then`).\
El îți permite să transmiți informații dintr-un pas în altul, menținând
coerența între diferitele acțiuni ale scenariului.

------------------------------------------------------------------------

## Ce este `context`

`context` este un obiect pe care Behave îl creează automat la rularea
unui test.\
Poți adăuga în el orice variabilă, valoare sau obiect (de exemplu,
driverul Selenium, răspunsuri HTTP, date de intrare etc.), iar acestea
pot fi accesate ulterior în alte funcții de pas.

------------------------------------------------------------------------

## Exemplu simplu

``` python
@given('I open the "Login Page"')
def step_impl(context):
    context.driver.get("https://example.com/login")
    context.username = "student"
    context.password = "1234"

@when('I submit my credentials')
def step_impl(context):
    username_box = context.driver.find_element(By.ID, "username")
    password_box = context.driver.find_element(By.ID, "password")
    username_box.send_keys(context.username)
    password_box.send_keys(context.password)
    context.driver.find_element(By.ID, "submit").click()

@then('I should see the "Dashboard" page')
def step_impl(context):
    assert "Dashboard" in context.driver.title
```

### Explicație

-   În primul pas, se salvează în `context` două variabile: `username`
    și `password`.\
-   În pasul `When`, aceste variabile sunt folosite pentru
    autentificare.\
-   `context.driver` este disponibil în toate funcțiile, deoarece a fost
    definit global în fișierul `environment.py`.

------------------------------------------------------------------------

## Beneficiile folosirii `context`

✅ Partajare ușoară de informații între pași\
✅ Reducerea duplicării codului\
✅ Menținerea unei structuri clare a datelor\
✅ Evitarea utilizării de variabile globale

------------------------------------------------------------------------

## Stocarea și transmiterea datelor

Poți salva în `context`: - Date numerice sau textuale\
- Liste, dicționare, obiecte Python\
- Răspunsuri HTTP (`context.response`)\
- Elemente Selenium (`context.driver`)

### Exemplu

``` python
@when('I search for "{term}"')
def step_impl(context, term):
    context.search_term = term
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(term)
    search_box.submit()

@then('I should see results related to my search')
def step_impl(context):
    assert context.search_term in context.driver.page_source
```

------------------------------------------------------------------------

## Context global și local

-   **Context global** -- Este disponibil pe durata întregului test
    (`before_all`, `after_all`).\
-   **Context local** -- Este creat pentru fiecare scenariu
    (`before_scenario`, `after_scenario`).

------------------------------------------------------------------------

## Bune practici

-   Păstrează datele în `context` doar pe durata necesară scenariului.\
-   Evită utilizarea `context` ca depozit global permanent.\
-   Inițializează variabilele în `before_all()` sau `before_scenario()`
    pentru claritate.\
-   Curăță resursele în `after_all()` sau `after_scenario()` (ex.
    închide browserul Selenium).

------------------------------------------------------------------------

## Concluzie

Prin folosirea eficientă a obiectului `context`, testele Behave devin: -
Mai clare\
- Mai reutilizabile\
- Mai ușor de întreținut

`context` este liantul care conectează pașii tăi și asigură coerența
datelor în întreg scenariul.
