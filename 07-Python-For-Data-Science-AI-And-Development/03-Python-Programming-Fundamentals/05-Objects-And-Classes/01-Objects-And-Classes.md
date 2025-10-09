# 🧩 Python Objects and Classes — Obiecte și Clase

## 📘 Introducere
În Python, **Programarea Orientată pe Obiecte (OOP)** este o metodă de organizare a codului care se bazează pe conceptele de **clasă** și **obiect**.  
O **clasă** definește structura și comportamentul (atribute și metode), iar un **obiect** este o instanță concretă a acelei clase.

---

## 🔹 Definirea unei clase
O clasă se definește folosind cuvântul cheie `class`.

```python
class Circle:
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
```
🔸 `__init__` este **constructorul** — metoda specială apelată automat la crearea unui obiect.  
🔸 `self` se referă la instanța curentă a clasei (obiectul creat).

---

## 🔹 Crearea unui obiect
```python
circle1 = Circle(5, 'red')
print(circle1.radius)
print(circle1.color)
```
📤 **Rezultat:**
```
5
red
```

---

## 🔹 Adăugarea metodelor
Metodele definesc comportamentul unei clase (ce poate face un obiect).

```python
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
```
### ✅ Utilizare:
```python
RedCircle = Circle(10, 'red')
print(RedCircle.radius)
RedCircle.drawCircle()
RedCircle.add_radius(5)
print(RedCircle.radius)
```

---

## 🔹 Exemplu cu clasa `Rectangle`
```python
class Rectangle:
    def __init__(self, width=2, height=3, color='green'):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()
```

### ✅ Utilizare:
```python
rect1 = Rectangle(4, 5, 'yellow')
rect1.drawRectangle()
```

---

## 🚗 Exemplu complex: Clasa `Vehicle`

```python
class Vehicle:
    color = "white"  # atribut de clasă (comun tuturor obiectelor)

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)
```

### ✅ Crearea obiectelor:
```python
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
```

📤 **Rezultat:**
```
Properties of the Vehicle:
Color: white
Maximum Speed: 200
Mileage: 20
Seating Capacity: 5

Properties of the Vehicle:
Color: white
Maximum Speed: 180
Mileage: 25
Seating Capacity: 4
```

---

## 🔹 Tipuri de atribute

| Tip | Descriere | Exemplu |
|-----|------------|----------|
| **Atribut de clasă** | Comun tuturor instanțelor | `color = "white"` |
| **Atribut de instanță** | Specific unui obiect | `self.mileage` |
| **Metodă de instanță** | Funcție definită într-o clasă | `def display_properties(self)` |

---

## 🔹 Funcția `dir()`
Returnează toate metodele și atributele unui obiect.

```python
print(dir(vehicle1))
```

---

## 🧠 Sfaturi utile
- Folosește nume descriptive pentru clase și metode.  
- Adaugă comentarii sau docstring-uri (""" text """).  
- Evită duplicarea codului prin reutilizarea metodelor.  
- O clasă = o responsabilitate clară.

---

## 🏁 Concluzie
Prin clase și obiecte, Python îți permite să modelezi entități din lumea reală, să structurezi codul logic și să reutilizezi componentele.  

> 💬 *„O clasă bine gândită este fundația unui program scalabil.”*
