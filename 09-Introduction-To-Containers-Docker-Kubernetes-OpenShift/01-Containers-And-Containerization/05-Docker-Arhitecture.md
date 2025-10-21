# 🏗️ Docker Architecture

## 📖 Overview
Această lecție explică **arhitectura Docker**, adică structura internă a platformei și modul în care componentele sale principale colaborează pentru a crea, rula și gestiona containere.  
Docker folosește o arhitectură **client–server**, ceea ce îi oferă flexibilitate, eficiență și scalabilitate în medii locale sau cloud.

---

## ⚙️ Ce este arhitectura Docker?

Arhitectura Docker este alcătuită din trei componente principale:
1. 🧑‍💻 **Docker Client (Clientul Docker)**  
2. 🐋 **Docker Daemon (Serverul Docker)**  
3. 🗂️ **Docker Registry (Registrul de imagini)**  

Aceste componente comunică între ele printr-un **API REST**, ceea ce permite interacțiuni standardizate între client și server.

---

## 🧑‍💻 1. Docker Client (Clientul Docker)

Clientul Docker este **interfața cu care interacționează utilizatorul**.  
Prin intermediul liniei de comandă (`docker CLI`), trimitem comenzi către Docker Daemon.

### 🔧 Exemple de comenzi:
```bash
docker build -t myapp .
docker run -d -p 8080:80 myapp
docker ps
docker stop <container_id>
```
Clientul Docker poate comunica cu:
- Docker Daemon local (pe aceeași mașină), sau
- Docker Daemon aflat pe un alt server (remote).

> 💡 Gândește-te la client ca la „telecomanda” care controlează serverul Docker.

---

## 🐋 2. Docker Daemon (Serverul Docker)

**Docker Daemon (`dockerd`)** este procesul de fundal care rulează pe sistem și execută efectiv toate operațiunile Docker.

Rolul său este să:
- construiască imagini (`docker build`),  
- ruleze și gestioneze containere (`docker run`, `docker stop`),  
- administreze volume și rețele,  
- comunice cu alte daemons (într-un cluster).

Daemonul ascultă cererile primite de la client prin API-ul Docker.

> 💡 Este „motorul” din spatele Docker – el face toată munca grea.

---

## 🗂️ 3. Docker Registry (Registrul de imagini)

**Registrul Docker** este locul unde sunt stocate imaginile Docker.  
Cel mai cunoscut este **Docker Hub**, dar există și registre private, cum ar fi **IBM Cloud Container Registry** sau **GitHub Container Registry**.

### 🔧 Comenzi uzuale:
```bash
docker pull nginx     # descarcă o imagine dintr-un registry
docker push myapp     # trimite o imagine către un registry
```

> 💡 Registrul funcționează ca un „depozit central” de imagini pe care le poți folosi oriunde.

---

## 🔄 Cum colaborează componentele Docker

Fluxul de lucru general:

1. 🔹 **Clientul** trimite o comandă către Daemon (ex: `docker run`).  
2. 🔹 **Daemonul** verifică dacă imaginea există local; dacă nu, o descarcă din **Registry**.  
3. 🔹 Daemonul creează un **container** pe baza imaginii.  
4. 🔹 Containerul rulează aplicația, iar clientul primește feedback-ul în terminal.

### 🔁 Reprezentare simplificată:
```
[ YOU ]
   │
   ▼
[ Docker Client ]  →  trimite comenzi prin API REST
   │
   ▼
[ Docker Daemon ]  →  construiește, rulează și gestionează containere
   │
   ▼
[ Docker Registry ]  →  stochează și furnizează imagini
```

---

## 🧠 Alte componente Docker importante

### 📦 Docker Objects
- **Images** – șabloanele aplicațiilor.  
- **Containers** – instanțele care rulează aplicațiile.  
- **Volumes** – persistă datele.  
- **Networks** – conectează containerele între ele.

### 🔒 Docker API
Docker oferă un **REST API** care permite integrarea cu alte instrumente DevOps sau servicii de orchestrare precum Kubernetes și OpenShift.

---

## 🧰 Exemple de flux de lucru complet

```bash
# 1. Construiește imaginea
docker build -t myapp .

# 2. Rulează aplicația în container
docker run -d -p 8080:80 myapp

# 3. Trimite imaginea către Docker Hub
docker tag myapp username/myapp:v1
docker push username/myapp:v1

# 4. Descarcă imaginea de pe alt sistem
docker pull username/myapp:v1
```

---

## 🧩 Rezumat general

| Componentă | Rol principal | Exemple |
|-------------|----------------|----------|
| 🧑‍💻 **Client** | Trimite comenzi către daemon | `docker run`, `docker build` |
| 🐋 **Daemon** | Creează, rulează și gestionează containere | `dockerd` |
| 🗂️ **Registry** | Stochează și distribuie imagini | `docker pull`, `docker push` |

---

## ✅ Concluzie

Arhitectura Docker este simplă, dar extrem de eficientă.  
Clientul trimite comenzi, daemonul le execută, iar registry-ul gestionează imaginile.  
Această structură modulară permite Docker să fie rapid, portabil și ușor de scalat.

> 🐳 **Pe scurt:** Client + Daemon + Registry = Ecosistemul complet Docker.

---

## 📚 Resurse recomandate
- [Docker Architecture Docs](https://docs.docker.com/get-started/overview/#docker-architecture)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/docker/)
- [Docker Hub](https://hub.docker.com/)
