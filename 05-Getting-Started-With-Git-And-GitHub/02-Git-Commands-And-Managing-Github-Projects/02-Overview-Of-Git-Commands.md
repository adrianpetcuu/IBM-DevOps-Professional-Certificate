# Overview of Git Commands

## Introducere
- **Git** este un sistem de control al versiunilor distribuit.
- Permite echipelor să urmărească schimbările, să colaboreze și să mențină istoricul proiectelor.
- Există o serie de comenzi de bază și avansate care te ajută să gestionezi codul în mod eficient.

---

## 📌 Comenzi de configurare

- **git config --global user.name "Nume"**
  - Setează numele utilizatorului la nivel global.
- **git config --global user.email "email@exemplu.com"**
  - Setează adresa de email la nivel global.
- **git config --list**
  - Afișează toate setările active.

---

## 📌 Comenzi de inițializare și clonare

- **git init**
  - Creează un repository Git local gol în directorul curent.
- **git clone <URL>**
  - Copiază un repository existent de pe GitHub sau altă sursă pe calculatorul tău.

---

## 📌 Comenzi de lucru cu fișiere

- **git status**
  - Arată starea actuală a repository-ului (fișiere modificate, staged, untracked).
- **git add <fisier>**
  - Adaugă un fișier în zona de staging.
- **git add .**
  - Adaugă toate fișierele modificate și noi.
- **git commit -m "Mesaj"**
  - Salvează modificările din staging area în repository-ul local.
- **git diff**
  - Arată diferențele dintre fișiere (față de ultimul commit).

---

## 📌 Comenzi pentru branch-uri

- **git branch**
  - Listează toate branch-urile existente.
- **git branch <nume-branch>**
  - Creează un branch nou.
- **git checkout <nume-branch>**
  - Schimbă pe alt branch.
- **git checkout -b <nume-branch>**
  - Creează și schimbă direct pe un branch nou.
- **git merge <nume-branch>**
  - Combină modificările dintr-un branch în branch-ul curent.
- **git switch <branch>**
  - Alternativă modernă pentru `git checkout` (pentru schimbarea branch-urilor).

---

## 📌 Comenzi pentru remote

- **git remote -v**
  - Listează remote-urile asociate cu repository-ul.
- **git remote add origin <URL>**
  - Adaugă un remote cu numele „origin”.
- **git remote rename origin upstream**
  - Redenumește un remote.
- **git remote rm <nume>**
  - Șterge un remote.

---

## 📌 Comenzi de sincronizare cu remote

- **git push origin <branch>**
  - Trimite modificările locale pe GitHub.
- **git pull origin <branch>**
  - Aduce modificările din remote și face merge în branch-ul curent.
- **git fetch**
  - Aduce actualizări din remote, dar nu face merge automat.

---

## 📌 Comenzi de resetare și revenire

- **git reset <commit>**
  - Resetează repository-ul la un anumit commit.
- **git reset --hard HEAD**
  - Revine la ultimul commit, ștergând modificările locale.
- **git revert <commit>**
  - Creează un nou commit care inversează modificările unui commit anterior.
- **git restore <fisier>**
  - Restaurează un fișier la ultima versiune salvată.
- **git restore --staged <fisier>**
  - Scoate un fișier din staging area.

---

## 📌 Comenzi pentru vizualizare și istoric

- **git log**
  - Listează istoricul commit-urilor.
- **git show <commit>**
  - Afișează detalii despre un commit.
- **git blame <fisier>**
  - Arată cine a modificat fiecare linie dintr-un fișier.

---

## 📌 Comenzi avansate

- **git stash**
  - Salvează modificările neterminate temporar.
- **git stash pop**
  - Aplică modificările salvate anterior.
- **git cherry-pick <commit>**
  - Copiază un commit dintr-un branch în altul.
- **git tag <nume>**
  - Creează un tag (de exemplu pentru versiuni de release).
- **git bisect**
  - Caută commit-ul unde a apărut un bug prin binary search.

---

## Concluzie
- Git are multe comenzi, dar cele mai folosite zilnic sunt:
  - `git status`, `git add`, `git commit`, `git push`, `git pull`
- Comenzile pentru branch-uri (`git branch`, `git checkout -b`, `git merge`) sunt esențiale în colaborare.
- Comenzile avansate (`git stash`, `git cherry-pick`, `git revert`) sunt foarte utile în cazuri speciale.
