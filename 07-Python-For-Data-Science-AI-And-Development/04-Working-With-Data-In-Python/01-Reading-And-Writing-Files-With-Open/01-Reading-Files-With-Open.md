# 📘 Citirea Fișierelor cu `open()` în Python

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Explica cum se utilizează funcțiile `open()` și `read()` pentru a deschide și citi conținutul unui fișier text.
- Utiliza instrucțiunea `with` în Python pentru gestionarea automată a fișierelor.
- Folosi metodele `readline()` și `readlines()` pentru citirea conținutului fișierelor.
- Utiliza funcția `seek()` pentru a citi caractere din poziții specifice ale fișierului.

---

## 📂 1. Deschiderea fișierelor

Există două metode principale pentru deschiderea fișierelor în Python:

### 🔹 a) Folosind funcția `open()`
```python
file = open('fisier.txt', 'r')
```
- `'r'` → mod de citire (read)
- `'w'` → mod de scriere (write)
- `'a'` → mod de adăugare (append)

După finalizarea operațiunilor, **închide fișierul**:
```python
file.close()
```

### 🔹 b) Folosind instrucțiunea `with`
```python
with open('fisier.txt', 'r') as file:
    continut = file.read()
    print(continut)
```
✅ Avantaj: `with` închide automat fișierul la finalul blocului de cod, chiar și în caz de eroare.

---

## 🧠 2. Citirea conținutului unui fișier

### 🔸 Citirea întregului fișier
```python
with open('example1.txt', 'r') as file:
    continut = file.read()
    print(continut)
```
> Metoda `read()` citește întregul conținut al fișierului ca un singur șir de caractere (`string`).

---

### 🔸 Citirea unui număr specific de caractere
```python
with open('example1.txt', 'r') as file:
    print(file.read(4))   # primele 4 caractere
    print(file.read(5))   # următoarele 5 caractere
```
Pentru a muta cursorul la o anumită poziție, folosește `seek()`:
```python
file.seek(10)  # mută cursorul la poziția 10
```

---

### 🔸 Citirea linie cu linie
```python
with open('example1.txt', 'r') as file:
    print("Prima linie:", file.readline())
    print("A doua linie:", file.readline())
```

Poți limita și numărul de caractere citite dintr-o linie:
```python
with open('example1.txt', 'r') as file:
    print(file.readline(20))  # citește doar 20 de caractere
```

---

### 🔸 Parcurgerea fișierului linie cu linie
```python
with open('example1.txt', 'r') as file:
    for i, line in enumerate(file):
        print(f"Linia {i}: {line}")
```

---

### 🔸 Salvarea liniilor într-o listă
```python
with open('example1.txt', 'r') as file:
    linii = file.readlines()

print(linii[0])  # prima linie
print(linii[1])  # a doua linie
```
> `readlines()` returnează o listă în care fiecare element reprezintă o linie din fișier.

---

## ⚙️ 3. Verificarea stării fișierului
După închiderea fișierului, poți verifica dacă acesta este închis:
```python
print(file.closed)  # Afișează True dacă fișierul este închis
```

---

## 🏁 4. Concluzie

- `open()` creează un obiect de tip fișier și permite citirea/scrierea datelor.
- `with open()` este recomandat pentru o gestionare automată a resurselor.
- Metode utile:
  - `read()` → citește întregul fișier
  - `readline()` → citește o singură linie
  - `readlines()` → returnează toate liniile ca o listă
  - `seek()` → mută poziția cursorului în fișier

---

## 💡 Sfat suplimentar
Dacă folosești Windows, ai grijă la **căile absolute** precum `'/Example.txt'`, care pot duce la erori de tip *PermissionError*.  
Folosește mereu `os.path.join()` pentru compatibilitate multiplatformă.

---

## 👩‍💻 Exemplu complet
```python
# Citirea unui fișier linie cu linie
with open('exemplu.txt', 'r') as f:
    for linie in f:
        print(linie.strip())
```

