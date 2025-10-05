# 🗂️ Python Dictionaries — Dicționare

## 📘 Introducere
Un **dicționar** în Python este o colecție **neordonată**, **modificabilă** și **indexată** de perechi `cheie: valoare`.  
Dicționarele sunt utile pentru stocarea datelor care pot fi accesate printr-o cheie unică.

Exemplu de dicționar:
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)
```
📤 **Rezultat:**
```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

## 🔹 Accesarea Valorilor
Poți accesa valorile folosind cheia asociată.

```python
print(person["name"])       # Alice
print(person.get("age"))    # 25
```

---

## 🔹 Adăugarea și Modificarea Elementelor
Dicționarele sunt **mutabile**, așa că poți adăuga sau modifica perechi `cheie: valoare`.

```python
person["job"] = "Engineer"      # adăugare
person["age"] = 26              # modificare
print(person)
```
📤 **Rezultat:**
```
{'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
```

---

## 🔹 Eliminarea Elementelor
Python oferă mai multe metode pentru eliminarea elementelor:

```python
person.pop("city")         # șterge cheia 'city'
print(person)

person.popitem()           # șterge ultimul element
print(person)

del person["age"]          # șterge o cheie specifică
print(person)

person.clear()             # golește dicționarul complet
print(person)
```
📤 **Rezultat:**
```
{'name': 'Alice', 'age': 26, 'job': 'Engineer'}
{'name': 'Alice', 'age': 26}
{'name': 'Alice'}
{}
```

---

## 🔹 Parcurgerea unui Dicționar
Poți itera prin chei, valori sau ambele:

```python
person = {"name": "Bob", "age": 30, "city": "London"}

for key in person:
    print(key)               # afișează doar cheile

for value in person.values():
    print(value)             # afișează valorile

for key, value in person.items():
    print(key, ":", value)   # afișează perechi cheie:valoare
```

📤 **Rezultat:**
```
name
age
city
Bob
30
London
name : Bob
age : 30
city : London
```

---

## 🔹 Verificarea existenței unei chei
```python
person = {"name": "Alice", "age": 25}
if "name" in person:
    print("Cheia 'name' există!")
```
📤 **Rezultat:**
```
Cheia 'name' există!
```

---

## 🔹 Dicționare Imbricate (Nested Dictionaries)
Dicționarele pot conține alte dicționare — utile pentru structuri complexe de date.

```python
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Emma", "age": 22}
}
print(students["student1"]["name"])  # John
```

📤 **Rezultat:**
```
John
```

---

## 🔹 Metode Utile

| Metodă | Descriere | Exemplu |
|--------|------------|----------|
| `keys()` | Returnează toate cheile | `person.keys()` |
| `values()` | Returnează toate valorile | `person.values()` |
| `items()` | Returnează toate perechile (cheie, valoare) | `person.items()` |
| `update()` | Adaugă sau actualizează valori din alt dicționar | `person.update({"city": "Paris"})` |
| `copy()` | Creează o copie a dicționarului | `new_dict = person.copy()` |

Exemplu:
```python
person = {"name": "Alice", "age": 25}
new_person = person.copy()
new_person.update({"city": "Paris"})
print(new_person)
```
📤 **Rezultat:**
```
{'name': 'Alice', 'age': 25, 'city': 'Paris'}
```

---

## 🔹 Funcții Built-in pentru Dicționare
| Funcție | Descriere | Exemplu |
|----------|------------|----------|
| `len()` | Lungimea dicționarului | `len(person)` → `3` |
| `str()` | Conversie în șir text | `str(person)` |
| `type()` | Tipul obiectului | `type(person)` → `<class 'dict'>` |

---

## 🧠 Diferențe față de Liste și Tupluri
| Caracteristică | Listă | Tuplu | Dicționar |
|------------------|--------|--------|------------|
| Structură | Elemente simple | Elemente fixe | Perechi cheie:valoare |
| Indexare | Numerică | Numerică | Bazată pe chei |
| Modificabilitate | Da | Nu | Da |
| Ordine | Da (Python 3.7+) | Da | Da (Python 3.7+) |

---

## 🏁 Concluzie
Dicționarele sunt printre cele mai puternice structuri de date în Python, oferind o modalitate clară și eficientă de a organiza informațiile.  

> 💬 *„Un dicționar bine gândit este cheia unei logici curate în Python.”*
