# Cloning and Forking GitHub Projects

## Introducere
- **Cloning** și **Forking** sunt două metode prin care poți obține o copie a unui proiect de pe GitHub.
- Ambele îți permit să lucrezi pe cod, dar există diferențe importante în utilizare.

---

## 📌 Git Clone
- **Ce este?**
  - Creează o copie **identică** a repository-ului de pe GitHub pe calculatorul tău.
  - Este conectată direct la repo-ul original (remote = origin).
- **Când se folosește?**
  - Când ai permisiune de citire/scriere în repository.
  - Când lucrezi la un proiect privat sau în echipă.
- **Comandă:**
  ```bash
  - git clone <URL-repository>
  ```
- **Exemplu:**
  ```bash
  - git clone https://github.com/firma/proiect.git
  ```

---

## 📌 Git Fork
- **Ce este?**
  - Creează o copie **separată** a unui repository în propriul tău cont GitHub.
  - Îți oferă control total asupra copiei tale (poți face modificări fără a afecta repo-ul original).
- **Când se folosește?**
  - În special în proiecte **open-source**.
  - Când vrei să contribui la un proiect, dar nu ai acces direct la repo-ul original.
- **Pași:**
  1. Apeși butonul **Fork** pe pagina proiectului GitHub.
  2. Repo-ul este copiat în contul tău GitHub.
  3. Îl poți clona local:
     ```bash
     - git clone https://github.com/utilizatorul-tau/proiect.git
     ```

---

## 📌 Diferențe între Clone și Fork
- **Clone**
  - Copie locală a repo-ului original.
  - Remote-ul implicit este `origin` (repo-ul original).
  - Folosit pentru proiecte unde ai acces direct.
- **Fork**
  - Copie pe contul tău GitHub (remote separat).
  - Poți crea Pull Requests pentru a propune schimbări repo-ului original.
  - Remote-ul tău este `origin`, iar repo-ul original poate fi adăugat ca `upstream`.

---

## 📌 Workflow tipic cu Fork
1. Fork repo-ul original pe GitHub.
2. Clonează fork-ul tău local:
   ```bash
   - git clone https://github.com/utilizatorul-tau/proiect.git
   ```
3. Adaugă repo-ul original ca `upstream`:
   ```bash
   - git remote add upstream https://github.com/original/proiect.git
   ```
4. Sincronizează fork-ul cu upstream:
   ```bash
   - git pull upstream main
   - git push origin main
   ```
5. Fă modificări în fork și creează un Pull Request pentru a contribui.

---

## ✅ Concluzie
- **Clone** → pentru a lucra direct cu un repo la care ai acces.  
- **Fork** → pentru a contribui la proiecte externe, mai ales open-source.  
- Împreună, aceste tehnici fac colaborarea prin GitHub mult mai flexibilă.
