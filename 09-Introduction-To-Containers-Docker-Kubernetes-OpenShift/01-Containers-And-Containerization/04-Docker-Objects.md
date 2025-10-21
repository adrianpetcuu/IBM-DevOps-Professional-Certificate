# 🧩 Docker Objects

## 📖 Overview
Această lecție explică principalele **obiecte Docker** – elementele de bază care alcătuiesc platforma Docker și care permit gestionarea completă a aplicațiilor containerizate.  
Obiectele Docker sunt componentele esențiale prin care Docker construiește, rulează, salvează și conectează containerele.

---

## 🧱 Ce sunt obiectele Docker?

În Docker, totul este construit în jurul unor **obiecte**. Acestea sunt entitățile pe care Docker le creează și le gestionează:  
➡️ **Images (imagini)**  
➡️ **Containers (containere)**  
➡️ **Volumes (volume)**  
➡️ **Networks (rețele)**  

Fiecare dintre aceste obiecte are un rol specific în procesul de dezvoltare și rulare a aplicațiilor.

---

## 📦 1. Docker Images (Imagini Docker)

O **imagine Docker** este un **șablon read-only** folosit pentru a crea containere.  
Ea conține codul aplicației, bibliotecile, dependențele și instrucțiunile necesare pentru rulare.

- Imaginile sunt construite dintr-un **Dockerfile**.  
- Pot fi stocate local sau în registre (ex: Docker Hub).  
- Fiecare strat al unei imagini corespunde unei instrucțiuni din Dockerfile.

### 🔧 Comenzi utile:
```bash
docker images          # Listează imaginile disponibile local
docker rmi <image_id>  # Șterge o imagine
docker pull nginx       # Descarcă o imagine din Docker Hub
```

> 💡 Gândește-te la o imagine ca la o „rețetă” – poți face oricâte containere vrei din ea.

---

## 🚀 2. Docker Containers (Containere Docker)

Un **container** este o **instanță activă a unei imagini**.  
Când rulezi o imagine, Docker creează un container care conține aplicația în execuție, complet izolată de restul sistemului.

- Containerele sunt **temporare** (se pot opri, porni sau șterge).  
- Poți avea mai multe containere pornite din aceeași imagine.

### 🔧 Comenzi utile:
```bash
docker run -d -p 8080:80 myapp   # Rulează un container
docker ps                        # Listează containerele active
docker stop <container_id>       # Oprește un container
docker rm <container_id>         # Șterge un container
```

> 💡 Imaginea = modelul, containerul = instanța activă a acelui model.

---

## 💾 3. Docker Volumes (Volume Docker)

Un **volum** este un spațiu de stocare folosit pentru a **păstra date persistente** între containere.  
Fără volume, toate datele dintr-un container se pierd la oprirea acestuia.

- Volumele sunt gestionate de Docker.  
- Pot fi partajate între containere.  
- Sunt esențiale pentru aplicațiile cu baze de date.

### 🔧 Comenzi utile:
```bash
docker volume create mydata      # Creează un volum nou
docker volume ls                 # Listează volumele existente
docker run -v mydata:/app/data mydb  # Montează un volum într-un container
docker volume rm mydata          # Șterge un volum
```

> 💡 Volumele salvează datele în afara containerului, deci sunt păstrate chiar dacă containerul e șters.

---

## 🌐 4. Docker Networks (Rețele Docker)

**Rețelele Docker** definesc modul în care containerele comunică între ele sau cu lumea exterioară.

- Docker creează automat o rețea implicită numită **bridge**.  
- Poți crea rețele personalizate pentru a izola grupuri de containere.  
- Containerele din aceeași rețea pot comunica folosind numele lor ca hostname.

### 🔧 Comenzi utile:
```bash
docker network ls                      # Listează rețelele Docker
docker network create mynetwork        # Creează o rețea personalizată
docker run --network mynetwork myapp   # Rulează un container într-o rețea specifică
docker network inspect mynetwork       # Afișează detalii despre o rețea
```

> 💡 Rețelele conectează containerele între ele, la fel cum un switch conectează calculatoarele.

---

## 🧠 Rezumat general

| Tip obiect | Descriere | Exemple de comenzi |
|-------------|------------|--------------------|
| 🧱 **Image** | Șablonul aplicației | `docker build`, `docker pull`, `docker images` |
| 🚀 **Container** | Instanța activă a imaginii | `docker run`, `docker ps`, `docker stop` |
| 💾 **Volume** | Spațiu de stocare persistent | `docker volume create`, `docker run -v` |
| 🌐 **Network** | Comunicare între containere | `docker network create`, `docker network ls` |

---

## 🧩 Relația dintre obiecte Docker

1. Scrii un **Dockerfile** → construiești o **imagine**.  
2. Din imagine creezi unul sau mai multe **containere**.  
3. Conectezi containerele între ele folosind **rețele**.  
4. Păstrezi datele în **volume**.  

> 🔁 Toate aceste obiecte lucrează împreună pentru a oferi un mediu complet de rulare a aplicațiilor.

---

## ✅ Concluzie

Obiectele Docker sunt elementele fundamentale care fac platforma Docker atât de flexibilă și puternică.  
Prin combinarea imaginilor, containerelor, volumelor și rețelelor, poți construi aplicații izolate, scalabile și portabile, gata să ruleze oriunde.

> 🐳 **Pe scurt:** Imagini → Containere → Rețele + Volume = Aplicație Docker complet funcțională.

---

## 📚 Resurse recomandate
- [Docker Objects Overview](https://docs.docker.com/get-started/overview/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/docker/)
- [Docker Networking](https://docs.docker.com/network/)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
