# 🔁 Python Loops — Bucles (Repetiții)

## 📘 Introducere
Bucla (**loop**) este o structură de control care permite executarea repetată a unui bloc de cod.  
Python oferă două tipuri principale de bucle:

- `for` loop → iterare printr-o secvență (listă, tuplu, dicționar, set, șir etc.)
- `while` loop → repetă codul **atâta timp cât** o condiție este adevărată

---

## 🔹 Bucla `for`
Bucla `for` este folosită pentru a parcurge elementele unei secvențe.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
📤 **Rezultat:**
```
apple
banana
cherry
```

---

### 🔸 Iterare printr-un șir (string)
```python
for letter in "Python":
    print(letter)
```
📤 **Rezultat:**
```
P
y
t
h
o
n
```

---

### 🔸 Folosirea funcției `range()`
`range()` generează o secvență de numere.

```python
for i in range(5):
    print(i)
```
📤 **Rezultat:**
```
0
1
2
3
4
```

🧠 Poți specifica și start, stop și pas:
```python
for i in range(2, 10, 2):
    print(i)
```
📤 **Rezultat:**
```
2
4
6
8
```

---

### 🔸 Folosirea `break` și `continue`
- `break` → oprește complet bucla  
- `continue` → sare peste iterația curentă și trece la următoarea

```python
for number in range(1, 6):
    if number == 3:
        continue  # sare peste 3
    if number == 5:
        break     # oprește la 5
    print(number)
```
📤 **Rezultat:**
```
1
2
4
```

---

## 🔹 Bucla `while`
Execută codul atâta timp cât condiția este `True`.

```python
count = 0

while count < 5:
    print("Număr:", count)
    count += 1
```
📤 **Rezultat:**
```
Număr: 0
Număr: 1
Număr: 2
Număr: 3
Număr: 4
```

---

### 🔸 Folosirea `break` și `continue` în `while`
```python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # sare peste 3
    if i == 7:
        break     # oprește la 7
    print(i)
```
📤 **Rezultat:**
```
1
2
4
5
6
```

---

## 🔹 Bucla imbricată (Nested Loop)
O buclă în interiorul altei bucle.

```python
for x in range(3):
    for y in range(2):
        print(f"x={x}, y={y}")
```
📤 **Rezultat:**
```
x=0, y=0
x=0, y=1
x=1, y=0
x=1, y=1
x=2, y=0
x=2, y=1
```

---

## 🔹 `else` în bucle
Instrucțiunea `else` dintr-o buclă se execută **numai dacă bucla nu este întreruptă de un `break`**.

```python
for i in range(3):
    print(i)
else:
    print("Bucla s-a terminat fără întrerupere.")
```
📤 **Rezultat:**
```
0
1
2
Bucla s-a terminat fără întrerupere.
```

---

## 🔹 Iterarea prin dicționare
```python
person = {"name": "Alice", "age": 25, "city": "Paris"}

for key, value in person.items():
    print(key, "→", value)
```
📤 **Rezultat:**
```
name → Alice
age → 25
city → Paris
```

---

## 🧠 Sfaturi utile
- Evită buclele infinite (`while True:`) fără o condiție de oprire clară.  
- Poți folosi `break` pentru a ieși din buclele infinite.  
- `for` este preferată pentru iterarea colecțiilor, `while` pentru condiții.

---

## 🏁 Concluzie
- `for` → iterare printr-o secvență  
- `while` → repetă cât timp condiția e `True`  
- `break`, `continue`, `else` → controlează fluxul în buclă  

> 💬 *„Buclele sunt inima programelor — ele fac ca lucrurile să se repete până la perfecțiune.”*
