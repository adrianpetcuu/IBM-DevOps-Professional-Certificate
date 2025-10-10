# 🧮 One-Dimensional NumPy Arrays

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Creezi și lucrezi cu **tablouri (arrays)** NumPy unidimensionale.  
- Accesezi, modifici și efectuezi operații matematice pe elemente.  
- Înțelegi diferențele dintre **listele Python** și **tablourile NumPy**.  
- Aplici funcții vectorizate pentru calcule rapide și eficiente.

---

## 🧠 Ce este NumPy?

**NumPy (Numerical Python)** este o bibliotecă esențială pentru calcule numerice în Python.  
Ea oferă structura **array**, care este mai eficientă decât listele Python standard, permițând:
- stocare compactă a datelor numerice,  
- operații vectorizate (fără bucle explicite),  
- funcții matematice rapide.  

Pentru a folosi NumPy, trebuie mai întâi importată biblioteca:

```python
import numpy as np
```

---

## 📗 Crearea unui array unidimensional

Poți crea un **array** NumPy dintr-o listă Python:

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a)
```

➡️ `a` este acum un **NumPy array**, nu o listă Python.

### Tipul de obiect:
```python
print(type(a))
# <class 'numpy.ndarray'>
```

---

## 🔍 Proprietăți ale unui array

```python
print(a.ndim)     # Dimensionalitatea (1 pentru unidimensional)
print(a.shape)    # Forma (numărul de elemente)
print(a.size)     # Numărul total de elemente
print(a.dtype)    # Tipul de date (ex: int32, float64)
```

---

## 📊 Accesarea elementelor

Similar listelor Python:

```python
print(a[0])    # Primul element
print(a[-1])   # Ultimul element
```

Poți selecta mai multe elemente cu **slicing**:

```python
print(a[1:4])   # Elemente de la indexul 1 la 3
```

---

## ✏️ Modificarea valorilor

```python
a[0] = 100
print(a)
```

---

## ➕ Operații matematice vectorizate

NumPy permite aplicarea directă a operațiilor asupra întregului array:

```python
b = np.array([5, 10, 15, 20, 25])
print(a + b)   # Adunare element cu element
print(a * 2)   # Înmulțire scalară
print(a / 10)  # Împărțire scalară
print(a ** 2)  # Ridicare la putere
```

---

## 🧮 Funcții matematice NumPy

```python
print(np.mean(a))     # Media aritmetică
print(np.std(a))      # Deviația standard
print(np.min(a))      # Valoarea minimă
print(np.max(a))      # Valoarea maximă
print(np.sum(a))      # Suma elementelor
```

---

## ⚙️ Generarea automată a array-urilor

### Array de numere consecutive
```python
arr = np.arange(0, 10, 2)
print(arr)
# [0 2 4 6 8]
```

### Array de numere liniare (spațiate egal)
```python
arr = np.linspace(0, 1, 5)
print(arr)
# [0.   0.25 0.5  0.75 1.  ]
```

### Array de zerouri sau de valori constante
```python
zeros = np.zeros(5)
ones = np.ones(5)
const = np.full(5, 7)

print(zeros)
print(ones)
print(const)
```

---

## 🔁 Conversii între tipuri de date

```python
a = np.array([1.7, 2.5, 3.9])
print(a.astype(int))   # Conversie la int
```

---

## ⚡ Diferențe față de listele Python

| Operație              | Listă Python          | NumPy Array              |
|------------------------|----------------------|--------------------------|
| Tip de date            | Poate conține orice  | Numai un singur tip      |
| Viteză                 | Mai lent             | Mult mai rapid           |
| Memorie                | Ineficientă          | Compactă                 |
| Operații element-wise  | Nu direct posibilă   | Da, prin vectorizare     |

---

## 🧩 Funcții utile pentru array-uri unidimensionale

| Funcție | Descriere |
|----------|------------|
| `np.arange()` | Creează un interval de valori numerice. |
| `np.linspace()` | Creează valori uniform distribuite. |
| `np.zeros()` | Creează un array plin cu zerouri. |
| `np.ones()` | Creează un array plin cu valori 1. |
| `np.full()` | Creează un array plin cu o valoare constantă. |
| `np.mean()` | Media valorilor. |
| `np.std()` | Deviația standard. |
| `np.sum()` | Suma elementelor. |
| `np.min()` / `np.max()` | Valorile minimă și maximă. |

---

## 🧠 Concluzie

Prin utilizarea **NumPy**, poți manipula și analiza rapid seturi mari de date numerice.  
Array-urile oferă o modalitate eficientă de a efectua calcule vectorizate fără a scrie bucle complexe.

**NumPy** este baza tuturor bibliotecilor majore din domeniul științei datelor, cum ar fi:
- **Pandas**  
- **Scikit-Learn**  
- **TensorFlow**  
- **PyTorch**

---
