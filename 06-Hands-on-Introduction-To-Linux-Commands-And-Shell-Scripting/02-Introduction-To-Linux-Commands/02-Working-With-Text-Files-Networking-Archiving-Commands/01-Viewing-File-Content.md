# 📘 Viewing File Content in Linux

Acest document prezintă comenzile utilizate pentru a vizualiza conținutul fișierelor în Linux.

---

## 🔹 cat
- Afișează conținutul complet al unui fișier în terminal.  
```bash
cat fisier.txt
```

---

## 🔹 more
- Afișează conținutul pe pagini (navigare cu `Space` pentru pagina următoare, `Enter` pentru linie).  
```bash
more fisier.txt
```

---

## 🔹 less
- Similar cu `more`, dar mai avansat (poți naviga înainte și înapoi).  
- Navigare cu săgeți, `Space` pentru pagină nouă, `q` pentru ieșire.  
```bash
less fisier.txt
```

---

## 🔹 head
- Afișează primele linii ale unui fișier (implicit 10).  
```bash
head fisier.txt
head -n 20 fisier.txt   # primele 20 de linii
```

---

## 🔹 tail
- Afișează ultimele linii ale unui fișier (implicit 10).  
```bash
tail fisier.txt
tail -n 15 fisier.txt   # ultimele 15 linii
tail -f fisier.log      # urmărește fișierul în timp real (util pentru loguri)
```

---

## 🔹 wc (word count)
- Afișează numărul de linii, cuvinte și caractere dintr-un fișier.  
```bash
wc fisier.txt       # linii, cuvinte, caractere
wc -l fisier.txt    # doar linii
wc -w fisier.txt    # doar cuvinte
wc -c fisier.txt    # doar caractere
```

---

## 🔹 Pe scurt
- **Vizualizare completă**: `cat`  
- **Vizualizare pe pagini**: `more`, `less`  
- **Primele/ultimele linii**: `head`, `tail`  
- **Numărare**: `wc`  
