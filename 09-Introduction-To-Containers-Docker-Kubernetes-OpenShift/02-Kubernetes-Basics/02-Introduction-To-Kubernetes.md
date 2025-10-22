# ☸️ Introduction to Kubernetes - README

## 🔹 Ce este Kubernetes

**Kubernetes** (K8s) este o platformă open-source pentru **orchestrarea
containerelor**, adică gestionează automat rularea, scalarea și
actualizarea aplicațiilor containerizate.\
Scopul său este să asigure că aplicațiile rulează mereu în starea
dorită, fără intervenție manuală.

Kubernetes este folosit de companii mari și mici pentru a rula aplicații
distribuite, în cloud sau local (on-premise).

------------------------------------------------------------------------

## 🔸 De ce avem nevoie de Kubernetes

Când o aplicație este alcătuită din zeci sau sute de containere,
administrarea lor manuală devine imposibilă.\
Kubernetes automatizează:

-   Pornirea, oprirea și repornirea containerelor
-   Distribuirea lor pe mai multe servere (load balancing)
-   Scalarea automată în funcție de trafic
-   Reparația containerelor eșuate (self-healing)
-   Actualizările fără întreruperi (rolling updates)

------------------------------------------------------------------------

## ⚙️ Arhitectura Kubernetes

Un cluster Kubernetes este alcătuit din două părți principale:

  -----------------------------------------------------------------------
  Componentă                           Descriere
  ------------------------------------ ----------------------------------
  **Control Plane (Master Node)**      Controlează întregul cluster,
                                       decide unde se rulează aplicațiile
                                       și monitorizează starea lor.

  **Worker Nodes**                     Mașinile (fizice sau virtuale)
                                       care rulează efectiv aplicațiile
                                       containerizate.
  -----------------------------------------------------------------------

Comunicarea dintre ele se face prin **Kubernetes API Server**.

------------------------------------------------------------------------

## 🧩 Componentele principale ale Kubernetes

### 1️⃣ Pod

Cea mai mică unitate din Kubernetes.\
Un **Pod** conține unul sau mai multe **containere** care împart
aceleași resurse (rețea, stocare).

Exemplu: un pod poate conține aplicația web și un container de loguri
auxiliar (sidecar).

------------------------------------------------------------------------

### 2️⃣ Node

Un **Node** este o mașină din cluster (fizică sau virtuală).\
Fiecare node are propriul agent **kubelet**, care comunică cu control
plane-ul și rulează podurile.

------------------------------------------------------------------------

### 3️⃣ Deployment

Un **Deployment** definește **cum** vrei să ruleze aplicația ta.\
Specifica lucruri precum:

-   Câte replici (instanțe) să existe
-   Ce imagine Docker să folosească
-   Cum să se facă actualizările

Kubernetes se ocupă de restul --- menține automat acel număr de replici
activ.

------------------------------------------------------------------------

### 4️⃣ ReplicaSet

Menține un număr constant de poduri active.\
Dacă un pod cade, **ReplicaSet** creează altul automat.

------------------------------------------------------------------------

### 5️⃣ Service

Un **Service** oferă o **adresă IP stabilă** și un **nume DNS** pentru
accesarea podurilor.\
Este util pentru load balancing între mai multe instanțe.

Tipuri de servicii: - **ClusterIP** -- acces intern între aplicații -
**NodePort** -- acces extern printr-un port al nodului -
**LoadBalancer** -- expunerea aplicației către Internet

------------------------------------------------------------------------

### 6️⃣ ConfigMap & Secret

-   **ConfigMap**: păstrează configurări (ex: variabile de mediu).\
-   **Secret**: păstrează date sensibile (ex: parole, chei API).\
    Ambele pot fi injectate în containere.

------------------------------------------------------------------------

### 7️⃣ Ingress

Gestionează traficul HTTP/HTTPS către aplicații.\
Poate direcționa cereri diferite către servicii diferite (ex: `/api` →
backend, `/web` → frontend).

------------------------------------------------------------------------

### 8️⃣ Persistent Volume (PV) & Persistent Volume Claim (PVC)

Oferă **stocare persistentă** pentru aplicații (ex: baze de date).\
- **PV** = spațiul de stocare disponibil în cluster.\
- **PVC** = cererea aplicației pentru acel spațiu.

------------------------------------------------------------------------

## 🔁 Cum funcționează fluxul Kubernetes

1.  Dezvoltatorul scrie un fișier YAML (de exemplu `deployment.yaml`)
    care descrie aplicația.\
2.  Trimite configurația către cluster cu
    `kubectl apply -f deployment.yaml`.\
3.  Control Plane-ul decide pe ce noduri se rulează podurile.\
4.  Worker nodes rulează efectiv containerele.\
5.  Kubernetes monitorizează aplicația și se asigură că totul rămâne în
    starea dorită.

------------------------------------------------------------------------

## 📘 Exemple de comenzi uzuale `kubectl`

  ------------------------------------------------------------------------
  Comandă                           Descriere
  --------------------------------- --------------------------------------
  `kubectl get nodes`               Listează nodurile din cluster

  `kubectl get pods`                Afișează podurile care rulează

  `kubectl get svc`                 Listează serviciile active

  `kubectl apply -f file.yaml`      Creează resursele definite într-un
                                    fișier YAML

  `kubectl delete pod <nume_pod>`   Șterge un pod (va fi recreat automat)

  `kubectl logs <nume_pod>`         Afișează logurile unui pod
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 Avantajele Kubernetes

-   **Automatizare completă** a rulării containerelor\
-   **Scalabilitate dinamică** bazată pe cerințe\
-   **Self-healing** -- repornește containerele defecte automat\
-   **Zero downtime updates** -- actualizări fără întreruperea
    serviciului\
-   **Portabilitate** -- poate rula pe orice platformă (bare-metal,
    cloud, hibrid)\
-   **Monitorizare și control complet** asupra aplicațiilor

------------------------------------------------------------------------

## 🧠 Concept cheie: *Declarative Management*

În Kubernetes, tu nu spui *cum* să ruleze aplicația, ci *ce vrei să
obții*.\
Aceasta se numește **stare dorită (desired state)**.

Kubernetes compară mereu: - **Starea dorită** (ce vrei să ruleze) -
**Starea actuală** (ce rulează efectiv)

➡️ Dacă există diferențe, sistemul face automat modificările necesare
pentru a le sincroniza.

------------------------------------------------------------------------

## ✅ Concluzie

Kubernetes este un instrument puternic care automatizează gestionarea
aplicațiilor containerizate.\
El asigură disponibilitate ridicată, scalabilitate, auto-vindecare și
actualizări fără întreruperi.

> Cu Kubernetes, tu definești ce vrei să se întâmple, iar platforma se
> asigură că așa rămâne --- mereu.
