# ⚠️ Antipattern-uri în Kubernetes

În Kubernetes, identificarea și evitarea **antipattern-urilor** este esențială pentru menținerea unui mediu de orchestrare a containerelor robust și stabil.  
Aceste practici greșite pot părea eficiente la început, dar duc adesea la complicații operaționale, instabilitate și probleme de mentenanță.  

Acest ghid prezintă **zece antipattern-uri frecvente** din Kubernetes și oferă **recomandări de bune practici** pentru o implementare mai sigură și sustenabilă.

---

## 1. ❌ Nu încorpora configurația în imaginile containerelor

### Problemă
Containerele oferă avantajul utilizării unei imagini consistente de-a lungul procesului de producție.  
Totuși, atunci când imaginile conțin artefacte dependente de mediu (IP-uri hardcodate, parole, prefixe specifice), apar probleme care necesită reconstruirea imaginilor și duc la riscuri de versiuni netestate în producție.

### ✅ Bună practică
Creează **imagini generice**, independente de configurări specifice mediului.  
Folosește fișiere de configurare, variabile de mediu sau volume montate pentru a gestiona diferențele între medii.

---

## 2. ⚙️ Separă implementarea aplicației de cea a infrastructurii

### Problemă
Utilizarea unei singure pipeline pentru implementarea atât a infrastructurii, cât și a aplicației, duce la pierderi de timp și resurse, mai ales când aplicația se schimbă mai des decât infrastructura.

### ✅ Bună practică
Separă pipeline-urile: una pentru **infrastructură (IaC)** și alta pentru **aplicație**.  
Astfel optimizezi procesele și reduci riscul de interferență între etapele de livrare.

---

## 3. 🚫 Nu impune o ordine strictă de pornire a serviciilor

### Problemă
În Kubernetes, componentele pornesc simultan, nu în ordine fixă.  
Dacă aplicația depinde de disponibilitatea unei alte componente (ex: bază de date) și nu gestionează întârzieri, pot apărea blocaje sau căderi de poduri.

### ✅ Bună practică
Adoptă o arhitectură **rezilientă la eșecuri temporare**.  
Implementează mecanisme de retry, timeouts și fallback pentru servicii dependente.

---

## 4. 💾 Setează limite de memorie și CPU pentru poduri

### Problemă
Fără limite de resurse, o aplicație poate consuma întregul cluster, afectând alte servicii.

### ✅ Bună practică
Definește **limite și cerințe (requests & limits)** pentru CPU și memorie la fiecare container.  
Testează comportamentul aplicației pentru a găsi echilibrul optim între performanță și stabilitate.

---

## 5. 🏷️ Evită utilizarea tag-ului „latest” în producție

### Problemă
Folosirea tag-ului `latest` poate cauza restarturi neașteptate și imposibilitatea identificării rapide a versiunii problematice.

### ✅ Bună practică
Folosește **tag-uri de versiune clare și semnificative**, ideal conținând data și ora build-ului.  
Menține **imaginile imutabile**, stochează datele în volume persistente și evită modificările post-deployment.

---

## 6. 🧩 Separă mediile de producție și non-producție

### Problemă
Un singur cluster pentru toate mediile poate duce la probleme de securitate și conflicte între resurse.

### ✅ Bună practică
Menține **cel puțin două clustere**: unul pentru producție și unul pentru testare/dezvoltare.  
Astfel previi interferențele și crești izolare și siguranța datelor.

---

## 7. 🚫 Nu face modificări ad-hoc cu `kubectl edit` sau `kubectl patch`

### Problemă
Modificările directe în resursele clusterului duc la **configurații divergente (configuration drift)** între medii, complicând mentenanța și reproducerea mediilor.

### ✅ Bună practică
Efectuează toate modificările prin **GitOps**, cu commit-uri în controlul de versiune.  
Astfel păstrezi un istoric clar, poți recrea mediile și faci rollback ușor.

---

## 8. 🩺 Implementează verificări de sănătate (`liveness` și `readiness` probes)

### Problemă
Lipsa verificărilor de sănătate poate face ca serviciile defecte să rămână active, în timp ce verificări prea complexe pot cauza restarturi inutile.

### ✅ Bună practică
Definește **probe simple și eficiente** pentru fiecare container:
- `livenessProbe` pentru a detecta și reporni containere blocate;
- `readinessProbe` pentru a semnala disponibilitatea serviciului înainte de primirea traficului.

---

## 9. 🔐 Gestionează corect secretele și folosește un vault

### Problemă
Includerea secretelor direct în imagine sau folosirea mai multor metode de gestionare complică dezvoltarea și testarea.

### ✅ Bună practică
Adoptă o **strategie unificată pentru gestionarea secretelor**, de preferat cu un sistem dedicat precum **HashiCorp Vault**.  
Transmite secretele containerelor la runtime, prin volume sau variabile de mediu, și nu le stoca în cod.

---

## 10. 🧠 Folosește controllere și evită mai multe procese per container

### Problemă
Podurile singure nu oferă durabilitate sau auto-rescheduling.  
Rularea mai multor procese în același container complică managementul și recuperarea în caz de eroare.

### ✅ Bună practică
Folosește **Deployment**, **Job** sau **StatefulSet** pentru orchestrare.  
Păstrează **un singur proces per container**, dar folosește mai multe containere într-un pod dacă acestea colaborează strâns (pattern-ul *sidecar*).

---

## 🧾 Concluzie

Evitarea acestor antipattern-uri Kubernetes contribuie la un mediu de orchestrare **mai rezilient, predictibil și ușor de administrat**.  
Adoptarea bunelor practici reduce datoria tehnică, minimizează downtime-ul și îmbunătățește stabilitatea aplicațiilor containerizate.

---
