# 📋 Python Lists and Tuples — Liste și Tupluri

## 📘 Introducere
În Python, **listele** și **tuplurile** sunt două tipuri fundamentale de colecții folosite pentru a stoca mai multe valori într-o singură variabilă.  
Diferența principală dintre ele este că **listele sunt modificabile (mutable)**, iar **tuplurile nu (immutable)**.

---

## 🔹 Liste (Lists)
O **listă** este o colecție ordonată de elemente care poate fi modificată după creare.  
Listele sunt definite folosind **paranteze drepte** `[ ]`.

### 🧩 Exemplu de listă:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```
📤 **Rezultat:**
```
['apple', 'banana', 'cherry']
```

### ✅ Caracteristici:
- Listele pot conține **elemente de tipuri diferite** (ex: întregi, șiruri, booleeni etc.).  
- Ordinea elementelor este **păstrată**.  
- Poți **adăuga, șterge sau modifica** elemente după creare.

---

### 🔧 Operații comune cu liste:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # accesarea primului element
fruits.append("orange")  # adăugare
fruits.remove("banana")  # ștergere
fruits[1] = "kiwi"       # modificare
print(fruits)
```
📤 **Rezultat:**
```
['apple', 'kiwi', 'cherry', 'orange']
```

---

### 🔁 Parcurgerea unei liste:
```python
for fruit in fruits:
    print(fruit)
```
📤 **Rezultat:**
```
apple
kiwi
cherry
orange
```

---

## 🔹 Tupluri (Tuples)
Un **tuplu** este o colecție **ordonată**, dar **nemodificabilă** (immutable).  
Tuplurile se definesc cu **paranteze rotunde** `( )`.

### 🧩 Exemplu de tuplu:
```python
colors = ("red", "green", "blue")
print(colors)
```
📤 **Rezultat:**
```
('red', 'green', 'blue')
```

### ✅ Caracteristici:
- Elementele nu pot fi modificate, adăugate sau șterse.  
- Ordinea este **fixă**.  
- Pot conține **valori duplicate**.  

---

### 🔎 Accesarea elementelor:
```python
print(colors[0])  # red
print(colors[-1]) # blue
```

---

## 🔄 Conversia între liste și tupluri
Python permite conversia ușoară între aceste două tipuri:

```python
list_to_tuple = tuple(["a", "b", "c"])
tuple_to_list = list(("x", "y", "z"))

print(list_to_tuple)
print(tuple_to_list)
```
📤 **Rezultat:**
```
('a', 'b', 'c')
['x', 'y', 'z']
```

---

## ⚙️ Funcții utile pentru liste și tupluri
| Funcție | Descriere | Exemplu |
|----------|------------|----------|
| `len()` | Lungimea colecției | `len(fruits)` → `4` |
| `min()` / `max()` | Cel mai mic / mare element | `min(numbers)` |
| `sum()` | Suma elementelor numerice | `sum([1,2,3])` → `6` |
| `count()` | Numărul de apariții ale unui element | `fruits.count("apple")` |
| `index()` | Indexul primei apariții | `colors.index("green")` |

---

## 🧠 Diferențe între Liste și Tupluri

| Caracteristică | Listă | Tuplu |
|------------------|--------|--------|
| Sintaxă | `[ ]` | `( )` |
| Modificabilă | ✅ Da | ❌ Nu |
| Viteză | Mai lentă | Mai rapidă |
| Ideală pentru | date care se schimbă | date fixe / constante |

---

## 🏁 Concluzie
- Folosește **liste** când ai nevoie de o colecție dinamică, modificabilă.  
- Folosește **tupluri** când vrei date **fixe și protejate** împotriva modificărilor.  

> 💬 *„Listele sunt flexibile, tuplurile sunt sigure.”*
