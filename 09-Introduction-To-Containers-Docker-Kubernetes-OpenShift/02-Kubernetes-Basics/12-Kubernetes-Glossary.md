# 📘 Glossar: Noțiuni de bază Kubernetes

Acest glosar oferă explicații pentru termenii esențiali din ecosistemul **Kubernetes**, pentru a ajuta la înțelegerea arhitecturii, componentelor și principiilor sale de funcționare.

---

| Termen | Definiție |
|--------|------------|
| **Împachetare automată (Automated bin packing)** | Crește utilizarea resurselor și reduce costurile prin combinarea sarcinilor critice cu cele de tip „best-effort”. |
| **Execuție batch (Batch execution)** | Gestionează sarcinile de tip batch și cele de integrare continuă, înlocuind automat containerele eșuate (dacă este configurat). |
| **Cloud Controller Manager** | Componentă din planul de control Kubernetes care conține logica specifică unui furnizor cloud. Permite conectarea clusterului la API-ul furnizorului de cloud și separă componentele care interacționează cu acesta de cele interne clusterului. |
| **Cluster** | Un set de mașini de lucru (noduri) care rulează aplicații containerizate. Fiecare cluster are cel puțin un nod de lucru. |
| **Orchestrarea containerelor (Container Orchestration)** | Procesul care automatizează ciclul de viață al aplicațiilor containerizate. |
| **Runtime de container (Container Runtime)** | Software-ul responsabil cu rularea efectivă a containerelor (ex: containerd, CRI-O). |
| **Buclă de control (Control Loop)** | Un ciclu continuu care reglează starea unui sistem — similar cu modul în care un termostat controlează temperatura. |
| **Plan de control (Control Plane)** | Stratul de orchestrare care expune API-ul și interfețele pentru definirea, implementarea și gestionarea containerelor. |
| **Controller** | Buclă de control care monitorizează starea clusterului și efectuează acțiuni pentru a o aduce în conformitate cu starea dorită. |
| **Plan de lucru (Data/Worker Plane)** | Stratul care oferă resurse precum CPU, memorie, rețea și stocare, astfel încât containerele să poată rula și comunica. |
| **DaemonSet** | Asigură rularea unei copii a unui Pod pe fiecare nod din cluster. |
| **Management declarativ (Declarative Management)** | Definirea unei stări dorite (ex: numărul de replici) — Kubernetes lucrează activ pentru a menține această stare. |
| **Deployment** | Obiect care oferă actualizări pentru Pods și ReplicaSets. Rulează mai multe instanțe ale aplicației și gestionează aplicațiile stateless. |
| **Proiectat pentru extensibilitate (Designed for extensibility)** | Permite adăugarea de funcționalități noi fără modificarea codului sursă existent. |
| **Docker Swarm** | Sistem de orchestrare a containerelor conceput special pentru Docker Engine, popular în echipele care utilizează ecosistemul Docker. |
| **Ecosistem (Ecosystem)** | Totalitatea serviciilor, suportului și instrumentelor din jurul Kubernetes — un ecosistem vast și în creștere rapidă. |
| **etcd** | Bază de date cheie-valoare, distribuită și foarte disponibilă, care stochează toate datele clusterului — sursa de adevăr a stării Kubernetes. |
| **Eviction (Evacuare)** | Procesul de terminare a unuia sau mai multor Poduri pe noduri, de obicei din motive de resurse insuficiente. |
| **Comenzi imperative (Imperative commands)** | Creează, actualizează sau șterg obiecte direct, în timp real. |
| **Management imperativ (Imperative Management)** | Definirea pașilor expliciți pentru atingerea unei stări dorite. |
| **Ingress** | Obiect API care gestionează accesul extern la servicii din cluster (de regulă HTTP/HTTPS). |
| **IPv4/IPv6 dual stack** | Atribuie adrese IPv4 și IPv6 atât pentru Pods, cât și pentru Services. |
| **Job** | Sarcină finită de tip batch care rulează până la finalizare. Kubernetes reia Job-ul dacă acesta eșuează. |
| **kubectl** | Instrument CLI (linie de comandă) pentru comunicarea cu planul de control Kubernetes, prin API-ul Kubernetes. |
| **Kubelet** | Agentul principal de pe fiecare nod. Se asigură că podurile specificate de serverul API rulează și sunt sănătoase. |
| **Kubernetes** | Platforma open-source standard pentru orchestrarea containerelor, creată de Google și menținută de CNCF. Automatizează gestionarea, scalarea, descoperirea și repararea containerelor. |
| **API-ul Kubernetes (Kubernetes API)** | Aplicația care expune funcționalitățile Kubernetes printr-o interfață RESTful și gestionează starea clusterului. |
| **Kubernetes API Server** | Componentă care validează și configurează datele pentru obiectele API (pods, servicii etc.) și oferă interfața principală a clusterului. |
| **Kubernetes Controller Manager** | Rulează toate procesele de tip controller, care urmăresc și ajustează starea clusterului. |
| **Kubernetes Cloud Controller Manager** | Permite integrarea clusterului Kubernetes cu furnizorul de cloud, separând logica specifică cloud-ului de restul componentelor. |
| **Kubernetes Proxy (kube-proxy)** | Proxy de rețea care rulează pe fiecare nod și gestionează regulile de rutare între Pods și servicii. |
| **kube-scheduler** | Componentă care atribuie noduri podurilor noi create, în funcție de resursele disponibile. |
| **Selector de etichete (Label Selector)** | Permite filtrarea resurselor după etichete (labels). |
| **Etichete (Labels)** | Atribute care identifică și grupează obiecte relevante pentru utilizatori. |
| **Echilibrare de încărcare (Load Balancing)** | Distribuie traficul între Pods pentru performanță și disponibilitate ridicată. |
| **Marathon** | Framework pentru Apache Mesos — un manager de clustere open-source care automatizează managementul containerelor. |
| **Namespace** | Abstracție folosită pentru a izola grupuri de resurse în cadrul aceluiași cluster. |
| **Nod (Node)** | Mașina de lucru (fizică sau virtuală) dintr-un cluster Kubernetes care rulează podurile. |
| **Nomad** | Instrument open-source (HashiCorp) de management și planificare a containerelor, compatibil cu Docker și alte aplicații. |
| **Obiect (Object)** | Entitate din sistemul Kubernetes care descrie o parte din starea clusterului. |
| **Persistență (Persistence)** | Asigură existența unui obiect în sistem până când este modificat sau șters. |
| **Preempțiune (Preemption)** | Mecanism care permite eliberarea resurselor prin înlocuirea podurilor cu prioritate scăzută. |
| **Auto-vindecare (Self-healing)** | Repornirea, înlocuirea sau reprogramarea containerelor eșuate automat. |
| **Serviciu (Service)** | Modalitate abstractă de a expune aplicațiile care rulează în Pods ca servicii de rețea stabile. |
| **Descoperire de servicii (Service Discovery)** | Găsirea și conectarea automată la Pods prin IP-uri sau DNS. |
| **StatefulSet** | Gestionează aplicațiile *stateful*, păstrând ordinea și unicitatea podurilor, cu stocare persistentă. |
| **Stocare (Storage)** | Spațiu de date care oferă suport pentru stocare persistentă sau temporară pentru Pods. |
| **Orchestrare de stocare (Storage Orchestration)** | Montează automat sistemul de stocare ales — local, rețea sau cloud public. |
| **Pod** | Cel mai mic și simplu obiect Kubernetes; reprezintă o instanță a unei aplicații care rulează în cluster. |
| **Proxy** | Server intermediar care facilitează comunicarea între client și un serviciu la distanță. |
| **ReplicaSet** | Asigură menținerea unui număr fix de instanțe (Pods) care rulează simultan. |
| **Workload** | O aplicație care rulează în Kubernetes (ex: Deployment, Job, StatefulSet). |

---

## 🧩 Concluzie

Acest glosar acoperă termenii fundamentali care descriu arhitectura și funcționarea Kubernetes.  
Înțelegerea acestor concepte este esențială pentru a lucra eficient cu resursele și procesele dintr-un cluster Kubernetes modern.
