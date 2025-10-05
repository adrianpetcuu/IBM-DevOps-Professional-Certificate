# 🧾 Python Data Structures Cheat Sheet

## 📋 Lists (Liste)

### 🔹 Creating a List
O **listă** este o colecție ordonată și modificabilă de elemente, delimitată prin paranteze drepte `[ ]`.
```python
fruits = ["apple", "banana", "orange", "mango"]
```

---

### 🔹 append()
Adaugă un element la finalul listei.
```python
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)
# Output: ['apple', 'banana', 'orange', 'mango']
```

---

### 🔹 copy()
Creează o copie superficială (shallow copy) a listei.
```python
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)
# Output: [1, 2, 3, 4, 5]
```

---

### 🔹 count()
Numără de câte ori apare un element în listă.
```python
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print(count)
# Output: 4
```

---

### 🔹 del
Șterge elementul de la un anumit index.
```python
my_list = [10, 20, 30, 40, 50]
del my_list[2]
print(my_list)
# Output: [10, 20, 40, 50]
```

---

### 🔹 extend()
Adaugă mai multe elemente dintr-o altă listă sau tuplu.
```python
fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)
# Output: ['apple', 'banana', 'orange', 'mango', 'grape']
```

---

### 🔹 Indexing
Accesează elemente după poziție (index). Indexarea începe de la `0`.
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[0])   # Output: 10
print(my_list[-1])  # Output: 50
```

---

### 🔹 insert()
Inserează un element la un anumit index.
```python
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)
# Output: [1, 2, 6, 3, 4, 5]
```

---

### 🔹 Modifying Elements
Modifică valorile folosind indexarea.
```python
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)
# Output: [10, 25, 30, 40, 50]
```

---

### 🔹 pop()
Elimină și returnează un element (implicit, ultimul).
```python
my_list = [10, 20, 30, 40, 50]
removed = my_list.pop(2)
print(removed)
# Output: 30
print(my_list)
# Output: [10, 20, 40, 50]
```

---

### 🔹 remove()
Șterge prima apariție a unui element.
```python
my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print(my_list)
# Output: [10, 20, 40, 50]
```

---

### 🔹 reverse()
Inversează ordinea elementelor din listă.
```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# Output: [5, 4, 3, 2, 1]
```

---

### 🔹 Slicing
Permite accesarea unei porțiuni din listă.
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])   # [2, 3, 4]
print(my_list[:3])    # [1, 2, 3]
print(my_list[2:])    # [3, 4, 5]
print(my_list[::2])   # [1, 3, 5]
```

---

### 🔹 sort()
Sortează elementele din listă.
```python
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)
# Output: [1, 2, 5, 8, 9]

my_list.sort(reverse=True)
print(my_list)
# Output: [9, 8, 5, 2, 1]
```

---

## 🔸 Tuples (Tupluri)

### 🔹 count()
Numără de câte ori apare un element într-un tuplu.
```python
fruits = ("apple", "banana", "apple", "orange")
print(fruits.count("apple"))
# Output: 2
```

---

### 🔹 index()
Returnează poziția primei apariții a unui element.
```python
fruits = ("apple", "banana", "orange", "apple")
print(fruits.index("apple"))
# Output: 0
```

---

### 🔹 sum()
Calculează suma elementelor numerice.
```python
numbers = (10, 20, 5, 30)
print(sum(numbers))
# Output: 65
```

---

### 🔹 min() / max()
Returnează cel mai mic și cel mai mare element.
```python
numbers = (10, 20, 5, 30)
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
```

---

### 🔹 len()
Returnează numărul total de elemente.
```python
fruits = ("apple", "banana", "orange")
print(len(fruits))
# Output: 3
```

---

## 🏁 Concluzie
- **Listele** sunt flexibile și pot fi modificate după creare.  
- **Tuplurile** sunt fixe și mai rapide, potrivite pentru date constante.  

> 💬 *„Stăpânirea listelor și tuplurilor în Python este cheia unei programări eficiente.”*
