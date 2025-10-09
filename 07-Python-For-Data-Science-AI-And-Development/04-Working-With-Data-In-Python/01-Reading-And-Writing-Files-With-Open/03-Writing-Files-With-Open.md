# ✍️ Scrierea Fișierelor cu `open()` în Python

## 🎯 Obiective
După finalizarea acestui laborator, vei putea:
- Crea și scrie date într-un fișier text în Python.
- Scrie mai multe linii într-un fișier folosind liste și bucle.
- Adăuga informații noi într-un fișier existent fără a șterge conținutul anterior.
- Înțelege diferitele moduri de deschidere a fișierelor și când să le folosești.
- Folosi funcțiile `seek()`, `tell()` și `truncate()` pentru gestionarea poziției și dimensiunii fișierului.

---

## 🧾 1. Crearea și Scrierea într-un Fișier (`'w'`)

```python
# Crearea unui fișier nou (sau suprascrierea dacă există)
with open('Exemplu.txt', 'w') as f:
    f.write("Aceasta este linia A\n")
    f.write("Aceasta este linia B\n")
# fișierul este închis automat la finalul blocului with
```

**Note:**
- Modul `'w'` **suprascrie** fișierul dacă acesta există deja.
- `\n` adaugă o nouă linie.

---

## 🧵 2. Scrierea Mai Multor Linii dintr-o Listă

```python
linii = ["Aceasta este linia 1\n", "Aceasta este linia 2\n", "Aceasta este linia 3\n"]
with open('Exemplu.txt', 'w') as f:
    for linie in linii:
        f.write(linie)
```

> Această metodă este utilă pentru a scrie conținut din liste generate dinamic sau rezultate din alte procese.

---

## ➕ 3. Adăugarea la un Fișier Existent (`'a'` / `'a+'`)

```python
# Adăugarea la sfârșitul fișierului
with open('Exemplu.txt', 'a') as f:
    f.write('Aceasta este o nouă linie\n')
```

> Modul `'a'` adaugă text la finalul fișierului fără a șterge conținutul existent.  
> Dacă fișierul nu există, este creat automat.

### Adăugare + Citire (`'a+'`)
```python
with open('Exemplu.txt', 'a+') as f:
    f.write('Altă linie nouă\n')
    f.seek(0)          # Mutăm cursorul la începutul fișierului
    print(f.read())    # Citim tot conținutul
```

---

## ✍️ 4. Citire și Scriere în Același Fișier (`'r+'`) + `seek()` + `truncate()`

```python
with open('Exemplu.txt', 'r+') as f:
    f.seek(0)                 # Mută cursorul la început
    f.write("Linia 1\n")
    f.write("Linia 2\n")
    f.write("Finalizat\n")
    f.truncate()              # Șterge orice conținut rămas după cursor
    f.seek(0)
    print(f.read())
```

**Explicație:**
- `seek(offset, whence)` → mută cursorul în fișier (0 = început, 1 = poziția curentă, 2 = final).
- `tell()` → returnează poziția curentă a cursorului.
- `truncate()` → taie fișierul de la poziția curentă (utile pentru rescrieri parțiale).

---

## 📄 5. Copierea Conținutului Între Fișiere

```python
with open('Sursa.txt', 'r') as sursa:
    with open('Destinatie.txt', 'w') as destinatie:
        for linie in sursa:
            destinatie.write(linie)
```

> Această metodă permite copierea simplă a conținutului dintr-un fișier în altul.

---

## ⚙️ 6. Modurile de Deschidere a Fișierelor în Python

| Mod | Descriere |
|------|-----------|
| `'r'` | Citire. Deschide un fișier existent pentru citire. Eroare dacă fișierul nu există. |
| `'w'` | Scriere. Creează un fișier nou sau suprascrie unul existent. |
| `'a'` | Adăugare. Deschide fișierul pentru adăugare la final. |
| `'x'` | Creare exclusivă. Creează un fișier nou, dă eroare dacă există deja. |
| `'r+'` | Citire și scriere într-un fișier existent. |
| `'w+'` | Scriere și citire. Suprascrie fișierul dacă există. |
| `'a+'` | Adăugare și citire. Creează fișierul dacă nu există. |
| `'b'` | Deschide fișierul în mod binar. Se combină cu alte moduri (ex: `'rb'`, `'wb'`). |
| `'t'` | Deschide fișierul în mod text (implicit). |

---

## ✅ 7. Recomandări Importante

- Folosește **`with open()`** — închide fișierul automat, chiar dacă apare o eroare.  
- Modul `'w'` **șterge conținutul existent**. Folosește `'a'` pentru a păstra datele vechi.  
- Cu `'a+'`, mută cursorul la început (`seek(0)`) înainte de citire.  
- Evită căile absolute precum `'/Exemplu.txt'` pe Windows → pot genera *PermissionError*.  
- Folosește `os.path.join()` pentru compatibilitate multiplatformă.  
- Adaugă întotdeauna `\n` la finalul liniilor pentru a păstra formatul corect.

---

## 👩‍💻 Exemplu Complet
```python
# Scrierea unui fișier
with open('demo.txt', 'w') as f:
    f.write("Linia 1\n")
    f.write("Linia 2\n")

# Adăugarea de text
with open('demo.txt', 'a') as f:
    f.write("Linia 3\n")

# Citirea fișierului
with open('demo.txt', 'r') as f:
    print(f.read())
```

---

## 📘 Concluzie
Python oferă funcționalități simple, dar puternice, pentru lucrul cu fișiere.  
Prin utilizarea corectă a modurilor (`'w'`, `'a'`, `'r+'`, `'a+'`) și a funcțiilor precum `seek()` și `truncate()`, poți controla complet procesul de scriere, citire și actualizare a datelor din fișiere.

---
