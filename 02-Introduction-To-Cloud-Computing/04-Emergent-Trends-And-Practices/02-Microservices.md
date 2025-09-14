# 🧩 Arhitectura pe Microservicii

## 📌 Definiție
Arhitectura pe **microservicii** este o abordare de dezvoltare software în care o aplicație este construită ca o colecție de **servicii mici, independente**, care comunică între ele prin API-uri standard (de obicei REST sau gRPC).  
Fiecare microserviciu rulează și poate fi scalat **independent**, având responsabilitate clară pentru o anumită funcționalitate.

---

## ⚙️ Caracteristici cheie
- **Loosely coupled** → fiecare serviciu este slab cuplat, nu depinde strâns de altele.  
- **Independent deployable** → poate fi lansat, actualizat sau înlocuit separat.  
- **Own database** → fiecare microserviciu își gestionează propria bază de date (evitând blocajele între echipe).  
- **Resilient** → căderea unui microserviciu nu afectează întreaga aplicație.  
- **Polyglot** → echipele pot folosi limbaje diferite (Java, Python, Go) pentru microservicii diferite.  

---

## ✅ Avantaje
- **Scalare flexibilă**: doar serviciile cu trafic mare sunt scalate, nu întreaga aplicație.  
- **Dezvoltare rapidă**: echipe diferite pot lucra pe microservicii separate.  
- **Ușurință la mentenanță**: mai simplu să actualizezi un serviciu mic decât o aplicație monolitică.  
- **Adoptare CI/CD**: microserviciile se pretează la pipeline-uri automate de test și deploy.  

---

## ⚠️ Provocări
- **Complexitate operațională**: ai zeci sau sute de microservicii de monitorizat.  
- **Comunicare inter-servicii**: trebuie gestionată (API Gateway, Service Mesh).  
- **Observabilitate**: loguri, metrics și tracing distribuit sunt obligatorii.  
- **Date distribuite**: consistency și tranzacții între microservicii pot fi complicate.  

---

## 📌 Exemple de utilizare
- **E-commerce**:  
  - `Catalog Service` → gestionează produsele.  
  - `Cart Service` → coșul de cumpărături.  
  - `Payment Service` → plăți online.  
  - `User Service` → utilizatori și autentificare.  

- **Streaming (Netflix, Spotify)**: fiecare microserviciu gestionează un aspect (recomandări, player, autentificare, billing).  

---

## 🛠️ Tehnologii folosite
- **Containere & Orchestrare**: Docker, Kubernetes, OpenShift.  
- **API Gateway**: Kong, NGINX, Istio.  
- **CI/CD**: Jenkins, GitHub Actions, GitLab CI, ArgoCD.  
- **Observabilitate**: Prometheus, Grafana, ELK Stack, OpenTelemetry.  

---

## 🏷️ Concluzie
Arhitectura pe **microservicii** oferă **scalabilitate, flexibilitate și viteză de dezvoltare**, dar introduce **complexitate** în management și observabilitate.  
Este preferată de companiile moderne care doresc să livreze rapid funcționalități noi și să scaleze doar ce este necesar.

