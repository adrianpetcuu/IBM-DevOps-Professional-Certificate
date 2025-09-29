# 📘 File and Directory Management Commands in Linux

Aceste comenzi sunt folosite pentru a crea, șterge, copia și muta fișiere și directoare.

---

## 🔹 Crearea fișierelor și directoarelor
- `touch fisier.txt` → creează un fișier gol.  
- `mkdir nume_dir` → creează un director nou.  
- `mkdir -p dir1/dir2/dir3` → creează o structură de directoare recursiv.  

---

## 🔹 Copiere
- `cp sursa dest` → copiază un fișier.  
- `cp file.txt /home/user/` → copiază fișierul în alt director.  
- `cp -r dir1 dir2` → copiază recursiv un director.  

---

## 🔹 Mutare și redenumire
- `mv sursa dest` → mută un fișier sau director.  
- `mv file.txt nou.txt` → redenumește un fișier.  
- `mv file.txt /home/user/` → mută fișierul în alt director.  

---

## 🔹 Ștergere
- `rm fisier.txt` → șterge un fișier.  
- `rm -i fisier.txt` → ștergere cu confirmare.  
- `rm -r dir/` → șterge un director recursiv.  
- `rm -rf dir/` → ștergere forțată (atenție, NU întreabă!).  

---

## 🔹 Căutare
- `find /cale -name "fisier.txt"` → caută un fișier după nume.  
- `find . -type f -name "*.txt"` → caută toate fișierele `.txt` în directorul curent.  

---

## 🔹 Exemple practice

```bash
touch test.txt                # creează fișier
mkdir proiect                 # creează director
cp test.txt proiect/          # copiază fișierul în director
mv proiect/test.txt demo.txt  # redenumește și mută
rm demo.txt                   # șterge fișierul
rm -r proiect/                # șterge directorul
```

---

## 🔹 Pe scurt
- **Creare**: `touch`, `mkdir`  
- **Copiere**: `cp`, `cp -r`  
- **Mutare/Rename**: `mv`  
- **Ștergere**: `rm`, `rm -r`, `rm -rf`  
- **Căutare**: `find`  
