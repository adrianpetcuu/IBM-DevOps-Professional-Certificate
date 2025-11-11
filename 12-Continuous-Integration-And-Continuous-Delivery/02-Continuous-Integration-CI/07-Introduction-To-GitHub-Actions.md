# ⚙️ Introducere în GitHub Actions

## 🔹 Ce este GitHub Actions?

**GitHub Actions** este o platformă integrată în GitHub care permite **automatizarea fluxurilor de lucru (workflows)** direct din repository-ul tău.  
Cu ajutorul acesteia, poți automatiza procese precum:
- testarea codului,  
- construirea aplicațiilor,  
- livrarea (deployment) automată,  
- verificarea calității codului,  
- actualizări de documentație.

> Pe scurt, GitHub Actions este modul prin care GitHub implementează **CI/CD (Continuous Integration și Continuous Delivery)**.

---

## 🧩 Cum funcționează GitHub Actions

Fluxurile GitHub Actions sunt definite prin fișiere **YAML** aflate în folderul:
```
.github/workflows/
```

Aceste fișiere descriu **când** și **ce** trebuie să se execute — de exemplu, la fiecare *push* în ramura `main`.

---

## ⚙️ Structura unui Workflow

Un fișier GitHub Actions are trei secțiuni principale:

### 1. `name:`  
Dă un nume workflow-ului.  
```yaml
name: CI Workflow
```

### 2. `on:`  
Definește **evenimentele** care declanșează execuția (ex: `push`, `pull_request`, `release` etc.).  
```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

### 3. `jobs:`  
Definește **sarcinile (jobs)** care trebuie executate. Fiecare job poate conține mai multe **pași (steps)**.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Run tests
        run: pytest
```

---

## 🧠 Termeni importanți

| Termen | Descriere |
|--------|------------|
| **Workflow** | Un fișier YAML care descrie procesul automatizat. |
| **Event** | Acțiunea care declanșează workflow-ul (ex: `push`, `pull_request`). |
| **Job** | Un set de pași care rulează pe aceeași mașină virtuală. |
| **Step** | O comandă individuală sau o acțiune care rulează în cadrul unui job. |
| **Action** | O sarcină reutilizabilă definită de GitHub sau de comunitate (ex: `actions/checkout`). |
| **Runner** | Mașina virtuală pe care rulează workflow-ul. |

---

## 🚀 Exemplu complet de Workflow

```yaml
name: Python CI Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

Acest exemplu definește un pipeline de testare automat pentru o aplicație Python.  
La fiecare *push* sau *pull request* către ramura `main`, GitHub:
1. descarcă codul,  
2. instalează Python,  
3. instalează pachetele,  
4. rulează testele automate.

---

## 🔑 Declanșatoare (Events)

Exemple de evenimente comune care pot declanșa workflow-uri:

| Eveniment | Descriere |
|------------|------------|
| `push` | Când cineva trimite cod în repository. |
| `pull_request` | Când se deschide sau se actualizează un PR. |
| `release` | Când se publică o nouă versiune. |
| `schedule` | La un interval de timp programat (cron job). |
| `workflow_dispatch` | Poate fi declanșat manual. |

---

## 🧰 Exemple de acțiuni comune

| Acțiune | Utilizare |
|----------|------------|
| `actions/checkout` | Clonează codul din repository. |
| `actions/setup-node` | Instalează Node.js. |
| `actions/setup-python` | Instalează Python. |
| `actions/upload-artifact` | Stochează fișiere generate de pipeline. |
| `actions/cache` | Optimizează timpul de execuție prin caching. |

---

## 🧩 Beneficiile GitHub Actions

- ⚙️ Automatizează complet procesul CI/CD.  
- 🚀 Reduce timpul de integrare și livrare.  
- 💬 Se integrează perfect cu GitHub (PR-uri, issues, commits).  
- 🧪 Rulează teste și builduri automat.  
- 🌍 Suportă orice limbaj (Python, Java, Node.js, Go, etc.).  

---

## 💡 Exemplu: Workflow declanșat manual

```yaml
name: Manual Deployment

on:
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Server
        run: echo "Deployment initiated manually"
```

> Acest exemplu poate fi rulat manual din interfața GitHub, în secțiunea **Actions**.

---

## 🧭 Pe scurt

> **GitHub Actions** este o unealtă puternică pentru automatizarea proceselor DevOps.  
> Cu ajutorul fișierelor YAML, poți defini fluxuri de lucru pentru testare, build, deployment sau orice alt proces repetitiv.

---