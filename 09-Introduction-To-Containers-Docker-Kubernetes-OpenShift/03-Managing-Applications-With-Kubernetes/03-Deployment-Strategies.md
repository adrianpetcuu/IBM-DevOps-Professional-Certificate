# ☸️ Strategii de Deployment în Kubernetes
## 🧭 Prezentare generală

O **strategie de deployment** în Kubernetes definește modul în care o aplicație este implementată, actualizată și menținută automat pentru a atinge starea configurată dorită.  
Scopul principal este **reducerea riscurilor** și menținerea disponibilității aplicațiilor.

### 🔧 Strategiile de deployment sunt folosite pentru:
- Implementarea, actualizarea sau revenirea (rollback) versiunilor de **ReplicaSets, Pods, Services și aplicații**
- Pauzarea sau reluarea deployment-urilor
- Scalarea aplicațiilor manual sau automat

---

## 🔹 Tipuri de strategii de deployment

Există 6 tipuri principale de strategii:

1. **Recreate**
2. **Rolling (Ramped)**
3. **Blue/Green**
4. **Canary**
5. **A/B Testing**
6. **Shadow**

Poți utiliza o singură strategie sau o combinație între mai multe.

---

## 1️⃣ Recreate Strategy

### 🧠 Ce este
În strategia **Recreate**, toate Pods care rulează versiunea curentă sunt oprite simultan, iar noua versiune este lansată pe Pods noi.

📌 Este cea mai simplă strategie, dar are un **scurt downtime** între oprirea versiunii vechi și pornirea celei noi.

### 🔧 Pași:
1. Noua versiune (v2) este pregătită pentru deployment.  
2. Toate Pods care rulează v1 sunt șterse.  
3. Se creează Pods noi cu versiunea v2.  
4. Rollback: se revine la versiunea v1, în ordine inversă.

### ✅ Avantaje:
- Configurare simplă  
- Înlocuire completă a versiunii aplicației  

### ❌ Dezavantaje:
- Downtime scurt între versiuni

---

## 2️⃣ Rolling (Ramped) Strategy

### 🧠 Ce este
Într-o **Rolling Update**, Pods sunt actualizate treptat — unul câte unul.  
Un Pod v1 este înlocuit de un Pod v2 până când toate instanțele rulează noua versiune.

📌 Nu există downtime semnificativ — utilizatorii pot accesa ambele versiuni în timpul procesului.

### 🔧 Pași:
1. Se pregătește versiunea v2.  
2. Se șterge un Pod v1.  
3. Se lansează un Pod v2.  
4. Se repetă procesul până toate Pods sunt actualizate.

### ✅ Avantaje:
- Fără downtime vizibil  
- Ușor de implementat  

### ❌ Dezavantaje:
- Rollout-ul și rollback-ul durează mai mult  
- Nu poți controla exact distribuția traficului

---

## 3️⃣ Blue/Green Strategy

### 🧠 Ce este
Strategia **Blue/Green** utilizează două medii identice:  
- **Blue** – mediul actual de producție (v1)  
- **Green** – un mediu identic, cu versiunea nouă (v2)

📌 După ce mediul „green” este testat complet, traficul utilizatorilor este mutat către el.

### 🔧 Pași:
1. Creezi un mediu nou (green), identic cu producția (blue).  
2. Instalezi și testezi noua versiune (v2).  
3. Redirecționezi traficul către mediul green.  
4. Rollback: revii la mediul blue.

### ✅ Avantaje:
- Rollout/Rollback instantaneu (fără downtime)  
- Noua versiune disponibilă imediat tuturor utilizatorilor  

### ❌ Dezavantaje:
- Costuri ridicate (două medii simultan)  
- Dificil pentru aplicații stateful

---

## 4️⃣ Canary Strategy

### 🧠 Ce este
Strategia **Canary** permite testarea versiunii noi (v2) pe un **grup mic de utilizatori**, în paralel cu versiunea existentă (v1).  
Dacă testul e reușit, v2 este lansată pentru toți utilizatorii.

### 🔧 Pași:
1. Creezi versiunea v2.  
2. Direcționezi o mică parte din trafic către ea (ex: 5%).  
3. Testezi performanța și stabilitatea.  
4. Dacă totul este ok → crești gradual procentul.  
5. Rollback: rapid, fără downtime.

### ✅ Avantaje:
- Fără downtime  
- Testare sigură pe utilizatori reali  
- Rollback rapid  

### ❌ Dezavantaje:
- Lansare lentă, graduală  
- Necesită load balancer inteligent

---

## 5️⃣ A/B Testing Strategy

### 🧠 Ce este
Numită și **split testing**, această strategie testează **două versiuni diferite (A și B)** simultan.  
Fiecare versiune are caracteristici diferite, iar utilizatorii sunt grupați în funcție de criterii specifice.

### 🔧 Pași:
1. Creezi versiunea nouă (B) – de obicei cu modificări UI.  
2. Alegi un set de utilizatori după criterii (cookie, locație, browser etc.).  
3. Direcționezi cererile acestora către versiunea B.  
4. Monitorizezi performanța și feedback-ul.  
5. După testare, alegi versiunea finală pentru producție.

### ✅ Avantaje:
- Control total asupra traficului  
- Poți testa mai multe versiuni simultan  

### ❌ Dezavantaje:
- Necesită load balancer inteligent  
- Dificil de analizat erorile (distribuție pe sesiuni)

---

## 6️⃣ Shadow Strategy

### 🧠 Ce este
În strategia **Shadow**, o versiune „umbră” (v2) rulează în paralel cu versiunea live (v1).  
Cererile utilizatorilor sunt trimise către ambele versiuni, dar **v2 nu trimite răspunsuri către utilizatori**.

📌 Permite testarea noii versiuni cu trafic real, fără a afecta experiența utilizatorilor.

### 🔧 Pași:
1. Rulează ambele versiuni (v1 și v2).  
2. Redirecționează traficul către ambele.  
3. Analizează performanța v2.  
4. Rollback: oprește versiunea shadow.

### ✅ Avantaje:
- Testare pe trafic real  
- Fără impact asupra utilizatorilor  
- Zero downtime  

### ❌ Dezavantaje:
- Costuri ridicate (resurse duble)  
- Configurație complexă  
- Poate genera rezultate false (nu e un test de utilizator real)

---

## 🧩 Rezumatul strategiilor

| Strategie | Downtime | Testare reală | Utilizatori țintiți | Cost | Rollback | Impact utilizatori | Complexitate |
|------------|-----------|----------------|----------------------|------|------------|--------------------|----------------|
| **Recreate** | ❌ Da | ❌ Nu | ❌ Nu | 🔹 Mic | 🔸 Rapid | 🔺 Mare | 🔹 Simplă |
| **Rolling** | ✅ Nu | ❌ Nu | ❌ Nu | 🔹 Mic | 🔸 Lent | 🔹 Mic | 🔸 Medie |
| **Blue/Green** | ✅ Nu | ❌ Nu | ❌ Nu | 🔺 Mare | ⚡ Instant | 🔹 Mic | 🔸 Medie |
| **Canary** | ✅ Nu | ✅ Da | ❌ Nu | 🔹 Mediu | ⚡ Rapid | 🔹 Mic | 🔸 Medie |
| **A/B Testing** | ✅ Nu | ✅ Da | ✅ Da | 🔹 Mediu | 🔸 Mediu | 🔹 Mic | 🔺 Complexă |
| **Shadow** | ✅ Nu | ✅ Da | ❌ Nu | 🔺 Mare | ⚡ Instant | 🔹 Zero | 🔺 Complexă |

---

## 💡 Alegerea strategiei potrivite

| Situație | Strategie recomandată |
|-----------|------------------------|
| Aplicație necritică | **Recreate** |
| Deploy gradual, fără downtime | **Rolling** |
| Aplicație critică, fără downtime | **Blue/Green** |
| Testare sigură pe utilizatori reali | **Canary** |
| Testare interfețe și UX | **A/B Testing** |
| Testare performanță fără impact | **Shadow** |

---

## 🚀 Concluzie

> Alegerea strategiei potrivite de deployment depinde de natura aplicației, riscuri acceptabile și resursele disponibile.

- **Recreate** → Simplu, dar cu downtime.  
- **Rolling** → Gradual, fără downtime.  
- **Blue/Green** → Două medii, comutare instant.  
- **Canary** → Testare treptată.  
- **A/B** → Testare comparativă pe utilizatori reali.  
- **Shadow** → Testare completă, fără impact vizibil.

Aceste strategii permit echipelor DevOps să **implementeze aplicații sigure, stabile și scalabile**, cu control total asupra procesului de lansare.
