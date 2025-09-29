# 📘 File Archiving and Compression Commands in Linux

Acest document prezintă comenzile utilizate pentru arhivarea și compresia fișierelor în Linux.

---

## 🔹 zip
- Comprimă fișiere și directoare într-o arhivă `.zip`.
```bash
zip arhiva.zip fisier1.txt fisier2.txt
zip -r arhiva.zip director/
```

---

## 🔹 unzip
- Extrage fișiere dintr-o arhivă `.zip`.
```bash
unzip arhiva.zip
unzip arhiva.zip -d destinatie/
```

---

## 🔹 tar
- Creează și extrage arhive tip `tar` sau `tar.gz`.

### Creare arhivă fără compresie:
```bash
tar -cvf arhiva.tar fisier1.txt fisier2.txt
```

### Creare arhivă comprimată (.tar.gz):
```bash
tar -czvf arhiva.tar.gz director/
```

### Extrage arhivă simplă:
```bash
tar -xvf arhiva.tar
```

### Extrage arhivă comprimată:
```bash
tar -xzvf arhiva.tar.gz
```

---

## 🔹 Avantajele compresiei
- Reduce spațiul de stocare.  
- Accelerează transferul de date.  
- Scade încărcarea pe sistem.  

---

## 🔹 Pe scurt
- **zip** → comprimă fișiere.  
- **unzip** → extrage arhive `.zip`.  
- **tar** → creează/extrage arhive `.tar` și `.tar.gz`.  
