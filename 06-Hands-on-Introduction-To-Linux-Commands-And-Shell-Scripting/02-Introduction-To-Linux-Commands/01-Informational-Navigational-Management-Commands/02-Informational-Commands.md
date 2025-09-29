# 📘 Informational Commands in Linux

Aceste comenzi sunt folosite pentru a obține informații despre sistem, utilizatori și procese.

---

## 🔹 Informații despre utilizator
- `whoami` → afișează numele utilizatorului curent.  
- `id` → afișează UID (user ID), GID (group ID) și grupurile asociate.  

---

## 🔹 Informații despre sistem
- `uname` → afișează informații despre kernel.  
  ```bash
  uname -r   # versiunea kernelului
  uname -a   # toate informațiile (kernel, arhitectură, etc.)
  ```

- `df -h` → afișează spațiul pe disc disponibil și utilizat (în format ușor de citit).  
- `free -h` → afișează utilizarea memoriei RAM și swap.  
- `uptime` → arată de cât timp este pornit sistemul și încărcarea medie.  

---

## 🔹 Procese și resurse
- `ps` → listează procesele care rulează pentru utilizatorul curent.  
- `ps aux` → listează toate procesele din sistem.  
- `top` → afișează în timp real procesele și utilizarea resurselor.  
- `htop` (dacă este instalat) → versiune interactivă și mai prietenoasă a lui `top`.  

---

## 🔹 Data și ora
- `date` → afișează data și ora curentă.  
- `cal` → afișează calendarul (luna curentă implicit).  
- `timedatectl` → arată setările de timp și fus orar.  

---

## 🔹 Manual și ajutor
- `man comanda` → afișează manualul unei comenzi.  
- `--help` → aproape fiecare comandă are această opțiune pentru explicații rapide.  

Exemplu:  
```bash
ls --help
```

---

## 🔹 Pe scurt
- **Utilizator**: `whoami`, `id`  
- **Sistem**: `uname`, `df`, `free`, `uptime`  
- **Procese**: `ps`, `top`, `htop`  
- **Data și ora**: `date`, `cal`, `timedatectl`  
- **Ajutor**: `man`, `--help`  
