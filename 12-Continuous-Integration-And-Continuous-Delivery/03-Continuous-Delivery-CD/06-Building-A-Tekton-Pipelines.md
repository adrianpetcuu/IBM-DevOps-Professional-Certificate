# 🏗️ Construirea unui Tekton Pipeline

## 🔹 Introducere

**Tekton** permite definirea și executarea de **pipeline-uri declarative** pentru automatizarea procesului CI/CD.  
Pipeline-urile sunt construite folosind resurse Kubernetes — `Task`, `Pipeline`, `PipelineRun`.

> Tekton este complet modular și rulează în containere, oferind flexibilitate și scalabilitate ridicată.

---

## ⚙️ 1. Structura de bază a unui pipeline Tekton

Un pipeline este format din:

- **Tasks** – unități de lucru (build, test, deploy).  
- **Steps** – comenzi care rulează în containere.  
- **Resources** – cod sursă, imagini Docker etc.  
- **PipelineRun** – o execuție completă a pipeline-ului.

---

## 🧩 2. Definirea unei Task

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-app
spec:
  steps:
    - name: build
      image: python:3.9
      script: |
        pip install -r requirements.txt
        python -m pytest
```

> Aceasta este o unitate reutilizabilă — o poți folosi în mai multe pipeline-uri.

---

## ⚙️ 3. Crearea unui Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: sample-pipeline
spec:
  tasks:
    - name: build
      taskRef:
        name: build-app
    - name: deploy
      runAfter: [build]
      taskRef:
        name: deploy-app
```

> `runAfter` definește ordinea de execuție între taskuri.

---

## 🧠 4. Executarea pipeline-ului

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: sample-pipeline-run
spec:
  pipelineRef:
    name: sample-pipeline
```

Rulează apoi în cluster:

```bash
kubectl apply -f pipeline-run.yaml
```

---

## 🧰 5. Exemple de Task suplimentare

### 🔹 Task pentru testare

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: test-app
spec:
  steps:
    - name: test
      image: python:3.9
      script: |
        pytest tests/
```

### 🔹 Task pentru deployment

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: deploy-app
spec:
  steps:
    - name: deploy
      image: alpine
      script: |
        echo "Deploying application..."
```

---

## 📦 6. Rulare și monitorizare

1. Aplică toate fișierele YAML:
   ```bash
   kubectl apply -f .
   ```

2. Verifică execuția pipeline-ului:
   ```bash
   tkn pipelinerun list
   tkn pipelinerun logs sample-pipeline-run -f
   ```

> Comanda `tkn` (CLI Tekton) este cea mai rapidă metodă de a urmări execuțiile.

---

## ⚙️ 7. Best Practices

| Practică | Descriere |
|-----------|------------|
| **Separă taskurile** | Fiecare task ar trebui să aibă o responsabilitate clară. |
| **Folosește workspaces** | Partajează fișiere între taskuri. |
| **Rulează în containere lightweight** | Optimizează timpul de execuție. |
| **Testează local YAML-urile** | Folosește `kubectl apply --dry-run=client`. |
| **Monitorizează pipeline-urile** | Utilizează `tkn dashboard` sau Tekton Dashboard UI. |

---

## 🧭 Concluzie

> Un pipeline Tekton bine construit este modular, portabil și scalabil.  
> Fiecare Task reprezintă o piesă reutilizabilă care contribuie la automatizarea completă a procesului DevOps.

---
