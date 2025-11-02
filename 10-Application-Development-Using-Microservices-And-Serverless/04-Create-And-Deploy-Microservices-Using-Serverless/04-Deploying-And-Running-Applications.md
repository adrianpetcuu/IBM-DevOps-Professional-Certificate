# 🚀 Deploying and Running Applications

## 🔹 Prezentare generală
După construirea imaginilor de container pentru microservicii, următorul pas este **implementarea (deployment)** și **rularea (runtime)** acestora într-un mediu cloud gestionat, cum ar fi **IBM Cloud Code Engine**.  
Scopul este de a rula aplicații scalabile, fără a te ocupa de infrastructura de bază.

---

## ⚙️ Procesul de implementare
Implementarea unei aplicații containerizate presupune următorii pași:

1. **Pregătirea imaginii containerului**
   - Imaginea trebuie încărcată într-un **Container Registry** (ex: IBM Cloud Container Registry).
   - Asigură-te că este accesibilă pentru Code Engine.

2. **Crearea unei aplicații în Code Engine**
   - Se definește numele aplicației, sursa imaginii și variabilele de mediu.
   - Poți face acest lucru prin **CLI** sau **UI**.

Exemplu CLI:
```bash
ibmcloud ce app create --name myapp --image us.icr.io/my-namespace/myapp:v1 --registry-secret myregistry
```

3. **Testarea aplicației implementate**
   - Odată implementată, aplicația primește un **URL public**.
   - Poți verifica rularea acesteia accesând linkul generat.

Exemplu:
```bash
https://myapp.us-south.codeengine.appdomain.cloud
```

---

## 🧩 Rularea aplicației
Aplicațiile implementate în **Code Engine** rulează în containere gestionate automat.  
Caracteristici cheie:

- **Scalare automată** – aplicația se adaptează la numărul de cereri primite.  
- **Plată pe utilizare** – plătești doar pentru resursele consumate în timpul execuției.  
- **Fără management de servere** – infrastructura este complet abstractizată.

---

## 🧱 Moduri de rulare a aplicațiilor
Există mai multe moduri de rulare în Code Engine:

| Tip rulare | Descriere | Exemplu utilizare |
|-------------|------------|------------------|
| **Application** | Serviciu web scalabil expus prin HTTP | API-uri, aplicații web |
| **Job** | Execuție unică sau batch fără endpoint HTTP | Procesare date, ETL |
| **Build** | Crearea automată a imaginii container | Continuous Integration |

---

## 🧰 Verificarea stării aplicației
Poți verifica starea aplicației folosind CLI:

```bash
ibmcloud ce app get --name myapp
```

Exemplu de răspuns:
```
Name:           myapp
Status:         Ready
URL:            https://myapp.us-south.codeengine.appdomain.cloud
Scale:          1 → 5
Image:          us.icr.io/my-namespace/myapp:v1
```

---

## 🧪 Testarea aplicației
După implementare, poți testa aplicația:
- Accesând **URL-ul public** al aplicației.
- Folosind **curl** din linia de comandă:
  ```bash
  curl -X GET "https://myapp.us-south.codeengine.appdomain.cloud"
  ```
- Sau testând endpoint-urile API în **Postman**.

---

## 🚀 Beneficii
- Rulare complet automatizată fără gestionarea serverelor.  
- Scalare instantanee în funcție de cerere.  
- Integrare cu **CI/CD pipelines**.  
- Izolare completă între aplicații.  
- Costuri optimizate prin modelul **pay-per-use**.

---

## 💡 Concluzie
Implementarea și rularea aplicațiilor în **IBM Cloud Code Engine** elimină complexitatea managementului infrastructurii.  
Dezvoltatorii se pot concentra exclusiv pe **scrierea codului** și **livrarea rapidă** a funcționalităților, în timp ce platforma gestionează automat scalarea, disponibilitatea și costurile.
