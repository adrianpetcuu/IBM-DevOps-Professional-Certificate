# 🐳 Introduction to Docker

## 📖 Overview
Această lecție oferă o introducere în **Docker**, cea mai populară platformă de containerizare din lume.  
Docker simplifică procesul de **creare**, **rulare** și **distribuire** a aplicațiilor prin intermediul containerelor — unități software portabile, rapide și izolate.

---

## ⚙️ Ce este Docker?

**Docker** este o platformă software open-source care permite dezvoltatorilor să împacheteze o aplicație împreună cu toate dependențele ei (biblioteci, configurări, cod) într-un **container**.  
Acest container poate rula **identic pe orice sistem** — fie local, pe un server, sau într-un mediu cloud.

> 💡 Cu Docker, aplicația „merge oriunde”, fără probleme de compatibilitate.

---

## 🧱 Componentele principale Docker

| Componentă | Descriere |
|-------------|------------|
| **Dockerfile** | Fișier text care conține instrucțiuni pentru construirea unei imagini. |
| **Image (imagine)** | Șablonul aplicației – conține codul, bibliotecile și mediul de rulare. |
| **Container** | Instanța activă a unei imagini (aplicația care rulează efectiv). |
| **Docker Engine** | Motorul care rulează și gestionează containerele. |
| **Docker Hub / Registry** | Serviciu online pentru stocarea și partajarea imaginilor Docker. |

---

## 🧩 Cum funcționează Docker

1. ✍️ Dezvoltatorul scrie un **Dockerfile** cu instrucțiunile de construire a aplicației.  
2. 🏗️ Docker creează o **imagine** (folosind `docker build`).  
3. 🚀 Imaginea este rulată ca un **container** (folosind `docker run`).  
4. 🌐 Imaginea poate fi **publicată** în Docker Hub pentru a fi partajată.  

---

## 💻 Exemple de comenzi uzuale Docker

| Comandă | Descriere |
|----------|------------|
| `docker build -t myapp .` | Construiește o imagine numită `myapp` din Dockerfile. |
| `docker run -d -p 8080:80 myapp` | Rulează un container în fundal, mapând portul 8080 al gazdei pe 80 din container. |
| `docker ps` | Listează containerele care rulează. |
| `docker stop <id>` | Oprește un container activ. |
| `docker images` | Afișează imaginile disponibile local. |
| `docker push myapp` | Trimite imaginea `myapp` într-un registru (ex: Docker Hub). |

---

## 🧠 Cum funcționează arhitectura Docker

Docker folosește o **arhitectură client–server**:
- **Clientul Docker (CLI)** → trimite comenzi (ex: `docker run`)  
- **Docker Daemon** → execută comenzile (creează containere, gestionează imagini)
- **Docker Registry** → locul unde sunt stocate imaginile (publice sau private)

Comunicația se face printr-un **API REST**.

---

## 📦 Beneficiile Docker

- 🚀 **Viteză** – containerele se pornesc în câteva secunde.  
- 📦 **Portabilitate** – aplicațiile rulează identic pe orice sistem.  
- ⚙️ **Izolare** – fiecare container rulează independent.  
- 💰 **Eficiență** – folosește mai puține resurse decât mașinile virtuale.  
- 🔄 **Scalabilitate** – perfect pentru aplicații distribuite și microservicii.  

---

## 🧭 Exemple practice

Construirea și rularea unei aplicații web simple:
```bash
# 1. Construiește imaginea
docker build -t mywebapp .

# 2. Rulează aplicația în container
docker run -d -p 8080:80 mywebapp

# 3. Verifică rularea
docker ps
curl localhost:8080
```

---

## 🔒 Docker Hub și registrele private

- **Docker Hub** este registrul public oficial unde poți descărca imagini existente (`nginx`, `mysql`, `python` etc.).
- **Registre private** (ex: IBM Cloud Container Registry) sunt folosite de organizații pentru stocare securizată a imaginilor.

---

## 🧩 Docker vs. Mașini Virtuale

| Aspect | Docker (Containere) | Mașini Virtuale |
|---------|----------------------|-----------------|
| Sistem de operare | Împarte kernelul gazdei | Include un OS complet |
| Viteză de pornire | Secunde | Minute |
| Resurse folosite | Reduse | Mai mari |
| Portabilitate | Foarte mare | Limitată |
| Izolare | La nivel de proces | La nivel hardware |

---

## ✅ Concluzie

**Docker** este fundamentul containerizării moderne.  
El oferă un mod rapid, sigur și consistent de a crea, testa și implementa aplicații în orice mediu.  

> 🐋 „Build once, run anywhere.” – Docker transformă aplicațiile în pachete universale.

---

## 📚 Resurse recomandate

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [IBM Cloud Container Registry](https://cloud.ibm.com/registry)
