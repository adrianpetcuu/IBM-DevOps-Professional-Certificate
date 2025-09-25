# Demo: Working with Branches using Git Commands

## Introducere
- **Branch-urile** (ramurile) în Git permit dezvoltarea de funcționalități sau fix-uri în paralel, fără a afecta codul principal.
- Acest demo arată cum să creezi, să schimbi, să unești și să ștergi branch-uri folosind comenzi Git.

---

## 📌 Pașii principali

### 1. Crearea unui branch nou
- git branch feature-login
  👉 Creează un branch numit `feature-login`.

### 2. Comutarea pe branch
- git checkout feature-login
  👉 Schimbă pe noul branch pentru a lucra la funcționalitatea dorită.  
  (alternativ, poți face direct `git checkout -b feature-login` pentru creare + schimbare)

### 3. Verificarea branch-ului curent
- git branch
  👉 Listează toate branch-urile, marcând cu `*` pe cel activ.

### 4. Adăugarea și commit-ul modificărilor
- git add .
- git commit -m "Adăugat funcționalitatea de login"
  👉 Salvează modificările pe branch-ul `feature-login`.

### 5. Revenirea pe branch-ul principal
- git checkout main
  👉 Te întorci la codul stabil de pe `main`.

### 6. Îmbinarea branch-ului secundar în main
- git merge feature-login
  👉 Integrează schimbările din `feature-login` în `main`.

### 7. Ștergerea unui branch după integrare
- git branch -d feature-login
  👉 Șterge branch-ul local pentru a menține repo-ul curat.

---

## 📌 Workflow recomandat
1. Creezi un branch pentru fiecare funcționalitate sau bugfix.
2. Faci modificările și le comiți pe acel branch.
3. Integrezi branch-ul în `main` prin `merge` (sau Pull Request pe GitHub).
4. Ștergi branch-ul după ce nu mai e necesar.

---

## ✅ Beneficii
- Permite lucru în paralel fără a strica codul principal.
- Ușurează code review și colaborarea în echipă.
- Păstrează istoricul proiectului mai curat și mai organizat.
