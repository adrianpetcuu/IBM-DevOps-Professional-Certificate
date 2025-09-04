# 🔐 Secure Networking in Cloud

## 📌 Ce este networking-ul securizat în cloud?
Networking-ul în cloud reprezintă conexiunile dintre resursele cloud (VMs, containere, storage, baze de date) și utilizatori.  
Pentru a asigura **confidențialitatea, integritatea și disponibilitatea datelor**, securitatea rețelei este esențială.

---

## 🌐 Elemente cheie de rețelistică în cloud
1. **Virtual Private Cloud (VPC)**  
   - O rețea privată izolată în cadrul cloud-ului public.  
   - Permite segmentarea resurselor în **subnet-uri publice și private**.  

2. **Subnets (subrețele)**  
   - Zone logice în rețea unde se aplică politici de securitate.  
   - Subnet-urile private protejează resursele critice de accesul direct din internet.  

3. **Firewalls și Security Groups**  
   - Controlează traficul de intrare și ieșire pe baza de reguli.  
   - Previn accesul neautorizat.  

4. **Load Balancers**  
   - Distribuie traficul între instanțe multiple.  
   - Asigură disponibilitate și reziliență.  

5. **VPN (Virtual Private Network)**  
   - Creează o conexiune securizată criptată între rețeaua locală și cloud.  

6. **Encryption (Criptare)**  
   - Criptarea traficului de rețea (TLS/SSL).  
   - Criptarea datelor stocate (at rest) și transmise (in transit).  

---

## ✅ Practici de securitate în networking-ul cloud
- Segmentează aplicațiile pe **mai multe nivele** (multi-tier apps).  
- Folosește **subnet-uri private** pentru baze de date și backend.  
- Activează **monitorizare și logging** pentru trafic suspect.  
- Aplică **principiul celui mai mic privilegiu** pentru accesul la rețea.  
- Utilizează **IDS/IPS (Intrusion Detection/Prevention Systems)** pentru protecție împotriva atacurilor.  

---

## 🛠️ Exemple de utilizare
- **E-commerce** → zona publică pentru site-ul web, zona privată pentru baze de date cu date de card.  
- **Bănci** → VPN + subrețele private pentru tranzacții securizate.  
- **Companii globale** → folosesc load balancers și criptare pentru aplicații accesibile la nivel mondial.  

---

## 📝 Concluzie
Networking-ul securizat în cloud este esențial pentru protejarea resurselor și a datelor.  
Prin folosirea de **VPC-uri, subrețele, firewall-uri, load balancere, VPN și criptare**, organizațiile pot construi un mediu cloud sigur, scalabil și rezilient.
