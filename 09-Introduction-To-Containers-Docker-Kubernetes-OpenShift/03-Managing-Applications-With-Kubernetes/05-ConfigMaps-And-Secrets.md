# ☸️ Kubernetes ConfigMaps și Secrets 

## 🧭 Ce sunt ConfigMaps și Secrets

În Kubernetes, **ConfigMaps** și **Secrets** sunt resurse folosite pentru a **gestiona separat configurația aplicațiilor** de codul sursă.  
Acest lucru permite modificarea valorilor de configurare fără a fi nevoie să refaci imaginea containerului sau să redeployezi complet aplicația.

| Resursă | Scop | Tip de date |
|----------|------|--------------|
| **ConfigMap** | Stochează date de configurare nesensibile (ex: fișiere de configurare, variabile de mediu, URL-uri, porturi) | Text simplu |
| **Secret** | Stochează date sensibile (ex: parole, token-uri, chei SSH) | Codificat/criptat (Base64) |

---

## 🧱 1️⃣ ConfigMaps

### 🧠 Ce este un ConfigMap
Un **ConfigMap** conține perechi cheie-valoare folosite pentru a configura aplicațiile.  
Este ideal pentru variabile care se pot schimba între medii (development, staging, production).

### 🧩 Exemplu YAML – ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: "production"
  APP_DEBUG: "false"
  DATABASE_URL: "mysql://db-service:3306"
```

### 🔍 Explicație:
- `APP_ENV`, `APP_DEBUG`, `DATABASE_URL` sunt variabile de configurare.
- Acestea pot fi folosite de aplicație sub formă de variabile de mediu.

### 💡 Cum se folosește un ConfigMap într-un Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
  - name: myapp
    image: nginx
    envFrom:
    - configMapRef:
        name: app-config
```

📘 Rezultat: toate variabilele definite în `app-config` devin disponibile în containerul aplicației.

---

## 🔒 2️⃣ Secrets

### 🧠 Ce este un Secret
Un **Secret** funcționează similar cu un ConfigMap, dar este conceput pentru a păstra **informații confidențiale** precum:

- parole de baze de date  
- token-uri API  
- chei de autentificare  
- certificate TLS  

### 🧩 Exemplu YAML – Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
data:
  username: YWRtaW4=     # "admin" codificat Base64
  password: cGFzc3dvcmQ= # "password" codificat Base64
```

### 💡 Cum se folosește un Secret într-un container

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  containers:
  - name: webapp
    image: nginx
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
```

📘 Rezultat: variabilele de mediu `DB_USER` și `DB_PASS` devin disponibile în container.

---

## 🧩 Alternativ: Montarea ConfigMap/Secret ca fișier

Atât ConfigMap cât și Secret pot fi montate ca fișiere în container.

### Exemplu:

```yaml
volumes:
- name: config-volume
  configMap:
    name: app-config

volumeMounts:
- name: config-volume
  mountPath: /etc/config
```

🔹 În acest caz, conținutul ConfigMap este disponibil în fișiere din `/etc/config`.

---

## 🧠 ConfigMap vs Secret

| Caracteristică | **ConfigMap** | **Secret** |
|-----------------|----------------|-------------|
| Scop | Date nesensibile (config) | Date sensibile (parole, chei) |
| Stocare | Text simplu | Codificat Base64 |
| Acces | Variabile de mediu / fișiere | Variabile de mediu / fișiere |
| Securitate | Public | Privată / restricționată |
| Tipuri | Generic | Opaque, TLS, Docker registry |
| Exemplu de utilizare | `DATABASE_URL`, `APP_MODE` | `DB_PASSWORD`, `API_KEY` |

---

## ⚙️ Comenzi utile

| Acțiune | Comandă |
|----------|----------|
| Creare ConfigMap din fișier | `kubectl create configmap app-config --from-file=config.env` |
| Creare ConfigMap din variabile | `kubectl create configmap app-config --from-literal=APP_ENV=prod` |
| Creare Secret din variabile | `kubectl create secret generic db-secret --from-literal=username=admin --from-literal=password=pass123` |
| Verificare ConfigMaps | `kubectl get configmaps` |
| Verificare Secrets | `kubectl get secrets` |
| Detalii despre un ConfigMap | `kubectl describe configmap app-config` |
| Detalii despre un Secret | `kubectl describe secret db-secret` |

---

## 🧩 Recomandări de bune practici

✅ Separă configurațiile de codul aplicației  
✅ Evită hardcodarea datelor sensibile în imagini Docker  
✅ Folosește **Secrets** pentru toate informațiile confidențiale  
✅ Montează ConfigMaps/Secrets ca fișiere dacă aplicația așteaptă fișiere de configurare  
✅ Utilizează un manager extern de secrete (ex: HashiCorp Vault, AWS Secrets Manager) pentru medii enterprise

---

## 🚀 Concluzie

> În Kubernetes, **ConfigMaps** și **Secrets** sunt instrumente cheie pentru gestionarea dinamică și sigură a configurațiilor aplicațiilor.

- **ConfigMap** → pentru date de configurare neconfidențiale  
- **Secret** → pentru informații sensibile  

Ambele contribuie la **securitatea, flexibilitatea și scalabilitatea** aplicațiilor dintr-un cluster Kubernetes.

> 🔹 Pe scurt: *ConfigMaps = configurare; Secrets = securitate.*
