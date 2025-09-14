# ⚡ Serverless Computing

## 📌 Definiție
**Serverless computing** este un model de calcul în cloud unde responsabilitățile legate de **provizionarea, gestionarea și scalarea serverelor** sunt preluate de furnizorul de cloud.  
Dezvoltatorii scriu doar codul (funcții sau servicii), iar cloud-ul îl rulează **on-demand**, facturând doar pentru resursele consumate.

---

## ⚙️ Caracteristici cheie
- **Fără servere gestionate manual** → infrastructura este ascunsă de dezvoltatori.  
- **Execuție on-demand** → codul se execută doar când este apelat.  
- **Scalare automată** → crește sau scade numărul de execuții în funcție de trafic.  
- **Plătești doar ce consumi** → billing per request și resurse utilizate.  
- **Event-driven** → declanșat de evenimente (HTTP request, mesaj într-o coadă, încărcare fișier).  

---

## ✅ Avantaje
- **Focus pe cod**: developerii se concentrează pe logica aplicației, nu pe infrastructură.  
- **Cost redus**: nu plătești resurse idle, doar execuțiile efective.  
- **Scalabilitate automată**: cloud-ul scalează în funcție de cerere.  
- **Timp rapid de lansare**: ideal pentru prototipuri și MVP-uri.  

---

## ⚠️ Provocări
- **Cold starts**: prima execuție după o pauză poate fi mai lentă.  
- **Limitări de runtime**: funcțiile rulează cu resurse limitate și timp maxim de execuție.  
- **Vendor lock-in**: fiecare furnizor are propriile implementări (AWS Lambda, Azure Functions).  
- **Debugging/observabilitate** mai dificilă în medii distribuite.  

---

## 📌 Exemple de utilizare
- **Procesare imagini**: la încărcarea unei poze, un serverless function o redimensionează și o salvează.  
- **API-uri simple**: endpoint-uri REST fără nevoie de server dedicat.  
- **Procesare evenimente**: loguri, notificări, mesaje dintr-o coadă.  
- **Automatizare DevOps**: scripturi care rulează când apare un commit nou în GitHub.  

---

## 🛠️ Servicii Serverless populare
- **AWS Lambda**  
- **Azure Functions**  
- **Google Cloud Functions**  
- **IBM Cloud Functions (OpenWhisk)**  

---

## 🏷️ Concluzie
**Serverless computing** schimbă modul în care sunt dezvoltate aplicațiile:  
- dezvoltatorii scriu doar cod,  
- furnizorul de cloud gestionează infrastructura,  
- plătești doar pentru ceea ce rulează.  

Este ideal pentru **aplicații event-driven, API-uri, prototipuri și workload-uri cu trafic variabil**.

