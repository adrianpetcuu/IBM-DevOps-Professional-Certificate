# 🧪 Crearea de Task-uri pentru Verificări de Calitate și Testare (Tekton)

## 🔹 Introducere

Într-un pipeline CI/CD, verificările automate de calitate și testele sunt esențiale.  
Tekton permite crearea de **Task-uri personalizate** care asigură conformitatea, calitatea codului și stabilitatea aplicației.

> Scopul acestor task-uri este de a preveni implementarea codului defectuos în producție.

---

## ⚙️ 1. Tipuri de verificări de calitate

| Tip verificare | Scop |
|-----------------|------|
| **Linting** | Asigură conformitatea codului cu standardele definite. |
| **Testare unitară** | Verifică funcționalitățile individuale. |
| **Testare de integrare** | Confirmă interacțiunea corectă între module. |
| **Scanare de securitate** | Detectează vulnerabilități în cod sau dependențe. |
| **Analiză statică** | Identifică erori logice sau cod duplicat. |

---

## 🧩 2. Exemplu: Task pentru linting Python

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: lint-python
spec:
  steps:
    - name: run-flake8
      image: python:3.9
      script: |
        pip install flake8
        flake8 --max-line-length=120 .
```

> Această task verifică stilul de cod folosind `flake8`.  
> Dacă sunt detectate erori, pipeline-ul se oprește automat.

---

## ⚙️ 3. Task pentru rularea testelor unitare

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: unit-tests
spec:
  steps:
    - name: run-tests
      image: python:3.9
      script: |
        pip install -r requirements.txt
        pytest --junitxml=report.xml
```

> Testele eșuate vor opri pipeline-ul automat, asigurând că doar codul valid continuă spre livrare.

---

## ⚙️ 4. Task pentru scanare de securitate

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: trivy-scan
spec:
  params:
    - name: image
      type: string
  steps:
    - name: scan
      image: aquasec/trivy:latest
      script: |
        trivy image $(params.image)
```

> Folosește **Trivy** pentru a scana imaginile container pentru vulnerabilități cunoscute.

---

## 🧰 5. Integrarea testelor în pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: ci-quality-pipeline
spec:
  tasks:
    - name: lint
      taskRef:
        name: lint-python
    - name: unit-test
      runAfter: [lint]
      taskRef:
        name: unit-tests
    - name: security-scan
      runAfter: [unit-test]
      taskRef:
        name: trivy-scan
      params:
        - name: image
          value: "docker.io/example/app:latest"
```

> Ordinea este importantă: lint → testare → scanare securitate.

---

## ⚙️ 6. Task pentru analiza codului cu SonarQube

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: sonar-analysis
spec:
  params:
    - name: sonar-url
    - name: sonar-token
  steps:
    - name: sonar-scan
      image: sonarsource/sonar-scanner-cli:latest
      script: |
        sonar-scanner           -Dsonar.host.url=$(params.sonar-url)           -Dsonar.login=$(params.sonar-token)
```

> Integrarea SonarQube ajută la detectarea codului duplicat, erorilor și vulnerabilităților.

---

## 🧠 7. Recomandări pentru testare eficientă

| Recomandare | Explicație |
|--------------|-------------|
| Rulează testele automat la fiecare commit. | Asigură detectarea rapidă a erorilor. |
| Păstrează testele independente. | Evită blocajele între module. |
| Folosește containere mici și rapide. | Optimizează timpul de execuție. |
| Colectează rapoarte JUnit / XML. | Permite analizarea automată a rezultatelor. |

---

## 🧩 8. Exemple de instrumente populare

| Tip verificare | Instrument | Imagine Docker recomandată |
|-----------------|-------------|-----------------------------|
| Linting Python | `flake8`, `pylint` | `python:3.9` |
| Teste unitare | `pytest`, `unittest` | `python:3.9` |
| Scanare securitate | `trivy`, `grype` | `aquasec/trivy` |
| Analiză statică | `sonar-scanner` | `sonarsource/sonar-scanner-cli` |
| Teste JS | `jest`, `mocha` | `node:18` |

---

## 🧭 9. Beneficii ale verificărilor automate de calitate

✅ Crește încrederea în codul livrat.  
✅ Detectează erorile înainte de livrare.  
✅ Îmbunătățește performanța echipei DevOps.  
✅ Asigură conformitatea cu standardele de dezvoltare.  
✅ Permite integrarea ușoară cu Tekton Catalog și GitOps.

---

## 🚀 Concluzie

> Tekton permite definirea rapidă a verificărilor automate de calitate și testare.  
> Task-urile dedicate pentru linting, testare și securitate îți asigură un pipeline complet, robust și sigur.

---