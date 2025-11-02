# 🔄 Updating Deployed Applications

## 🔹 Prezentare generală
După ce o aplicație a fost implementată în **IBM Cloud Code Engine**, este posibil să fie necesar să o actualizezi pentru a adăuga noi funcționalități, a corecta erori sau a schimba configurațiile.  
Procesul de actualizare este simplificat și nu necesită oprirea completă a serviciului, permițând **implementări fără întreruperi** (zero downtime).

---

## ⚙️ Motive pentru actualizare
Actualizările pot include:
- Modificarea codului sursă sau a versiunii imaginii containerului.
- Schimbarea variabilelor de mediu sau a secretelor.
- Ajustarea setărilor de scalare.
- Actualizarea resurselor alocate aplicației (CPU, memorie, etc.).

---

## 🧱 Actualizarea aplicației prin CLI
Pentru a actualiza o aplicație existentă, se folosește comanda:

```bash
ibmcloud ce app update --name myapp --image us.icr.io/my-namespace/myapp:v2
```

Această comandă:
- Înlocuiește imaginea curentă cu cea nouă.
- Rulează o **implementare graduală (rolling update)**.
- Menține aplicația disponibilă în timpul procesului.

Dacă ai modificat doar o variabilă de mediu:
```bash
ibmcloud ce app update --name myapp --env DEBUG=true
```

---

## 🧩 Actualizarea prin interfața grafică (UI)
1. Accesează **IBM Cloud Console → Code Engine → Applications**.  
2. Selectează aplicația pe care dorești să o actualizezi.  
3. Modifică imaginea, variabilele sau resursele.  
4. Apasă **Deploy Revision** pentru a lansa noua versiune.

---

## 🔄 Actualizări fără întreruperi (Zero Downtime)
Code Engine gestionează tranziția între versiuni automat.  
- Noua versiune este lansată treptat.  
- Traficul este redirecționat progresiv către noua versiune.  
- Vechea versiune este eliminată doar după confirmarea funcționării corecte.

Acest proces se numește **Rolling Deployment**.

---

## 🧰 Verificarea actualizării
După actualizare, poți verifica starea aplicației:

```bash
ibmcloud ce app get --name myapp
```

Exemplu de ieșire:
```
Name:           myapp
Status:         Ready
Image:          us.icr.io/my-namespace/myapp:v2
Revision:       myapp-00002
URL:            https://myapp.us-south.codeengine.appdomain.cloud
```

Pentru a verifica versiunile implementate:
```bash
ibmcloud ce revision list --app myapp
```

---

## 🧪 Testarea noii versiuni
După implementarea noii versiuni:
1. Accesează URL-ul aplicației.  
2. Rulează un test API (ex: Postman sau cURL):  
   ```bash
   curl -X GET "https://myapp.us-south.codeengine.appdomain.cloud/version"
   ```
3. Confirmă că răspunsul indică noua versiune a aplicației.

---

## 🧠 Recomandări de bune practici
- Folosește **versionare semantică** (ex: v1.0.1 → v1.0.2).  
- Testează local înainte de a actualiza aplicația live.  
- Automatizează procesul de update prin **CI/CD pipelines**.  
- Monitorizează performanța noii versiuni imediat după implementare.  
- Utilizează rollback în caz de erori majore.

Exemplu rollback:
```bash
ibmcloud ce app update --name myapp --image us.icr.io/my-namespace/myapp:v1
```

---

## 💡 Concluzie
Actualizarea aplicațiilor implementate în **IBM Cloud Code Engine** este un proces simplu, sigur și automatizat.  
Platforma gestionează tranziția între versiuni fără întreruperi, oferind o metodă eficientă de **livrare continuă (Continuous Delivery)** și **menținere a disponibilității aplicațiilor**.
