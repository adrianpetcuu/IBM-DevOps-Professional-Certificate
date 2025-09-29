# 📘 Managing File Permissions and Ownership in Linux

În Linux, fiecare fișier și director are **permisiuni** și un **proprietar**. Acestea controlează cine poate citi, scrie sau executa un fișier.

---

## 🔹 Tipuri de permisiuni
- **r (read)** → citire (deschidere fișier, listare conținut director).  
- **w (write)** → scriere (modificare fișier, creare/ștergere în director).  
- **x (execute)** → executare (rulare script/program, acces în director).  

---

## 🔹 Categorii de utilizatori
- **u (user)** → utilizatorul (proprietarul fișierului).  
- **g (group)** → grupul de utilizatori asociat fișierului.  
- **o (others)** → restul utilizatorilor.  
- **a (all)** → toți utilizatorii (user + group + others).  

---

## 🔹 Afișarea permisiunilor
```bash
ls -l
```
Exemplu output:
```
-rwxr-xr--  1 andrei users  120 Sep 29  file.sh
```
Explicație:  
- `rwx` → proprietarul are **read, write, execute**.  
- `r-x` → grupul are **read, execute**.  
- `r--` → alții au doar **read**.  

---

## 🔹 Modificarea permisiunilor (`chmod`)

### Mod simbolic
```bash
chmod u+x script.sh     # adaugă execute pentru user
chmod g-w fisier.txt    # elimină write pentru group
chmod o=r fisier.txt    # setează doar read pentru others
chmod a+x program.sh    # toată lumea poate executa
```

### Mod numeric (octal)
- `r = 4`, `w = 2`, `x = 1`.  
- Se adună valorile pentru fiecare categorie.  
Exemple:
```bash
chmod 755 script.sh     # rwx (7) user, r-x (5) group, r-x (5) others
chmod 644 fisier.txt    # rw- (6) user, r-- (4) group și others
chmod 700 secret.txt    # rwx user, nimic pentru ceilalți
```

---

## 🔹 Schimbarea proprietarului și grupului
```bash
chown user fisier.txt         # schimbă proprietarul
chown user:grup fisier.txt    # schimbă proprietarul și grupul
chgrp grup fisier.txt         # schimbă doar grupul
```

Exemplu:
```bash
sudo chown maria raport.docx
sudo chown andrei:dev proiect/ -R   # recursiv pentru un director
```

---

## 🔹 Permisiuni pe directoare
- **r** → poți lista conținutul (`ls`).  
- **w** → poți crea/șterge fișiere.  
- **x** → poți intra (`cd`).  

Exemplu:
```bash
chmod 755 /home/maria     # user are acces complet, ceilalți doar listare+intrare
```

---

## 🔹 Pe scurt
- **Vizualizare**: `ls -l`  
- **Permisiuni**: `chmod` (simbolic sau numeric)  
- **Proprietar**: `chown`, `chgrp`  
- **Categorii**: user (u), group (g), others (o), all (a)  
