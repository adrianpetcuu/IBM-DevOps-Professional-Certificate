# ☸️ Noțiuni de bază despre Kubernetes (Kubernetes Basics)

## 🧩 Termeni și definiții

| **Termen** | **Definiție** |
|-------------|---------------|
| **Împachetare automată (Automated bin packing)** | Tehnică ce crește utilizarea resurselor și reduce costurile prin combinarea sarcinilor critice cu cele de tip best-effort. |
| **Execuție batch (Batch execution)** | Gestionează sarcini batch și de integrare continuă. Poate înlocui automat containerele eșuate, asigurând funcționarea continuă. |
| **Cloud Controller Manager** | Componentă a planului de control Kubernetes care gestionează logica specifică unui furnizor cloud, integrând Kubernetes cu diverse servicii cloud. |
| **Cluster** | Un set de mașini de lucru (nodes) care rulează și gestionează aplicații containerizate într-un mod coordonat. |
| **Orchestrare de containere (Container Orchestration)** | Procesul de automatizare a ciclului de viață al aplicațiilor containerizate. |
| **Runtime de container (Container Runtime)** | Software-ul care execută și gestionează containerele, asigurând rularea corectă a acestora. |
| **Buclă de control (Control Loop)** | O buclă continuă care menține starea dorită a sistemului prin monitorizare și ajustări automate. |
| **Plan de control (Control Plane)** | Componenta centrală a orchestrării containerelor, oferind API-ul și interfețele pentru definirea, implementarea și gestionarea ciclului de viață al containerelor. |
| **Controller** | Buclă de control din Kubernetes care monitorizează starea clusterului și face modificări dacă este necesar. |
| **Plan de date (Data/Worker Plane)** | Strat care furnizează resursele esențiale (CPU, memorie, rețea, stocare) necesare containerelor pentru a funcționa și comunica. |
| **DaemonSet** | Controller care asigură rularea unui anumit Pod pe toate nodurile dintr-un cluster. Util pentru daemonii de sistem, cum ar fi colectoarele de loguri sau agenții de monitorizare. |
| **Management declarativ (Declarative Management)** | Abordare Kubernetes unde se definește starea dorită a sistemului, iar Kubernetes ajustează continuu pentru a o menține. |
| **Deployment** | Resursă Kubernetes care gestionează actualizările și scalarea Pod-urilor și ReplicaSet-urilor, facilitând rollout-uri și rollback-uri automate. |
| **Extensibilitate (Designed for extensibility)** | Capacitatea Kubernetes de a adăuga funcționalități în cluster fără a modifica codul sursă. |
| **Docker Swarm** | Instrument care automatizează implementarea aplicațiilor containerizate, proiectat să funcționeze cu Docker Engine. |
| **Ecosistem (Ecosystem)** | Gama largă de servicii, suport și instrumente compatibile cu Kubernetes. |
| **etcd** | Magazin cheie-valoare fiabil folosit ca depozit de date consistent pentru sistemele distribuite și stocarea stării clusterului. |
| **Evacuare (Eviction)** | Procesul de terminare și eliminare a unuia sau mai multor Pods dintr-un nod. |
| **Comenzi imperative (Imperative commands)** | Comenzi care creează, actualizează sau șterg direct obiecte în timp real. |
| **Management imperativ (Imperative Management)** | Abordare în care se definesc pașii exacți pentru a atinge o stare dorită. |
| **Ingress** | Componentă Kubernetes care gestionează accesul extern către servicii dintr-un cluster, oferind un punct unic de intrare și rutare către mai multe servicii. |
| **IPv4/IPv6 dual stack** | Funcționalitate care atribuie atât adrese IPv4 cât și IPv6 pentru Pods și Servicii, permițând compatibilitate în medii mixte. |
| **Job** | Sarcină cu început și sfârșit definit, folosită frecvent pentru execuții finite sau batch în Kubernetes. |
| **Kubectl** | Interfața de linie de comandă folosită pentru a interacționa cu planul de control Kubernetes și pentru a gestiona resursele clusterului. |
| **Kubelet** | Agentul principal care rulează pe fiecare nod și gestionează containerele, comunicând cu planul de control. |
| **Kubernetes** | Principala platformă open-source pentru orchestrarea containerelor. |
| **Kubernetes API** | Interfață RESTful care expune funcționalitățile Kubernetes și stochează starea clusterului, permițând automatizări și integrare cu alte sisteme. |
| **Kubernetes API Server** | Componenta care validează și configurează datele pentru obiectele API din Kubernetes. |
| **Kubernetes Controller Manager** | Componentă esențială care rulează procesele de control și menține starea dorită a clusterului. |
| **Kubernetes Cloud Controller Manager** | Componentă Kubernetes care include logica specifică furnizorilor cloud. |
| **Kubernetes Proxy (kube-proxy)** | Serviciu proxy din Kubernetes care gestionează regulile de trafic și comunicația între Pods și Servicii. |
| **kube-scheduler** | Componenta care selectează nodul potrivit pe care să ruleze noile Pods. |
| **Selector de etichete (Label Selector)** | Mecanism de filtrare a resurselor pe baza etichetelor (labels), pentru o administrare mai eficientă. |
| **Etichete (Labels)** | Metadate atașate obiectelor Kubernetes (Pod-uri, Servicii etc.) sub formă de perechi cheie-valoare, utile pentru organizare și grupare. |
| **Echilibrarea sarcinii (Load balancing)** | Distribuirea traficului de rețea între mai multe Pods pentru performanță și disponibilitate optimă. |
| **Marathon** | Framework Apache Mesos pentru scalarea infrastructurii containerizate. |
| **Namespace** | Mecanism Kubernetes care permite izolarea resurselor într-un singur cluster. |
| **Nod (Node)** | Mașină de lucru dintr-un cluster Kubernetes care rulează aplicații containerizate. |
| **Nomad** | Instrument de gestionare a clusterelor și programare a sarcinilor care suportă Docker și alte aplicații. |
| **Obiect (Object)** | Reprezintă o entitate în sistemul Kubernetes. |
| **Persistență (Persistence)** | Proprietatea unui obiect Kubernetes de a exista până când este modificat sau șters explicit. |
| **Preempțiune (Preemption)** | Mecanism care permite unui Pod cu prioritate mare să ocupe resursele unui nod prin eliminarea Pods-urilor cu prioritate mică. |
| **Pod** | Unitatea fundamentală de execuție în Kubernetes, reprezentând unul sau mai multe containere care rulează împreună și partajează resurse. |
| **Proxy** | Server intermediar care facilitează accesul la servicii externe. |
| **ReplicaSet** | Resursă care asigură că un număr specific de Pods identice rulează mereu, oferind redundanță și scalabilitate. |
| **Auto-vindecare (Self-healing)** | Capacitatea Kubernetes de a reporni, înlocui sau reprograma automat containerele care eșuează. |
| **Serviciu (Service)** | Abstracție de rețea care expune un grup de Pods sub o adresă IP stabilă și un punct final comun, oferind echilibrare de sarcină. |
| **Descoperire de servicii (Service Discovery)** | Procesul de identificare și conectare la Pods prin adrese IP sau nume DNS unice. |
| **StatefulSet** | Componentă Kubernetes care gestionează implementarea aplicațiilor de tip stateful (ex: baze de date), asigurând unicitate și ordine în Pods. |
| **Stocare (Storage)** | Mecanismele folosite pentru a oferi stocare persistentă și temporară pentru Pods (Persistent Volumes, StorageClasses, Claims). |
| **Orchestrare a stocării (Storage Orchestration)** | Mecanism care montează automat sistemele de stocare pentru Pods și gestionează resursele de stocare. |
| **Workload** | Orice aplicație care rulează pe Kubernetes. |

---

# 🧱 Înțelegerea arhitecturii Kubernetes (Understanding Kubernetes Architecture)

## 🧰 Comenzi Kubernetes CLI

| **Comandă** | **Descriere** |
|--------------|----------------|
| `for …do` | Rulează o secvență de comenzi de mai multe ori, conform specificației. |
| `kubectl apply` | Aplică o configurație specificată asupra unei resurse. |
| `kubectl config get-clusters` | Afișează toate clusterele definite în fișierul `kubeconfig`. |
| `kubectl config get-contexts` | Afișează contextul curent. |
| `kubectl create` | Creează o nouă resursă Kubernetes pe baza unei specificații. |
| `kubectl delete` | Șterge resurse. |
| `kubectl describe` | Oferă detalii despre o resursă sau grup de resurse. |
| `kubectl expose` | Expune o resursă către internet sub forma unui serviciu Kubernetes. |
| `kubectl get` | Afișează resurse. |
| `kubectl get pods` | Listează toate Pods-urile. |
| `kubectl get pods -o wide` | Listează toate Pods-urile cu detalii suplimentare. |
| `kubectl get deployments` | Afișează toate deployments-urile create. |
| `kubectl get services` | Listează serviciile create. |
| `kubectl proxy` | Creează un server proxy între localhost și API-ul Kubernetes. |
| `kubectl run` | Creează și rulează o imagine într-un Pod. |
| `kubectl version` | Afișează informațiile despre versiunea clientului și serverului Kubernetes. |
