# 📘 Software Architecture, Design and Modeling

## 1. Introduction to Software Architecture
Software Architecture reprezintă structura de bază a unui sistem software și modul în care componentele sale interacționează.

### 🔹 Definiție
- Arhitectura software definește **componentele majore ale sistemului**, relațiile dintre ele și principiile de proiectare.  
- Este echivalentul „planului arhitectural” din construcția unei clădiri.

### 🔹 Obiective
- **Scalabilitate:** sistemul poate crește odată cu numărul de utilizatori.  
- **Fiabilitate:** funcționare corectă în condiții variate.  
- **Securitate:** protejarea datelor și comunicațiilor.  
- **Performanță:** răspuns rapid și eficient.  
- **Ușurință în întreținere:** posibilitatea de a actualiza și extinde sistemul.  

### 🔹 Exemple de arhitecturi
- **2-Tier (Client–Server):** aplicații simple cu client și server.  
- **3-Tier:** strat de prezentare, strat de aplicație, strat de bază de date.  
- **Microservices:** servicii mici, independente, care comunică între ele.  
- **Event-driven:** reacționează la evenimente externe (ex: ride-sharing apps).  
- **Peer-to-peer:** nodurile acționează atât ca server, cât și ca client (ex: blockchain).  

---

## 2. Software Design and Modeling
Designul software este procesul de **traducere a cerințelor** într-o structură tehnică clară, care să poată fi implementată și testată.

### 🔹 Software Design
- Reprezintă planul detaliat al sistemului.  
- Include decizii despre **structuri de date, algoritmi, interfețe și fluxuri logice**.  

### 🔹 Software Modeling
- Folosește **diagrame vizuale** pentru a reprezenta structura și comportamentul sistemului.  
- Instrumente principale: **UML (Unified Modeling Language)** și **ERD (Entity-Relationship Diagrams)**.  

### 🔹 Tipuri de modele
- **Structural Models:** arată organizarea componentelor (ex: UML Class Diagrams).  
- **Behavioral Models:** arată cum se comportă sistemul (ex: UML State Diagrams, Sequence Diagrams).  
- **Interaction Models:** descriu interacțiunea utilizatorilor cu sistemul (ex: Use Case Diagrams).  

### 🔹 Beneficii
- Claritate și comunicare mai bună în echipă.  
- Documentație reutilizabilă și ușor de întreținut.  
- Identificarea problemelor înainte de implementare.  

---

## 3. Object-Oriented Analysis and Design (OOAD)
OOAD este o metodologie ce combină **analiza** și **designul** folosind concepte de programare orientată pe obiecte.

### 🔹 Object-Oriented Analysis (OOA)
- Analizează cerințele și le modelează prin **obiecte** și **relațiile dintre ele**.  
- Identifică entitățile (ex: Pacient, Doctor, Programare) și comportamentele lor.  

### 🔹 Object-Oriented Design (OOD)
- Transformă analiza în **plan de implementare**.  
- Definește **clase, metode, atribute și interacțiuni**.  
- Aplica principiile OOP:  
  - **Encapsulation (încapsulare):** ascunderea detaliilor interne.  
  - **Inheritance (moștenire):** reutilizarea codului.  
  - **Polymorphism (polimorfism):** flexibilitate prin metode comune cu implementări diferite.  

### 🔹 Beneficii ale OOAD
- Reutilizarea componentelor software.  
- Reducerea complexității prin modelare orientată pe obiecte.  
- Cod mai ușor de întreținut și extins.  

---

## 📌 Concluzie
- **Software Architecture** definește structura de ansamblu și asigură scalabilitate, performanță și securitate.  
- **Software Design and Modeling** oferă planul detaliat și vizualizări pentru implementare corectă.  
- **OOAD** aduce o abordare orientată pe obiecte pentru analiză și design, facilitând dezvoltarea modulară și clară.
