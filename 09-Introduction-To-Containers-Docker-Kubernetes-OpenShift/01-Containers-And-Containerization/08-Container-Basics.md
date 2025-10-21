# 📦 Container Basics

## 📖 Overview
Acest fișier explică termenii fundamentali din ecosistemul **containerelor**, oferind o bază clară pentru înțelegerea conceptelor de **Docker**, **cloud-native**, **DevOps**, și a arhitecturii moderne bazate pe containere.

---

## 🧠 Termeni și definiții

| Term | Definition |
|------|-------------|
| **Agile** | O metodologie iterativă de management al proiectelor și dezvoltare software, care permite echipelor să livreze valoare mai rapid și cu mai puține erori. |
| **Client-server architecture** | O structură de aplicație distribuită care împarte sarcinile între furnizori de servicii (servere) și clienți care solicită servicii. |
| **Container** | O unitate standard de software care conține codul aplicației, runtime-ul, librăriile, instrumentele de sistem și setările necesare pentru a construi, livra și rula aplicații eficient. |
| **Container Registry** | Un serviciu utilizat pentru stocarea și distribuirea imaginilor de containere. Exemple: Docker Hub, IBM Cloud Container Registry. |
| **CI/CD pipelines** | Procese automatizate de integrare continuă (CI) și livrare continuă (CD) care asigură implementarea rapidă și fiabilă a versiunilor noi de software. |
| **Cloud native** | Aplicațiile „cloud-native” sunt proiectate pentru arhitecturi cloud, profitând de scalabilitate și reziliență nativă. |
| **Daemon-less** | Un runtime de containere care nu necesită un proces daemon central pentru a crea și administra obiecte (imagini, volume, rețele). |
| **DevOps** | O cultură și un set de practici care unesc dezvoltarea software (Dev) și operațiunile IT (Ops), promovând automatizarea și colaborarea. |
| **Docker** | O platformă deschisă pentru dezvoltarea, livrarea și rularea aplicațiilor în containere. |
| **Dockerfile** | Un fișier text care conține instrucțiunile necesare pentru a construi automat o imagine Docker. |
| **Docker client** | Interfața principală prin care utilizatorii trimit comenzi Docker către daemon (ex: `docker run`, `docker build`). |
| **Docker Command Line Interface (CLI)** | Interfața de linie de comandă care permite construirea, rularea și oprirea containerelor prin comenzi către Docker Daemon. |
| **Docker daemon (dockerd)** | Serviciul care creează și gestionează obiecte Docker precum imagini, containere, rețele și volume. |
| **Docker Hub** | Cel mai popular registry public pentru partajarea și distribuirea imaginilor containerelor. |
| **Docker localhost** | Rețeaua host partajată care permite containerelor să folosească stiva de rețea a gazdei; `localhost` din container indică hostul fizic. |
| **Docker remote host** | O mașină aflată local sau în rețea, care rulează un Docker Engine accesibil prin API-ul Docker. |
| **Docker networks** | Mecanismul care permite izolarea și comunicarea între containere. |
| **Docker plugins** | Extensii Docker, cum ar fi plugin-urile de stocare, care conectează platforme externe. |
| **Docker storage** | Folosește volume și bind mounts pentru a păstra datele persistente chiar și după oprirea containerelor. |
| **LXC (Linux Containers)** | Tehnologie de virtualizare la nivel de sistem de operare care permite rularea mai multor medii Linux izolate pe același host. |
| **IBM Cloud Container Registry** | Serviciu IBM pentru stocarea și distribuirea imaginilor containerelor într-un registry privat complet gestionat. |
| **Image** | Fișier imuabil care conține codul sursă, librăriile și dependențele necesare pentru rularea aplicației. |
| **Immutability** | Imaginile Docker sunt *read-only*; orice modificare generează o imagine nouă. |
| **Microservices** | Arhitectură modulară în care o aplicație este compusă din servicii mici, independente și ușor de scalat. |
| **Namespace** | Funcție a kernelului Linux care izolează resursele sistemului (procese, rețele, stocare). Element cheie în izolarea containerelor. |
| **Operating System Virtualization** | Virtualizare la nivel de sistem de operare care permite rularea mai multor spații de utilizator izolate numite containere. |
| **Private Registry** | Registry cu acces restricționat – doar utilizatorii autorizați pot vizualiza sau folosi imaginile. |
| **REST API** | Interfață de programare care respectă principiile REST și permite interacțiunea cu servicii web. |
| **Registry** | Serviciu găzduit care conține depozite (repositories) de imagini și răspunde la solicitări API. |
| **Repository** | Set de imagini Docker care pot fi etichetate și împinse (push) într-un registry. |
| **Server Virtualization** | Procesul de împărțire a unui server fizic în mai multe servere virtuale independente. |
| **Serverless** | Model de dezvoltare cloud-native în care aplicațiile rulează fără gestionarea explicită a serverelor. |
| **Tag** | Etichetă aplicată unei imagini Docker care o distinge de alte versiuni din același repository. |

---

## ✅ Concluzie
Aceste concepte formează vocabularul de bază al containerizării moderne.  
Prin înțelegerea lor, poți lucra eficient cu Docker, CI/CD, DevOps și infrastructuri cloud-native.

> 🐳 **Pe scurt:** Containerele sunt unități standardizate care permit portabilitate, eficiență și automatizare completă în livrarea aplicațiilor.

---

## 📚 Resurse recomandate
- [Docker Glossary](https://docs.docker.com/glossary/)
- [IBM Cloud Container Registry Docs](https://cloud.ibm.com/docs/Registry)
- [What is a Container? – Docker Docs](https://docs.docker.com/get-started/overview/)
