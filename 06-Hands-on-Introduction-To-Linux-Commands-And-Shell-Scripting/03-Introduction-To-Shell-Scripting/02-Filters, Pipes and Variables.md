# 📘 Filters, Pipes, and Variables

## 🔹 Ce sunt filtrele în Linux?
- **Filtrele** sunt programe/command-line tools care citesc date de la **stdin** (standard input), le procesează și trimit rezultatul către **stdout** (standard output).
- Exemple comune:
  - `grep` → caută linii care conțin un anumit pattern.
  - `sort` → sortează liniile dintr-un fișier sau flux.
  - `uniq` → elimină liniile duplicate consecutive.
  - `wc` → numără caractere, cuvinte și linii.
  - `cut` → extrage coloane sau câmpuri.

Exemple:
```bash
cat fisier.txt | grep "cuvant"
ls -l | sort -k 5
cat fisier.txt | uniq
```

---

## 🔹 Ce sunt pipe-urile (`|`)?
- **Pipe-ul** (`|`) conectează ieșirea unei comenzi la intrarea altei comenzi.  
- Se folosește pentru a crea **lanțuri de comenzi**.

Exemple:
```bash
cat log.txt | grep "ERROR" | sort | uniq
ls -l | grep ".sh" | wc -l
```

Explicație exemplu:
- `ls -l` → listează fișierele.
- `grep ".sh"` → selectează doar fișierele `.sh`.
- `wc -l` → numără câte fișiere `.sh` există.

---

## 🔹 Variabile în Shell
- O **variabilă** reține o valoare (text, număr etc.).  
- Se definește cu `=` (fără spații).

Exemple:
```bash
nume="Ana"
echo $nume
```

- Variabile de mediu → vizibile pentru toate procesele:
```bash
export PATH=$PATH:/home/user/bin
```

- Listarea variabilelor de mediu:
```bash
env
```

---

## 🔹 Exemple practice combinate
1. Folosind variabile și filtre:
```bash
cuvant="Linux"
cat fisier.txt | grep "$cuvant"
```

2. Numărăm fișierele `.log` dintr-un folder:
```bash
ls *.log | wc -l
```

3. Extragem primele 5 linii unice dintr-un fișier:
```bash
cat fisier.txt | sort | uniq | head -n 5
```

---

## 🔹 Rezumat
- **Filtrele** → procesează date (grep, sort, wc, uniq, cut).  
- **Pipe-urile (`|`)** → leagă comenzi între ele.  
- **Variabilele** → stochează valori, accesate cu `$nume`.  
- Împreună → permit construirea de **pipeline-uri** pentru procesarea rapidă a datelor.
