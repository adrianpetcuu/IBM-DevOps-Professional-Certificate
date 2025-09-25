# Overview of Git Workflows

## Ce este un Workflow Git?
- Un **workflow Git** reprezintă modul în care o echipă folosește Git pentru a organiza dezvoltarea codului.
- Scopul este de a avea un proces clar, care permite colaborare, versionare și integrare continuă.

---

## Tipuri de Git Workflows

### 1. Centralized Workflow
- Toată echipa lucrează pe un singur branch principal (de obicei `main` sau `master`).
- Fiecare developer face commit și push direct pe branch-ul central.
- Simplu de înțeles, dar pot apărea conflicte frecvente.
- Potrivit pentru echipe mici sau proiecte foarte simple.

### 2. Feature Branch Workflow
- Fiecare funcționalitate nouă se dezvoltă pe un **branch separat**.
- După ce e gata, se face **merge** în `main` printr-un **Pull Request**.
- Avantaje:
  - Codul principal rămâne stabil.
  - Permite code review înainte de integrare.
- Este unul dintre cele mai folosite modele în dezvoltarea modernă.

### 3. Gitflow Workflow
- Un workflow mai avansat, cu ramuri dedicate:
  - `main` – pentru versiuni stabile, gata de producție.
  - `develop` – pentru integrarea funcționalităților noi.
  - `feature/*` – pentru dezvoltarea de funcționalități.
  - `release/*` – pentru pregătirea unei versiuni.
  - `hotfix/*` – pentru bugfix-uri rapide pe producție.
- Structurat, dar poate fi prea complex pentru echipe mici.

### 4. Forking Workflow
- Folosit mai ales la proiecte **open-source**.
- Fiecare contributor face un **fork** al repository-ului oficial.
- Modificările se fac în fork → apoi se creează un Pull Request spre repo-ul original.
- Avantaje:
  - Contribuitorii nu au nevoie de permisiuni pe repo-ul oficial.
  - Oferă un control strict asupra codului care intră în proiect.

---

## Cum alegi un Workflow?
- **Echipe mici, proiect simplu** → Centralized Workflow.
- **Echipe de mărime medie** → Feature Branch Workflow.
- **Proiecte mari, cu release-uri clare** → Gitflow Workflow.
- **Open-source** → Forking Workflow.

---

## Beneficii ale folosirii Workflows
- Claritate în modul de lucru.
- Colaborare mai bună între dezvoltatori.
- Reducerea conflictelor și a erorilor.
- Integrare mai ușoară cu procese DevOps (CI/CD).

