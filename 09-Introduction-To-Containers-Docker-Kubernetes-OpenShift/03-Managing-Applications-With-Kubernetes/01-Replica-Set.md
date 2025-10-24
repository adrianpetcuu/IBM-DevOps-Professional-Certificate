# ☸️ Kubernetes ReplicaSet 

## 🧭 Ce este un ReplicaSet
Un **ReplicaSet** este un obiect din Kubernetes care asigură că un **număr specificat de Pods** rulează permanent într-un cluster.  
Dacă un Pod este șters sau cade, ReplicaSet-ul creează automat unul nou pentru a menține numărul dorit de instanțe.

Scopul principal al unui ReplicaSet este **disponibilitatea continuă** a aplicației.

---

## ⚙️ Cum funcționează
ReplicaSet monitorizează în permanență starea aplicației și compară:

> ✅ *Starea dorită* (definită în YAML – câte Pods ar trebui să existe)  
> ⚙️ *Starea actuală* (câte Pods există efectiv în cluster)

Dacă există o diferență, ReplicaSet creează sau șterge Pods pentru a aduce sistemul la starea dorită.

---

## 🧩 Structura unui ReplicaSet
Un fișier YAML pentru ReplicaSet conține 4 secțiuni principale:

1. `apiVersion` – versiunea API Kubernetes (de ex. `apps/v1`)  
2. `kind` – tipul obiectului, în acest caz `ReplicaSet`  
3. `metadata` – informații descriptive (nume, etichete)  
4. `spec` – specificațiile ReplicaSet-ului, cum ar fi:
   - `replicas`: numărul de copii dorite  
   - `selector`: criteriul de identificare a Pods-urilor gestionate  
   - `template`: șablonul pentru crearea Pods noi

---

## 🧱 Exemplu YAML – ReplicaSet NGINX

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

### 🔍 Explicație:
- Creează un ReplicaSet numit **nginx-replicaset**
- Rulează **3 Pods** bazate pe imaginea `nginx:latest`
- Fiecare Pod are eticheta `app=nginx`
- Dacă un Pod moare → ReplicaSet îl recreează automat

---

## ⚡ Comenzi utile Kubernetes

| Acțiune | Comandă |
|----------|----------|
| Creare ReplicaSet | `kubectl apply -f nginx-replicaset.yaml` |
| Verificare ReplicaSets | `kubectl get replicasets` sau `kubectl get rs` |
| Verificare Pods gestionate | `kubectl get pods -l app=nginx` |
| Scalare manuală | `kubectl scale rs nginx-replicaset --replicas=5` |
| Ștergere ReplicaSet | `kubectl delete rs nginx-replicaset` |

---

## 🔄 Relația cu Deployments
De obicei, **nu creezi ReplicaSets manual**, ci Kubernetes le creează automat atunci când definești un **Deployment**.

Exemplu:
```bash
kubectl create deployment nginx --image=nginx --replicas=3
```
➡️ Creează:
- un **Deployment**
- un **ReplicaSet** automat
- și 3 **Pods** active

---

## ⚙️ ReplicaSet vs. ReplicationController

| Diferență | ReplicaSet | ReplicationController |
|------------|-------------|------------------------|
| Versiune | Nou (apps/v1) | Vechi (core/v1) |
| Selector | `matchLabels`, `matchExpressions` | Doar `matchLabels` |
| Utilizare | Folosit de Deployments | Învechit, rar folosit |

✅ ReplicaSet este versiunea modernă și mai puternică a ReplicationController.

---

## 🧠 Pe scurt

| Concept | Explicație |
|----------|------------|
| **Rol** | Asigură că un număr fix de Pods sunt mereu în funcțiune |
| **Creează** | Pods pe baza unui șablon (`template`) |
| **Reacționează** | La erori, eliminări sau căderi de Pods |
| **Folosit de** | Deployment-uri Kubernetes |
| **Beneficiu** | Menține stabilitatea și disponibilitatea aplicației |

---

## 🚀 Concluzie
ReplicaSet este un mecanism esențial în Kubernetes care garantează **reziliență și disponibilitate** pentru aplicații.  
El este „gardianul” care veghează ca numărul de Pods să rămână exact cel specificat, indiferent de erori sau restarturi.

> 🔹 Pe scurt: *ReplicaSet = Asigurarea că aplicația ta e mereu disponibilă.*
