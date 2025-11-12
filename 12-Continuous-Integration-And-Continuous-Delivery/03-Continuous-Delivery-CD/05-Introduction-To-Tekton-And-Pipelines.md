# 🚀 Introducere în Tekton și Pipeline-uri

## 🔹 Ce este Tekton?

**Tekton** este un framework open-source dezvoltat inițial de Google și acum parte din **Continuous Delivery Foundation (CDF)**.  
Este utilizat pentru a construi **pipeline-uri CI/CD** portabile, scalabile și declarative care rulează pe **Kubernetes**.

> Tekton permite echipelor DevOps să automatizeze întreg procesul de build, testare și livrare, folosind resurse native Kubernetes.

---

## ⚙️ 1. Caracteristici cheie ale Tekton

| Caracteristică | Descriere |
|-----------------|------------|
| **Kubernetes-native** | Rulează direct pe Kubernetes folosind CRD-uri (Custom Resource Definitions). |
| **Declarativ** | Pipeline-urile sunt definite prin fișiere YAML, similare cu manifestele Kubernetes. |
| **Portabilitate** | Poate fi utilizat cu diverse instrumente CI/CD (Jenkins X, OpenShift Pipelines). |
| **Modularitate** | Fiecare pas din pipeline este o componentă reutilizabilă (Task). |
| **Scalabilitate** | Rulează în containere independente și se scalează automat. |

---

## 🧩 2. Arhitectura Tekton

Tekton definește mai multe tipuri de **resurse Kubernetes personalizate (CRD-uri)** care lucrează împreună:

| Componentă | Descriere |
|-------------|------------|
| **Task** | O unitate de lucru – de exemplu, build, test sau deploy. |
| **Step** | Un pas dintr-o sarcină; fiecare step rulează într-un container separat. |
| **Pipeline** | O serie ordonată de taskuri. |
| **PipelineRun** | O execuție a unui pipeline. |
| **TaskRun** | O execuție individuală a unei taskuri. |
| **Workspace** | Spațiu partajat între taskuri (de ex. codul sursă). |
| **Resource** | Input/output extern, cum ar fi un repository Git sau o imagine Docker. |

---

## 🧠 3. Cum funcționează un Pipeline Tekton

1. Definiți o **Task** (ce trebuie făcut).  
2. Combinați mai multe taskuri într-un **Pipeline**.  
3. Lansați execuția printr-un **PipelineRun**.  

### 🔧 Exemplu simplu de Task

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-app
spec:
  steps:
    - name: build
      image: golang:1.19
      script: |
        go build -o app .
```

### 🔧 Exemplu de Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: app-pipeline
spec:
  tasks:
    - name: build
      taskRef:
        name: build-app
    - name: test
      taskRef:
        name: test-app
```

### 🔧 Exemplu de PipelineRun

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: app-pipeline-run
spec:
  pipelineRef:
    name: app-pipeline
```

> Fiecare PipelineRun rulează într-un pod separat în Kubernetes.

---

## 🧰 4. Integrarea Tekton cu alte instrumente

Tekton se integrează perfect cu alte soluții DevOps și CI/CD:

| Instrument | Scop |
|-------------|------|
| **GitHub Actions** | Lansarea automată a pipeline-urilor Tekton la push sau PR. |
| **Jenkins X** | Folosește Tekton ca motor CI/CD. |
| **ArgoCD** | Pentru deployment continuu bazat pe GitOps. |
| **OpenShift Pipelines** | Implementare enterprise a Tekton de la Red Hat. |

---

## 📦 5. Avantajele folosirii Tekton

✅ **Portabilitate completă** — rulează pe orice cluster Kubernetes.  
✅ **Configurare declarativă** — ușor de gestionat în Git (GitOps).  
✅ **Reutilizare** — taskuri și pipeline-uri pot fi partajate între proiecte.  
✅ **Scalabilitate automată** — fiecare task rulează în propriul container.  
✅ **Comunitate activă** — parte din CNCF și CDF.

---

## ⚙️ 6. Tekton Hub

**Tekton Hub** este o bibliotecă publică unde poți găsi **Task-uri și Pipeline-uri predefinite**.  
Este similar cu un registru de componente reutilizabile.

🌐 [https://hub.tekton.dev](https://hub.tekton.dev)

Exemplu de task predefinită pentru build Docker:
```yaml
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: build-docker
spec:
  taskRef:
    name: buildah
  params:
    - name: IMAGE
      value: my-app:latest
```

---

## 🧩 7. Tekton vs Alte Instrumente CI/CD

| Caracteristică | Tekton | Jenkins | GitHub Actions | ArgoCD |
|-----------------|--------|----------|----------------|--------|
| Kubernetes-native | ✅ | ❌ | ❌ | ✅ |
| Configurare declarativă | ✅ YAML | ✅ Groovy | ✅ YAML | ✅ YAML |
| Deployment continuu | ✅ | ✅ | ✅ | ✅ |
| Extensibilitate | ✅ | ✅ | ✅ | ✅ |
| Portabilitate | ✅ | ❌ | ✅ | ✅ |

> Tekton oferă combinația ideală de **portabilitate**, **automatizare declarativă** și **integrare cloud-native**.

---

## 🧭 8. Pe scurt

| Concept | Descriere |
|----------|------------|
| **Task** | O acțiune individuală (build, test, deploy). |
| **Pipeline** | O serie logică de taskuri. |
| **PipelineRun** | Execuția unui pipeline. |
| **Workspace** | Spațiu partajat între taskuri. |
| **Tekton Hub** | Bibliotecă de componente reutilizabile. |

---

## 🚀 Concluzie

> Tekton reprezintă viitorul livrării continue în ecosistemul Kubernetes.  
> Cu un design modular și complet declarativ, oferă o metodă modernă, scalabilă și portabilă pentru gestionarea pipeline-urilor DevOps.

---
