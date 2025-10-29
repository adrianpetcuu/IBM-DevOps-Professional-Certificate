# 🧩 Modele de Arhitectură pentru Microservicii (Microservices Patterns)

## 🔹 Introducere
Într-o arhitectură bazată pe microservicii, aplicația este împărțită în **servicii independente** care comunică prin API-uri.  
Pentru a proiecta, implementa și scala eficient aceste servicii, se folosesc anumite **modele (patterns)** care abordează provocările comune legate de integrare, comunicare, consistență a datelor, disponibilitate și monitorizare.

---

## 🧱 1. API Gateway Pattern
### 🔸 Descriere
Un **API Gateway** acționează ca **punct unic de intrare** pentru toate cererile către microservicii.  
El gestionează rutarea, autentificarea, agregarea răspunsurilor și limitarea traficului.

### ✅ Avantaje
- Simplifică comunicarea dintre client și microservicii.  
- Poate aplica politici comune de securitate și autentificare.  
- Reduce numărul de apeluri directe către servicii interne.

### ⚠️ Dezavantaje
- Devine un punct critic de eșec (single point of failure).  
- Necesită mentenanță suplimentară.  

---

## 🧩 2. Database per Service Pattern
### 🔸 Descriere
Fiecare microserviciu are **baza sa de date proprie**, pentru a asigura independența completă și izolarea datelor.  
Acest model previne dependențele între servicii la nivel de stocare.

### ✅ Avantaje
- Serviciile pot evolua independent.  
- Evită blocajele cauzate de schema comună de date.  

### ⚠️ Dezavantaje
- Gestionarea consistenței datelor devine mai complexă.  
- Necesită implementarea unor mecanisme de sincronizare (ex: Saga Pattern).

---

## 🔄 3. Saga Pattern
### 🔸 Descriere
**Saga Pattern** gestionează tranzacțiile distribuite între mai multe microservicii.  
În loc de o tranzacție unică (ca în monolit), fiecare serviciu efectuează propria acțiune și trimite un eveniment pentru a continua fluxul în celelalte servicii.

### ✅ Avantaje
- Menține consistența datelor între microservicii.  
- Scalabilitate și fiabilitate mai bune.  

### ⚠️ Dezavantaje
- Implementare complexă.  
- Dificil de gestionat în cazul erorilor în lanț.

---

## 🔁 4. Event Sourcing Pattern
### 🔸 Descriere
În loc să actualizeze direct starea bazei de date, aplicația salvează **o secvență de evenimente** care descriu modificările.  
Starea finală se reconstruiește prin reexecutarea evenimentelor.

### ✅ Avantaje
- Istoric complet al modificărilor.  
- Ușor de auditat și de restaurat starea.  

### ⚠️ Dezavantaje
- Necesită spațiu de stocare suplimentar.  
- Reconstrucția stării poate fi costisitoare.

---

## 🧠 5. CQRS Pattern (Command Query Responsibility Segregation)
### 🔸 Descriere
Separă **operațiile de scriere (Command)** de cele de **citire (Query)**, fiecare având propria bază de date optimizată.  
Se folosește adesea împreună cu *Event Sourcing*.

### ✅ Avantaje
- Performanță ridicată la citire.  
- Scalabilitate independentă între citiri și scrieri.  

### ⚠️ Dezavantaje
- Crește complexitatea arhitecturii.  
- Poate apărea latență între actualizare și afișarea datelor.

---

## 🧩 6. Strangler Fig Pattern
### 🔸 Descriere
Permite **migrarea graduală** a unei aplicații monolitice către microservicii.  
Componentele noi sunt dezvoltate ca microservicii, iar cele vechi sunt eliminate treptat.

### ✅ Avantaje
- Permite modernizarea fără oprirea sistemului.  
- Risc minim de întrerupere.  

### ⚠️ Dezavantaje
- Perioadă de tranziție îndelungată.  
- Dublă mentenanță temporară.

---

## 🔧 7. Service Discovery Pattern
### 🔸 Descriere
Într-un sistem cu multe microservicii dinamice, *Service Discovery* permite găsirea automată a serviciilor disponibile.  
Se poate realiza printr-un **registru centralizat** (ex: Consul, Eureka, etc.).

### ✅ Avantaje
- Rutează automat cererile către instanțele disponibile.  
- Suportă scalarea automată și înlocuirea instanțelor.  

### ⚠️ Dezavantaje
- Adaugă un strat suplimentar de complexitate.  

---

## 🔒 8. Circuit Breaker Pattern
### 🔸 Descriere
Protejează aplicația de eșecurile în lanț atunci când un microserviciu nu răspunde.  
Circuitul „se deschide” când numărul de erori depășește un prag și blochează temporar apelurile ulterioare.

### ✅ Avantaje
- Previne supraîncărcarea sistemului.  
- Îmbunătățește stabilitatea generală.

### ⚠️ Dezavantaje
- Poate introduce întârzieri în reluarea conexiunilor.  

---

## 📊 Rezumat rapid

| Model | Scop principal | Beneficiu cheie |
|--------|----------------|-----------------|
| **API Gateway** | Gestionarea cererilor externe | Control centralizat și securitate |
| **Database per Service** | Izolare a datelor | Independență completă |
| **Saga** | Coordonarea tranzacțiilor | Consistență distribuită |
| **Event Sourcing** | Înregistrarea tuturor schimbărilor | Trasabilitate completă |
| **CQRS** | Separarea citirilor de scrieri | Performanță și scalabilitate |
| **Strangler Fig** | Migrare graduală | Modernizare fără downtime |
| **Service Discovery** | Localizare automată a serviciilor | Scalabilitate automată |
| **Circuit Breaker** | Prevenirea erorilor în lanț | Stabilitate și reziliență |

---

## 🏁 Concluzie

Modelele pentru microservicii ajută la:
- Gestionarea **complexității arhitecturii distribuite**  
- Asigurarea **scalabilității și rezilienței**  
- Implementarea **DevOps și CI/CD** eficiente  
- Reducerea riscului de erori și downtime  

Aplicarea acestor *patterns* este esențială pentru proiectarea sistemelor **cloud-native** moderne.

---

📚 *Referințe:*  
- [Microservices.io – Patterns](https://microservices.io/patterns)  
- [IBM Cloud – Microservices Patterns](https://www.ibm.com/cloud/architecture/architectures/microservices)
