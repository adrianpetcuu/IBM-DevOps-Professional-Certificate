# 📘 Useful Commands for Wrangling Text Files in Linux

Acest document prezintă comenzile utile pentru manipularea și procesarea fișierelor text în Linux.

---

## 🔹 sort
- Sortează liniile dintr-un fișier în ordine alfabetică sau numerică.
```bash
sort fisier.txt
sort -n numere.txt   # sortare numerică
```

---

## 🔹 uniq
- Elimină liniile duplicate consecutive dintr-un fișier.
```bash
uniq fisier.txt
sort fisier.txt | uniq       # sortare + eliminare duplicate
sort fisier.txt | uniq -c    # afișează și numărul aparițiilor
```

---

## 🔹 grep
- Caută text sau șabloane în fișiere.
```bash
grep "cuvant" fisier.txt
grep -i "linux" fisier.txt    # ignoră majusculele
grep -r "eroare" /var/log     # caută recursiv în directoare
```

---

## 🔹 cut
- Extrage coloane sau părți din fiecare linie.
```bash
cut -d "," -f1,3 date.csv   # extrage coloanele 1 și 3 delimitate prin virgulă
cut -c 1-5 fisier.txt       # extrage primele 5 caractere din fiecare linie
```

---

## 🔹 paste
- Combină liniile din două sau mai multe fișiere, linie cu linie.
```bash
paste fisier1.txt fisier2.txt
```

---

## 🔹 Pe scurt
- **sort** → ordonează liniile.  
- **uniq** → elimină duplicate.  
- **grep** → caută text.  
- **cut** → extrage coloane/fragmente.  
- **paste** → îmbină fișiere.  
