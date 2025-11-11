# 🧠 Deeper Dive into GitHub Actions

## 🔹 Introducere

După ce ai învățat bazele GitHub Actions, este timpul să explorăm mai în detaliu modul în care funcționează această platformă.  
În această secțiune vom analiza:
- cum funcționează **declanșatoarele (events)**,  
- cum se definesc **variabilele și secretele**,  
- cum funcționează **dependențele între joburi**,  
- și cum poți **extinde** GitHub Actions cu acțiuni personalizate.

---

## ⚙️ 1. Evenimente (Triggers)

GitHub Actions poate fi declanșat de o gamă largă de evenimente.  
Cuvântul cheie folosit pentru a specifica un eveniment este `on:`.

### 🔑 Exemple comune de evenimente:

```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  release:
    types: [created]
  schedule:
    - cron: "0 9 * * 1"   # Luni, ora 09:00 UTC
  workflow_dispatch:       # Declanșare manuală
```

| Cuvânt cheie | Descriere |
|---------------|------------|
| `push` | Rulează workflow-ul la fiecare commit trimis. |
| `pull_request` | Se declanșează când un PR este deschis sau actualizat. |
| `release` | Rulează workflow-ul la publicarea unei versiuni noi. |
| `schedule` | Rulează automat pe baza unui program (folosește sintaxa cron). |
| `workflow_dispatch` | Permite rularea manuală a workflow-ului din interfața GitHub. |

---

## 🧩 2. Variabile și Secrete

GitHub Actions permite utilizarea **variabilelor de mediu** pentru a stoca informații reutilizabile.

### 🔹 Variabile implicite
GitHub oferă variabile implicite cum ar fi:
- `GITHUB_REPOSITORY` → numele repository-ului
- `GITHUB_REF` → ramura curentă
- `GITHUB_SHA` → hash-ul commitului

Exemplu:
```yaml
run: echo "Rulez pe branch-ul ${{ github.ref }}"
```

### 🔹 Variabile definite de utilizator
```yaml
env:
  APP_ENV: production
  DEBUG: false

steps:
  - name: Print environment
    run: echo "Mediul este $APP_ENV"
```

### 🔒 Secrete
Valorile sensibile (tokenuri, parole, chei API) se salvează în secțiunea **Settings → Secrets → Actions**  
Apoi pot fi utilizate astfel:

```yaml
env:
  API_KEY: ${{ secrets.MY_SECRET_KEY }}
```

---

## 🔀 3. Joburi dependente

În GitHub Actions, poți defini joburi care depind unul de altul folosind `needs:`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Build complet!"

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - run: echo "Rulez testele după build."
```

> Jobul `test` se va executa **numai după** ce `build` s-a terminat cu succes.

---

## 🧰 4. Matrici de builduri (Build Matrix)

Poți rula același set de teste pe mai multe platforme și versiuni simultan:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ "3.8", "3.9", "3.10" ]
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - run: pytest
```

> Astfel, aplicația ta este testată automat pe mai multe versiuni de Python.

---

## 🧱 5. Cache și Artefacte

### 🔹 Cache
Folosește cache pentru a accelera instalarea dependențelor:

```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

### 🔹 Artefacte
Salvează fișierele generate în timpul pipeline-ului pentru descărcare ulterioară:

```yaml
- name: Upload build output
  uses: actions/upload-artifact@v3
  with:
    name: build-output
    path: dist/
```

---

## ⚙️ 6. Rularea pe mai multe sisteme

GitHub Actions oferă suport pentru mai multe medii de execuție (`runners`):

| Runner | Descriere |
|---------|------------|
| `ubuntu-latest` | Linux (cel mai folosit pentru CI/CD) |
| `windows-latest` | Windows Server |
| `macos-latest` | macOS |

Exemplu:
```yaml
runs-on: windows-latest
```

---

## 🧩 7. Acțiuni personalizate

Pe lângă acțiunile existente (oficiale sau din marketplace), poți crea și **acțiuni personalizate**.

### 🔧 Tipuri de acțiuni personalizate
| Tip | Limbaj | Exemplu |
|------|----------|----------|
| **JavaScript Actions** | Node.js | Crează logică direct în JS |
| **Docker Actions** | Dockerfile | Rulează în containere izolate |

Exemplu de acțiune Docker (`action.yml`):

```yaml
name: Hello World
runs:
  using: 'docker'
  image: 'Dockerfile'
inputs:
  who-to-greet:
    description: 'Cine să fie salutat'
    required: true
```

---

## 🧭 8. Debugging și Loguri

Pentru a activa modul de depanare:
```yaml
ACTIONS_RUNNER_DEBUG: true
ACTIONS_STEP_DEBUG: true
```

sau adaugă în interfața GitHub un secret numit `ACTIONS_STEP_DEBUG` cu valoarea `true`.

> Logurile detaliate ajută la identificarea rapidă a erorilor în pipeline.

---

## 🚀 Exemplu complex – Build + Test + Deploy

```yaml
name: Full CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build app
        run: echo "Building app..."

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Run tests
        run: echo "Running tests..."

  deploy:
    runs-on: ubuntu-latest
    needs: [ build, test ]
    steps:
      - name: Deploy to server
        run: echo "Deployment successful!"
```

> Acest workflow execută buildul, rulează testele și apoi face deploy doar dacă pașii anteriori au fost finalizați cu succes.

---

## 🧭 Pe scurt

> GitHub Actions oferă control complet asupra proceselor CI/CD, permițând configurarea avansată a joburilor, dependențelor, secretelelor și mediilor.  
> Cu o planificare corectă, poți automatiza aproape orice proces DevOps direct din GitHub.

---
