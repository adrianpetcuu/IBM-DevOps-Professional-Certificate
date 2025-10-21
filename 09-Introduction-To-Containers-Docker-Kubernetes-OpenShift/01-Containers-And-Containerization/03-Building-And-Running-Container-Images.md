# 🏗️ Building and Running Container Images

## 📖 Overview
Această lecție explică procesul de **construire** (building) și **rulare** (running) a imaginilor Docker, adică pașii prin care o aplicație devine un container funcțional.  
Prin acest proces, înveți cum se creează o imagine dintr-un `Dockerfile` și cum se rulează un container pe baza acelei imagini.

---

## 🧱 Ce este o imagine Docker?

O **imagine Docker** este un șablon (template) care conține tot codul, fișierele și dependențele necesare pentru a rula o aplicație într-un container.  
Imaginile sunt **read-only** și pot fi refolosite pentru a crea mai multe containere identice.

> 💡 Imaginea este ca o „rețetă”, iar containerul este „mâncarea gătită” după acea rețetă.

---

## ⚙️ Cum se construiește o imagine

Pentru a crea o imagine, ai nevoie de un fișier numit **Dockerfile**, care conține instrucțiuni pas cu pas pentru configurarea mediului de rulare al aplicației.

### 🧩 Exemplu simplu de Dockerfile:
```Dockerfile
# Folosește o imagine de bază oficială
FROM python:3.11

# Copiază fișierul aplicației în container
COPY app.py /app/

# Definește comanda care pornește aplicația
CMD ["python", "/app/app.py"]
```

### 🔧 Construirea imaginii:
```bash
docker build -t myapp .
```
Explicație:
- `docker build` → creează o imagine nouă pe baza Dockerfile-ului.
- `-t myapp` → denumește imaginea „myapp”.
- `.` → indică directorul curent unde se află Dockerfile-ul.

Rezultat: o imagine locală numită **myapp**.

---

## 🚀 Cum se rulează o imagine (crearea unui container)

După ce imaginea este creată, o poți rula într-un container activ:
```bash
docker run -p 8080:80 myapp
```
Explicație:
- `docker run` → creează și pornește un container din imagine.
- `-p 8080:80` → mapează portul 80 din container la portul 8080 pe calculatorul tău.
- `myapp` → numele imaginii.

➡️ Rezultatul: aplicația ta rulează în izolare și este accesibilă prin `localhost:8080`.

---

## 🔍 Verificarea containerelor active

Pentru a vedea containerele care rulează:
```bash
docker ps
```
Pentru a opri un container:
```bash
docker stop <container_id>
```

Pentru a porni un container oprit:
```bash
docker start <container_id>
```

---

## 🧰 Fluxul complet de lucru Docker

1. ✍️ Scrii un **Dockerfile**.  
2. 🏗️ Construiești o **imagine** cu `docker build`.  
3. 🚀 Rulezi un **container** cu `docker run`.  
4. 🔎 Verifici containerele cu `docker ps`.  
5. 🛑 Oprești sau ștergi containerele după utilizare.  

---

## 📦 Exercițiu practic (exemplu complet)

```bash
# 1. Construiește imaginea
docker build -t hello-world .

# 2. Rulează containerul
docker run -d -p 8080:80 hello-world

# 3. Verifică rularea
docker ps

# 4. Accesează aplicația
curl localhost:8080

# 5. Oprește containerul
docker stop <container_id>
```

---

## 🧠 Recomandări utile

- Folosește nume clare pentru imagini (`mywebapp:v1`).  
- Adaugă etichete (tags) pentru versiuni.  
- Nu include fișiere inutile în imagine (folosește `.dockerignore`).  
- Testează imaginea local înainte de a o trimite într-un registry (ex: Docker Hub).

---

## ✅ Concluzie

Construirea și rularea imaginilor Docker reprezintă baza containerizării.  
Odată ce o imagine este creată, ea poate fi distribuită și rulată oriunde, fără modificări.  

> 🐳 **Rezumat:** Scrii un Dockerfile → Construiești imaginea → Rulezi containerul → Aplicația funcționează identic pe orice sistem.

---

## 📚 Resurse utile
- [Docker Build Reference](https://docs.docker.com/engine/reference/commandline/build/)
- [Docker Run Reference](https://docs.docker.com/engine/reference/commandline/run/)
- [Best Practices for Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
