# 📘 Git Repository Guidelines

## 🔹 Git Feature Branch Workflow (Fluxul de lucru pe ramuri de funcționalități)

1. **Clone** – copiezi repository-ul de pe GitHub în local:  
   - git clone <url>

2. **Branch** – creezi o ramură nouă pentru o funcționalitate:  
   - git checkout -b feature/nume-functie

3. **Local Work** – faci modificările în branch-ul tău și le salvezi:  
   - git add .
   - git commit -m "Adăugat funcționalitate X"

4. **Push** – trimiți branch-ul pe GitHub:  
   - git push origin feature/nume-functie

5. **Pull Request (PR)** – ceri integrarea branch-ului tău în branch-ul principal (de obicei `main` sau `develop`).  
   - Aici echipa face **code review**.  

6. **Merge** – după aprobare, branch-ul tău se unește cu branch-ul principal.  

✅ **Avantaje:**  
- Evită conflictele.  
- Permite lucru paralel pe mai multe funcționalități.  
- Asigură calitate prin Pull Requests și Code Reviews.  

---

## 🔹 Guidelines recomandate pentru Git Repo

### 1. Un repository pentru fiecare componentă/proiect  
- Ușurează întreținerea și colaborarea.  
- Claritate: fiecare repo are un scop bine definit.  

### 2. Folosește Git Feature Branch Workflow  
- Creează branch-uri separate pentru fiecare feature, bugfix sau experiment.  
- Convenție recomandată:  
  - feature/login-page  
  - bugfix/fix-header  
  - hotfix/security-patch  

### 3. Pull Requests (PRs)  
- Toate modificările trec prin PR.  
- Permit **code review**, feedback și discuții înainte de integrare.  
- Asigură transparență și calitate.  

### 4. Mesaje de commit clare  
- Un commit = o schimbare logică.  
- Format recomandat:  
  - [tip] descriere scurtă  

  Exemple:  
  - [feature] Adăugat formular de login  
  - [fix] Rezolvat bug la validarea emailului  
  - [hotfix] Patch de securitate pentru autentificare  

### 5. README.md și documentație  
- Fiecare repo trebuie să aibă un fișier `README.md` cu:  
  - descrierea proiectului,  
  - instrucțiuni de instalare,  
  - ghid de contribuție,  
  - tehnologii folosite.  

### 6. .gitignore  
- Exclude fișierele inutile precum:  
  - logs,  
  - build-uri,  
  - configuri locale,  
  - fișiere temporare.  

### 7. Automatizare și CI/CD  
- Folosește GitHub Actions, Jenkins sau alte unelte pentru:  
  - testare automată,  
  - build automat,  
  - deployment continuu.  

---

## ✅ Concluzie
Un repository bine organizat are:
- branch-uri curate și bine denumite,  
- commit-uri clare și concise,  
- Pull Requests pentru fiecare schimbare,  
- documentație de bază (`README.md`, `CONTRIBUTING.md`),  
- fișiere inutile excluse cu `.gitignore`,  
- procese de CI/CD pentru calitate și viteză.  
