# 🎵 Python Sets — Mulțimi

## 📘 Introducere
Un **set** (mulțime) în Python este o colecție **neordonată**, **fără elemente duplicate** și **mutabilă**.  
Seturile sunt utile pentru eliminarea valorilor duplicate și pentru efectuarea operațiilor matematice de tip mulțime (uniune, intersecție etc.).

Exemplu simplu:
```python
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "disco"}
print(set1)
```
📤 **Rezultat:**
```
{'R&B', 'soul', 'disco', 'pop', 'hard rock', 'rock'}
```
➡️ Observă că `rock` apare o singură dată — duplicatele sunt eliminate automat.

---

## 🔹 Crearea unui Set
Seturile se pot crea fie cu `{}`, fie cu funcția `set()`:
```python
# Dintr-o listă
album_list = ["Thriller", "Back in Black", "Thriller", "AC/DC"]
album_set = set(album_list)
print(album_set)
# Output: {'Back in Black', 'AC/DC', 'Thriller'}
```

---

## 🔹 Adăugarea și Eliminarea Elementelor
```python
A = {"Thriller", "Back in Black", "AC/DC"}
A.add("NSYNC")       # Adăugare
print(A)

A.add("NSYNC")       # Duplicatele sunt ignorate
print(A)

A.remove("NSYNC")    # Eliminare
print(A)
```
📤 **Rezultat:**
```
{'Thriller', 'Back in Black', 'AC/DC', 'NSYNC'}
{'Thriller', 'Back in Black', 'AC/DC', 'NSYNC'}
{'Thriller', 'Back in Black', 'AC/DC'}
```

---

## 🔹 Verificarea existenței unui element
```python
A = {"Thriller", "Back in Black", "AC/DC"}
print("AC/DC" in A)   # True
print("NSYNC" in A)   # False
```

📤 **Rezultat:**
```
True
False
```

---

## 🔹 Operații cu Seturi
Python permite operații matematice între seturi.

### 🔸 Uniune (`|` sau `.union()`)
Reunește toate elementele din ambele seturi.
```python
A = {"rock", "pop", "soul"}
B = {"disco", "pop", "jazz"}
print(A | B)
# sau
print(A.union(B))
```
📤 **Rezultat:**
```
{'jazz', 'pop', 'rock', 'disco', 'soul'}
```

### 🔸 Intersecție (`&` sau `.intersection()`)
Returnează elementele comune ambelor seturi.
```python
print(A & B)
# sau
print(A.intersection(B))
```
📤 **Rezultat:**
```
{'pop'}
```

### 🔸 Diferență (`-` sau `.difference()`)
Returnează elementele din primul set care nu apar în al doilea.
```python
print(A - B)
# sau
print(A.difference(B))
```
📤 **Rezultat:**
```
{'rock', 'soul'}
```

### 🔸 Diferență Simetrică (`^` sau `.symmetric_difference()`)
Returnează elementele care se află în unul dintre seturi, dar nu în ambele.
```python
print(A ^ B)
# sau
print(A.symmetric_difference(B))
```
📤 **Rezultat:**
```
{'rock', 'disco', 'soul', 'jazz'}
```

---

## 🔹 Conversia din alte tipuri
Orice **listă** sau **tuplu** poate fi convertită într-un set pentru a elimina duplicatele:
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
# Output: {1, 2, 3, 4, 5}
```

---

## 🔹 Metode utile pentru Seturi
| Metodă | Descriere | Exemplu |
|--------|------------|----------|
| `add()` | Adaugă un element | `A.add("jazz")` |
| `remove()` | Elimină un element (eroare dacă nu există) | `A.remove("rock")` |
| `discard()` | Elimină un element fără eroare | `A.discard("rock")` |
| `clear()` | Golește setul | `A.clear()` |
| `copy()` | Creează o copie a setului | `B = A.copy()` |
| `union()` | Returnează uniunea a două seturi | `A.union(B)` |
| `intersection()` | Returnează intersecția | `A.intersection(B)` |
| `difference()` | Returnează diferența | `A.difference(B)` |
| `symmetric_difference()` | Returnează diferența simetrică | `A.symmetric_difference(B)` |

---

## 🔹 Seturi Imutabile (frozenset)
Python are și o versiune **imutabilă** a setului numită `frozenset`.  
Aceasta nu permite modificări (adică nu poți adăuga sau elimina elemente).

```python
fs = frozenset(["rock", "pop", "jazz"])
print(fs)
# fs.add("metal")  # ❌ Va genera eroare
```

📤 **Rezultat:**
```
frozenset({'rock', 'pop', 'jazz'})
```

---

## 🧠 Diferențe între Set, Listă și Tuplu

| Caracteristică | Set | Listă | Tuplu |
|------------------|--------|--------|--------|
| Sintaxă | `{ }` | `[ ]` | `( )` |
| Duplicare | ❌ Nu permite | ✅ Permite | ✅ Permite |
| Ordine | ❌ Neordonat | ✅ Ordine păstrată | ✅ Ordine păstrată |
| Modificabilitate | ✅ Da | ✅ Da | ❌ Nu |
| Operații matematice | ✅ Da | ❌ Nu | ❌ Nu |

---

## 🏁 Concluzie
- Seturile sunt ideale pentru **eliminarea valorilor duplicate** și **compararea colecțiilor**.  
- Poți efectua rapid operații de tip **uniune**, **intersecție** și **diferență**.  

> 💬 *„Dacă datele trebuie să fie unice, atunci setul este soluția perfectă.”*
