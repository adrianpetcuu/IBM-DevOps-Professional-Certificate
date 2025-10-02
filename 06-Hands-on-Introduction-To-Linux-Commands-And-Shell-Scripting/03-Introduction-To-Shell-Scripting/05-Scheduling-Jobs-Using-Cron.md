# 📘 Scheduling Jobs using Cron

## 🔹 Ce este `cron`?
- **Cron** este un serviciu Linux folosit pentru a rula comenzi sau scripturi la intervale regulate.  
- Util pentru sarcini repetitive precum backup, actualizări automate sau monitorizare.

---

## 🔹 Structura unei linii din crontab
Fiecare linie din `crontab` are forma:

```
* * * * * comanda
- - - - -
| | | | |
| | | | +---- ziua săptămânii (0 - 6) (Duminică = 0 sau 7)
| | | +------ luna (1 - 12)
| | +-------- ziua lunii (1 - 31)
| +---------- ora (0 - 23)
+------------ minutul (0 - 59)
```

Exemplu:  
```bash
30 2 * * * /home/user/backup.sh
```
➡ Rulează scriptul `backup.sh` zilnic la ora **02:30**.

---

## 🔹 Cum editezi crontab
- Deschide editorul pentru utilizatorul curent:
```bash
crontab -e
```

- Vezi joburile programate:
```bash
crontab -l
```

- Șterge crontab-ul curent:
```bash
crontab -r
```

---

## 🔹 Exemple utile de cron jobs
1. Rulează script la fiecare 5 minute:
```bash
*/5 * * * * /home/user/script.sh
```

2. Rulează zilnic la miezul nopții:
```bash
0 0 * * * /home/user/cleanup.sh
```

3. Rulează doar lunea la ora 8 dimineața:
```bash
0 8 * * 1 /home/user/report.sh
```

4. Rulează la fiecare reboot:
```bash
@reboot /home/user/startup.sh
```

---

## 🔹 Operatorii speciali
- `@reboot` → la fiecare pornire a sistemului.  
- `@daily` → o dată pe zi la miezul nopții.  
- `@weekly` → o dată pe săptămână.  
- `@monthly` → o dată pe lună.  
- `@yearly` sau `@annually` → o dată pe an.  

Exemplu:
```bash
@daily /home/user/sync.sh
```

---

## 🔹 Redirectarea logurilor în cron
Pentru a salva ieșirea în fișier log:
```bash
0 3 * * * /home/user/backup.sh >> /var/log/backup.log 2>&1
```

---

## 🔹 Rezumat
- `cron` → programator de task-uri în Linux.  
- Folosește `crontab -e` pentru configurare.  
- Format: `minut ora zi_lună lună zi_săptămână comanda`.  
- Oferă și comenzi rapide (`@daily`, `@reboot`).  
- Poți redirecționa ieșirea către loguri.  
