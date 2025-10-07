# ⚙️ Python Exception Handling — Tratarea Erorilor

## 📘 Introducere
În Python, **excepțiile** apar atunci când o operație nu poate fi finalizată corect — de exemplu, împărțirea la zero, accesarea unui element inexistent într-o listă, sau conversia unui text în număr.  
Pentru a evita oprirea programului în aceste cazuri, folosim mecanismul de **try / except**.

---

## 🔹 Sintaxa de bază

```python
try:
    # Cod care poate genera o eroare
    rezultat = 10 / 0
except:
    # Cod care se execută dacă apare o eroare
    print("A apărut o eroare!")
```
📤 **Rezultat:**
```
A apărut o eroare!
```

---

## 🔹 Tipuri de excepții specifice

Poți prinde erori specifice pentru a trata diferite tipuri de probleme.

```python
try:
    a = int(input("Introdu un număr: "))
    b = 10 / a
    print("Rezultat:", b)
except ZeroDivisionError:
    print("Eroare: Împărțirea la zero nu este permisă.")
except ValueError:
    print("Eroare: Trebuie să introduci un număr valid.")
except Exception as e:
    print("Alt tip de eroare:", e)
```
📤 **Rezultat posibil:**
```
Eroare: Împărțirea la zero nu este permisă.
```

---

## 🔹 Blocul `else`
Blocul `else` se execută doar dacă **nu apare nicio eroare**.

```python
try:
    num = 5
    result = 10 / num
except ZeroDivisionError:
    print("Eroare: împărțirea la zero!")
else:
    print("Totul a mers bine, rezultatul este:", result)
```
📤 **Rezultat:**
```
Totul a mers bine, rezultatul este: 2.0
```

---

## 🔹 Blocul `finally`
Blocul `finally` se execută **întotdeauna**, indiferent dacă apare sau nu o eroare. Este folosit pentru închideri de fișiere, conexiuni sau eliberarea resurselor.

```python
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Fișierul nu a fost găsit!")
finally:
    print("Blocul finally s-a executat.")
```
📤 **Rezultat:**
```
Fișierul nu a fost găsit!
Blocul finally s-a executat.
```

---

## 🔹 Combinarea `try`, `except`, `else`, `finally`

```python
try:
    x = int(input("Introdu un număr: "))
    y = 10 / x
except ZeroDivisionError:
    print("Eroare: împărțirea la zero!")
except ValueError:
    print("Eroare: valoare invalidă!")
else:
    print("Rezultatul este:", y)
finally:
    print("Execuția s-a încheiat.")
```
📤 **Rezultat posibil:**
```
Eroare: împărțirea la zero!
Execuția s-a încheiat.
```

---

## 🔹 Ridicarea unei excepții manual (`raise`)
Dacă vrei să oprești execuția și să semnalezi o problemă personalizată, folosește `raise`.

```python
def verifica_varsta(varsta):
    if varsta < 0:
        raise ValueError("Varsta nu poate fi negativă!")
    else:
        print("Varsta validă:", varsta)

try:
    verifica_varsta(-5)
except ValueError as e:
    print("Eroare:", e)
```
📤 **Rezultat:**
```
Eroare: Varsta nu poate fi negativă!
```

---

## 🔹 Crearea de excepții personalizate
Poți defini propriile clase de excepții pentru cazuri specifice aplicației tale.

```python
class InvalidInputError(Exception):
    # Eroare ridicată pentru input invalid
    pass

def proceseaza_input(val):
    if not isinstance(val, int):
        raise InvalidInputError("Valoarea trebuie să fie un număr întreg.")
    return val * 2

try:
    proceseaza_input("abc")
except InvalidInputError as e:
    print("Eroare personalizată:", e)
```
📤 **Rezultat:**
```
Eroare personalizată: Valoarea trebuie să fie un număr întreg.
```

---

## 🔹 Exemple practice

### 🧮 Funcție de împărțire sigură

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Eroare: împărțirea la zero nu este permisă.")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```
📤 **Rezultat:**
```
5.0
Eroare: împărțirea la zero nu este permisă.
None
```

### 🧠 Calcul cu `math.sqrt()`

```python
import math

def perform_calculation(number):
    try:
        result = math.sqrt(number)
        print("Rezultat:", result)
    except ValueError:
        print("Eroare: număr invalid. Introdu o valoare pozitivă.")

perform_calculation(9)
perform_calculation(-4)
```
📤 **Rezultat:**
```
Rezultat: 3.0
Eroare: număr invalid. Introdu o valoare pozitivă.
```

---

## 🔹 Bune practici
✅ Prinde doar excepțiile de care ai nevoie (nu folosi `except:` gol).  
✅ Adaugă mesaje clare de eroare pentru utilizator.  
✅ Folosește `finally` pentru curățare (închiderea fișierelor, conexiunilor etc.).  
✅ Evită ca logica aplicației să depindă complet de blocurile `try/except`.

---

## 🏁 Concluzie
**Exception Handling** este esențial pentru ca aplicațiile Python să fie robuste și stabile.  
Permite tratarea elegantă a erorilor și prevenirea întreruperii bruște a execuției.

> 💬 *„O excepție tratată bine poate salva un program întreg.”*
