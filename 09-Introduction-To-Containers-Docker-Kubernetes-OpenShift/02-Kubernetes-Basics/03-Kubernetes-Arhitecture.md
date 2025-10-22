# ☸️ Kubernetes Architecture - README

## 🔹 Ce este Arhitectura Kubernetes

Arhitectura Kubernetes este bazată pe un model **client--server**, în
care **Control Plane-ul (master-ul)** gestionează starea generală a
clusterului, iar **Worker Nodes** rulează efectiv aplicațiile
containerizate.

Scopul acestei arhitecturi este să ofere un sistem **scalabil,
automatizat și rezilient**, capabil să ruleze aplicații distribuite în
mod eficient.

------------------------------------------------------------------------

## 🧱 Componentele majore ale unui cluster Kubernetes

Un cluster Kubernetes este alcătuit din două straturi principale:

  -----------------------------------------------------------------------
  Strat                                    Rol
  ---------------------------------------- ------------------------------
  **Control Plane (Master)**               Se ocupă de controlul și
                                           deciziile de management ale
                                           clusterului.

  **Worker Nodes**                         Rulează containerele
                                           aplicațiilor (Pods).
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧩 Componentele Control Plane-ului

### 1️⃣ **API Server**

-   Este punctul central de comunicare al întregului cluster.
-   Primește comenzi de la utilizatori (prin `kubectl`) și de la alte
    componente.
-   Expune interfața REST (Kubernetes API).

📌 Exemplu: când rulezi `kubectl apply -f app.yaml`, comanda ajunge la
**API Server**, care o validează și o salvează în etcd.

------------------------------------------------------------------------

### 2️⃣ **etcd**

-   Este **baza de date distribuită** unde se salvează **starea
    întregului cluster**.
-   Conține informații precum: ce noduri există, ce poduri rulează, ce
    configurații sunt active.
-   Este extrem de importantă --- pierderea datelor din etcd poate
    însemna pierderea întregii configurații.

------------------------------------------------------------------------

### 3️⃣ **Controller Manager**

-   Are rolul de a **monitoriza constant starea clusterului**.
-   Dacă observă diferențe între **starea dorită** și **starea reală**,
    acționează pentru a le sincroniza.

🔹 Exemple de controllere: - Replication Controller -- asigură că un
anumit număr de poduri rulează. - Node Controller -- monitorizează
starea nodurilor. - Endpoint Controller -- menține informațiile despre
rețele.

------------------------------------------------------------------------

### 4️⃣ **Scheduler**

-   Decide **pe ce nod** va rula fiecare pod.
-   Se bazează pe resursele disponibile (CPU, RAM) și pe constrângeri
    definite de utilizator (affinity, tolerations).
-   Obiectiv: **echilibrarea sarcinii** și utilizarea optimă a
    resurselor.

------------------------------------------------------------------------

## 🧩 Componentele Worker Nodes

### 1️⃣ **Kubelet**

-   Agent care rulează pe fiecare nod.
-   Comunică cu API Server-ul și se asigură că **podurile specificate
    sunt active**.
-   Dacă un container cade, kubelet îl repornește automat.

------------------------------------------------------------------------

### 2️⃣ **Kube-proxy**

-   Gestionează rețeaua și **traficul între poduri și servicii**.
-   Permite accesul aplicațiilor din afara nodului către container.

------------------------------------------------------------------------

### 3️⃣ **Container Runtime**

-   Este software-ul care **rulează efectiv containerele**.
-   Kubernetes este agnostic --- poate folosi:
    -   **Docker**
    -   **containerd**
    -   **CRI-O**
    -   alte runtime-uri compatibile cu CRI (Container Runtime
        Interface)

------------------------------------------------------------------------

## ⚙️ Cum funcționează fluxul Kubernetes

1.  Tu creezi un fișier YAML cu o descriere (Deployment, Service,
    etc.).\
2.  Trimiți fișierul la API Server (`kubectl apply -f file.yaml`).\
3.  API Server validează și salvează configurația în etcd.\
4.  Controller Manager verifică dacă există diferențe între starea
    dorită și cea reală.\
5.  Scheduler decide unde să ruleze noile poduri.\
6.  Kubelet de pe nodul ales pornește containerele.\
7.  Kube-proxy asigură conexiunile în rețea.

------------------------------------------------------------------------

## 🧠 Concept cheie: *Starea dorită vs. starea reală*

Kubernetes funcționează după principiul **desired state**.\
Tu definești *cum vrei să arate aplicația* (câte instanțe, ce imagine,
ce porturi), iar Kubernetes: - monitorizează constant starea reală, - și
o ajustează automat pentru a se potrivi cu cea dorită.

Exemplu: dacă vrei 3 poduri și unul cade → Kubernetes creează automat
altul.

------------------------------------------------------------------------

## 📊 Diagrama Arhitecturii Kubernetes

                   +-----------------------+
                   |     Control Plane      |
                   |------------------------|
                   |  API Server            |
                   |  Scheduler             |
                   |  Controller Manager    |
                   |  etcd (Database)       |
                   +-----------+------------+
                               |
                               |
              ---------------------------------------------
              |                   |                      |
      +---------------+   +---------------+      +---------------+
      |   Node 1      |   |   Node 2      |      |   Node 3      |
      |---------------|   |---------------|      |---------------|
      | Kubelet       |   | Kubelet       |      | Kubelet       |
      | Kube-proxy    |   | Kube-proxy    |      | Kube-proxy    |
      | Containers    |   | Containers    |      | Containers    |
      +---------------+   +---------------+      +---------------+

------------------------------------------------------------------------

## 🚀 Beneficiile arhitecturii Kubernetes

-   **Scalabilitate automată** -- adăugarea dinamică de resurse.\
-   **Rezistență la erori** -- redistribuie automat aplicațiile.\
-   **Separare clară între control și execuție.**\
-   **Portabilitate** -- rulează pe orice infrastructură.\
-   **Disponibilitate ridicată** -- fără puncte unice de eșec.

------------------------------------------------------------------------

## ✅ Concluzie

Arhitectura Kubernetes oferă o infrastructură robustă și automatizată
pentru rularea aplicațiilor containerizate la scară largă.\
Prin separarea controlului (Control Plane) de execuție (Worker Nodes),
sistemul oferă **scalabilitate, fiabilitate și auto-vindecare**.

> Kubernetes = automatizare + orchestrare + reziliență pentru
> aplicațiile moderne.
