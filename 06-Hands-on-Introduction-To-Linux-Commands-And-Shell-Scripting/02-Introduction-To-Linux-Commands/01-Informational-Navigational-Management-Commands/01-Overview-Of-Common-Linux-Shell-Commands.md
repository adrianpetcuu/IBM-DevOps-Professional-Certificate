# 📘 Common Linux Shell Commands

Acest document oferă o privire de ansamblu asupra celor mai comune comenzi Linux folosite pentru navigare, gestionarea fișierelor, procese și permisiuni.

---

## 🔹 Informații despre utilizator și sistem
- `whoami` → afișează numele utilizatorului curent.  
- `uname` → afișează informații despre kernel.  
- `id` → arată ID-ul utilizatorului și al grupului.  
- `date` → afișează data și ora curentă.  

---

## 🔹 Fișiere și directoare
- `pwd` → arată directorul curent.  
- `ls` → listează fișierele și directoarele.  
- `cd nume_dir` → schimbă directorul curent.  
- `mkdir nume_dir` → creează un director nou.  
- `touch fisier.txt` → creează un fișier gol.  
- `cp sursa dest` → copiază un fișier sau director.  
- `mv sursa dest` → mută sau redenumește.  
- `rm fisier.txt` → șterge un fișier.  
- `find /cale -name "fisier"` → caută fișiere.  

---

## 🔹 Spațiu pe disc și procese
- `df -h` → arată spațiul liber pe disc (în format ușor de citit).  
- `ps` → afișează procesele care rulează.  
- `top` → monitorizare în timp real a proceselor.  

---

## 🔹 Afișare text și mesaje
- `echo "text"` → afișează textul dat.  

---

## 🔹 Permisiuni
- `ls -l` → afișează permisiunile fișierelor și directoarelor.  
- `chmod 755 fisier` → schimbă permisiunile.  

---

## 🔹 Manual și ajutor
- `man comanda` → afișează manualul pentru o comandă.  
  ```bash
  man ls
  ```  

---

## 🔹 Pe scurt
- **Navigare**: `pwd`, `ls`, `cd`, `mkdir`  
- **Fișiere**: `touch`, `cp`, `mv`, `rm`, `find`  
- **Procese și sistem**: `ps`, `top`, `df`, `uname`, `id`, `whoami`  
- **Permisiuni**: `ls -l`, `chmod`  
- **Ajutor**: `man`  
