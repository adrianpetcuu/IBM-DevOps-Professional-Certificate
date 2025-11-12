# 📦 Utilizarea Tekton Catalog

## 🔹 Introducere

**Tekton Catalog** este o colecție publică de **Task-uri, Pipeline-uri și alte resurse Tekton** reutilizabile.  
Scopul său este de a accelera dezvoltarea fluxurilor CI/CD prin furnizarea de componente deja testate și gata de utilizare.

> Tekton Catalog permite echipelor DevOps să își construiască pipeline-uri complexe fără a rescrie sarcini de bază precum build, test, deploy sau scanări de securitate.

---

## ⚙️ 1. Ce este Tekton Hub?

**Tekton Hub** este interfața web și API-ul asociat catalogului Tekton.  
Aici poți căuta, descărca și reutiliza resurse create de comunitate.

🌐 **Link oficial:** [https://hub.tekton.dev](https://hub.tekton.dev)

---

## 🧰 2. Tipuri de resurse disponibile

| Tip resursă | Descriere |
|--------------|------------|
| **Tasks** | Unități individuale de lucru, cum ar fi: build, test, deploy, linting etc. |
| **Pipelines** | Secvențe de task-uri preconfigurate pentru diverse tehnologii. |
| **TriggerBindings & Templates** | Resurse pentru automatizarea declanșării pipeline-urilor. |
| **Workspaces** | Configurații pentru partajarea datelor între task-uri. |

---

## ⚙️ 3. Căutarea unei Task în Tekton Hub

Poți căuta task-uri direct în browser sau folosind CLI-ul Tekton (`tkn hub`).

### 🔍 Exemplu de căutare

```bash
tkn hub search build
```

Rezultatul va afișa o listă de task-uri disponibile, precum:

```
NAME          KIND   CATALOG   DESCRIPTION
buildah       Task   Tekton    Build an image using Buildah
kaniko        Task   Tekton    Build a container image with Kaniko
maven         Task   Tekton    Build Java projects using Maven
```

> Fiecare task din catalog este testată și compatibilă cu versiuni specifice ale Tekton.

---

## 🧩 4. Instalarea unei Task din Tekton Hub

Poți instala o task direct în clusterul Kubernetes folosind CLI-ul Tekton:

```bash
tkn hub install task buildah
```

sau o versiune specifică:

```bash
tkn hub install task buildah --version 0.3
```

Aceasta va descărca și aplica fișierul YAML corespunzător în spațiul de lucru (`namespace`) curent.

Verifică instalarea:

```bash
kubectl get tasks
```

---

## ⚙️ 5. Exemple populare de Task-uri din Catalog

| Task | Descriere | Utilizare |
|------|------------|-----------|
| **git-clone** | Clonează un repository Git. | Pas inițial în pipeline. |
| **buildah** | Construiește imagini container fără privilegiu root. | Înlocuitor pentru Docker build. |
| **kaniko** | Creează imagini Docker în containere. | CI/CD fără acces la daemon Docker. |
| **maven** | Compilează și testează proiecte Java. | Folosit în proiecte Spring, Quarkus. |
| **npm** | Rulează comenzi npm (install, test, build). | Proiecte Node.js. |
| **trivy-scanner** | Scanează imagini container pentru vulnerabilități. | Integrare securitate DevSecOps. |

---

## 🧠 6. Exemplu: Folosirea unei Task „git-clone” și „buildah”

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: build-pipeline
spec:
  workspaces:
    - name: shared-data
  tasks:
    - name: clone-repo
      taskRef:
        name: git-clone
      workspaces:
        - name: output
          workspace: shared-data
      params:
        - name: url
          value: "https://github.com/example/repo.git"
    - name: build-image
      taskRef:
        name: buildah
      runAfter: [clone-repo]
      workspaces:
        - name: source
          workspace: shared-data
      params:
        - name: IMAGE
          value: "docker.io/example/app:latest"
```

> Cu doar câteva linii YAML, poți combina task-uri predefinite într-un pipeline complet funcțional.

---

## ⚙️ 7. Actualizarea și întreținerea task-urilor din catalog

Pentru a actualiza o task instalată:

```bash
tkn hub upgrade task buildah
```

Poți lista versiunile disponibile:

```bash
tkn hub info task buildah
```

> Recomandare: folosește versiuni specifice pentru a evita incompatibilitățile.

---

## 🔧 8. Integrarea Tekton Catalog în GitOps

Tekton Catalog poate fi integrat într-un flux **GitOps**, unde toate task-urile și pipeline-urile sunt stocate într-un repository Git.  
Astfel, actualizările pot fi gestionate prin **pull requests** și versiuni controlate.

### Exemplu structură GitOps:

```
tekton-resources/
├── tasks/
│   ├── git-clone.yaml
│   ├── buildah.yaml
├── pipelines/
│   ├── build-pipeline.yaml
└── triggers/
    ├── eventlistener.yaml
```

> Integrarea cu GitOps asigură trasabilitate completă și rollback facil.

---

## ⚙️ 9. Vizualizarea task-urilor în Tekton Dashboard

Dacă ai Tekton Dashboard instalat, poți vizualiza task-urile și pipeline-urile din catalog într-o interfață grafică:

```bash
kubectl get svc tekton-dashboard -n tekton-pipelines
```

Deschide adresa afișată în browser și mergi la secțiunea **Catalog**.

---

## 🧭 10. Beneficii ale utilizării Tekton Catalog

✅ Reutilizare de componente verificate și testate.  
✅ Reducerea timpului de dezvoltare a pipeline-urilor.  
✅ Promovarea standardizării în echipele DevOps.  
✅ Compatibilitate cross-cloud (AWS, Azure, GCP, OpenShift).  
✅ Integrare ușoară cu GitOps și CI/CD existente.

---

## 🚀 Concluzie

> **Tekton Catalog** oferă o bibliotecă completă de resurse CI/CD reutilizabile.  
> Prin folosirea task-urilor predefinite, echipele DevOps pot construi pipeline-uri complexe, standardizate și portabile în doar câteva minute.

---
