# 🚀 Implementarea aplicațiilor în Kubernetes cu Tekton

## 🔹 Introducere

După construirea și testarea imaginii aplicației, următorul pas natural este **implementarea acesteia într-un cluster Kubernetes**.  
Tekton oferă task-uri dedicate pentru **deployment automat**, permițând integrarea completă a CI/CD — de la cod la producție.

> Scopul este de a automatiza implementările în Kubernetes într-un mod sigur, controlat și repetabil.

---

## ⚙️ 1. Ce este Deployment-ul în Tekton?

În Tekton, deployment-ul este o **task** care folosește `kubectl` sau `kustomize` pentru a aplica fișierele manifest (`.yaml`) în cluster.  
Aceasta poate fi inclusă în pipeline imediat după etapa de build.

---

## 🧩 2. Exemplu simplu de Task pentru deploy

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: deploy-to-k8s
spec:
  params:
    - name: manifest-dir
      type: string
      description: Directorul cu fișierele Kubernetes YAML
  steps:
    - name: kubectl-apply
      image: bitnami/kubectl:latest
      script: |
        kubectl apply -f $(params.manifest-dir)
```

> Această task aplică toate fișierele `.yaml` dintr-un director specificat (ex: `k8s/` sau `manifests/`).

---

## ⚙️ 3. Integrarea în pipeline-ul CI/CD

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: deploy-pipeline
spec:
  params:
    - name: IMAGE
    - name: MANIFEST_DIR
  tasks:
    - name: build
      taskRef:
        name: build-with-kaniko
      params:
        - name: IMAGE
          value: "$(params.IMAGE)"
    - name: deploy
      runAfter: [build]
      taskRef:
        name: deploy-to-k8s
      params:
        - name: manifest-dir
          value: "$(params.MANIFEST_DIR)"
```

> Pipeline-ul construiește imaginea, apoi aplică manifestele Kubernetes.

---

## ⚙️ 4. Definirea PipelineRun-ului

```yaml
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: deploy-pipeline-run
spec:
  pipelineRef:
    name: deploy-pipeline
  params:
    - name: IMAGE
      value: "docker.io/example/app:latest"
    - name: MANIFEST_DIR
      value: "k8s/"
  serviceAccountName: tekton-deployer
```

> Rulează pipeline-ul folosind:  
> ```bash
> kubectl apply -f deploy-pipeline-run.yaml
> ```

---

## 🧠 5. Crearea unui ServiceAccount pentru deploy

Pentru a permite Tekton să aplice manifestele, creează un ServiceAccount cu roluri adecvate.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tekton-deployer
secrets:
  - name: regcred
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: tekton-deploy-role
rules:
  - apiGroups: ["", "apps"]
    resources: ["deployments", "services", "pods"]
    verbs: ["get", "list", "create", "update", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: tekton-deploy-binding
subjects:
  - kind: ServiceAccount
    name: tekton-deployer
roleRef:
  kind: Role
  name: tekton-deploy-role
  apiGroup: rbac.authorization.k8s.io
```

> Asigură-te că ServiceAccount-ul este folosit în `PipelineRun`.

---

## ⚙️ 6. Exemplu de fișiere Kubernetes pentru deploy

### 🔹 deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: example-app
  template:
    metadata:
      labels:
        app: example-app
    spec:
      containers:
        - name: example-app
          image: docker.io/example/app:latest
          ports:
            - containerPort: 5000
```

### 🔹 service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

---

## 🧰 7. Automatizarea update-urilor imaginii

Pentru actualizarea automată a imaginii în `deployment.yaml`, poți folosi o task Tekton care înlocuiește tag-ul:

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: update-image-tag
spec:
  params:
    - name: IMAGE
    - name: MANIFEST
  steps:
    - name: update-tag
      image: alpine
      script: |
        sed -i "s|image:.*|image: $(params.IMAGE)|" $(params.MANIFEST)
```

> Aceasta permite actualizarea automată a fișierelor YAML cu imaginea cea mai recentă.

---

## 🧠 8. Monitorizarea deployment-ului

Poți verifica statusul deployment-ului folosind:

```bash
kubectl get pods
kubectl rollout status deployment/example-app
```

sau prin CLI Tekton:

```bash
tkn pipelinerun logs deploy-pipeline-run -f
```

---

## ⚙️ 9. Best Practices pentru Deploy Tekton

| Practică | Descriere |
|-----------|------------|
| **Separă environment-urile** | Folosește namespace-uri diferite (dev, staging, prod). |
| **Automatizează rollback-ul** | Rulează `kubectl rollout undo` dacă build-ul eșuează. |
| **Folosește Secrets și ConfigMaps** | Nu salva date sensibile în YAML-uri. |
| **Monitorizează resursele** | Integrează Prometheus/Grafana pentru vizibilitate. |
| **Adaugă validare** | Rulează `kubectl diff` sau `kubeval` înainte de `apply`. |

---

## 🧭 10. Beneficii

✅ Automatizare completă a livrării aplicațiilor în Kubernetes.  
✅ Control granular asupra deployment-ului.  
✅ Ușor de integrat cu GitOps (ex: ArgoCD).  
✅ Suport pentru multiple environment-uri.  
✅ Siguranță prin roluri RBAC dedicate.

---

## 🚀 Concluzie

> Cu Tekton, procesul de livrare către Kubernetes devine complet automatizat și sigur.  
> De la build până la deployment, Tekton oferă flexibilitate, scalabilitate și control total asupra fluxului DevOps.

---
