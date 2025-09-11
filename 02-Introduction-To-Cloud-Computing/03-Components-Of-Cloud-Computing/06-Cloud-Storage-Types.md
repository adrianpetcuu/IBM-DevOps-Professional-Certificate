# Cloud Storage Types

Acest document explică principalele tipuri de stocare în Cloud: **File Storage**, **Block Storage** și **Object Storage**.

---

## 1. File Storage
### Descriere
- Stocare organizată ierarhic, similară cu un sistem de fișiere tradițional (foldere și fișiere).
- Accesată prin protocoale standard precum **NFS (Network File System)** sau **SMB (Server Message Block)**.
- Permite mai multor instanțe să acceseze simultan aceleași fișiere.

### Cazuri de utilizare
- Partajare de fișiere între aplicații.
- Medii enterprise unde mai multe servere accesează aceleași date.
- Sisteme de management al conținutului (CMS), aplicații media, arhivare documente.

### Avantaje
- Ușor de utilizat și familiar.
- Ideal pentru scenarii unde este nevoie de acces partajat.

### Limitări
- Scalabilitate mai mică față de Object Storage.
- Performanța depinde de rețeaua de acces.

---

## 2. Block Storage
### Descriere
- Împarte datele în **blocuri de dimensiuni fixe**, fiecare cu un identificator unic.
- Este prezentat mașinii de calcul ca un **disc virtual**.
- Oferă latență foarte mică și viteză mare de citire/scriere.

### Cazuri de utilizare
- Baze de date care necesită acces rapid și consistent la disc.
- Aplicații enterprise cu tranzacții frecvente.
- Medii virtualizate și servere de aplicații.

### Avantaje
- Performanță ridicată, aproape de nivelul stocării fizice.
- Ideal pentru aplicații critice care cer viteză.

### Limitări
- De obicei poate fi atașat la o singură instanță de calcul.
- Costuri mai mari decât File și Object Storage.

---

## 3. Object Storage
### Descriere
- Datele sunt stocate ca **obiecte** (fișiere + metadate + identificator unic).
- Acces prin **API-uri REST** (de exemplu S3 API).
- Scalabilitate virtual nelimitată.

### Cazuri de utilizare
- Backup și arhivare pe termen lung.
- Conținut static pentru aplicații web sau mobile.
- Stocarea de fișiere media mari (imagini, video, loguri).

### Avantaje
- Scalabilitate infinită, plătești doar pentru cât utilizezi.
- Suportă metadate avansate pentru organizare și căutare.
- Disponibilitate și durabilitate ridicate.

### Limitări
- Viteză mai mică de citire/scriere față de Block Storage.
- Nu este potrivit pentru rularea sistemelor de operare sau bazelor de date.

---

## 🔑 Concluzie
- **File Storage** → partajare fișiere între aplicații și utilizatori.  
- **Block Storage** → performanță ridicată pentru baze de date și aplicații critice.  
- **Object Storage** → capacitate nelimitată pentru backup, arhivare și conținut static.  
