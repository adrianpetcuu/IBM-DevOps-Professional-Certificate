# 📘 Docker Concepts & Understanding a Dockerfile

## Overview
Acest README rezumă conceptele cheie **Docker** și explică pas cu pas cum să **înțelegi și să scrii un Dockerfile**. După parcurgere, vei ști ce este o imagine, un container, unde sunt stocate imaginile și cum construiești o imagine complet funcțională pentru o aplicație Node.js.

---

## 🔹 Docker Concepts

### Ce este Docker?
**Docker** simplifică procesul de creare, livrare și rulare a aplicațiilor prin **containere**. Un container împachetează aplicația împreună cu dependențele ei într-o unitate standardizată, portabilă și izolată.

### Terminologie esențială
- **Dockerfile** – fișier text cu instrucțiuni pentru **construirea** unei imagini.
- **Image (imagine)** – șablon *read‑only* care conține runtime‑ul și aplicația; din imagini se creează containere.
- **Container** – **instanță rulantă** a unei imagini (un proces izolat pe gazdă), ușoară, portabilă și ideală pentru scalare.
- **Registry** – depozit pentru imagini (public: **Docker Hub**; privat: registre de companie).

### Unde există imaginile Docker?
- **Local** – după `docker build`, imaginea este salvată local. Listezi imaginile cu:
  ```bash
  docker images
  ```
- **Registry** – după build, poți face **push** pentru a o partaja:
  ```bash
  docker push <repo>/<image>:<tag>
  ```

---

## 🔹 Exemplu de Dockerfile (Node.js)
```dockerfile
# Use the official Node.js image as the base image
FROM node:14

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY . .

# Add additional file
ADD public/index.html /app/public/index.html

# Expose the port on which the application will run
EXPOSE $PORT

# Specify the default command to run when the container starts
CMD ["node", "app.js"]

# Labeling the image
LABEL version="1.0"
LABEL description="Node.js application Docker image"
LABEL maintainer="Your Name"

# Healthcheck to ensure the container is running correctly
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -fs http://localhost:$PORT || exit 1

# Set a non-root user for security purposes
USER node
```

> ℹ️ **Notă:** în unele ghiduri vei vedea `WORKDIR /usr/src/app`. Directorul de lucru poate fi oricare (ex. `/app`), important e să fie folosit **constant** în restul instrucțiunilor.

---

## 🔹 Înțelegerea instrucțiunilor din Dockerfile

1. **Specify the Base Image**
   ```dockerfile
   FROM node:14
   ```
   Alege imaginea de bază; aici este imaginea oficială Node.js v14 din registry.

2. **Set Environment Variables**
   ```dockerfile
   ENV NODE_ENV=production
   ENV PORT=3000
   ```
   Definește variabilele de mediu folosite în runtime (modul de execuție, portul aplicației).

3. **Set the Working Directory**
   ```dockerfile
   WORKDIR /app
   ```
   Directorul curent pentru instrucțiunile următoare (`COPY`, `RUN`, `CMD` etc.).

4. **Copy Package Files**
   ```dockerfile
   COPY package*.json ./
   ```
   Copiază `package.json` și `package-lock.json` pentru a permite un layer de cache eficient la instalarea dependențelor.

5. **Install Dependencies**
   ```dockerfile
   RUN npm install --production
   ```
   Rulează comenzi în timpul build-ului; instalează dependențele fără `devDependencies`.

6. **Copy Application Code**
   ```dockerfile
   COPY . .
   ```
   Copiază restul codului aplicației în imagine.

7. **Add Additional File(s)**
   ```dockerfile
   # ADD <source_path> <destination_path>
   ADD public/index.html /app/public/index.html
   ```
   `ADD` poate copia fișiere locale sau extrage arhive. Pentru fișiere simple, `COPY` este de regulă preferat.

8. **Expose the Application Port**
   ```dockerfile
   EXPOSE $PORT
   ```
   Documentează portul pe care ascultă aplicația (folosit de tooling/orchestrare).

9. **Specify the Default Command**
   ```dockerfile
   CMD ["node", "app.js"]
   ```
   Comanda implicită la startul containerului (forma JSON – *exec form* – gestionează corect semnalele OS).

10. **Label the Image**
    ```dockerfile
    LABEL version="1.0"
    LABEL description="Node.js application Docker image"
    LABEL maintainer="Your Name"
    ```
    Metadate utile pentru versionare, audit și căutare.

11. **Add a Healthcheck**
    ```dockerfile
    HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3       CMD curl -fs http://localhost:$PORT || exit 1
    ```
    Verifică starea aplicației; marchează containerul *healthy/unhealthy*.

12. **Set a Non‑Root User**
    ```dockerfile
    USER node
    ```
    Rulează procesul ca utilizator neprivilegiat – bună practică de securitate.

---

## 🔹 Workflow rapid: Build & Run

```bash
# Construiește imaginea
docker build -t mynodeapp:1.0 .

# Rulează containerul (mapare port gazdă:container)
docker run -d -p 3000:3000 --name mynodeapp mynodeapp:1.0

# Verifică
docker ps
curl localhost:3000
```

> Dacă aplicația nu răspunde: asigură-te că serverul Node ascultă pe `0.0.0.0` și că ai mapat portul corect (ex. `-p 3000:3000`).

---

## 🔹 Unde salvez și cum partajez imaginea?

```bash
# Autentificare la Docker Hub
docker login

# Etichetare și push
docker tag mynodeapp:1.0 <username>/mynodeapp:1.0
docker push <username>/mynodeapp:1.0
```

---

## ✅ Rezumat
- **Dockerfile** descrie pașii de build; fiecare instrucțiune creează un *layer* cache‑abil.
- **Image** = pachet *read‑only*; **Container** = proces izolat pornit din imagine.
- Imaginile trăiesc **local** și/sau într‑un **registry**.
- Practici bune: formă JSON la `CMD`, `.dockerignore`, utilizator **non‑root**, `COPY` înainte de `RUN npm install` pentru cache eficient.

---

## 📚 Resurse
- Documentație: https://docs.docker.com/
- Best practices Dockerfile: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Docker Hub: https://hub.docker.com/
