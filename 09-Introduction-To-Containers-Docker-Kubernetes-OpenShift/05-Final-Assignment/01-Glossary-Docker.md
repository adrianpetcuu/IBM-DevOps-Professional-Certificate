# 📦 Noțiuni de bază despre containere (Container Basics)

## 🧩 Termeni și definiții

| **Termen** | **Definiție** |
|-------------|---------------|
| **Agile** | O abordare iterativă de management de proiect și dezvoltare software care ajută echipele să livreze valoare clienților mai rapid și cu mai puține probleme. |
| **Arhitectură client-server** | O structură de aplicație distribuită care împarte sarcinile între furnizorii de resurse sau servicii (servere) și utilizatori (clienți). |
| **Container** | O unitate standard de software, bazată pe o platformă de containerizare, care include codul aplicației, runtime-ul, instrumentele de sistem, bibliotecile și setările necesare pentru a construi, livra și rula eficient aplicațiile. |
| **Container Registry** | Un sistem utilizat pentru stocarea și distribuirea imaginilor containerizate. Principalele sale funcții includ stocarea imaginilor și facilitarea recuperării acestora. |
| **Pipeline CI/CD** | O secvență de pași automatizați pentru a optimiza procesul de livrare a noilor versiuni software. Îmbunătățește ciclul de viață al dezvoltării software prin automatizare pentru a crește eficiența și calitatea livrării. |
| **Cloud native** | Tip de aplicație conceput special pentru o arhitectură cloud. Aceste aplicații rulează direct în cloud și profită de modelele de livrare software bazate pe cloud. |
| **Fără daemon (Daemon-less)** | Un runtime de container care funcționează fără un proces de fundal dedicat pentru a gestiona imagini, containere, rețele sau volume. |
| **DevOps** | Un set de practici, instrumente și o cultură organizațională care automatizează și integrează procesele dintre dezvoltare software și echipele IT pentru eficiență și colaborare. |
| **Docker** | O platformă open-source de containere care permite dezvoltarea, implementarea și rularea aplicațiilor în containere. |
| **Dockerfile** | Un fișier de configurare ce conține instrucțiuni pentru crearea unei imagini Docker. Docker poate construi automat o imagine urmând instrucțiunile din acest fișier. |
| **Client Docker** | Interfața principală folosită de majoritatea utilizatorilor Docker. Când sunt executate comenzi (ex: `docker run`), clientul trimite instrucțiunile către daemonul Docker (`dockerd`), care le execută folosind API-ul Docker. |
| **Interfața Docker CLI (Command Line Interface)** | Permite utilizatorilor să ruleze comenzi pentru a construi, rula și opri aplicații prin interacțiunea cu daemonul Docker. |
| **Docker daemon (`dockerd`)** | Motorul principal care creează și gestionează obiectele Docker (imagini, containere, rețele și volume). |
| **Docker Hub** | Serviciu cloud pentru stocarea, gestionarea și distribuirea aplicațiilor containerizate. Permite colaborarea în echipă, automatizarea fluxurilor de lucru și menținerea consistenței mediilor. |
| **Docker localhost** | Mod de rețea care permite containerelor să folosească stiva de rețea a gazdei. `localhost` dintr-un container se referă la mașina gazdă, nu la container. |
| **Docker remote host** | Un motor Docker care rulează pe o altă mașină (locală sau externă), accesibil pentru gestionarea containerelor de la distanță prin API-ul Docker Engine. |
| **Rețele Docker** | Permit izolarea comunicațiilor între containere, oferind securitate și control. Numai containerele din aceeași rețea pot comunica între ele. |
| **Plugin-uri Docker** | Extensii care adaugă funcționalități suplimentare Docker-ului, cum ar fi integrarea cu sisteme de stocare externe, rețelistică, securitate sau logare. |
| **Stocare Docker** | Metode de păstrare a datelor dincolo de durata de viață a unui container. Include volume și bind mounts, care permit accesul containerelor la directoare partajate de pe gazdă. |
| **IBM Cloud Container Registry** | Un registry privat complet gestionat de IBM Cloud pentru stocarea și distribuirea imaginilor containerizate. |
| **Imagine (Image)** | Un fișier static care conține codul sursă, bibliotecile și dependențele necesare pentru a rula o aplicație. Servește drept șablon pentru containere. |
| **Imutabilitate** | Proprietatea unei imagini de a fi doar în citire — orice modificare creează o nouă imagine. |
| **LXC (Linux Containers)** | O tehnologie de virtualizare la nivel de sistem de operare care permite crearea de medii Linux izolate pe o singură gazdă. |
| **Microservicii** | O arhitectură cloud-native unde o aplicație este împărțită în componente mici, independente și ușor de implementat separat. |
| **Namespace** | Funcție a kernel-ului Linux care izolează și virtualizează resursele sistemului, permițând proceselor să interacționeze doar în propriul spațiu de nume. |
| **Virtualizare la nivel de sistem de operare** | Permite kernel-ului să suporte mai multe instanțe izolate de spațiu utilizator, adesea denumite containere, jails sau virtual environments. |
| **Registry privat** | Un registry care limitează accesul la imagini doar utilizatorilor autorizați, oferind securitate suplimentară pentru aplicațiile containerizate. |
| **REST API** | API care respectă principiile arhitecturii REST și permite interacțiunea cu servicii web RESTful. |
| **Registry** | Serviciu găzduit care stochează depozite de imagini Docker și interacționează cu clienții prin API-ul Registry. |
| **Repository (Depozit)** | O colecție de imagini Docker ce pot fi partajate printr-un registry. Fiecare imagine din repository poate fi etichetată (tag) pentru versiuni diferite. |
| **Virtualizare server** | Procesul de împărțire a unui server fizic în mai multe servere virtuale independente. |
| **Serverless** | Model de dezvoltare cloud care permite dezvoltatorilor să creeze aplicații fără a gestiona serverele. |
| **Tag** | Etichetă care diferențiază imaginile Docker dintr-un repository. |

---

## 🧰 Comenzi Docker CLI

| **Comandă** | **Descriere** |
|--------------|----------------|
| `curl localhost` | Trimite o cerere HTTP către aplicație (pentru testare). |
| `docker build` | Construiește o imagine Docker dintr-un fișier Dockerfile specificat. |
| `docker build . -t` | Construiește imaginea și îi adaugă o etichetă (tag). |
| `docker CLI` | Pornește interfața de linie de comandă Docker. |
| `docker container rm` | Șterge un container. |
| `docker images` | Afișează lista imaginilor Docker disponibile local. |
| `docker ps` | Listează containerele active. |
| `docker ps -a` | Listează toate containerele, inclusiv cele oprite. |
| `docker pull` | Descarcă cea mai recentă imagine dintr-un registry. |
| `docker push` | Încarcă o imagine sau un repository într-un registry. |
| `docker run` | Rulează o comandă într-un container nou. |
| `docker run -p` | Rulează containerul și mapează porturile publice. |
| `docker stop` | Oprește unul sau mai multe containere în execuție. |
| `docker stop $(docker ps -q)` | Oprește toate containerele care rulează. |
| `docker tag` | Creează o etichetă pentru o imagine. |
| `docker –version` | Afișează versiunea CLI-ului Docker. |
| `exit` | Închide sesiunea terminalului. |
| `export MY_NAMESPACE` | Exportă un spațiu de nume ca variabilă de mediu. |
| `git clone` | Clonează un repository Git cu artefactele necesare. |
| `ibmcloud cr images` | Listează imaginile din IBM Cloud Container Registry. |
| `ibmcloud cr login` | Conectează daemonul Docker local la IBM Cloud Container Registry. |
| `ibmcloud cr namespaces` | Afișează namespace-urile disponibile utilizatorului curent. |
| `ibmcloud cr region-set` | Setează regiunea corespunzătoare contului tău IBM Cloud. |
| `ibmcloud target` | Afișează informații despre contul IBM Cloud curent. |
| `ibmcloud version` | Afișează versiunea curentă a IBM Cloud CLI. |
| `ls` | Listează fișierele și directoarele din directorul curent. |
