# 🐳 Docker CLI – Command Line Interface

## 📖 Overview
**Docker CLI (Command Line Interface)** este instrumentul principal cu care interacționezi cu Docker din linia de comandă.  
Prin CLI poți construi, rula, opri, șterge și publica imagini sau containere, precum și interacționa cu registre precum **Docker Hub** sau **IBM Cloud Container Registry**.

Acest ghid include o listă completă de comenzi frecvente Docker și IBM Cloud CLI, folosite pentru administrarea containerelor și imaginilor.

---

## ⚙️ Docker CLI Commands

| Command | Description |
|----------|--------------|
| `curl localhost` | Verifică dacă aplicația rulează și răspunde local. |
| `docker build` | Construiește o imagine Docker pe baza unui fișier **Dockerfile**. |
| `docker build . -t <nume_imagine>` | Construiește imaginea din directorul curent și adaugă o etichetă (`tag`). |
| `docker container rm <id>` | Șterge un container specific. |
| `docker images` | Listează toate imaginile Docker existente local. |
| `docker ps` | Listează containerele care rulează în prezent. |
| `docker ps -a` | Listează toate containerele – inclusiv cele care s-au oprit. |
| `docker pull <nume_imagine>` | Descarcă ultima versiune a unei imagini dintr-un registry (ex: Docker Hub). |
| `docker push <nume_imagine>` | Trimite o imagine către un registry (public sau privat). |
| `docker run <nume_imagine>` | Rulează o comandă într-un container nou. |
| `docker run -p <port_local>:<port_container> <nume_imagine>` | Rulează containerul și publică porturile (ex: `8080:80`). |
| `docker stop <id>` | Oprește unul sau mai multe containere care rulează. |
| `docker stop $(docker ps -q)` | Oprește **toate containerele** care rulează. |
| `docker tag <sursa> <destinatie>` | Creează o etichetă nouă pentru o imagine. |
| `docker --version` | Afișează versiunea instalată a Docker CLI. |
| `exit` | Închide sesiunea curentă de terminal. |

---

## ☁️ IBM Cloud Container Registry Commands

| Command | Description |
|----------|--------------|
| `export MY_NAMESPACE=<nume>` | Definește o variabilă de mediu pentru namespace-ul IBM Cloud Registry. |
| `git clone <repo_url>` | Clonează un repository Git ce conține fișierele aplicației sau laboratorului. |
| `ibmcloud cr images` | Listează imaginile disponibile în IBM Cloud Container Registry. |
| `ibmcloud cr login` | Conectează Docker Daemon-ul local la IBM Cloud Container Registry. |
| `ibmcloud cr namespaces` | Afișează toate namespace-urile disponibile în contul tău IBM Cloud. |
| `ibmcloud cr region-set <regiune>` | Setează regiunea IBM Cloud pe care vrei să o folosești. |
| `ibmcloud target` | Afișează detalii despre contul și regiunea țintă curentă. |
| `ibmcloud version` | Afișează versiunea curentă a CLI-ului IBM Cloud. |
| `ls` | Listează conținutul directorului curent (utile pentru verificarea fișierelor laboratorului). |

---

## 🧩 Exemple practice

### 🔹 Construirea și rularea unei aplicații
```bash
# Construiește imaginea
docker build -t myapp .

# Rulează containerul și mapează portul 8080
docker run -d -p 8080:80 myapp

# Verifică dacă aplicația răspunde
curl localhost:8080
```

### 🔹 Publicarea unei imagini în IBM Cloud Container Registry
```bash
# Autentificare la IBM Cloud
ibmcloud login

# Setează regiunea corectă
ibmcloud cr region-set eu-de

# Conectează Docker la IBM Cloud Registry
ibmcloud cr login

# Etichetează imaginea
docker tag myapp:latest de.icr.io/${MY_NAMESPACE}/myapp:v1

# Trimite imaginea către registry
docker push de.icr.io/${MY_NAMESPACE}/myapp:v1
```

---

## 🧠 Recomandări utile

- Folosește `docker ps -a` pentru depanarea containerelor oprite.  
- Curăță mediul Docker periodic:
  ```bash
  docker system prune -a
  ```
- Pentru a verifica logurile unui container:
  ```bash
  docker logs <container_id>
  ```
- Poți opri toate containerele rapid:
  ```bash
  docker stop $(docker ps -q)
  ```

---

## ✅ Rezumat

- Docker CLI oferă comenzi rapide pentru a **construi**, **rula** și **gestiona** aplicațiile containerizate.  
- IBM Cloud CLI extinde aceste funcționalități pentru **stocarea și partajarea imaginilor** în cloud.  
- Cunoașterea comenzilor de bază te ajută să administrezi eficient întregul ciclu de viață al containerelor.

> 🐳 **Pe scurt:** Docker CLI = Controlul complet al containerelor tale din terminal!

---

## 📚 Resurse utile
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/docker/)
- [IBM Cloud Container Registry Docs](https://cloud.ibm.com/docs/Registry)
- [Docker Getting Started](https://docs.docker.com/get-started/)
