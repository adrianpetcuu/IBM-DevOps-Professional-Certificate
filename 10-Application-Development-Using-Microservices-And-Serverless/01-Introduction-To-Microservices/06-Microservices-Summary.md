# 🏁 Felicitări! Ai finalizat acest modul

În acest moment al cursului, știi deja următoarele concepte esențiale:

---

## 🧠 Cunoștințe dobândite

- Dezvoltarea software modernă presupune adesea livrarea de **aplicații centralizate, bazate pe web, oferite ca servicii (SaaS – Software as a Service)**.

- **Metodologia Twelve-Factor App** îi ajută pe dezvoltatori să creeze aplicații SaaS **mai eficiente, scalabile și ușor de întreținut**.

- Cei **12 factori** se aliniază cu cele trei etape principale ale ciclului de livrare software:
  - **Codificare (Code)**
  - **Implementare (Deploy)**
  - **Operare (Operate)**

- **Microserviciile** transformă fiecare componentă a aplicației într-un **serviciu independent**, iar serviciile comunică între ele prin **API-uri**.

- Microserviciile permit fiecărui component al aplicației să folosească **stack-uri tehnologice diferite** (de exemplu: Java pentru un serviciu, Python pentru altul).

- Arhitectura cu microservicii permite **scalarea individuală** a componentelor, în funcție de cererea utilizatorilor.

- Microserviciile **reduc riscurile** asociate schimbărilor, deoarece fiecare componentă poate fi actualizată sau iterată independent.

- Eșecurile dintr-un serviciu **nu afectează neapărat** funcționarea celorlalte servicii.

- Există însă și **anti-modele (anti-patterns)** care trebuie evitate atunci când construim microservicii, pentru a preveni complexitatea excesivă și problemele operaționale.

---

# 📘 Glosar – Prezentare generală Microservicii (M1: Glossary – Microservices Overview)

| Termen | Definiție |
|--------|------------|
| **Build (Construcție)** | O unitate executabilă a aplicației (cod compilat și pregătit pentru implementare). |
| **BFF (Backend for Frontend)** | Model arhitectural în care fiecare tip de interfață (web, mobil etc.) are propriul backend dedicat. |
| **Configurație (Configuration)** | Tot ceea ce poate diferi între implementări sau medii (de ex: chei API, adrese servere, baze de date). |
| **Variabile de mediu (Environment variables)** | Permit modificarea configurațiilor între medii fără a schimba codul sursă. |
| **Scalare orizontală (Horizontal scaling)** | Scalarea prin adăugarea de noi instanțe de resurse — numită și “scalare pe orizontală” sau “scaling out”. |
| **Microservicii (Microservices)** | O aplicație unică este compusă din mai multe servicii mici, independente și slab cuplate, implementabile separat. |
| **Aplicație monolitică (Monolithic application)** | Conține toată sau cea mai mare parte a funcționalității într-un singur proces. |
| **Etapa de release (Release stage)** | Combină codul construit cu configurația curentă a mediului de implementare, pregătind aplicația pentru rulare. |
| **Etapa de rulare (Run stage)** | Reprezintă faza în care aplicația este efectiv executată. |
| **SaaS (Software as a Service)** | Model de livrare software în care aplicațiile sunt găzduite central și accesate prin internet. |
| **SPA (Single Page Application)** | Aplicație web care se actualizează dinamic fără reîncărcarea completă a paginii. |
| **SOA (Service-Oriented Architecture)** | Arhitectură bazată pe servicii reutilizabile care comunică între ele prin protocoale standard. |
| **Strangler Pattern** | Model care ajută la refactorizarea unei aplicații monolitice în etape, înlocuind gradual părțile vechi. |
| **Service Discovery Pattern** | Permite aplicațiilor și serviciilor să se descopere automat între ele într-un mediu distribuit. |
| **TLS (Transport Layer Security)** | Protocol de securitate care asigură criptarea comunicației între aplicații și servicii. |

---

## 🧭 Concluzie

Prin învățarea acestor concepte:
- Ai înțeles diferențele dintre **Monolit, SOA și Microservicii**.  
- Știi cum se aplică **Metodologia Twelve-Factor App** în dezvoltarea aplicațiilor cloud-native.  
- Poți identifica **modelele (patterns)** și **anti-modelele (anti-patterns)** esențiale în proiectarea microserviciilor moderne.  

Ești acum pregătit să treci la următorul modul din cursul **IBM DevOps Engineering – Application Development using Microservices and Serverless** 🚀

---

📚 *Referințe utile:*  
- [IBM Cloud – Microservices Overview](https://www.ibm.com/cloud/learn/microservices)  
- [The Twelve-Factor App](https://12factor.net)  
- [Microservices.io – Patterns & Practices](https://microservices.io)
