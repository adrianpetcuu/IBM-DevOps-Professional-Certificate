# GitOps cu Argo CD

Argo CD este un instrument declarativ de Continuous Delivery bazat pe GitOps, conceput special pentru Kubernetes.  
Acesta sincronizează automat starea aplicațiilor dintr-un repository Git cu starea din clusterul Kubernetes, asigurând consistență și control total asupra deployment-urilor.

---

## 1. Ce este Argo CD?

Argo CD este o platformă GitOps care folosește principiile:
- declarației (infrastructure-as-code),
- controlului versiunilor,
- automatizării deployment-urilor.

Funcționează urmărind repository-ul Git și aplicând automat schimbările în cluster.

### Caracteristici principale:
- Sincronizare Git → Kubernetes
- Suport pentru helm, kustomize, yaml plain, jsonnet
- Interfață Web UI modernă
- CLI și API puternice
- Observabilitate completă
- Suport multi-cluster
- Deploy automat sau manual

---

## 2. Argo CD și GitOps

Argo CD implementează complet fluxul GitOps:
- Git → sursa unică de adevăr
- Argo CD → reconciliere continuă
- Kubernetes → mediul de execuție

Orice schimbare în Git este preluată și aplicată automat în cluster, iar drift-ul este corectat.

---

## 3. Arhitectura Argo CD

Componente principale:

### **UI**
- Vizualizare grafică a aplicațiilor  
- Status, istoricul sync, health  

### **API Server**
- Comunicare cu UI și CLI  
- Validări și RBAC  

### **Repo Server**
- Interfață cu repository-urile Git  
- Procesează manifestele  

### **Application Controller**
- Se ocupă de reconciliere  
- Compară starea dorită vs actuală  
- Execută sync dacă este nevoie  

---

## 4. Conceptul de Aplicatie în Argo CD

O resursă `Application` definește:
- repo Git
- branch / path
- cluster țintă
- namespace
- politica de sincronizare

### Exemplu simplu:
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: demo-app
spec:
  destination:
    namespace: demo
    server: https://kubernetes.default.svc
  project: default
  source:
    repoURL: https://github.com/example/demo-app.git
    path: kubernetes
    targetRevision: main
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

## 5. Politici de sincronizare în Argo CD

### **Sync Manual**
Necesită apăsarea butonului „Sync”.

### **Sync Automat**
Argo CD detectează schimbarea și aplică automat resursele.

Opțiuni:
- `selfHeal`: corectează drift automat
- `prune`: șterge resursele eliminate din Git

---

## 6. Suport pentru multiple surse

Argo CD suportă aplicații definite în:
- YAML Kubernetes
- Helm Charts
- Kustomize
- Jsonnet

---

## 7. Integrarea Argo CD cu GitOps

### Flux GitOps cu Argo CD:

1. Developer face commit în Git
2. Git repo conține manifestele
3. Argo CD detectează schimbarea
4. Reconciliere Git → Cluster
5. Aplicația este actualizată automat

Argo CD vizualizează:
- stări
- diferențe (diff)
- istoricul deploymenturilor

---

## 8. Management multi-cluster

Argo CD poate gestiona mai multe clustere:
- cluster on-prem
- AWS EKS
- GCP GKE
- Azure AKS
- OpenShift

Adăugarea unui cluster este facilă cu:
```bash
argocd cluster add <context>
```

---

## 9. Avantaje ale GitOps cu Argo CD

### **Fiabilitate ridicată**
Rulează reconciliere continuă.

### **Rollback instant**
Făcut prin revert în Git.

### **Audit și trasabilitate complete**
Totul e în Git.

### **Separarea clară între aplicații și infrastructură**

### **UI avansat pentru debugging**
Vizualizare live a stării aplicațiilor.

### **Securitate**
RBAC + SSO + token-uri + control granular.

---

## 10. Argo CD pe OpenShift

OpenShift include Argo CD prin:
- **Operatorul OpenShift GitOps**
- UI integrată
- Argo CD instance management
- Proiecte GitOps separate

Beneficii:
- instalare rapidă
- securitate enterprise
- suport oficial Red Hat

---

## 11. Exemplu workflow complet

1. Dezvoltatorul modifică `deployment.yaml`
2. Commit & push în Git
3. Argo CD vede diferența
4. Aplică automat manifestele
5. Clusterul reflectă starea din Git
6. UI afișează aplicația sincronizată

---

## 12. Concluzie

GitOps cu Argo CD oferă:
- automatizare completă a deployment-urilor,
- scalabilitate multi-cluster,
- observabilitate puternică,
- siguranță și auditabilitate,
- experiență DevOps modernizată.

Argo CD este componenta centrală în majoritatea implementărilor GitOps din ecosistemul Kubernetes și OpenShift.
