# 🚫 Anti-modele pentru Microservicii (Microservices Anti-Patterns)

## 🔹 Introducere
Deși există multe modele care ajută la implementarea corectă a microserviciilor, există la fel de multe **anti-modele** — practici greșite care pot duce rapid o echipă de dezvoltare în dificultate.  

Mai jos sunt prezentate câteva dintre **lucrurile pe care NU ar trebui să le faci** atunci când dezvolți aplicații bazate pe microservicii.

---

## ❌ 1. Nu începe direct cu microservicii

**Prima regulă a microserviciilor:** *nu începe cu microservicii*.  

Atunci când complexitatea unei aplicații monolitice începe să afecteze dezvoltarea și mentenanța, abia atunci merită să iei în considerare **refactorizarea** aplicației în servicii mai mici.  

Când aplicația devine prea mare pentru a fi actualizată și întreținută ușor, **microserviciile** devin soluția ideală pentru a reduce complexitatea și a face sistemul mai ușor de gestionat.

👉 Până când nu ajungi să „simți durerea” complexității, **nu ai încă un monolit care necesită refactorizare**.

---

## ⚙️ 2. Neacordarea atenției necesare automatizării

Într-o aplicație monolitică, ai de implementat doar o singură componentă.  
Dar într-o arhitectură bazată pe microservicii, ai **mai multe aplicații independente**, fiecare cu propriul cod, teste și ciclu de implementare.

A încerca să dezvolți microservicii **fără:**

- un sistem de **automatizare a implementării și monitorizării**, sau  
- **servicii cloud gestionate** care să susțină infrastructura ta eterogenă  

înseamnă a te expune la o mulțime de probleme inutile.

✅ Când dezvolți microservicii, **folosește întotdeauna practici DevOps** și servicii cloud pentru automatizare.

---

## 🧩 3. Nu construi „nanoservicii”

Dacă exagerezi cu partea „micro” din *microservicii*, riști să ajungi să construiești **nanoservicii** — atât de mici încât complexitatea lor depășește beneficiile arhitecturii microserviciilor.

Este mai bine să începi cu **servicii mai mari**, pe care să le subdivizi doar atunci când:

- implementarea modificărilor devine dificilă;  
- modelul comun de date devine prea complex;  
- cerințele de încărcare și scalare diferă și afectează performanța aplicației.  

---

## 🏗️ 4. Nu transforma proiectul într-un SOA

Conceptele de **Microservicii** și **Arhitectură orientată pe servicii (SOA)** sunt adesea confundate, deoarece ambele implică **crearea de componente reutilizabile**.  

Diferența este că:
- microserviciile sunt **fine-grained** (de granularitate fină),  
- iar fiecare are **propria stocare de date independentă** (bounded context).  

Dacă un proiect bazat pe microservicii ajunge să semene cu un SOA clasic, el va deveni rapid **greoi și dificil de întreținut**.

---

## 🔌 5. Nu construi un gateway pentru fiecare serviciu

În loc să implementezi în fiecare microserviciu funcții precum:
- autentificare,  
- control al ratei (throttling),  
- orchestrare,  
- transformare,  
- rutare,  
- colectare de analitice,  

folosește un **API Gateway** centralizat.

Un **API Gateway** este un instrument de management API care acționează ca intermediar între client și colecția de servicii backend.  
Astfel, toate aceste aspecte „non-funcționale” (securitate, rutare, logging etc.) sunt gestionate într-un singur loc, fără a le reimplementa în fiecare serviciu.

---

## 🧭 Concluzie

Scopul arhitecturii bazate pe **microservicii** este de a rezolva trei provocări majore:
1. îmbunătățirea experienței utilizatorului,  
2. flexibilitatea față de cerințele noi,  
3. reducerea costurilor prin oferirea funcționalităților de business sub formă de servicii mici și independente.  

Însă, pentru a obține aceste beneficii, trebuie să **eviți anti-modelele** de mai sus, care pot transforma microserviciile dintr-un avantaj într-un obstacol pentru dezvoltare, livrare și mentenanță.

---

📚 *Referințe:*  
- [IBM Cloud – Microservices Best & Anti-Patterns](https://www.ibm.com/cloud/architecture/architectures/microservices)
- [Microservices.io – Anti-Patterns](https://microservices.io/patterns/antipatterns.html)
