# 📘 Shell Scripting Basics

## 🔹 Ce este un Shell Script?
- Un **shell script** este un fișier text care conține o colecție de comenzi Linux/Unix.
- Aceste comenzi sunt executate secvențial de către un **shell interpreter** (ex: `sh`, `bash`, `zsh`).

Exemplu simplu de script:

```bash
#!/bin/bash
echo "Salut, lume!"
```

---

## 🔹 Shebang (`#!`)
- Prima linie dintr-un script începe, de obicei, cu **shebang** (`#!`).
- Indică ce **interpreter** trebuie să execute scriptul.

Exemple:
```bash
#!/bin/sh       # folosește Bourne Shell
#!/bin/bash     # folosește Bash (Bourne Again Shell)
#!/usr/bin/env python3   # folosește Python 3
```

---

## 🔹 Pașii pentru a crea și rula un shell script
1. **Creează fișierul:**
   ```bash
   nano script.sh
   ```

2. **Adaugă comenzi în fișier:**
   ```bash
   #!/bin/bash
   echo "Acesta este primul meu script"
   ```

3. **Fă fișierul executabil:**
   ```bash
   chmod +x script.sh
   ```

4. **Rulează scriptul:**
   ```bash
   ./script.sh
   ```

---

## 🔹 Variabile în Shell
- Definire variabilă:
  ```bash
  nume="Andrei"
  ```
- Folosire variabilă:
  ```bash
  echo "Salut, $nume"
  ```

---

## 🔹 Redirectări și Pipe-uri
- Redirecționarea ieșirii standard:
  ```bash
  ls > output.txt
  ```
- Redirecționarea erorilor:
  ```bash
  ls /folder/inexistent 2> erori.txt
  ```
- Combinarea stdout și stderr:
  ```bash
  comanda > out.txt 2>&1
  ```
- Pipe (`|`) → trimite ieșirea unei comenzi ca intrare pentru alta:
  ```bash
  cat fisier.txt | grep "cuvant"
  ```

---

## 🔹 Structuri de control
### IF-ELSE
```bash
#!/bin/bash
if [ -f "fisier.txt" ]; then
    echo "Fisierul exista"
else
    echo "Fisierul NU exista"
fi
```

### For loop
```bash
for i in 1 2 3
do
  echo "Valoare: $i"
done
```

### While loop
```bash
count=1
while [ $count -le 5 ]
do
  echo "Numar: $count"
  count=$((count+1))
done
```

---

## 🔹 Avantaje ale shell scripting
- Ușor de scris și rulat pentru task-uri repetitive.
- Automatizează procese (backup, monitorizare, configurări).
- Interpretează comenzi direct (nu necesită compilare).
- Portabilitate între majoritatea distribuțiilor Linux/Unix.

---

## 🔹 Rezumat
- **Shell scripts** = fișiere text cu comenzi Linux.
- Încep cu un **shebang** (`#!`) care specifică interpretul.
- Se fac executabile cu `chmod +x`.
- Pot folosi variabile, redirectări, pipe-uri și structuri de control.
