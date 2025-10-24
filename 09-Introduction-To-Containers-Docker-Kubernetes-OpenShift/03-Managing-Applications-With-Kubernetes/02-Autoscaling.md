# ☸️ Kubernetes Autoscaling 

## 🧭 Ce este Autoscaling
**Autoscaling** în Kubernetes înseamnă capacitatea sistemului de a **mări sau micșora automat** resursele disponibile (Pods, noduri, CPU etc.) în funcție de încărcare.  
Scopul este să mențină performanța aplicațiilor, dar să reducă și costurile atunci când sarcina scade.

---

## ⚙️ Tipuri principale de autoscaling în Kubernetes

Kubernetes oferă **trei tipuri majore de autoscaling**:

| Tip | Ce scalează | Descriere |
|------|--------------|-----------|
| **HPA (Horizontal Pod Autoscaler)** | Numărul de Pods | Adaugă sau elimină Pods în funcție de încărcare (CPU, memorie, metrici). |
| **VPA (Vertical Pod Autoscaler)** | Resursele unui Pod | Ajustează automat CPU și RAM pentru Pods existente. |
| **CA (Cluster Autoscaler)** | Numărul de noduri | Adaugă sau elimină noduri (mașini de lucru) în funcție de nevoile clusterului. |

---

## 🔹 1️⃣ Horizontal Pod Autoscaler (HPA)

### 🧠 Ce face
Monitorizează valorile de utilizare a resurselor (CPU, RAM etc.) pentru aplicații și ajustează numărul de Pods pentru a menține un nivel de performanță constant.

Exemplu: dacă media utilizării CPU depășește 70%, HPA adaugă mai multe Pods; dacă scade, elimină unele.

---

### 🧩 Exemplu YAML – HPA

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 🔍 Explicație:
- Rulează între **2 și 10 Pods**
- Ținta de utilizare CPU este **70%**
- Dacă depășește această valoare, HPA creează noi Pods

---

### ⚙️ Comenzi utile:

| Acțiune | Comandă |
|----------|----------|
| Creare HPA | `kubectl apply -f nginx-hpa.yaml` |
| Vizualizare HPA | `kubectl get hpa` |
| Detalii despre metrici | `kubectl describe hpa nginx-hpa` |

📌 Pentru ca HPA să funcționeze, trebuie instalat **Metrics Server** în cluster.

---

## 🔹 2️⃣ Vertical Pod Autoscaler (VPA)

### 🧠 Ce face
**VPA** ajustează automat valorile `resources.requests` și `resources.limits` pentru un Pod existent, în funcție de consumul real de resurse.

Util pentru aplicații care **nu pot fi scalate pe orizontală** (ex: procese unice sau batch jobs).

### ⚠️ Atenție:
- Poate reporni Pods pentru a aplica noile valori.  
- Nu se folosește simultan cu HPA (pe aceleași metrici).

---

## 🔹 3️⃣ Cluster Autoscaler (CA)

### 🧠 Ce face
**Cluster Autoscaler** acționează la nivelul nodurilor (mașini fizice sau virtuale).  
Dacă nu există suficiente resurse pentru a lansa un Pod nou, adaugă un nod.  
Dacă unele noduri sunt idle (nefolosite), le elimină automat.

Funcționează perfect în cloud (AWS, GCP, Azure, IBM Cloud), dar și on-premise.

---

## 🧩 Cum lucrează împreună cele trei mecanisme

| Nivel | Tip Autoscaler | Rol |
|--------|----------------|------|
| Pod | **HPA** | Ajustează numărul de Pods |
| Pod | **VPA** | Ajustează resursele fiecărui Pod |
| Nod | **CA** | Ajustează numărul de noduri din cluster |

### 🧠 Exemplu de scenariu:
1. Traficul crește → CPU > 70%  
2. **HPA** adaugă Pods noi.  
3. Nu există resurse → **CA** adaugă un nod nou.  
4. Când traficul scade → HPA elimină Pods, CA închide nodurile idle.

---

## ⚡ Avantajele Autoscaling-ului

✅ Scalare automată în funcție de încărcare  
✅ Fără intervenție manuală  
✅ Menține performanța constantă  
✅ Optimizează costurile de infrastructură  
✅ Funcționează în orice tip de cluster Kubernetes

---

## 🧠 Pe scurt

| Tip | Nivel | Ce face | Beneficiu |
|------|-------|----------|------------|
| **HPA** | Pod | Ajustează numărul de Pods | Scalare automată fără downtime |
| **VPA** | Pod | Ajustează CPU/RAM pentru Pods | Eficiență resurse |
| **CA** | Cluster | Ajustează numărul de noduri | Optimizare costuri și performanță |

---

## 🚀 Concluzie

Autoscaling este o componentă esențială a Kubernetes care permite aplicațiilor să **se adapteze automat la cerere**, păstrând echilibrul între performanță și cost.  

> 🔹 HPA → scalează pe orizontală (mai multe Pods)  
> 🔹 VPA → scalează pe verticală (mai multe resurse pentru Pods)  
> 🔹 CA → scalează infrastructura (numărul de noduri)

Astfel, Kubernetes oferă o **scalabilitate inteligentă și dinamică**, ideală pentru aplicațiile moderne DevOps și cloud-native.
