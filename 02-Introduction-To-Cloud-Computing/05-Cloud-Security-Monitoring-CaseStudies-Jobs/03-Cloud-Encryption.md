# 🔐 Cloud Encryption

**Cloud Encryption** este procesul prin care datele stocate sau transferate în cloud sunt transformate într-un format criptat, astfel încât să nu poată fi citite de utilizatori neautorizați.  

---

## 📌 Cum funcționează?
1. **Algoritmi de criptare**  
   - Datele sunt transformate folosind algoritmi matematici (ex: AES-256, RSA).  
   - Rezultatul este un text criptat (ciphertext), imposibil de înțeles fără cheia corectă.  

2. **Chei de criptare (Encryption Keys)**  
   - **Cheie de criptare**: folosită pentru a transforma datele în ciphertext.  
   - **Cheie de decriptare**: folosită pentru a restaura datele originale.  
   - Cheile sunt stocate și gestionate prin servicii de tip **KMS (Key Management Service)**.  

3. **Procese implicate**  
   - **Criptare la rest (At Rest)** – protejează datele stocate pe serverele cloud.  
   - **Criptare în tranzit (In Transit)** – protejează datele în mișcare între utilizatori și cloud, folosind protocoale ca TLS/SSL.  
   - **Criptare în uz (In Use)** – protejează datele chiar și atunci când sunt procesate, prin tehnologii avansate ca confidential computing.  

---

## 🛡️ Beneficiile Cloud Encryption
- **Confidențialitate** – doar utilizatorii autorizați pot accesa datele.  
- **Protecție împotriva scurgerilor de date** – chiar dacă un hacker obține date criptate, acestea sunt inutile fără cheie.  
- **Conformitate** – respectă cerințele legale și standardele (GDPR, HIPAA, PCI-DSS).  
- **Încredere** – clienții și partenerii au mai multă siguranță privind protecția datelor.  

---

## 📊 Exemple de utilizare
- O companie stochează date financiare criptate în **AWS S3** folosind **AWS KMS**.  
- În **Google Cloud**, datele stocate în **BigQuery** sunt criptate implicit cu chei gestionate de Google.  
- În **Microsoft Azure**, organizațiile pot folosi **Azure Key Vault** pentru a controla și roti cheile de criptare.  

---

## ✅ Concluzie
Criptarea în cloud este esențială pentru securitatea datelor moderne. Ea asigură că informațiile sensibile rămân confidențiale, protejate și accesibile doar persoanelor autorizate, chiar și în cazul unor atacuri sau breșe de securitate.
