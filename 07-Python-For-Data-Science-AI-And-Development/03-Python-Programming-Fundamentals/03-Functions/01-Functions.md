# 🧩 Python Functions — Funcții

## 📘 Introducere
O **funcție** în Python este un bloc de cod reutilizabil care execută o sarcină specifică.  
Funcțiile sunt folosite pentru a **evita repetarea codului**, pentru a **organiza logica** programului și pentru a **face codul mai clar și ușor de întreținut**.

---

## 🔹 Definirea unei funcții
Funcțiile se definesc folosind cuvântul cheie `def`, urmat de numele funcției și de paranteze `()` care pot conține parametri.

```python
def greet():
    print("Hello, world!")

# Apelarea funcției
greet()
```
📤 **Rezultat:**
```
Hello, world!
```

---

## 🔹 Funcții cu parametri
Funcțiile pot primi **argumente (parametri)** care le permit să lucreze cu valori dinamice.

```python
def add(a, b):
    c = a + b
    return c

result = add(3, 5)
print(result)
```
📤 **Rezultat:**
```
8
```

---

## 🔹 Funcții cu `return`
Instrucțiunea `return` face ca funcția să trimită înapoi o valoare către apelant.

```python
def square(x):
    return x * x

y = square(4)
print(y)
```
📤 **Rezultat:**
```
16
```

💡 Dacă o funcție nu are `return`, ea returnează implicit `None`.

---

## 🔹 Docstring (comentariu de funcție)
Poți adăuga o descriere scurtă între `"""` pentru a documenta scopul funcției.

```python
def multiply(a, b):
    """
    Inmulteste doua numere si returneaza rezultatul.
    """
    return a * b

help(multiply)
```

📤 **Rezultat:**
```
Help on function multiply in module __main__:

multiply(a, b)
    Inmulteste doua numere si returneaza rezultatul.
```

---

## 🔹 Parametri cu valori implicite
Poți seta o valoare implicită pentru parametrii unei funcții.

```python
def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Alice")
```
📤 **Rezultat:**
```
Hello, Student
Hello, Alice
```

---

## 🔹 Funcții cu număr variabil de argumente (`*args` și `**kwargs`)
- `*args` — permite trimiterea unui **număr nelimitat de argumente poziționale** (stocate într-un tuplu).  
- `**kwargs` — permite trimiterea unui **număr nelimitat de argumente cheie-valoare** (stocate într-un dicționar).

```python
def printAll(*args):
    print("Număr de argumente:", len(args))
    for argument in args:
        print(argument)

printAll("Python", "C++", "Java")

def printDictionary(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

printDictionary(Country="Romania", City="Bucuresti")
```
📤 **Rezultat:**
```
Număr de argumente: 3
Python
C++
Java
Country: Romania
City: Bucuresti
```

---

## 🔹 Variabile locale și globale
- **Variabile locale** — definite în interiorul funcției și vizibile doar acolo.  
- **Variabile globale** — definite în afara oricărei funcții și vizibile peste tot.

```python
x = "global"

def my_function():
    x = "local"
    print("În funcție:", x)

my_function()
print("În afara funcției:", x)
```
📤 **Rezultat:**
```
În funcție: local
În afara funcției: global
```

Dacă vrei să modifici o variabilă globală în interiorul unei funcții, trebuie să folosești `global`:

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```
📤 **Rezultat:**
```
1
```

---

## 🔹 Funcții care modifică obiecte mutabile
Când transmiți o listă sau dicționar, modificările făcute în funcție afectează și variabila originală.

```python
def add_items(lst):
    lst.append("Three")
    lst.append("Four")

my_list = ["One", "Two"]
add_items(my_list)
print(my_list)
```
📤 **Rezultat:**
```
['One', 'Two', 'Three', 'Four']
```

---

## 🔹 Funcții lambda (anonime)
Funcțiile **lambda** sunt funcții scurte, fără nume, utile pentru expresii simple.

```python
square = lambda x: x * x
print(square(5))
```
📤 **Rezultat:**
```
25
```

Exemplu cu `map()`:
```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)
```
📤 **Rezultat:**
```
[1, 4, 9, 16]
```

---

## 🔹 Funcții încorporate (Built-in Functions)
Python are multe funcții predefinite utile.

| Funcție | Descriere | Exemplu |
|----------|------------|----------|
| `len()` | Returnează lungimea | `len([1,2,3])` → `3` |
| `sum()` | Returnează suma elementelor | `sum([1,2,3])` → `6` |
| `max()` | Returnează valoarea maximă | `max([3,7,2])` → `7` |
| `min()` | Returnează valoarea minimă | `min([3,7,2])` → `2` |
| `type()` | Returnează tipul obiectului | `type(5)` → `<class 'int'>` |

---

## 🔹 Funcții și erori (try/except)
Poți folosi `try` și `except` în interiorul funcțiilor pentru a preveni blocarea programului în caz de erori.

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

---

## 🧠 Sfaturi utile
- Fiecare funcție ar trebui să facă **un singur lucru bine**.  
- Folosește **nume descriptive** pentru funcții și parametri.  
- Adaugă **comentarii** și **docstring-uri** pentru claritate.  
- Testează funcțiile cu diferite tipuri de date.

---

## 🏁 Concluzie
Funcțiile sunt coloana vertebrală a oricărui program Python. Ele permit:
- Reutilizarea codului  
- Organizarea logică a programului  
- Debugging mai simplu și claritate sporită  

> 💬 *„Funcțiile transformă codul repetitiv în cod elegant.”*
