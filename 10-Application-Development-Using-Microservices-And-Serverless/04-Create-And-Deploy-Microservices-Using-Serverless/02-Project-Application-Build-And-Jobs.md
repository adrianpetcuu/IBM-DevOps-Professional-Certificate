# 🧱 Project, Application, Build și Jobs

## 🔹 Prezentare generală
În **IBM Cloud Code Engine**, conceptele de *Project*, *Application*, *Build* și *Jobs* definesc modul în care resursele sunt organizate, create și executate. Aceste componente lucrează împreună pentru a oferi un flux complet de dezvoltare, implementare și rulare a aplicațiilor fără a gestiona infrastructura manual.

---

## 🧩 Project (Proiect)
- Un **proiect** este unitatea principală de organizare în Code Engine.  
- Fiecare proiect acționează ca un **namespace izolat**, care conține toate resursele legate de o aplicație — aplicații, joburi, build-uri, loguri și secrete.  
- Permite gestionarea resurselor, permisiunilor și costurilor la nivel de proiect.  
- Poți crea și gestiona mai multe proiecte independente.

---

## ⚙️ Application (Aplicație)
- O **aplicație** reprezintă o componentă implementată în Code Engine care rulează ca serviciu web.  
- Poate fi construită:
  - Din **cod sursă**,  
  - Dintr-o **imagine de container**,  
  - Sau dintr-un **build predefinit**.  
- Fiecare aplicație are un endpoint HTTP public (URL) și poate scala automat în funcție de trafic.  
- Scalarea automată se poate face **până la zero** când nu există cereri active.

---

## 🏗️ Build (Construcție)
- Un **build** este procesul de creare a unei imagini de container pornind de la codul sursă.  
- Code Engine suportă două metode principale de build:
  - **Dockerfile** – pentru control complet asupra configurației imaginii.  
  - **Buildpack** – pentru automatizarea procesului fără a scrie un Dockerfile.  
- Build-ul generează o imagine care este stocată într-un **container registry** (ex: IBM Cloud Container Registry).

---

## 🧮 Jobs (Sarcini)
- **Joburile** sunt utilizate pentru a rula sarcini unice (batch) care nu necesită un endpoint web permanent.  
- Exemple: procesare de date, analiză de loguri, sau sarcini programate.  
- Joburile pot rula:
  - **O singură dată**,  
  - Sau pot fi **programate** pentru execuție periodică.  
- Se termină automat după finalizarea execuției.

---

## 🚀 Rezumat
| Componentă | Descriere | Exemple |
|-------------|------------|----------|
| **Project** | Spațiu logic care conține toate resursele | Gestionare costuri, permisiuni |
| **Application** | Serviciu web care răspunde la cereri HTTP | API, site web, microserviciu |
| **Build** | Proces de creare a imaginii container | Dockerfile, Buildpack |
| **Job** | Sarcină unică, fără endpoint HTTP | Batch processing, ETL |

---

## 💡 Concluzie
Prin combinarea acestor concepte, **IBM Cloud Code Engine** oferă o platformă completă pentru dezvoltare, rulare și scalare a aplicațiilor cloud — fără a fi nevoie să gestionezi servere sau infrastructură.

