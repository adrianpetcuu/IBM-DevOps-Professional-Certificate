# 📘 Useful Features of the Bash Shell

## 🔹 Introducere
**Bash (Bourne Again SHell)** este cel mai folosit shell pe sistemele Linux.  
Are multe funcționalități utile pentru automatizare, scripting și lucrul interactiv.

---

## 🔹 1. Istoricul comenzilor
- Bash salvează comenzile introduse anterior.  
- Navigare în istoric:
  - `↑` și `↓` pentru a naviga.  
  - `history` → listează comenzile rulate.  
  - `!n` → rulează comanda cu numărul `n` din istoric.  
  - `!!` → rulează ultima comandă.  
  - `!string` → rulează ultima comandă care începe cu `string`.

Exemplu:
```bash
!!        # repetă ultima comandă
!ls       # repetă ultima comandă care începe cu 'ls'
```

---

## 🔹 2. Auto-completion (Tab Completion)
- Apasă **Tab** pentru a completa automat comenzi, fișiere sau foldere.  
- Dacă există mai multe opțiuni, apasă **Tab** de două ori pentru listare.

Exemplu:
```bash
cd Doc<Tab>
```

---

## 🔹 3. Aliasuri
- Aliasurile sunt scurtături pentru comenzi mai lungi.

Exemple:
```bash
alias ll='ls -la'
alias gs='git status'
```

- Pentru a le face permanente, adaugă în `~/.bashrc`.

---

## 🔹 4. Substituirea comenzilor
- Poți folosi ieșirea unei comenzi ca input pentru alta.

Exemplu:
```bash
echo "Astăzi este: $(date)"
```

---

## 🔹 5. Redirecționări avansate
- Redirectează ieșirea sau erorile către fișiere.

Exemple:
```bash
ls > out.txt         # stdout → fișier
ls 2> erori.txt      # stderr → fișier
ls &> toate.txt      # stdout + stderr → fișier
```

---

## 🔹 6. Job Control (procese)
- Rulează comenzi în background cu `&`.

Exemplu:
```bash
ping google.com &
```

- Comenzi utile:
  - `jobs` → arată procesele curente.  
  - `fg %1` → aduce jobul nr. 1 în foreground.  
  - `bg %1` → rulează jobul nr. 1 în background.  
  - `kill %1` → oprește jobul nr. 1.

---

## 🔹 7. Expansiunea variabilelor și globbing
- `*` → orice secvență de caractere.  
- `?` → un singur caracter.  
- `{}` → set de opțiuni.

Exemple:
```bash
echo *.txt        # toate fișierele .txt
echo file?.log    # file1.log, file2.log etc.
echo {a,b,c}.txt  # a.txt b.txt c.txt
```

---

## 🔹 Rezumat
- **Istoric** → `history`, `!!`, `!n`.  
- **Autocomplete** → Tab.  
- **Aliasuri** → scurtături pentru comenzi.  
- **Substituirea comenzilor** → `$(...)`.  
- **Redirectări** → `>`, `2>`, `&>`.  
- **Job control** → `jobs`, `fg`, `bg`, `kill`.  
- **Globbing** → `*`, `?`, `{}`.  

Aceste funcții fac Bash-ul mai puternic și mai productiv pentru utilizatorii Linux.
