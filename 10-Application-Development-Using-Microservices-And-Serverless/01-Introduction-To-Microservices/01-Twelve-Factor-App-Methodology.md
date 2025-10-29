# 🧩 Metodologia Twelve-Factor App

**Twelve-Factor App** este o metodologie pentru construirea de aplicații moderne, scalabile și ușor de întreținut în medii cloud.  
Ea definește doisprezece principii care ajută dezvoltatorii să creeze aplicații **portabile, reziliente și ușor de implementat** în diferite medii (dezvoltare, test, producție).

---

## ⚙️ 1. Codul sursă (Codebase)
- O singură bază de cod urmărită în controlul versiunilor (ex: Git).  
- Mai multe implementări (staging, producție) pot proveni din același cod sursă.

---

## ⚙️ 2. Dependențe (Dependencies)
- Declară explicit toate dependențele aplicației.  
- Izolează-le de mediul sistemului folosind manageri de pachete (ex: pip, npm, Maven).

---

## ⚙️ 3. Configurația (Config)
- Stochează configurațiile în **variabile de mediu**, nu direct în cod.  
- Permite separarea clară între codul aplicației și mediul în care rulează.

---

## ⚙️ 4. Servicii externe (Backing Services)
- Tratează serviciile externe (baze de date, cozi de mesaje, cache-uri etc.) ca **resurse atașate**.  
- Acestea pot fi înlocuite fără modificări în codul aplicației.

---

## ⚙️ 5. Build, Release, Run
- Separă clar etapele:
  - **Build** – compilarea și pregătirea codului  
  - **Release** – combinarea codului cu configurațiile  
  - **Run** – executarea aplicației  
- Asigură implementări consistente și reproductibile.

---

## ⚙️ 6. Procese (Processes)
- Rulează aplicația ca unul sau mai multe procese **fără stare (stateless)**.  
- Nu se partajează starea între procese — persistarea se face prin servicii externe.

---

## ⚙️ 7. Legarea porturilor (Port Binding)
- Aplicația trebuie să-și expună serviciile prin **porturi proprii**.  
- Nu depinde de un server web extern (ex: Apache, Nginx) — rulează autonom.

---

## ⚙️ 8. Concurența (Concurrency)
- Scalarea aplicației se face prin **multiplicarea proceselor**.  
- Fiecare proces este independent și poate fi reprodus ușor.

---

## ⚙️ 9. Disponibilitatea (Disposability)
- Procesele trebuie să pornească rapid și să se oprească elegant.  
- Asigură o scalare rapidă și implementări fără întreruperi.

---

## ⚙️ 10. Paritatea Dev/Prod (Dev/Prod Parity)
- Mediile de dezvoltare, testare și producție trebuie să fie **cât mai asemănătoare**.  
- Previne problemele cauzate de diferențele dintre medii.

---

## ⚙️ 11. Logurile (Logs)
- Tratează logurile ca **fluxuri de evenimente**.  
- Aplicația nu trebuie să stocheze sau să gestioneze fișiere de log — acestea se trimit la stdout sau către un serviciu extern.

---

## ⚙️ 12. Procese administrative (Admin Processes)
- Rulează sarcinile administrative (ex: migrarea bazei de date, scripturi) ca **procese separate**.  
- Nu le include în execuția normală a aplicației.

---

## 🚀 Rezumat
Metodologia **Twelve-Factor App** promovează:
- **Scalabilitate**
- **Reziliență**
- **Automatizare**
- **Independență de mediu**

Este fundamentul dezvoltării **aplicațiilor cloud-native și DevOps moderne**.

---

📚 *Referință:*  
[https://12factor.net](https://12factor.net)
