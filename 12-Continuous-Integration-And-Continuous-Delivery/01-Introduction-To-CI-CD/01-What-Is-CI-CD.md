# 🔁 Ce este CI/CD (Continuous Integration și Continuous Delivery)

## 🧩 Continuous Integration (CI) – Integrare Continuă

**Definiție:**  
Integrarea continuă este o practică de dezvoltare software în care membrii echipei își integrează frecvent modificările de cod într-un depozit comun (repository).  
Fiecare integrare declanșează un proces automat de **build** și **testare** pentru a detecta rapid erorile.

**Scopul CI:**  
Să asigure că aplicația rămâne într-o stare funcțională și stabilă, chiar și atunci când mai mulți dezvoltatori lucrează simultan pe același proiect.

**Etapele tipice ale CI:**
1. Dezvoltatorul face un *commit* al codului în repository (ex: GitHub, GitLab).  
2. Sistemul CI (ex: Jenkins, Travis CI, GitHub Actions) pornește automat un build.  
3. Se rulează testele automate (unitare, de integrare).  
4. Se verifică calitatea codului și compatibilitatea cu restul aplicației.  

**Beneficii:**
- Detectarea timpurie a erorilor.  
- Reducerea conflictelor de cod („merge conflicts”).  
- Feedback rapid pentru echipă.  
- Codul rămâne mereu într-o stare stabilă și testată.

---

## 🚀 Continuous Delivery (CD) – Livrare Continuă

**Definiție:**  
Livrarea continuă este o extensie a integrării continue. După ce codul este integrat și testat, acesta este **automat pregătit pentru lansare** și **implementare (deploy)** într-un mediu de testare sau producție.

**Scopul CD:**  
Să permită livrarea rapidă, sigură și frecventă a aplicației către utilizatori.

**Etapele tipice ale CD:**
1. Preia codul testat din pipeline-ul CI.  
2. Creează automat artefactele aplicației (ex: imagine Docker, pachet executabil).  
3. Rulează teste suplimentare în medii de staging.  
4. Poate implementa automat în producție (dacă este folosită *Continuous Deployment*).  

**Beneficii:**
- Lansări rapide și frecvente.  
- Reducerea riscului de erori la deploy.  
- Proces de livrare predictibil și automatizat.  
- Feedback continuu de la utilizatori și echipă.  

---

## ⚙️ Relația dintre CI, CD și Continuous Deployment

| Practică | Ce face | Automatizează până la |
|-----------|----------|------------------------|
| **Continuous Integration (CI)** | Integrează și testează codul frecvent | Build + Test |
| **Continuous Delivery (CD)** | Pregătește codul testat pentru lansare | Build + Test + Deploy în staging |
| **Continuous Deployment** | Publică automat codul în producție | Build + Test + Deploy în producție |

---

## 🧠 Pe scurt

> **CI/CD** este coloana vertebrală a practicilor **DevOps**, permițând echipelor să livreze software mai **rapid**, mai **sigur** și cu **mai puțin efort manual**.  
> CI se concentrează pe *integrarea și testarea* codului, iar CD pe *livrarea și implementarea* lui automată.

---

## 🔧 Exemple de instrumente CI/CD

- **CI Tools:** Jenkins, GitHub Actions, GitLab CI, Travis CI, CircleCI  
- **CD Tools:** ArgoCD, Spinnaker, Tekton, Azure DevOps  

---
