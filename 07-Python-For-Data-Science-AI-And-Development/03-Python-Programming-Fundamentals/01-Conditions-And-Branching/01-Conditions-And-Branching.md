# 🌿 Python Conditions and Branching — Condiții și Ramificări

## 📘 Introducere
În Python, **condițiile și ramificările** (conditions and branching) sunt folosite pentru a lua **decizii** în funcție de anumite criterii.  
Ele permit programului să execute cod **numai dacă** anumite condiții sunt îndeplinite.

---

## 🔹 Declarația `if`
Instrucțiunea `if` evaluează o expresie logică și execută un bloc de cod dacă expresia este `True`.

```python
x = 10

if x > 5:
    print("x este mai mare decât 5")
```
📤 **Rezultat:**
```
x este mai mare decât 5
```

---

## 🔹 `if...else`
Dacă expresia din `if` este falsă (`False`), se execută blocul de cod din `else`.

```python
x = 3

if x > 5:
    print("x este mai mare decât 5")
else:
    print("x NU este mai mare decât 5")
```
📤 **Rezultat:**
```
x NU este mai mare decât 5
```

---

## 🔹 `if...elif...else`
Când există mai multe condiții posibile, se folosește `elif` („else if”).

```python
x = 10

if x > 15:
    print("x este mai mare decât 15")
elif x > 5:
    print("x este mai mare decât 5, dar mai mic sau egal cu 15")
else:
    print("x este 5 sau mai mic")
```
📤 **Rezultat:**
```
x este mai mare decât 5, dar mai mic sau egal cu 15
```

---

## 🔹 Condiții multiple
Poți combina mai multe condiții folosind operatorii logici `and`, `or`, `not`.

```python
x = 7
y = 10

if x > 5 and y > 5:
    print("Ambele valori sunt mai mari decât 5")

if x > 5 or y < 5:
    print("Cel puțin una dintre condiții este adevărată")

if not (x < 5):
    print("x NU este mai mic decât 5")
```
📤 **Rezultat:**
```
Ambele valori sunt mai mari decât 5
Cel puțin una dintre condiții este adevărată
x NU este mai mic decât 5
```

---

## 🔹 Operatorii de comparație
| Operator | Descriere | Exemplu | Rezultat |
|-----------|------------|----------|-----------|
| `==` | Egalitate | `5 == 5` | True |
| `!=` | Diferit | `5 != 3` | True |
| `>` | Mai mare | `7 > 4` | True |
| `<` | Mai mic | `2 < 5` | True |
| `>=` | Mai mare sau egal | `5 >= 5` | True |
| `<=` | Mai mic sau egal | `3 <= 7` | True |

---

## 🔹 Ramificare imbricată (Nested if)
Poți pune un `if` în interiorul altui `if`.

```python
x = 10
y = 20

if x > 5:
    if y > 15:
        print("x > 5 și y > 15")
```
📤 **Rezultat:**
```
x > 5 și y > 15
```

---

## 🔹 Declarația `pass`
Uneori vrei o condiție care **nu face nimic** (de exemplu, ca un placeholder).  
Folosim cuvântul cheie `pass`.

```python
x = 10

if x > 5:
    pass  # codul va fi adăugat mai târziu
```
📤 **Rezultat:**  
Nimic nu se afișează (programul nu face nimic în acel bloc).

---

## 🔹 Expresii condiționale (Ternary Operator)
Python permite o formă scurtă a instrucțiunii `if...else`:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```
📤 **Rezultat:**
```
adult
```

---

## 🧠 Sfaturi utile
- Folosește **indentarea corectă** (de obicei 4 spații) — Python folosește indentarea pentru a delimita blocurile de cod.  
- Fiecare `if`, `elif`, `else` trebuie să se termine cu `:`.  
- Poți combina condiții complexe cu paranteze pentru claritate.

---

## 🏁 Concluzie
- `if`, `elif`, `else` controlează fluxul logic al programului.  
- Operatorii de comparație și logici sunt fundamentali pentru condiții.  
- Indentarea corectă este **esențială** în Python.  

> 💬 *„Condițiile dau viață logicii unui program — fără ele, codul ar curge fără direcție.”*
