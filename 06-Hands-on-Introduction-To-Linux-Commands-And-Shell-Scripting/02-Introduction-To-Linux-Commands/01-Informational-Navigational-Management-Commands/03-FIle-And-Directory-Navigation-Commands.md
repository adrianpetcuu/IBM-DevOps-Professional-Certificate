# 📘 File and Directory Navigation Commands in Linux

Aceste comenzi sunt folosite pentru a naviga prin sistemul de fișiere, a afla locația curentă și a lista conținutul directoarelor.

---

## 🔹 Comenzi de bază

- `pwd` → afișează calea completă a directorului curent (print working directory).  
- `ls` → listează fișierele și directoarele din directorul curent.  
- `ls -l` → afișare detaliată (permisiuni, dimensiune, proprietar, dată).  
- `ls -a` → afișează și fișierele ascunse (cele care încep cu `.`).  
- `cd nume_dir` → schimbă directorul curent în `nume_dir`.  
- `cd ..` → urcă un nivel mai sus (directorul părinte).  
- `cd ~` → merge direct în directorul home al utilizatorului.  
- `cd /` → merge la directorul rădăcină.  

---

## 🔹 Exemple practice

```bash
pwd                      # arată directorul curent
ls -l                    # listă detaliată a fișierelor
cd /home/user/Documente  # mergi într-un director specific
cd ..                    # urcă un nivel în sus
cd ~                     # mergi în /home/user (directorul personal)
```

---

## 🔹 Comenzi utile combinate

```bash
ls -lh                   # listă cu dimensiuni ușor de citit (KB, MB)
ls -R                    # listă recursivă (inclusiv subdirectoare)
ls /etc                  # afișează conținutul directorului /etc
```

---

## 🔹 Pe scurt
- **Afișare locație**: `pwd`  
- **Listare fișiere**: `ls`, `ls -l`, `ls -a`  
- **Schimbare director**: `cd`, `cd ..`, `cd ~`, `cd /`  
