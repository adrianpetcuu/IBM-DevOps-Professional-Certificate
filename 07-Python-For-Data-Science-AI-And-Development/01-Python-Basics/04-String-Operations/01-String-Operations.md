# 🔤 Python String Operations — Operații cu șiruri de caractere

## 📘 Ce este un șir (string)
Un **șir de caractere** (string) este o secvență de caractere delimitată de ghilimele simple `' '` sau duble `" "`.  
În Python, șirurile sunt **imutabile**, adică nu pot fi modificate după ce au fost create.

Exemple:
```python
text1 = "Salut"
text2 = 'Python'
```

---

## 🔹 Concatenarea șirurilor
Concatenarea înseamnă **unirea a două sau mai multe șiruri**.

```python
a = "Hello"
b = "World"
rezultat = a + " " + b
print(rezultat)
```
📤 **Rezultat:**
```
Hello World
```

---

## 🔹 Repetarea unui șir
Operatorul `*` permite **repetarea** unui șir de mai multe ori.

```python
text = "Hi! "
print(text * 3)
```
📤 **Rezultat:**
```
Hi! Hi! Hi!
```

---

## 🔹 Accesarea caracterelor
Poți accesa caracterele individuale folosind **indexul** lor.  
Indexarea începe de la `0`.

```python
text = "Python"
print(text[0])  # P
print(text[-1]) # n (ultimul caracter)
```

---

## 🔹 Subșiruri (Slicing)
Poți extrage o porțiune dintr-un șir folosind `:` (slicing).

```python
text = "Python"
print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
```

---

## 🔹 Lungimea unui șir
Funcția `len()` returnează numărul total de caractere dintr-un șir.

```python
text = "Hello"
print(len(text))
```
📤 **Rezultat:**
```
5
```

---

## 🔹 Verificarea conținutului
Poți verifica dacă un subșir se află într-un alt șir folosind operatorul `in`.

```python
text = "Python programming"
print("Python" in text)  # True
print("Java" not in text)  # True
```

---

## 🔹 Transformarea literelor
Python oferă metode utile pentru transformarea literelor:
```python
text = "Python"
print(text.upper())  # majuscule
print(text.lower())  # minuscule
print(text.title())  # prima literă mare
```

📤 **Rezultat:**
```
PYTHON
python
Python
```

---

## 🔹 Eliminarea spațiilor
Metodele `strip()`, `lstrip()` și `rstrip()` elimină spațiile:
```python
text = "  Hello  "
print(text.strip())   # elimină spațiile din ambele părți
print(text.lstrip())  # elimină din stânga
print(text.rstrip())  # elimină din dreapta
```

---

## 🔹 Înlocuirea textului
Metoda `replace()` înlocuiește un subșir cu altul:
```python
text = "I like Java"
print(text.replace("Java", "Python"))
```
📤 **Rezultat:**
```
I like Python
```

---

## 🔹 Împărțirea și îmbinarea textului
Metoda `split()` separă un șir în funcție de un delimitator, iar `join()` leagă elementele dintr-o listă într-un singur șir.

```python
text = "apple,banana,cherry"
fructe = text.split(",")   # -> listă
print(fructe)

rezultat = " - ".join(fructe)
print(rezultat)
```
📤 **Rezultat:**
```
['apple', 'banana', 'cherry']
apple - banana - cherry
```

---

## 🔹 Șiruri multi-linie
Pentru texte lungi sau paragrafe, poți folosi triple ghilimele.

```python
text = """Python este un limbaj
ușor de învățat
și foarte popular."""
print(text)
```
📤 **Rezultat:**
```
Python este un limbaj
ușor de învățat
și foarte popular.
```

---

## 🏁 Concluzie
Operațiile cu șiruri sunt esențiale în Python pentru manipularea textului.  
Poți combina metodele pentru a crea, modifica și analiza texte complexe.

> 💬 *„În Python, șirurile sunt simple de folosit, dar extrem de puternice în practică.”*
