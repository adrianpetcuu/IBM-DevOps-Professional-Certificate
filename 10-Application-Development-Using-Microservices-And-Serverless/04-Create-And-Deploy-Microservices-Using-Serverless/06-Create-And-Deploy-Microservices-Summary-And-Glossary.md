# 🎓 Felicitări! Ai finalizat acest modul

În acest punct al cursului, știi că:

---

### 🔹 Concepte cheie

- **Microserviciile găzduite local (self-hosted)** pot fi foarte complexe și dificil de gestionat.  
- **IBM Cloud Code Engine** este o platformă complet gestionată care se ocupă de toate aspectele dificile ale implementării aplicațiilor, permițând dezvoltatorilor să se concentreze pe cod.  
- **IBM Cloud Code Engine** are trei cazuri principale de utilizare:  
  1. Implementarea aplicațiilor (Deploy applications)  
  2. Construirea și implementarea aplicațiilor (Build and deploy applications)  
  3. Rularea joburilor (Run jobs)  
- Un **proiect (project)** este o grupare de entități Code Engine precum aplicații, joburi și build-uri.  
- O **aplicație (application)** rulează codul tău pentru a răspunde la cereri HTTP sau pentru a crea sesiuni WebSocket.  
- Un **build** este procesul prin care se creează o imagine de container din codul sursă.  
- Un **job** rulează una sau mai multe instanțe ale codului executabil.  
- Un **container** este o unitate software executabilă, autonomă, care include toate dependențele necesare.  
- **Docker** este o platformă populară pentru construirea și rularea containerelor.  
- Poți crea un fișier **Dockerfile** pentru a instrui platforma Docker cum să construiască o imagine de container.  
- După ce imaginea containerului este creată, aceasta poate fi **încărcată (push)** într-un **container registry** și ulterior **descărcată (pull)** folosind numele imaginii.  
- Poți crea o aplicație **Cloud Engine** fie dintr-o imagine de container încărcată, fie dintr-un **repository de cod sursă**.  
- În funcție de preferințe, poți alege între:
  - **IBM Cloud Console** – interfață grafică web pentru gestionarea aplicațiilor.  
  - **IBM Cloud CLI** – interfață de linie de comandă pentru implementarea rapidă și controlul avansat al aplicațiilor.  

---

## 📘 Introducere în Microservicii

Microserviciile sunt o abordare modernă de dezvoltare a aplicațiilor, unde o aplicație este împărțită în componente mici, independente, care comunică între ele prin API-uri (de obicei REST sau WebSocket).  
Această arhitectură oferă **scalabilitate**, **reziliență** și **ușurință în actualizare**, fiind ideală pentru mediile cloud.

---

## 🧾 Glosar – Crearea și implementarea microserviciilor

| Termen | Definiție |
|--------|------------|
| **ASGI** | *Asynchronous Server Gateway Interface* – interfață între serverul web și microserviciu pentru apeluri asincrone. |
| **Buildpack** | Conține executabile pentru sarcini precum inspecția codului sursă, crearea unui plan de build și generarea imaginii containerului. |
| **CaaS** | *Containers as a Service* – model de livrare cloud care oferă gestionarea containerelor. |
| **Code Engine** | Simplifică procesul de construire, implementare și gestionare a aplicațiilor, astfel încât dezvoltatorii să se concentreze pe scrierea codului. |
| **Container** | Unitate software autonomă și executabilă, care include toate librăriile, dependențele și runtime-urile necesare. |
| **Container image** | Fișier imutabil care conține toate resursele aplicației (cod, librării, dependențe). |
| **Docker** | Platformă software pentru construirea și rularea aplicațiilor ca și containere. |
| **Dockerfile** | Fișier text care conține toate comenzile pentru construirea unei imagini Docker. |
| **IBM Cloud CLI** | Interfață de linie de comandă pentru gestionarea serviciilor IBM Cloud. |
| **IBM Cloud Console** | Portal web intuitiv pentru administrarea serviciilor IBM Cloud, inclusiv Code Engine. |
| **Job** | Rulează o singură dată codul executabil și apoi se închide. |
| **PaaS** | *Platform as a Service* – model cloud care oferă o platformă completă pentru dezvoltare și implementare. |
| **Repository** | Grup de imagini de container înrudite. |
| **TCP** | *Transmission Control Protocol* – protocol de transport pentru comunicații de rețea fiabile. |
| **TLS** | *Transport Layer Security* – protocol de securitate pentru comunicații criptate. |
| **WebSocket** | Protocol de comunicare bidirecțional bazat pe TCP. |
| **WSGI** | *Web Server Gateway Interface* – standard Python pentru comunicarea dintre servere web și aplicații web/microservicii. |

---

## 💡 Concluzie
După parcurgerea acestui modul, ai învățat cum să construiești, implementezi și rulezi microservicii folosind **IBM Cloud Code Engine**.  
Dezvoltatorii pot beneficia de **automatizare completă**, **scalare dinamică**, **eficiență în costuri** și **implementări rapide**, fără a se ocupa direct de gestionarea infrastructurii.
  