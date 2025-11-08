# Rezumat: Rularea Behave pentru Dezvoltarea Condusă de Comportament (BDD)

## Felicitări!

Ai finalizat acest modul!\
În acest punct al cursului, știi următoarele:

------------------------------------------------------------------------

## Ce face Behave

-   **Behave** raportează toți pașii Python lipsă și oferă **fragmente
    de cod** (code snippets) pe care le poți folosi pentru a-i
    implementa.\
-   Acest cod îți oferă **un punct de plecare** pentru construirea
    fișierelor de pași (`steps files`).

------------------------------------------------------------------------

## Fluxul de lucru pentru implementarea pașilor în Python

1.  Implementează un pas.\
2.  Rulează Behave și verifică dacă pasul trece.\
3.  Implementează următorul pas care eșuează.\
4.  Rulează din nou Behave și verifică dacă acest pas trece.\
5.  Repetă procesul până când **toți pașii sunt executați cu succes.**

------------------------------------------------------------------------

## Utilizarea contextului în Behave

-   `context` este o **variabilă** care este transmisă automat în
    fiecare definiție de pas.\
-   Pentru a transmite informații între pași, **stochează date în
    `context`** într-un pas și **accesază-le** într-un alt pas.\
-   Astfel, poți partaja date între pași fără a folosi variabile
    globale.

------------------------------------------------------------------------

## Substituția de variabile

Substituția de variabile **reduce numărul de pași** și **maximizează
reutilizarea**.

Pentru a utiliza substituția de variabile:

1.  Înlocuiește datele din șirul decoratorului (ex: `@when(...)`) cu
    variabile între **acolade `{}`**.\
2.  Adaugă parametri în funcția Python cu aceleași nume ca variabilele
    definite.\
3.  Folosește acești parametri în locul valorilor statice transmise din
    fișierul `.feature`.

Exemplu:

``` gherkin
When I set the "Pet Name" to "Fido"
```

Poate fi implementat ca:

``` python
@when('I set the "{element_name}" to "{value}"')
def step_impl(context, element_name, value):
    ...
```

------------------------------------------------------------------------

## Avantaje cheie

✅ Mai puțin cod duplicat\
✅ Reutilizare maximă a pașilor\
✅ Teste mai dinamice și mai ușor de întreținut\
✅ Claritate între pașii Gherkin și implementarea Python

------------------------------------------------------------------------

## Tabel de termeni

  -----------------------------------------------------------------------
  Termen                       Definiție
  ---------------------------- ------------------------------------------
  **context**                  O variabilă disponibilă în toate funcțiile
                               de pas care conține informații ce pot fi
                               transmise între pași.

  **context.base_url**         Variabila care indică pagina principală
                               (Home Page).

  **environment.py**           Un fișier Python care stabilește mediul
                               inițial de testare. Este folosit adesea
                               pentru configurarea driverelor și salvarea
                               variabilelor de context precum `base_url`.

  **HTTP GET**                 O metodă folosită pe URL-ul paginii
                               principale pentru a obține conținutul
                               paginii.

  **NotImplementedError**      O eroare utilizată pentru a indica faptul
                               că o funcție de pas nu este încă
                               implementată.

  **Red/Green/Refactor**       Fluxul de lucru TDD în care scrii un test
                               care eșuează (roșu), scrii cod pentru a-l
                               face să treacă (verde) și apoi
                               refactorizezi pentru a-l îmbunătăți.

  **Variable substitution      O modalitate de a trece dinamic nume de
  (Substituția de variabile)** elemente care își pot schimba valoarea la
                               rulare, sporind reutilizarea pașilor în
                               testarea BDD.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Concluzie

Prin utilizarea corectă a **Behave**, a obiectului **context** și a
**substituției de variabile**, poți scrie teste: - mai eficiente,\
- mai flexibile,\
- mai apropiate de limbajul natural al utilizatorului final.

Aceste practici îți oferă o bază solidă pentru dezvoltarea orientată
spre comportament (BDD).
