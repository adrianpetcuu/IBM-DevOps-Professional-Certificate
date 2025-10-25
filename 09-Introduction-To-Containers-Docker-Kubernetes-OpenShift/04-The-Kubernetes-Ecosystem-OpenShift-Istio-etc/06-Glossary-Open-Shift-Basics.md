# 🌐 Ecosistemul Kubernetes: OpenShift, Istio și altele

🎉 **Felicitări!** Ai finalizat acest modul.  
În acest punct, ar trebui să știi următoarele concepte cheie:

---

## 🚀 OpenShift

- **OpenShift®** este o platformă Kubernetes **enterprise-ready**, construită pentru **cloud hibrid deschis**.  
- Este mai ușor de utilizat, se **integrează cu Jenkins** și oferă mai multe **servicii și funcționalități** decât Kubernetes standard.  
- Oferă o experiență completă pentru dezvoltare, testare și implementare a aplicațiilor containerizate.

---

## ⚙️ Extinderea Kubernetes cu CRD-uri și Operatorii

- **Custom Resource Definitions (CRD)** extind API-ul Kubernetes, permițând definirea de **resurse personalizate**.  
- Când CRD-urile sunt combinate cu **controlere personalizate**, ele creează **API-uri declarative noi** în Kubernetes.  
- **Operatorii** utilizează aceste CRD-uri și controlere pentru a **automatiza sarcinile de administrare a clusterului**, cum ar fi instalări, upgrade-uri sau backup-uri.

---

## 🏗️ Build-uri și imagini în OpenShift

- Un **Build** este procesul prin care **intrările (codul sursă, imaginile de bază, configurațiile)** sunt transformate într-un **obiect final** – de obicei o **imagine container**.  
- Un **ImageStream** reprezintă o **abstracție** pentru gestionarea și referențierea imaginilor container în OpenShift.  
  Acesta facilitează actualizările automate și controlul versiunilor imaginilor folosite de aplicații.

---

## 🔗 Service Mesh și Istio

- Un **Service Mesh** oferă:
  - 🧭 **Management al traficului** – controlează fluxul comunicațiilor între servicii.  
  - 🔒 **Securitate** – criptează traficul dintre servicii (mTLS).  
  - 👁️ **Observabilitate** – monitorizează comportamentul aplicațiilor pentru depanare și optimizare.  

- **Istio** este un **service mesh** care sprijină patru concepte fundamentale:
  1. **Conectivitate (Connection)**  
  2. **Securitate (Security)**  
  3. **Politici și control (Enforcement)**  
  4. **Observabilitate (Observability)**  

- Istio este utilizat frecvent în **arhitecturi de microservicii**, oferind:
  - Măsurători esențiale pentru monitorizare: **latență, trafic, erori și saturație**.  
  - Instrumente integrate pentru optimizarea performanței aplicațiilor distribuite.

---

## 🧾 Rezumat

✅ **Ce ai învățat:**
- OpenShift este o platformă Kubernetes enterprise-ready pentru cloud hibrid.  
- OpenShift oferă mai multe servicii, integrare CI/CD (Jenkins) și o utilizare simplificată.  
- CRD-urile extind API-ul Kubernetes, iar Operatorii automatizează sarcini prin CRD-uri și controlere personalizate.  
- Build-urile transformă sursa în imagini container, gestionate prin ImageStreams.  
- Service Mesh-urile, precum **Istio**, aduc securitate, management al traficului și observabilitate între microservicii.  

---

📘 *Ecosistemul Kubernetes – cu OpenShift, CRD-uri, Operatorii și Istio – oferă o bază solidă pentru dezvoltarea, implementarea și administrarea aplicațiilor moderne, scalabile și sigure.*


# 🧰 OpenShift CLI (Linia de comandă)

Tabelul de mai jos conține cele mai utilizate comenzi CLI din OpenShift, împreună cu descrierea acestora:

| Comandă | Descriere |
|----------|------------|
| **oc get** | Afișează informații despre o resursă (poduri, deployment-uri, servicii etc.). |
| **oc project** | Schimbă proiectul (namespace-ul) curent. |
| **oc version** | Afișează informații despre versiunea OpenShift CLI și a clusterului. |

---

# 📘 Glosar: Noțiuni de bază OpenShift

| Termen | Definiție |
|--------|------------|
| **A/B Testing** | Strategie folosită pentru testarea noilor funcționalități în aplicațiile front-end. Se compară două versiuni – *A* și *B* – pentru a evalua care performează mai bine. Versiunile sunt testate pe grupuri diferite de utilizatori, iar în funcție de feedback, se alege varianta care merge în producție. |
| **Build** | Procesul de transformare a intrărilor (cod, imagini, configurări) într-un obiect rezultat – de obicei o imagine container. |
| **BuildConfig** | Un obiect specific OpenShift care definește pașii unui proces de build: surse, strategie și rezultate. Este ca un „plan” al build-ului, iar build-ul efectiv este o instanță a acelui plan. |
| **Canary Deployments** | Strategie care implementează o nouă versiune a aplicației pentru un număr mic de utilizatori, crescând treptat audiența. Permite identificarea și corectarea problemelor înainte de lansarea completă. |
| **Circuit Breaking** | Mecanism pentru prevenirea răspândirii erorilor între microservicii (izolează un serviciu defect pentru a proteja restul sistemului). |
| **Configuration Change** | Tip de trigger care declanșează un build nou atunci când este creat sau modificat un `BuildConfig`. |
| **Control Plane** | Componenta care gestionează configurația dorită a clusterului, programând și actualizând proxy-urile în funcție de schimbările mediului. |
| **Custom Build Strategy** | Strategie de build care necesită o imagine personalizată a constructorului (builder image). |
| **Custom Builder Images** | Imagini Docker personalizate ce conțin logica necesară pentru a transforma sursele în rezultat. |
| **CRDs (Custom Resource Definitions)** | Cod personalizat care definește resurse noi în API-ul Kubernetes fără a crea un server nou. |
| **Custom Controllers** | Controlează și sincronizează starea efectivă a resurselor personalizate (CRDs) cu starea dorită. |
| **Data Plane** | Gestionarea comunicației între servicii. Fără un service mesh, rețeaua nu poate identifica tipul de trafic, sursa sau destinația acestuia. |
| **Enforceability (Control)** | În Istio, reprezintă capacitatea de a aplica politici și de a distribui corect resursele între consumatori. |
| **Envoy Proxy** | Proxy-ul utilizat de service mesh pentru interceptarea traficului dintre servicii, permițând filtrare, criptare și rutare inteligentă. |
| **Human Operators** | Administratorii umani care știu cum să implementeze servicii, să recunoască problemele și să le remedieze. |
| **Image Change** | Trigger care pornește un build atunci când este disponibilă o nouă versiune a unei imagini (ex: actualizări de securitate în imaginea de bază Node.js). |
| **ImageStream** | Abstracție pentru referențierea imaginilor container în OpenShift. Nu stochează date, ci indicii către imagini reale dintr-un registry. |
| **ImageStream Tag** | Etichetă care identifică o imagine specifică dintr-un ImageStream. |
| **Istio** | Platformă de *service mesh* folosită adesea cu Kubernetes. Controlează traficul și apelurile API între servicii, asigură securitatea (autentificare, autorizare, criptare) și observabilitatea (tracing, metrici, loguri). |
| **Man-in-the-Middle (MiTM) Attack** | Tip de atac cibernetic în care atacatorul interceptează comunicația între două părți, fără ca acestea să știe, manipulând mesajele transmise. |
| **Observability (Observabilitate)** | Capacitatea de a urmări fluxul traficului, apelurile și dependențele între servicii, vizualizând metrici precum latența, erorile și saturația. |
| **OpenShift** | Platformă Kubernetes enterprise pentru cloud hibrid. |
| **OpenShift CI/CD Process** | Flux automat care integrează, construiește, testează și implementează noi versiuni de aplicații în medii diferite. |
| **Operators** | Extind API-ul Kubernetes și automatizează sarcinile de cluster (instalare, upgrade, backup). |
| **Operator Framework** | Suită de instrumente pentru crearea, testarea și gestionarea Operatorilor în Kubernetes și OpenShift. |
| **OperatorHub** | Interfața web unde administratorii pot descărca și instala Operatorii disponibili (Red Hat, Certified, Community sau Custom). |
| **Operator Lifecycle Manager (OLM)** | Componenta care controlează instalarea, actualizarea și accesul bazat pe rol (RBAC) pentru Operatorii dintr-un cluster. |
| **Operator Maturity Model** | Definește nivelurile de maturitate ale Operatorilor, de la *Basic Install* până la *Auto Pilot* (automatizare completă). |
| **Operator Pattern** | Model arhitectural care leagă un Controller de una sau mai multe resurse personalizate (CRs). |
| **Operator Registry** | Stochează CRD-uri, versiuni de serviciu și metadate ale Operatorilor, oferind date către OLM. |
| **Operator SDK** | Kit de dezvoltare (Helm, Go, Ansible) pentru a construi și testa Operatorii fără a necesita cunoștințe profunde de Kubernetes API. |
| **postCommit** | Secțiune opțională a unui build care definește acțiuni executate după finalizarea procesului de construire. |
| **Retries** | Mecanism de reîncercare automată a unei cereri eșuate între microservicii. |
| **runPolicy** | Parametru care definește modul de rulare a build-urilor: secvențial (Serial) sau simultan (Parallel). |
| **Service Broker** | Proces de scurtă durată care oferă servicii, dar nu gestionează operațiuni continue (ex: scaling sau failover). |
| **Service Mesh** | Strat dedicat pentru comunicația securizată și fiabilă între servicii. Oferă control al traficului, criptare și observabilitate completă. |
| **Software Operators** | Reproduc cunoștințele operatorilor umani prin cod, automatizând procesele administrative. |
| **Source-to-Image (S2I)** | Instrument pentru crearea de imagini container reproducibile. Injectează codul sursă într-o imagine de bază pentru a genera o aplicație gata de rulare. |
| **Source Strategy** | Definește strategia de build (Source, Docker sau Custom). |
| **Source Type** | Specifică sursa principală de intrare – un repository Git, un Dockerfile inline sau un fișier binar. |
| **Webhook** | Trigger care trimite cereri către API-ul OpenShift pentru a declanșa build-uri automate. De obicei este configurat cu GitHub, dar poate fi generic. Webhook-urile permit declanșarea automată a build-urilor la fiecare commit, merge sau pull request. |

---

📘 *Acest glosar oferă o referință completă pentru termenii-cheie din ecosistemul OpenShift și Kubernetes – de la comenzi de bază CLI până la concepte avansate precum build-uri, operatori și service mesh.*
