# CI/CD cu OpenShift Pipelines (Tekton)

OpenShift Pipelines este implementarea Red Hat a proiectului Tekton, oferind o soluție **Kubernetes-native** pentru construirea și automatizarea proceselor CI/CD.  
Acesta permite orchestrationarea pipeline-urilor direct în clusterul Kubernetes, folosind resurse declarative YAML.

---

## 1. Ce este CI/CD?

### **CI – Continuous Integration (Integrare Continuă)**
Este procesul prin care codul este integrat frecvent în repository și testat automat prin:
- build-uri automate,
- testare,
- validare.

### **CD – Continuous Delivery / Continuous Deployment**
Este procesul care permite livrarea automată a aplicațiilor în diferite medii:
- Dev
- QA
- Staging
- Production

---

## 2. Ce este OpenShift Pipelines?

OpenShift Pipelines se bazează pe **Tekton**, un framework open-source pentru CI/CD pe Kubernetes.

### Beneficii principale:
- 100% Kubernetes-native
- Declarativ (YAML)
- Scalabil
- Izolare prin TaskRun/PipelineRun
- Integrat cu OpenShift Web Console
- Suport pentru GitOps și Argo CD

---

## 3. Componentele principale ale Tekton / OpenShift Pipelines

### **Task**
O unitate individuală care execută un set de pași (steps).

### **Pipeline**
Combină mai multe Task-uri într-o secvență CI/CD.

### **TaskRun**
O execuție a unei definiții Task.

### **PipelineRun**
O execuție a unui Pipeline.

### **Workspace**
Spațiu partajat între Task-uri (de ex., pentru cod sursă).

### **Pipeline Resources** *(deprecated)*  
Folosit în versiunile vechi pentru definirea input/output.

---

## 4. Exemple de scenarii CI/CD în OpenShift

### **a) Build + Test + Deploy**
1. Task pentru clonarea repository-ului Git  
2. Task pentru build (ex: build Docker)  
3. Task pentru testare unitară  
4. Task pentru deploy în OpenShift  

### **b) Build imagini container**
Folosește:
- Buildah
- Kaniko
- S2I (Source-to-Image)

### **c) Automatizare GitOps**
Pipeline → Push în Git → Argo CD → Deploy automat

---

## 5. Exemplu simplificat de Pipeline Tekton

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: sample-pipeline
spec:
  tasks:
    - name: clone-repo
      taskRef:
        name: git-clone
    - name: run-tests
      taskRef:
        name: test-app
      runAfter:
        - clone-repo
```

---

## 6. Triggers (Tekton Triggers)

Permit pornirea automată a Pipeline-urilor în funcție de evenimente (webhook-uri).

### Componente:
- **EventListener**
- **TriggerBinding**
- **TriggerTemplate**

### Exemplu:
GitHub trimite webhook → EventListener → PipelineRun

---

## 7. Integrarea cu OpenShift

OpenShift adaugă funcționalități suplimentare:
- vizualizare grafică a pipeline-urilor în web console  
- loguri structurate  
- integrare cu imagestreams  
- securitate RBAC avansată  

---

## 8. Integrarea CI/CD cu GitOps (Argo CD)

Fluxul devine:

1. Pipeline creează o nouă imagine
2. Actualizează manifest-ele în Git
3. Argo CD detectează commit-ul
4. Sincronizează clusterul automat

---

## 9. Avantaje ale CI/CD cu OpenShift Pipelines

- Fără nevoie de server dedicat (Jenkins)  
- Pipeline-uri rulate nativ ca pod-uri Kubernetes  
- Scalabilitate orizontală  
- Declarativ și reproductibil  
- Flexibilitate mare în definirea etapelor  
- Compatibil cu GitHub, GitLab, Bitbucket  

---

## 10. Concluzie

CI/CD cu OpenShift Pipelines permite:
- construirea rapidă și sigură a aplicațiilor  
- testare automată  
- livrare continuă  
- integrare cu ecosistemul GitOps și Argo CD  

Este o soluție modernă și complet integrată în Kubernetes, ideală pentru organizațiile enterprise.

