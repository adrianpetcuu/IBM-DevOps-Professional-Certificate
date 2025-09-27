# 📘 Creating and Editing Text Files (Linux)

Un ghid practic pentru a crea, vizualiza și edita fișiere text din linia de comandă. Perfect pentru începători, dar include și tips & tricks utile în DevOps.

---

## 🔹 Ce este un fișier text?
Un fișier text conține **caractere** (ASCII/UTF‑8) fără formatare. Este folosit pentru:
- configurații (`*.conf`, `*.ini`, `*.yaml`)
- scripturi (`*.sh`, `*.py`)
- notițe, loguri etc.

---

## 🔹 Crearea fișierelor

### 1) Fișier gol
```bash
touch fisier.txt         # creează fișier dacă nu există (sau îi schimbă timestamp-ul)
```

### 2) Creare cu conținut imediat
```bash
echo "Salut, Linux!" > fisier.txt          # suprascrie conținutul
echo "Linie nouă" >> fisier.txt            # adaugă la final
printf "Prima linie
A doua linie
" > fisier.txt
```

### 3) Redirecționare cu `cat` / here-doc
```bash
cat > notite.txt <<'EOF'
Asta este o notiță.
Liniile rămân exact cum le scrii.
EOF
# Folosește ghilimele în <<'EOF' ca să NU expandeze variabilele sau backslash-urile.
```

### 4) Din output-ul unei comenzi
```bash
ls -l /etc > lista_etc.txt
date >> jurnal.txt
```

> ℹ️ Dacă numele are spații, folosește ghilimele: `echo ok > "nume fisier cu spatiu.txt"`.

---

## 🔹 Vizualizarea fișierelor

```bash
cat fisier.txt                  # afișează întregul fișier
less fisier.txt                 # navigare cu săgeți / PgUp / PgDn, taste: q=quit, /cuvant=caută
head -n 10 fisier.txt           # primele 10 linii (implicit 10)
tail -n 20 fisier.txt           # ultimele 20 de linii
tail -f /var/log/syslog         # urmărește în timp real (follow)
nl fisier.txt                   # numerotează liniile
```

---

## 🔹 Editarea fișierelor (CLI)

### 1) **Nano** – simplu și prietenos
```bash
nano fisier.txt
```
- `Ctrl + O` salvează, `Enter` confirmă numele
- `Ctrl + X` iese, `Ctrl + W` căutare, `Alt + 6` copiere, `Ctrl + K` tăiere, `Ctrl + U` lipire

### 2) **Vim** – puternic (scurt pe 3 comenzi esențiale)
```bash
vim fisier.txt
```
- `i` intri în modul Insert → scrii
- `Esc :w` salvezi, `Esc :q` ieși, `Esc :wq` salvezi & ieși, `Esc :q!` ieși fără salvare
- căutare `/text`, înlocuire `:%s/vechi/nou/g`

### 3) **Editoare grafice** (dacă ai GUI)
```bash
gedit fisier.txt        # GNOME
kate fisier.txt         # KDE
code fisier.txt         # VS Code (dacă e instalat)
```

---

## 🔹 Editări rapide fără editor (one-liners utile)

### Înlocuire text cu `sed`
```bash
sed -i 's/vechi/nou/g' fisier.txt              # -i = editează în loc (in-place)
sed -i.bak 's/8080/80/' app.conf               # păstrează backup app.conf.bak
```

### Afișează doar liniile ce conțin un șablon cu `grep`
```bash
grep -n "ERROR" /var/log/app.log               # -n numerotează liniile
grep -i "user" fisier.txt                      # -i = case-insensitive
```

### Adăugare la început/sfârșit
```bash
printf "HEADER
%s" "$(cat fisier.txt)" > fisier.txt     # adaugă „HEADER” la început
echo "FOOTER" >> fisier.txt                              # adaugă la final
```

### Inserare multi-linie (append) cu here-doc
```bash
cat >> config.ini <<'EOF'
[feature]
enabled=true
EOF
```

---

## 🔹 Permisiuni și executabile
```bash
chmod 644 fisier.txt         # rw-r--r-- (utilizator poate scrie, ceilalți doar citesc)
chmod +x script.sh           # face scriptul executabil
./script.sh                  # rulează (dacă are shebang corect: #!/bin/bash)
```

---

## 🔹 Redirecționări & pipe-uri (cheat sheet)
```bash
cmd > file         # scrie (suprascrie)
cmd >> file        # adaugă
cmd < file         # citește input din fișier
cmd1 | cmd2        # pipe: output-ul lui cmd1 devine input pentru cmd2
cmd 2> erori.log   # redirecționează eroarea (stderr)
cmd > out 2>&1     # unește stdout + stderr în același fișier
```

---

## 🔹 Encodări și terminatoare de linie
- În Linux, terminatorul de linie este **LF** (`\n`). În Windows este **CRLF** (`\r\n`).
- Conversii:
```bash
dos2unix fisier.txt      # CRLF → LF
unix2dos fisier.txt      # LF → CRLF
file fisier.txt          # detectează encodarea/terminatorul
iconv -f ISO-8859-2 -t UTF-8 vechi.txt > nou.txt
```

---

## 🔹 Bune practici
- Folosește **UTF-8** pentru encodare și **LF** pentru linii.
- Păstrează **backup** când faci înlocuiri automate (`-i.bak` la `sed`).
- Denumește clar fișierele: `YYYY-MM-DD-nume-scurt.md`.
- Pentru fișiere de config, preferă formate predictibile: **YAML/TOML/INI**.
- Documentează comenzile într-un README sau în comentarii.

---

## 🔹 Rezumat rapid (cheat sheet)
```bash
# creare
touch f.txt
echo "text" > f.txt
cat > f.txt <<'EOF'
Linii multiple
EOF

# vizualizare
cat f.txt | nl
less f.txt
head -n 5 f.txt
tail -f f.txt

# editare
nano f.txt
vim f.txt
sed -i 's/vechi/nou/g' f.txt

# permisiuni & execuție
chmod 644 f.txt
chmod +x script.sh && ./script.sh
```

---

## 🔹 Troubleshooting frecvent
- **„Permission denied”** → folosește `sudo` sau verifică `chmod`/`chown`.
- **„No such file or directory”** → verifică calea, folosește `pwd`/`ls`.
- **Caractere ciudate la afișare** → problemă de encodare; verifică `file`, convertește cu `iconv`.
- **Nu pot salva în `/etc`** → ai nevoie de privilegii: `sudo nano /etc/nume.conf`.

---

**Succes!** Acum poți crea și edita fișiere text rapid și în siguranță în Linux.
