# ☸️ Kubernetes Objects - README

## 🔹 Ce sunt Kubernetes Objects

În Kubernetes, **obiectele (objects)** sunt componentele fundamentale
care descriu **starea dorită a clusterului**.\
Fiecare obiect reprezintă o **resursă gestionată de Kubernetes**, cum ar
fi o aplicație, un container, o configurație sau o politică de acces.

> Pe scurt: un „object" este o **entitate persistentă în Kubernetes**,
> care definește *ce vrei să ruleze, cum să ruleze și cum să se
> comporte*.

------------------------------------------------------------------------

## 🧩 Exemple de Kubernetes Objects

Kubernetes are mai multe tipuri de obiecte esențiale. Iată cele mai
importante:

  --------------------------------------------------------------------------
  Tip obiect                Descriere            Rol principal
  ------------------------- -------------------- ---------------------------
  **Pod**                   Cea mai mică unitate Rulează aplicațiile.
                            de execuție, conține 
                            unul sau mai multe   
                            containere.          

  **Service**               Expune o aplicație   Permite comunicarea internă
                            rulată într-un set   și externă.
                            de poduri către      
                            rețea.               

  **Deployment**            Gestionează crearea  Asigură disponibilitate și
                            și actualizarea      actualizări fără
                            aplicațiilor.        întreruperi.

  **ReplicaSet**            Menține un număr fix Scalare automată și
                            de poduri active.    reziliență.

  **ConfigMap**             Stochează            Parametrizare aplicații.
                            configurări          
                            non-confidențiale.   

  **Secret**                Stochează date       Securitate și acces
                            sensibile (parole,   controlat.
                            token-uri).          

  **Namespace**             Segmentează          Izolare și organizare.
                            resursele în grupuri 
                            logice.              

  **Ingress**               Gestionează accesul  Expune serviciile la
                            HTTP/HTTPS către     exterior.
                            aplicații.           

  **PersistentVolume /      Oferă stocare        Salvare de date între
  PersistentVolumeClaim**   persistentă pentru   reporniri.
                            date.                
  --------------------------------------------------------------------------

------------------------------------------------------------------------

## ⚙️ Structura generală a unui obiect Kubernetes (YAML)

Orice obiect Kubernetes este definit printr-un fișier YAML cu o
structură standard:

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
    - name: myapp-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

### 🔍 Explicația secțiunilor:

-   **apiVersion:** versiunea API-ului Kubernetes folosită pentru acest
    obiect.\
-   **kind:** tipul obiectului (Pod, Deployment, Service etc.).\
-   **metadata:** informații despre obiect (nume, etichete, adnotări).\
-   **spec:** specificațiile obiectului --- ce ar trebui să ruleze, cum,
    și cu ce setări.

------------------------------------------------------------------------

## 🧱 1️⃣ Pod -- unitatea de bază în Kubernetes

Un **Pod** este cea mai mică unitate pe care o poți crea și gestiona în
Kubernetes.\
El conține unul sau mai multe **containere** care rulează împreună,
partajând aceeași rețea și spațiu de stocare.

Exemplu:

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx-container
    image: nginx:1.25
    ports:
    - containerPort: 80
```

📌 Dacă un Pod cade, Kubernetes îl recreează automat.

------------------------------------------------------------------------

## 🧭 2️⃣ Deployment -- managementul aplicațiilor

Un **Deployment** controlează versiunea aplicației și câte instanțe
(replici) rulează.

Exemplu:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web-container
        image: nginx:1.25
        ports:
        - containerPort: 80
```

Kubernetes se asigură că **exact 3 poduri** rulează permanent, chiar
dacă unul eșuează.

------------------------------------------------------------------------

## 🌐 3️⃣ Service -- comunicarea între poduri și cu exteriorul

Un **Service** este un obiect care expune un grup de poduri ca un singur
serviciu de rețea.

Exemplu:

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

📌 Tipuri de Service: - `ClusterIP` -- acces intern în cluster
(implicit).\
- `NodePort` -- expunere externă pe un port al nodului.\
- `LoadBalancer` -- expunere completă către internet (prin load
balancer).

------------------------------------------------------------------------

## 🧰 4️⃣ ConfigMap & Secret -- configurare și securitate

### ConfigMap

Folosit pentru configurări neconfidențiale:

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: "production"
  APP_PORT: "8080"
```

### Secret

Folosit pentru informații sensibile (ex: parole, token-uri):

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  username: admin
  password: supersecret
```

În poduri, aceste valori pot fi montate ca **variabile de mediu** sau
**fișiere**.

------------------------------------------------------------------------

## 🧭 5️⃣ Namespace -- organizare și izolare

**Namespace**-urile separă resursele dintr-un cluster.\
Astfel, echipele sau aplicațiile pot lucra independent în același
cluster.

Exemplu:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: development
```

Comandă utilă:

``` bash
kubectl get namespaces
```

------------------------------------------------------------------------

## 💾 6️⃣ Persistent Volumes (PV) & Persistent Volume Claims (PVC)

Aceste obiecte gestionează stocarea datelor persistente în Kubernetes.

### PersistentVolume (PV)

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-example
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /data
```

### PersistentVolumeClaim (PVC)

``` yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-example
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
```

PVC „cere" spațiu din PV, iar aplicația poate salva datele în mod
persistent.

------------------------------------------------------------------------

## ⚙️ 7️⃣ Ingress -- acces HTTP/HTTPS

Un **Ingress** permite accesul extern către aplicațiile web din
cluster.\
Poate direcționa cereri către servicii diferite în funcție de rută.

Exemplu:

``` yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

------------------------------------------------------------------------

## 🔁 Relațiile dintre obiecte

    Deployment → creează → ReplicaSet → creează → Pods
    Service → expune → Pods
    Ingress → direcționează → trafic către Service
    ConfigMap/Secret → injectează → configurări în Pods
    PVC → montează → volum pentru stocare

------------------------------------------------------------------------

## 🧠 Concept cheie: *Declarative Management*

Tu nu gestionezi manual fiecare componentă.\
Tu **descrii starea dorită** (în fișiere YAML), iar Kubernetes se ocupă
automat de crearea, menținerea și restaurarea acelei stări.

------------------------------------------------------------------------

## ✅ Concluzie

Kubernetes Objects sunt **piatra de temelie** a platformei.\
Ele definesc aplicațiile, conexiunile și resursele lor, permițând
Kubernetes să: - ruleze aplicațiile în mod automat, - le scaleze
dinamic, - le repare la nevoie, - și să ofere un mediu complet de
orchestrare.

> Kubernetes Objects = limbajul prin care spui clusterului *ce vrei să
> se întâmple*.
