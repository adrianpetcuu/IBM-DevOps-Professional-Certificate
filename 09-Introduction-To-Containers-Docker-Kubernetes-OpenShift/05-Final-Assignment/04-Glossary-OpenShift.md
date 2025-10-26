# 🐧 Noțiuni de bază despre OpenShift (OpenShift Basics)

## 🧩 Termeni și definiții

| **Termen** | **Definiție** |
|-------------|---------------|
| **Testare A/B (A/B testing)** | Strategie folosită frecvent pentru a testa funcționalități noi în aplicațiile front-end. Implică compararea a două versiuni, A și B, pentru a determina care oferă performanțe mai bune într-un mediu controlat. |
| **Build** | Procesul de transformare a input-urilor (cod sursă, configurații etc.) într-un obiect rezultat (imagine container, binar etc.). |
| **BuildConfig** | Un obiect specific OpenShift care definește pașii și strategia de construire a unei aplicații. Servește drept plan (blueprint) pentru procesul de build, indicând cum sunt folosite sursele pentru a genera rezultatul dorit. |
| **Implementare Canary (Canary Deployments)** | Strategie de implementare în care o versiune nouă a aplicației este lansată treptat către un subset de utilizatori sau trafic, pentru testare în condiții reale înainte de lansarea completă. |
| **Circuit breaking** | Metodă folosită pentru a preveni propagarea erorilor dintr-un microserviciu către alte microservicii. |
| **Schimbare de configurație (Configuration Change)** | Declanșator care pornește un nou build atunci când este creată o nouă resursă `BuildConfig`. |
| **Plan de control (Control Plane)** | Componenta care interpretează configurația dorită și actualizează dinamic serverele proxy pe măsură ce mediul se modifică. |
| **Strategie de build personalizată (Custom Build Strategy)** | Permite utilizatorilor să definească și să folosească propriile imagini personalizate de tip builder pentru procesul de build. |
| **Imagini builder personalizate (Custom Builder Images)** | Imagini Docker standard care conțin logica necesară pentru a transforma input-urile în rezultatul dorit. |
| **CRD (Custom Resource Definition)** | Cod personalizat care permite adăugarea de resurse noi în API-ul Kubernetes fără a crea un server complet nou. |
| **Controlere personalizate (Custom Controllers)** | Gestionază resursele definite prin CRD-uri, asigurând ca starea curentă a acestora se aliniază cu starea dorită, acționând automat pentru a menține consistența. |
| **Plan de date (Data Plane)** | Strat al arhitecturii de rețea care gestionează comunicațiile dintre servicii. În absența unui Service Mesh, rețeaua nu poate identifica tipul traficului, sursa și destinația. |
| **Control și aplicabilitate (Enforceability)** | În Istio, asigură aplicarea politicilor la nivel de sistem pentru distribuirea echitabilă a resurselor între consumatori. |
| **Proxy Envoy** | Proxy utilizat de Istio pentru interceptarea și gestionarea traficului de rețea. Oferă funcții precum balansare de sarcină, observabilitate și securitate. |
| **Operatori umani (Human Operators)** | Persoane care administrează sistemele, implementează servicii, detectează probleme și aplică soluții pentru a menține funcționarea stabilă. |
| **Schimbare de imagine (Image Change)** | Declanșator pentru reconstruirea unei aplicații containerizate atunci când este disponibilă o nouă versiune a imaginii. Exemplu: o aplicație bazată pe imaginea Node.js este reconstruită automat la lansarea unei actualizări de securitate. |
| **ImageStream** | Abstracție OpenShift folosită pentru a referenția imagini container. Conține metadate (ID-uri, digests), dar nu stochează efectiv imaginile — doar indică versiunile disponibile. |
| **Etichetă ImageStream (ImageStream Tag)** | Identificator dintr-un ImageStream care face referire la o versiune specifică a unei imagini dintr-un registry. |
| **Istio** | Platformă open-source, independentă de infrastructură, pentru Service Mesh. Controlează traficul și apelurile API dintre servicii și simplifică gestionarea rețelelor. |
| **Atacuri Man-in-the-Middle** | Atacuri cibernetice în care un terț interceptează și retransmite comunicațiile dintre două părți care cred că discută direct între ele. |
| **Observabilitate (Observability)** | Capacitatea de a monitoriza fluxul traficului într-un service mesh, de a urmări traseele apelurilor și de a vizualiza metrici precum latența și erorile. |
| **OpenShift** | Platformă enterprise de tip hibrid cloud, bazată pe Kubernetes, care permite dezvoltatorilor să construiască, implementeze și administreze aplicații containerizate. |
| **Proces CI/CD în OpenShift** | Proces automat de integrare continuă și livrare care integrează schimbări de cod, construiește, testează și implementează automat noi versiuni în diferite medii. |
| **Operatori (Operators)** | Extensii software Kubernetes care automatizează sarcini complexe, acționând ca și controlere personalizate pentru a extinde funcționalitatea API-ului Kubernetes. |
| **Operator Framework** | Suită de instrumente și capabilități pentru dezvoltarea, testarea, livrarea și actualizarea Operatorilor în medii Kubernetes. |
| **OperatorHub** | Interfață web în OpenShift unde administratorii de cluster pot descoperi și instala Operatorii disponibili (certificați Red Hat, comunitari sau personalizați). |
| **Operator Lifecycle Manager (OLM)** | Componentă care gestionează ciclul de viață al Operatorilor (instalare, upgrade, control al accesului RBAC) în Kubernetes și OpenShift. |
| **Modelul de maturitate al Operatorilor (Operator Maturity Model)** | Cadrul care definește nivelurile de maturitate ale Operatorilor, de la instalare manuală până la automatizare completă (Auto Pilot). |
| **Pattern Operator (Operator Pattern)** | Model de design care leagă un Controller de una sau mai multe resurse personalizate. |
| **Registry Operator (Operator Registry)** | Sistem care stochează CRD-uri, CSV-uri și metadate despre Operatorii disponibili și canalele acestora. Rulează în cluster și furnizează datele către OLM. |
| **Operator SDK** | Set de instrumente pentru dezvoltatorii de Operator, care simplifică procesul de creare, testare și împachetare fără cunoștințe profunde despre API-ul Kubernetes. |
| **postCommit** | Secțiune dintr-un `BuildConfig` care definește un hook opțional executat după finalizarea unui build. |
| **Retry-uri (Retries)** | Mecanism în microservicii care reîncearcă automat cereri eșuate către alte servicii. |
| **runPolicy** | Câmp în `BuildConfig` care definește modul de execuție a build-urilor — secvențial (Serial, implicit) sau concurent. |
| **Service Broker** | Proces de scurtă durată care gestionează conexiunile între servicii, dar nu efectuează operațiuni pe termen lung (upgrade, failover, scaling). |
| **Service Mesh** | Strat dedicat care asigură securitatea și fiabilitatea comunicațiilor dintre servicii. Oferă gestionarea traficului, criptarea datelor și vizibilitate completă asupra comportamentului aplicațiilor. |
| **Operatori software (Software Operators)** | Încearcă să reproducă cunoștințele operatorilor umani și să automatizeze aceleași procese. |
| **Source-to-Image (S2I)** | Instrument OpenShift care construiește imagini container reproducibile prin injectarea codului sursă direct într-o imagine de bază. |
| **Strategie de sursă (Source Strategy)** | Definește modul în care se execută build-urile: prin cod sursă (Source), containere (Docker) sau configurații personalizate. Fiecare opțiune oferă avantaje diferite în funcție de proiect. |
| **Tip de sursă (Source Type)** | Tipul de input principal pentru build — de exemplu, un repository Git, un Dockerfile inline sau fișiere binare. |
| **Webhook** | Declanșator care trimite o cerere către un endpoint API din OpenShift Container Platform. Permite automatizarea fluxurilor de dezvoltare, declanșând build-uri automat la fiecare commit nou de cod. |

---

## 💻 Comenzi OpenShift CLI

| **Comandă** | **Descriere** |
|--------------|----------------|
| `oc get` | Afișează resursele existente într-un proiect. |
| `oc project` | Schimbă proiectul activ curent. |
| `oc version` | Afișează informațiile despre versiunea OpenShift CLI. |

---

📘 *OpenShift extinde Kubernetes prin adăugarea de funcționalități enterprise precum build-uri automate, control avansat al aplicațiilor, operatori software și procese CI/CD complet integrate.*
