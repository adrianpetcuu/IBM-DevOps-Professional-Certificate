# 📘 Application Architecture and Deployment

## 1. Approaches to Application Architecture
Aplicațiile software pot fi proiectate folosind mai multe abordări arhitecturale, în funcție de complexitatea sistemului și cerințele de scalabilitate.

### 🔹 Tipuri de abordări
- **Monolithic Architecture**
  - Toate funcționalitățile sunt într-o singură aplicație.
  - Avantaje: simplă, ușor de implementat inițial.
  - Dezavantaje: greu de scalat, dificil de întreținut.

- **Layered Architecture (N-Tier)**
  - Împarte aplicația în straturi: prezentare, logică, date.
  - Ușor de întreținut și de testat.
  - Folosită des în aplicații enterprise.

- **Microservices Architecture**
  - Aplicația este împărțită în servicii mici, independente.
  - Avantaje: scalabilitate, independență, flexibilitate.
  - Dezavantaje: complexitate mare în gestionarea comunicației și a infrastructurii.

- **Event-Driven Architecture**
  - Componentele reacționează la evenimente.
  - Exemplu: aplicații de ride-sharing unde o acțiune (cerere) declanșează o reacție (alocarea șoferului).

- **Serverless Architecture**
  - Rulează funcții în cloud fără a gestiona servere.
  - Cost-eficient și scalabil, dar depinde de providerul cloud.

---

## 2. Architectural Patterns in Software
Modelele arhitecturale sunt soluții reutilizabile pentru probleme comune din proiectarea aplicațiilor.

### 🔹 Tipuri principale
- **2-Tier Architecture**
  - Client–Server.
  - Exemplu: aplicații simple de mesagerie.

- **3-Tier Architecture**
  - Prezentare – Aplicație – Bază de date.
  - Exemplu: aplicații web cu interfață, logică și DB separate.

- **Event-Driven Pattern**
  - Bazat pe producători și consumatori de evenimente.
  - Exemplu: aplicații de ridesharing, streaming.

- **Peer-to-Peer (P2P)**
  - Nodurile acționează atât ca servere, cât și ca clienți.
  - Exemplu: blockchain, torrenting, criptomonede.

- **Microservices Pattern**
  - Servicii independente care colaborează prin API-uri.
  - Exemplu: aplicații e-commerce cu servicii separate pentru plăți, produse, livrări.

---

## 3. Application Deployment Environments
Un sistem software este testat și lansat în mai multe medii, fiecare cu un rol specific.

### 🔹 Tipuri de medii
- **Development Environment**
  - Folosit de programatori pentru a scrie și testa cod.
  - Include tool-uri de debugging și librării de dezvoltare.

- **Testing / QA Environment**
  - Folosit pentru a valida cerințele și a testa funcționalități.
  - Se concentrează pe bug-uri și performanță.

- **Staging Environment**
  - Copie aproape identică a producției.
  - Teste finale înainte de lansare pentru a simula condiții reale.

- **Production Environment**
  - Mediul real în care aplicația este accesată de utilizatori.
  - Include monitorizare, securitate și optimizare pentru încărcare mare.

---

## 4. Production Deployment Components
Pentru a asigura scalabilitatea și disponibilitatea aplicației în producție, sunt utilizate mai multe componente cheie.

### 🔹 Componente principale
- **Load Balancer**
  - Distribuie traficul între servere multiple.
  - Previne supraîncărcarea unui singur server.

- **Web Servers**
  - Servesc conținut static (HTML, CSS, JS).
  - Exemplu: Apache, Nginx.

- **Application Servers**
  - Rulează logica aplicației și gestionează cererile complexe.
  - Exemplu: Tomcat, Node.js.

- **Database Servers**
  - Stochează și gestionează datele aplicației.
  - Pot fi replici pentru disponibilitate ridicată (High Availability DB Replica).

- **Firewall & Security**
  - Protejează aplicația de atacuri și acces neautorizat.

### 🔹 Beneficii
- Fiabilitate și disponibilitate ridicată.
- Performanță îmbunătățită prin distribuirea sarcinii.
- Scalabilitate prin adăugarea de servere noi.
