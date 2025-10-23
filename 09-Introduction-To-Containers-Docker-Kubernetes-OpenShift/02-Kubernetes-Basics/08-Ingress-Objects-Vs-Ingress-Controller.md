# 🌐 Ingress Objects vs. Ingress Controller în Kubernetes

În Kubernetes, accesul extern la serviciile dintr-un cluster este gestionat prin **Ingress**, care este compus din două elemente esențiale:

- **Obiectul Ingress (Ingress Object)**
- **Controllerul Ingress (Ingress Controller)**

Aceste două componente lucrează împreună pentru a permite rutarea traficului HTTP/HTTPS către serviciile interne ale clusterului.

---

## 🔹 Ingress Objects

**Ingress** acționează ca un supraveghetor al accesului extern, expunând rute din afara clusterului către serviciile interne.  
Scopul principal este gestionarea traficului **HTTP** și **HTTPS**.

### ✅ Funcționalități principale:
- Definește **reguli de rutare** pentru traficul extern.
- Permite expunerea serviciilor cu **URL-uri accesibile extern**.
- Poate efectua **echilibrarea traficului** (load balancing).
- Asigură **terminarea SSL/TLS**.
- Oferă **virtual hosting bazat pe nume** (name-based virtual hosting).

> ⚠️ Pentru protocoale non-HTTP/HTTPS (de exemplu TCP sau UDP), se folosesc alte tipuri de servicii precum:
> - `Service.Type=NodePort`
> - `Service.Type=LoadBalancer`

---

## 🔹 Ingress Controllers

Pe partea operațională, **Ingress Controller** este componenta care **implementează regulile** definite de obiectul Ingress.  
Spre deosebire de alte controllere (care rulează automat în Kubernetes), un Ingress Controller trebuie **instalat și activat explicit** pentru ca resursele Ingress să funcționeze.

### ✅ Roluri principale:
- Interpretează și aplică regulile definite în obiectul Ingress.
- Utilizează un **load balancer** sau configurează **front-end-uri** pentru a gestiona traficul de intrare.
- Este responsabil pentru **execuția efectivă** a rutării traficului.

Exemple populare de Ingress Controllers:
- **NGINX Ingress Controller**
- **Traefik**
- **HAProxy**
- **Kubernetes Gateway API Controller** (noua generație)

---

## 🔸 Tabel Comparativ

| Caracteristică | **Ingress Objects** | **Ingress Controllers** |
|-----------------|---------------------|--------------------------|
| **Definiție** | Obiect API care gestionează accesul extern la servicii | Resursă din cluster care implementează regulile definite de Ingress |
| **Funcția principală** | Reglează rutarea accesului extern | Aplică regulile și direcționează efectiv traficul |
| **Sursa configurației** | Reguli definite în resursa Ingress | Citește și procesează informațiile din obiectul Ingress |
| **Gestionarea traficului** | Rutează traficul HTTP și HTTPS | Configurează load balancerul / front-end-urile pentru trafic |
| **Activare** | Activ automat odată cu definirea resursei Ingress | Necesită instalare și activare explicită în cluster |
| **Protocoale gestionate** | Doar HTTP și HTTPS | Poate implementa reguli și pentru alte protocoale și porturi |
| **Pornire automată** | Activă la configurare | Trebuie pornit explicit în cluster |
| **Analogie** | Set de reguli pentru trafic | Executorul regulilor (ex: instanța NGINX care aplică regulile) |

---

## 🧩 Concluzie

În Kubernetes, gestionarea accesului extern la servicii implică colaborarea dintre **Ingress Object** și **Ingress Controller**:

- **Ingress Object** definește **regulile de rutare** pentru traficul HTTP/HTTPS.  
- **Ingress Controller** le **implementează** în mod efectiv în cluster, utilizând mecanisme de load balancing și configurare de front-end.

👉 Înțelegerea modului în care aceste două componente interacționează este esențială pentru o **administrare eficientă a accesului extern** în Kubernetes.

---

## 🧱 Exemplu practic – Ingress + Service

Mai jos este un exemplu simplu de configurare a unui **Ingress Object** pentru un serviciu numit `my-app`, utilizând un **NGINX Ingress Controller**.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app
                port:
                  number: 80
  tls:
    - hosts:
        - myapp.example.com
      secretName: myapp-tls
```

### Explicații:
- `kubernetes.io/ingress.class: "nginx"` — indică faptul că acest Ingress va fi gestionat de **NGINX Ingress Controller**.
- `rules` — definește regulile de rutare a traficului către serviciul intern `my-app`.
- `tls` — specifică configurarea SSL/TLS pentru domeniul expus.

---

## 📘 Resurse utile
- [Documentația oficială Kubernetes – Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Ghid de instalare NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/)
- [Gateway API – succesorul Ingress](https://gateway-api.sigs.k8s.io/)

---
