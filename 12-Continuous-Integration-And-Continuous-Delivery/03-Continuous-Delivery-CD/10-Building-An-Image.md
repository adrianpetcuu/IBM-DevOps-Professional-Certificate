# 🏗️ Construirea unei Imagini Docker cu Tekton

## 🔹 Introducere

Tekton permite automatizarea completă a procesului de **construire a imaginilor container (Docker)** direct în pipeline-uri CI/CD.  
Prin integrarea cu instrumente precum **Buildah**, **Kaniko** sau **Docker CLI**, echipele DevOps pot crea imagini sigure, reproductibile și fără acces root.

> Scopul: automatizarea build-urilor containerizate într-un mod portabil și sigur.

---

## ⚙️ 1. Abordări posibile pentru construirea imaginilor

| Instrument | Descriere | Avantaj principal |
|-------------|------------|------------------|
| **Kaniko** | Creează imagini Docker fără daemon. | Siguranță și compatibilitate. |
| **Buildah** | Alternativă lightweight pentru construirea imaginilor. | Nu necesită privilegiu root. |
| **Docker CLI** | Folosește daemonul Docker. | Simplu, dar necesită acces root. |

---

## 🧩 2. Task din Tekton Catalog pentru Buildah

```yaml
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: buildah-build
spec:
  taskRef:
    name: buildah
  params:
    - name: IMAGE
      value: docker.io/example/app:latest
    - name: CONTEXT
      value: .
    - name: DOCKERFILE
      value: ./Dockerfile
  workspaces:
    - name: source
      persistentVolumeClaim:
        claimName: buildah-workspace
```

> Task-ul `buildah` poate fi instalat din Tekton Hub și rulează fără daemon Docker.

---

## ⚙️ 3. Task alternativă pentru Kaniko

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-with-kaniko
spec:
  params:
    - name: IMAGE
      description: Imaginea care va fi construită
    - name: CONTEXT
      description: Directorul sursă
      default: .
  steps:
    - name: kaniko-build
      image: gcr.io/kaniko-project/executor:latest
      args:
        - "--dockerfile=Dockerfile"
        - "--context=$(params.CONTEXT)"
        - "--destination=$(params.IMAGE)"
```

> Kaniko este ideal pentru medii Kubernetes fără acces root.

---

## 🧰 4. Integrarea Task-ului într-un Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: image-build-pipeline
spec:
  workspaces:
    - name: shared-data
  params:
    - name: IMAGE
  tasks:
    - name: git-clone
      taskRef:
        name: git-clone
      workspaces:
        - name: output
          workspace: shared-data
      params:
        - name: url
          value: "https://github.com/example/app.git"
    - name: build-image
      runAfter: [git-clone]
      taskRef:
        name: build-with-kaniko
      params:
        - name: IMAGE
          value: "$(params.IMAGE)"
      workspaces:
        - name: source
          workspace: shared-data
```

> Acest pipeline clonează repository-ul și apoi construiește imaginea automat.

---

## ⚙️ 5. PipelineRun pentru declanșarea procesului

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: image-build-run
spec:
  pipelineRef:
    name: image-build-pipeline
  params:
    - name: IMAGE
      value: "docker.io/example/app:latest"
  workspaces:
    - name: shared-data
      persistentVolumeClaim:
        claimName: buildah-workspace
```

> Poți lansa pipeline-ul cu `kubectl apply -f image-build-run.yaml`.

---

## 🧠 6. Adăugarea autentificării la registry

Pentru a putea publica imaginea într-un registry privat, creează un secret Docker:

```bash
kubectl create secret docker-registry regcred   --docker-server=docker.io   --docker-username=<username>   --docker-password=<password>   --docker-email=<email>
```

Apoi atașează secretul la ServiceAccount-ul Tekton:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-sa
secrets:
  - name: regcred
```

> Task-urile Buildah și Kaniko pot folosi acest cont pentru push automat.

---

## 🧩 7. Exemple de fișiere Dockerfile

### 🔹 Python Flask App

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 🔹 Node.js App

```dockerfile
FROM node:18-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
```

> Dockerfile-ul trebuie să fie în directorul de context specificat în pipeline.

---

## ⚙️ 8. Best Practices pentru construire imagini

| Recomandare | Descriere |
|--------------|------------|
| **Folosește imagini de bază mici** | Ex: `alpine`, `slim` pentru a reduce dimensiunea. |
| **Cache inteligent** | Optimizează ordinele în Dockerfile. |
| **Scanează imaginile pentru vulnerabilități** | Integrează `trivy` sau `grype`. |
| **Tag-uri semantice** | Folosește versiuni (`1.0.0`, `latest`) pentru claritate. |
| **Elimină fișierele temporare** | Curăță mediul pentru imagini mai curate. |

---

## 🧭 9. Beneficii ale construirii imaginilor cu Tekton

✅ Automatizare completă a build-urilor container.  
✅ Elimină dependența de Docker daemon.  
✅ Integrare perfectă cu CI/CD și GitOps.  
✅ Crește securitatea prin execuții izolate.  
✅ Reutilizare prin Tekton Catalog.  

---

## 🚀 Concluzie

> Tekton oferă o soluție puternică, sigură și declarativă pentru construirea imaginilor container.  
> Cu task-uri predefinite din Tekton Hub și pipeline-uri automatizate, echipele pot livra aplicații containerizate rapid și eficient.

---