# Introducere în GitOps

GitOps este o abordare modernă de operare și gestionare a aplicațiilor și infrastructurii, bazată pe utilizarea Git ca **sursă unică de adevăr** (Single Source of Truth).  
Prin GitOps, toate schimbările aduse resurselor sunt efectuate prin modificări în repository (commit & push), iar un operator GitOps aplică automat schimbările în cluster.

---

## 1. Ce este GitOps?

GitOps este un model operațional care combină:
- **principiile DevOps**,  
- **abordarea declarativă (IaC – Infrastructure as Code)**,  
- **controlul versiunilor oferit de Git**,  
pentru a automatiza implementarea aplicațiilor și a infrastructurii.

### Principiul central:
➡️ *„Dacă nu este în Git, nu există în producție.”*

---

## 2. De ce Git ca sursă unică de adevăr?

Git este ideal pentru GitOps deoarece:
- oferă istoric detaliat al fiecărei schimbări,
- permite auditarea completă,
- suportă colaborare în echipă,
- permite rollback instant prin revert,
- este deja un instrument standard în industrie.

---

## 3. Componentele GitOps

### 3.1. Repository-ul Git
Conține:
- manifestele Kubernetes,
- configurările infrastructurii,
- definițiile aplicațiilor,
- politicile de deployment.

### 3.2. Operator GitOps
Exemple:
- Argo CD  
- Flux CD  
- OpenShift GitOps  

Operatorul:
- monitorizează repository-ul Git,
- detectează schimbările,
- aplică automat manifestele în cluster.

### 3.3. Cluster Kubernetes
Este mediul în care sunt implementate aplicațiile și resursele definite în Git.

---

## 4. Cum funcționează GitOps?

### Fluxul GitOps:

1. Dezvoltatorul modifică un fișier YAML / configurare.
2. Commit & push în Git.
3. Operatorul GitOps detectează schimbarea.
4. Aplică automat update-urile în cluster.
5. Monitorizează dacă starea reală corespunde cu cea din Git.

➡️ Dacă apare o diferență (drift), operatorul GitOps o corectează automat.

---

## 5. Beneficiile GitOps

### **5.1. Securitate și auditabilitate**
- Fiecare schimbare trece prin pull request-uri
- Audit trail complet prin Git

### **5.2. Fiabilitate și consistență**
- Starea clusterului este mereu sincronizată cu Git
- Eliminarea configurațiilor „drifted”

### **5.3. Productivitate crescută**
- Deployment automat
- Eliminarea operațiunilor manuale

### **5.4. Rollback instant**
- Un revert în Git resetează întreaga infrastructură

### **5.5. Scalabilitate**
- Același repo Git poate alimenta mai multe clustere

---

## 6. GitOps vs DevOps

| DevOps | GitOps |
|--------|--------|
| Automatizare CI/CD | Automatizare declarativă |
| Focalizare pe procese | Focalizare pe starea sistemului |
| Tool-uri diverse | Git + operator GitOps |
| Pipelines imperative | Configurații declarative |

---

## 7. GitOps în OpenShift

OpenShift include Argo CD sub numele **OpenShift GitOps**, oferind:

- Sincronizare automată Git → cluster  
- UI vizual pentru starea aplicațiilor  
- Gestionarea mai multor clustere  
- Pipeline GitOps complet integrat  

---

## 8. Exemple de utilizare GitOps

### **Automatizarea deployment-urilor**
Commit → Argo CD → deployment automat

### **Controlul versiunilor pentru infrastructură (IaC)**
Terraform + GitOps = infrastructură complet versionată

### **Gestionarea microserviciilor**
Fiecare microserviciu are propriul repo Git + Argo CD App

---

## 9. Concluzie

GitOps este o practică esențială pentru:
- automatizare completă,
- fiabilitate,
- consistență,
- versionarea infrastructurii și aplicațiilor.

Este fundamentul modern al DevOps în ecosistemele Kubernetes și OpenShift.

