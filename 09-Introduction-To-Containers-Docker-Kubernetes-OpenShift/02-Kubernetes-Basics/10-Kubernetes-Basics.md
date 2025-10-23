# ☸️ Noțiuni de bază Kubernetes (Kubernetes Basics)

## 🔹 Ce este orchestrarea containerelor

**Orchestrarea containerelor** automatizează întreg ciclul de viață al containerelor, rezultând:
- implementări mai rapide,
- reducerea erorilor,
- disponibilitate ridicată,
- și o securitate mai robustă.

---

## 🔹 Ce este Kubernetes

**Kubernetes** este un sistem open-source de orchestrare a containerelor, extrem de portabil și scalabil pe orizontală.  
Acesta oferă **implementare automată** și **management simplificat** al aplicațiilor containerizate.

---

## ⚙️ Arhitectura Kubernetes

Arhitectura Kubernetes este compusă din două părți principale:

### 🔸 Planul de control (*Control Plane*)
Include componentele care coordonează clusterul:
- **API Server** – punctul central de comunicare între utilizatori și cluster;
- **Scheduler** – decide pe ce nod vor rula podurile;
- **Controller Manager** – gestionează procesele de replicare, starea aplicațiilor și monitorizarea nodurilor;
- **etcd** – baza de date distribuită ce stochează starea clusterului.

### 🔸 Planul de lucru (*Worker Plane*)
Include componentele care execută efectiv aplicațiile:
- **Noduri (Nodes)** – mașinile fizice sau virtuale care rulează aplicațiile;
- **Kubelet** – agentul care rulează pe fiecare nod și comunică cu planul de control;
- **Container Runtime** – software-ul care execută containerele (ex: containerd, CRI-O);
- **kube-proxy** – gestionează rutarea traficului de rețea către și între poduri.

---

## 🧩 Obiecte Kubernetes

Kubernetes gestionează aplicațiile și resursele printr-o serie de **obiecte** de bază:

| Obiect | Descriere |
|---------|------------|
| **Namespaces** | Izolează grupuri de resurse în cadrul aceluiași cluster. |
| **Pods** | Reprezintă o instanță sau un proces al aplicației care rulează în cluster. |
| **ReplicaSets** | Creează și gestionează mai multe copii ale podurilor pentru scalare orizontală. |
| **Deployments** | Gestionează actualizările pentru poduri și ReplicaSets. |
| **Services** | Obiecte REST care definesc politici de acces la poduri și în cadrul clusterului. |

---

## 🔸 Servicii (Services) în Kubernetes

**Serviciile** facilitează comunicarea între componentele aplicației și utilizatori.  
Ele oferă un mecanism stabil pentru accesarea podurilor, chiar dacă acestea se modifică dinamic.

### Tipuri de servicii:
- **ClusterIP** – oferă comunicație internă între servicii din cluster.  
- **NodePort** – expune un port pe fiecare nod și redirecționează cererile către serviciul ClusterIP.  
- **LoadBalancer (ELB)** – creează automat servicii de tip NodePort și ClusterIP, oferind acces extern.  
- **ExternalName** – face legătura cu resurse externe sau permite comunicarea între namespace-uri diferite.

---

## 🌐 Ingress

**Ingress** este un obiect API care oferă **reguli de rutare** pentru gestionarea accesului utilizatorilor externi la mai multe servicii dintr-un cluster Kubernetes.  
Permite accesul prin HTTP/HTTPS către aplicațiile interne, oferind:
- rutare bazată pe nume de domeniu,
- terminare SSL/TLS,
- și un punct unic de intrare pentru trafic extern.

---

## 🧱 Alte resurse Kubernetes importante

| Resursă | Rol |
|----------|-----|
| **DaemonSet** | Asigură că cel puțin o copie a unui pod rulează pe fiecare nod din cluster. |
| **StatefulSet** | Gestionează aplicațiile *stateful*, menține identitatea persistentă a fiecărui pod și oferă stocare durabilă. |
| **Job** | Creează poduri temporare care rulează până la finalizarea unei sarcini specifice; Job-urile sunt reluate automat până la completare. |

---

## 🚀 Capabilități Kubernetes

Kubernetes oferă un set extins de funcționalități integrate:

- Implementări și rollback-uri automate  
- Orchestrarea stocării  
- Scalare orizontală automată  
- Alocare inteligentă a resurselor (*bin packing*)  
- Gestionarea secretelor și a configurațiilor  
- Suport IPv4/IPv6 dual-stack  
- Execuție batch (joburi temporare)  
- Auto-vindecare a aplicațiilor (self-healing)  
- Descoperire automată a serviciilor și echilibrare de încărcare  
- Design extensibil prin CRD-uri (Custom Resource Definitions)

---

## 🧾 Concluzie

**Kubernetes** este coloana vertebrală a orchestrării moderne a containerelor.  
Prin combinarea automatizării, scalabilității și rezilienței, el simplifică gestionarea aplicațiilor distribuite și asigură un mediu stabil, sigur și flexibil pentru rularea acestora.

---
