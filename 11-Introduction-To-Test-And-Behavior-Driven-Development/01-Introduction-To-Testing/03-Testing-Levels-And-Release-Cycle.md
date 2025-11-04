# 🧩 Nivelurile de Testare și Ciclul de Lansare

## 💡 Introducere

Testarea software-ului este organizată în **niveluri** și integrată în **ciclul de lansare** al produsului.  
Fiecare nivel de testare are un scop specific, verificând diferite aspecte ale calității aplicației.  
Prin testare continuă, echipele pot detecta defecte mai devreme și pot livra software stabil și sigur.

---

## 🧱 Nivelurile de Testare (Testing Levels)

Există patru niveluri principale de testare într-un ciclu de dezvoltare software:

### 1. **Testarea Unităților (Unit Testing)**
- Verifică funcționalitatea componentelor individuale ale codului (funcții, metode, clase).  
- Este efectuată de dezvoltatori, de obicei automatizată.  
- Exemple de instrumente: `unittest`, `pytest`, `JUnit`, `NUnit`.

🎯 **Scop:** Confirmă că fiecare unitate de cod funcționează corect în mod izolat.

---

### 2. **Testarea de Integrare (Integration Testing)**
- Verifică interacțiunea dintre mai multe module sau componente.  
- Asigură că unitățile integrate comunică și se comportă corect împreună.  
- Exemple: testarea conexiunilor dintre API-uri, baze de date sau servicii externe.

🎯 **Scop:** Confirmă că modulele funcționează corect în combinație.

---

### 3. **Testarea Sistemului (System Testing)**
- Testează aplicația completă ca un sistem unitar.  
- Verifică toate componentele integrate într-un mediu controlat.  
- Include teste funcționale, de performanță, securitate și compatibilitate.

🎯 **Scop:** Asigură că întregul sistem îndeplinește cerințele specificate.

---

### 4. **Testarea de Acceptanță (Acceptance Testing)**
- Este efectuată din perspectiva utilizatorului final.  
- Poate fi automată (ex. teste BDD) sau manuală (user acceptance testing).  
- Scopul este de a valida că produsul este pregătit pentru lansare.

🎯 **Scop:** Confirmă că aplicația satisface nevoile și așteptările utilizatorilor.

---

## 🔄 Ciclul de Lansare (Release Cycle)

Procesul de testare este strâns legat de ciclul de viață al dezvoltării software.  
Un **release cycle** tipic implică următoarele etape:

1. **Planificare:** Definirea cerințelor și criteriilor de acceptare.  
2. **Dezvoltare:** Scrierea codului și a testelor unitare (TDD).  
3. **Integrare:** Combinarea componentelor și rularea testelor de integrare.  
4. **Testare sistem:** Validarea completă a aplicației.  
5. **Testare de acceptanță:** Confirmarea că produsul este gata pentru livrare.  
6. **Lansare (Release):** Distribuirea software-ului către utilizatori.  
7. **Mentenanță:** Monitorizare, actualizări și corecții post-lansare.

---

## ⚙️ Testarea Continuă (Continuous Testing)

În mediile moderne DevOps, testarea este **continuă** pe tot parcursul ciclului de dezvoltare.  
Testele automate rulează la fiecare modificare de cod, integrându-se cu pipeline-urile **CI/CD**.

🔁 **Beneficii ale testării continue:**
- Detectarea timpurie a problemelor.  
- Reducerea riscului de regresii.  
- Feedback rapid pentru dezvoltatori.  
- Livrări mai frecvente și mai sigure.

---

## 🧭 Concluzie

- Testarea este un proces pe mai multe niveluri, de la unități până la sistem complet.  
- Fiecare nivel contribuie la asigurarea calității și stabilității produsului.  
- Testarea continuă și automatizarea sunt esențiale pentru un **ciclu de lansare eficient**.  
- Prin aplicarea consecventă a testării, echipele pot livra software **fiabil, sigur și de înaltă calitate**.

> 💬 „Testarea nu este o fază — este un proces continuu care însoțește fiecare etapă a dezvoltării.”
