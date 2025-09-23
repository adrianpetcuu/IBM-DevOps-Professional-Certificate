# 📘 Programming Languages and Code Organization

## 1. Interpreted and Compiled Programming Languages
Limbajele de programare pot fi clasificate în **interpretate** și **compilate**, în funcție de modul în care codul sursă este transformat în instrucțiuni executabile.

### 🔹 Compiled Languages (Limbaje compilate)
- Codul sursă este **tradus în cod mașină** de către un compilator.
- Executabilele rezultate pot fi rulate direct de sistemul de operare.
- Oferă performanță ridicată.
- Exemple: **C, C++, Rust, Go**.

✅ **Avantaje:**
- Viteză mare de execuție.
- Optimizare la nivel de mașină.
- Detectarea erorilor la compilare.

❌ **Dezavantaje:**
- Timp mai mare de compilare.
- Mai puțin flexibil pentru testare rapidă.

---

### 🔹 Interpreted Languages (Limbaje interpretate)
- Codul este **executat linie cu linie** de un interpret.
- Nu generează un fișier executabil separat.
- Exemple: **Python, JavaScript, Ruby, PHP**.

✅ **Avantaje:**
- Ușor de testat și modificat.
- Portabilitate ridicată între platforme.

❌ **Dezavantaje:**
- Performanță mai mică decât limbajele compilate.
- Erorile pot apărea doar în timpul execuției.

---

## 2. Comparing Compiled and Interpreted Programming Languages
### 🔹 Diferențe principale
| Caracteristică         | Limbaje Compilate       | Limbaje Interpretate     |
|-------------------------|-------------------------|---------------------------|
| Execuție               | Cod mașină (rapid)     | Linie cu linie (mai lent) |
| Erori                  | Detectate la compilare | Detectate la runtime      |
| Portabilitate          | Necesită recompilare   | Portabile direct          |
| Exemple                | C, C++, Go, Rust       | Python, JS, PHP, Ruby     |

### 🔹 Limbaje hibride
Unele limbaje combină ambele abordări:
- **Java**: compilat în bytecode → interpretat de JVM.
- **C#**: compilat în IL (Intermediate Language) → executat de CLR.

---

## 3. Query and Assembly Programming Languages

### 🔹 Query Languages
- Folosite pentru **interogarea și manipularea datelor**.
- Exemple:  
  - **SQL (Structured Query Language):** select, insert, update, delete.  
  - **GraphQL:** interogare flexibilă pentru API-uri.  

✅ Ideal pentru baze de date și aplicații ce manipulează mari volume de date.

---

### 🔹 Assembly Languages
- Limbaj de **nivel jos**, aproape de cod mașină.  
- Instrucțiunile sunt specifice arhitecturii procesorului.  
- Exemple: **x86 Assembly, ARM Assembly**.  

✅ Avantaj: control total asupra hardware-ului.  
❌ Dezavantaj: foarte greu de învățat și utilizat.  

💡 Se folosește mai ales pentru:  
- Programe de **sisteme embedded**.  
- Optimizări de performanță extremă.  
- Scrierea de **driver-e și OS kernels**.

---

## 4. Understanding Code Organization Methods
O bună organizare a codului face proiectele mai **scalabile, ușor de întreținut și colaborative**.

### 🔹 Metode de organizare
1. **Modular Programming**  
   - Împarte aplicația în module independente.  
   - Fiecare modul rezolvă o problemă specifică.  

2. **Object-Oriented Programming (OOP)**  
   - Codul este organizat în clase și obiecte.  
   - Principii: **encapsulation, inheritance, polymorphism**.  

3. **Layered Architecture**  
   - Separă aplicația în straturi: prezentare, logică de business, date.  

4. **Packages & Namespaces**  
   - Gruparea claselor/funțiilor similare.  
   - Evită conflictele de nume.  

5. **Design Patterns**  
   - Soluții standardizate pentru probleme comune de design (ex: Singleton, MVC, Observer).  

---

## 📌 Concluzie
- **Compiled vs Interpreted:** fiecare are avantaje și dezavantaje în funcție de performanță și flexibilitate.  
- **Query & Assembly:** două extreme → de la interogarea bazelor de date la programare aproape de hardware.  
- **Code Organization:** cheia pentru aplicații mari și echipe numeroase → modularizare, OOP, arhitecturi stratificate și pattern-uri.
