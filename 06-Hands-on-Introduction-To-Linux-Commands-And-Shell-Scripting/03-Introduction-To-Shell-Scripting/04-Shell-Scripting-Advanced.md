# 📘 Advanced Bash Scripting

## 🔹 Introducere
Advanced Bash Scripting presupune folosirea funcțiilor, expresiilor condiționale, trap, subshells și concepte avansate pentru a crea scripturi robuste și reutilizabile.

---

## 🔹 1. Funcții în Bash
Funcțiile permit structurarea codului și reutilizarea.

```bash
#!/bin/bash

salut() {
  echo "Salut, $1!"
}

salut "Andrei"
```

- Se pot returna valori prin `return` (coduri numerice) sau prin `echo`.

---

## 🔹 2. Parametri și argumente
- `$0` → numele scriptului.  
- `$1`, `$2` → primul și al doilea argument.  
- `$@` → lista tuturor argumentelor.  
- `$#` → numărul de argumente.  

Exemplu:
```bash
#!/bin/bash
echo "Script: $0"
echo "Primul argument: $1"
echo "Număr argumente: $#"
```

---

## 🔹 3. Expresii condiționale avansate
Se folosesc pentru testarea fișierelor, stringurilor și numerelor.

```bash
if [[ -f "fisier.txt" && -r "fisier.txt" ]]; then
  echo "Fisierul există și poate fi citit."
fi
```

Operatori utili:  
- `-f` fișier existent  
- `-d` director existent  
- `-r` citibil  
- `-w` scriibil  
- `-x` executabil  
- `==`, `!=` pentru stringuri  
- `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge` pentru numere  

---

## 🔹 4. Bucla `for`, `while`, `until`
```bash
for i in {1..5}; do
  echo "Valoare: $i"
done

count=1
while [ $count -le 3 ]; do
  echo "Count: $count"
  ((count++))
done

num=5
until [ $num -eq 0 ]; do
  echo "Countdown: $num"
  ((num--))
done
```

---

## 🔹 5. Subshells și comenzi în linie
- Parantezele rotunde `( )` creează un subshell.  
- Poți executa comenzi fără să afectezi mediul curent.

```bash
(cd /tmp && ls)
```

---

## 🔹 6. Redirecționări și here documents
- Redirectări avansate:
```bash
command > out.txt 2>&1
```

- Here document:
```bash
cat <<EOF > fisier.txt
Aceasta este o linie
Alta linie
EOF
```

---

## 🔹 7. Gestionarea erorilor și `trap`
- `trap` → permite executarea de comenzi la semnale sau la terminarea scriptului.

```bash
trap 'echo "Script întrerupt"; exit 1' SIGINT

echo "Apasă Ctrl+C pentru test"
sleep 10
```

---

## 🔹 8. Arrays în Bash
```bash
fructe=("mar" "banana" "portocala")
echo ${fructe[1]}     # banana
echo ${fructe[@]}     # toate elementele
echo ${#fructe[@]}    # numărul de elemente
```

---

## 🔹 9. Expresii regulate și `case`
```bash
echo "Introdu o literă:"
read litera

case $litera in
  [a-z]) echo "Literă mică";;
  [A-Z]) echo "Literă mare";;
  [0-9]) echo "Cifră";;
  *) echo "Alt caracter";;
esac
```

---

## 🔹 10. Scripturi robuste
- Folosește `set -euo pipefail` pentru a opri execuția la erori.  
- Folosește funcții pentru structurare.  
- Adaugă logging și mesaje de eroare.  

Exemplu:
```bash
#!/bin/bash
set -euo pipefail

log() { echo "$(date +%F_%T) - $*"; }

if [ ! -f "config.txt" ]; then
  log "Configurația lipsește!"
  exit 1
fi
```

---

## 🔹 Rezumat
- **Funcții** și **parametri** → modularitate.  
- **Expresii condiționale** → verificări complexe.  
- **Subshells** și **here documents** → flexibilitate.  
- **trap** → gestionarea semnalelor și cleanup.  
- **Arrays și case** → structură avansată de date și control.  
- **Best practices** → `set -euo pipefail`, logging, modularizare.

