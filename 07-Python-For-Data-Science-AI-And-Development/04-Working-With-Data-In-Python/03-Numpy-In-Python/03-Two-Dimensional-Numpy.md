# 🧮 Two-Dimensional NumPy Arrays

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Creezi și manipulezi **tablouri (arrays)** NumPy bidimensionale.  
- Accesezi și modifici elemente, rânduri și coloane într-un array 2D.  
- Aplici operații matematice și funcții NumPy pe matrice.  
- Înțelegi structura și utilizarea **array-urilor 2D** pentru analize de date.

---

## 🧠 Ce este un array bidimensional?

Un **array bidimensional (2D)** este o structură de date care conține **rânduri și coloane**, similar unui tabel sau unei matrici.  
În Python, aceste structuri sunt esențiale pentru calcule numerice și pentru prelucrarea datelor tabelare.

---

## 📗 Crearea unui array bidimensional

```python
import numpy as np

# Creăm un array 2D
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
```
➡️ `a` este o matrice de 3 rânduri și 3 coloane.

---

## 🔍 Proprietăți ale unui array 2D

```python
print(a.ndim)    # Numărul de dimensiuni (2)
print(a.shape)   # Forma (3, 3)
print(a.size)    # Numărul total de elemente (9)
print(a.dtype)   # Tipul de date al elementelor
```

---

## 📊 Accesarea elementelor

### Accesarea unui element specific
```python
print(a[0, 1])  # Elementul de pe primul rând, a doua coloană -> 2
```

### Accesarea unui rând
```python
print(a[1])  # Al doilea rând -> [4 5 6]
```

### Accesarea unei coloane
```python
print(a[:, 2])  # A treia coloană -> [3 6 9]
```

### Submatrice (slicing)
```python
print(a[0:2, 1:3])  # Primele două rânduri, coloanele 2 și 3
```

---

## ✏️ Modificarea valorilor

```python
a[1, 1] = 50     # Modifică elementul din rândul 2, coloana 2
print(a)
```

```python
a[:, 0] = [10, 20, 30]   # Modifică prima coloană
print(a)
```

---

## ➕ Operații matematice pe array-uri 2D

```python
b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(a + b)  # Adunare element cu element
print(a * 2)  # Înmulțire cu scalar
print(a - b)  # Scădere
print(a / b)  # Împărțire element cu element
```

---

## 🧮 Funcții NumPy utile pentru matrice

```python
print(np.mean(a))       # Media tuturor elementelor
print(np.mean(a, axis=0))  # Media pe coloane
print(np.mean(a, axis=1))  # Media pe rânduri
print(np.min(a))        # Valoarea minimă
print(np.max(a))        # Valoarea maximă
print(np.sum(a))        # Suma totală
```

---

## ⚙️ Generarea automată a array-urilor 2D

### Array de zerouri
```python
zeros = np.zeros((2, 3))
print(zeros)
```

### Array de valori constante
```python
const = np.full((3, 3), 5)
print(const)
```

### Array de numere consecutive
```python
seq = np.arange(9).reshape(3, 3)
print(seq)
```

### Array de numere aleatoare
```python
rand = np.random.rand(2, 4)
print(rand)
```

---

## 🔄 Operații pe rânduri și coloane

```python
print(a.sum(axis=0))  # Suma pe coloane
print(a.sum(axis=1))  # Suma pe rânduri
```

```python
print(a.T)  # Transpune matricea (rândurile devin coloane)
```

---

## 🔁 Îmbinarea (Concatenarea) matricei

### Pe rânduri
```python
c = np.array([[10, 11, 12]])
new_matrix = np.concatenate((a, c), axis=0)
print(new_matrix)
```

### Pe coloane
```python
d = np.array([[10], [20], [30]])
new_matrix = np.concatenate((a, d), axis=1)
print(new_matrix)
```

---

## 🧩 Funcții importante pentru array-uri 2D

| Funcție | Descriere |
|----------|------------|
| `np.array()` | Creează un array NumPy. |
| `reshape()` | Schimbă forma unui array. |
| `np.zeros()` | Creează un array de zerouri. |
| `np.ones()` | Creează un array de valori 1. |
| `np.full()` | Creează un array plin cu o valoare constantă. |
| `np.arange()` | Creează o secvență de valori. |
| `np.mean()` | Calculează media. |
| `np.sum()` | Calculează suma. |
| `np.transpose()` / `.T` | Transpune matricea. |
| `np.concatenate()` | Îmbină mai multe array-uri. |

---

## 🧠 Concluzie

Prin utilizarea **NumPy 2D Arrays**, poți:
- Modela și analiza tabele mari de date numeric.  
- Aplica operații vectorizate eficient.  
- Manipula rapid structuri matriciale pentru calcule științifice, date tabulare și machine learning.

**Array-urile bidimensionale** reprezintă baza manipulării datelor în biblioteci precum:
- **Pandas DataFrame**  
- **TensorFlow Tensors**  
- **Scikit-learn Matrices**  

---
