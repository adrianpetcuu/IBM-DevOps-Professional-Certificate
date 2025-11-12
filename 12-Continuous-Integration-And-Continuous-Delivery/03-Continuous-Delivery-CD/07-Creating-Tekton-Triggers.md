# ⚡ Crearea Tekton Triggers

## 🔹 Introducere

**Tekton Triggers** permite **declanșarea automată** a execuțiilor de pipeline (`PipelineRuns`) atunci când apar evenimente externe, cum ar fi un *push* într-un repository GitHub, un *pull request*, sau un *webhook* dintr-o aplicație externă.

> Triggers automatizează lansarea pipeline-urilor fără intervenție manuală, fiind esențiale pentru implementarea CI/CD complet automatizată.

---

## ⚙️ 1. Componentele principale ale Tekton Triggers

Un sistem de trigger Tekton include mai multe componente care lucrează împreună:

| Componentă | Descriere |
|-------------|------------|
| **EventListener** | Primește cereri HTTP (de ex. webhook-uri). |
| **TriggerBinding** | Mapează datele din eveniment către variabile. |
| **TriggerTemplate** | Definește resursele Tekton care vor fi create (de ex. PipelineRun). |
| **Interceptor** | (Opțional) Procesează sau filtrează evenimentele înainte de a le trimite mai departe. |

---

## 🧩 2. Exemplu simplu de Trigger Tekton

Acest exemplu pornește un pipeline Tekton atunci când are loc un *push* într-un repository GitHub.

### 🔧 TriggerTemplate

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerTemplate
metadata:
  name: pipeline-template
spec:
  params:
    - name: git-repo-url
    - name: git-revision
  resourcetemplates:
    - apiVersion: tekton.dev/v1beta1
      kind: PipelineRun
      metadata:
        generateName: triggered-pipeline-run-
      spec:
        pipelineRef:
          name: sample-pipeline
        params:
          - name: repo-url
            value: $(params.git-repo-url)
          - name: revision
            value: $(params.git-revision)
```

### 🔧 TriggerBinding

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerBinding
metadata:
  name: git-trigger-binding
spec:
  params:
    - name: git-repo-url
      value: $(body.repository.url)
    - name: git-revision
      value: $(body.head_commit.id)
```

### 🔧 EventListener

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-listener
spec:
  serviceAccountName: tekton-triggers-sa
  triggers:
    - name: github-trigger
      bindings:
        - ref: git-trigger-binding
      template:
        ref: pipeline-template
```

---

## ⚙️ 3. Crearea unui Service Account pentru Tekton

Pentru a permite EventListener-ului să creeze resurse Tekton, este necesar un cont de serviciu (ServiceAccount).

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tekton-triggers-sa
secrets:
  - name: tekton-triggers-secret
```

> Asigură-te că acest ServiceAccount are permisiuni RBAC suficiente pentru a crea `PipelineRun`.

---

## ⚙️ 4. Configurarea Webhook-ului GitHub

După ce ai creat resursele Tekton, trebuie configurat webhook-ul GitHub pentru a trimite evenimentele către Tekton:

1. Mergi în **Settings → Webhooks** din repository.  
2. Adaugă o nouă adresă URL (exemplu):  
   ```
   http://<EXTERNAL-IP>:8080
   ```
3. Selectează evenimentele dorite (ex: **Push events**).  
4. Salvează webhook-ul.

> Poți afla IP-ul EventListener-ului Tekton rulând:  
```bash
kubectl get svc
```

---

## 🧰 5. Verificarea funcționării

După configurare, testează sistemul făcând un **commit & push** în repository.  
Ar trebui să vezi că un nou **PipelineRun** este generat automat.

Verifică execuțiile folosind CLI-ul Tekton:

```bash
tkn pipelinerun list
tkn pipelinerun logs <nume-pipeline-run> -f
```

---

## 🧠 6. Adăugarea Interceptorilor

Interceptors sunt folosiți pentru a filtra sau modifica evenimentele înainte de procesare.

Exemplu: filtrarea doar pentru evenimente de tip *push*.

```yaml
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: filtered-listener
spec:
  triggers:
    - name: github-push-only
      interceptors:
        - ref:
            name: "github"
          params:
            - name: "eventTypes"
              value: ["push"]
      bindings:
        - ref: git-trigger-binding
      template:
        ref: pipeline-template
```

> Poți folosi interceptori pentru GitHub, CEL (Common Expression Language) sau propriile reguli personalizate.

---

## 🧩 7. Vizualizarea execuțiilor

Dacă ai instalat **Tekton Dashboard**, poți urmări pipeline-urile și trigger-ele vizual:

```bash
kubectl get routes -n tekton-pipelines
```

Apoi accesează adresa din browser.  
Dashboard-ul oferă o interfață grafică completă pentru monitorizarea execuțiilor.

---

## ⚙️ 8. Best Practices

| Practică | Descriere |
|-----------|------------|
| **Separă fișierele YAML** | Creează fișiere distincte pentru Template, Binding și Listener. |
| **Folosește nume unice** | Evită coliziunea între pipeline-uri. |
| **Adaugă autentificare la EventListener** | Protejează endpointurile publice. |
| **Testează webhook-ul GitHub** | Folosește tab-ul „Recent Deliveries” pentru debugging. |

---

## 🧭 Concluzie

> Tekton Triggers transformă pipeline-urile Tekton din procese manuale în fluxuri complet automate.  
> Cu ele, echipele DevOps pot implementa cu ușurință fluxuri CI/CD reactive, scalabile și cloud-native.

---
