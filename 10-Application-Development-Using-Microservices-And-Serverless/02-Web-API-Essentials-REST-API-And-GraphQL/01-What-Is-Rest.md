# 🌐 Ce este REST? (What is REST?)

## 🔹 Introducere
**REST** (din engleză *Representational State Transfer*) este un **stil arhitectural** utilizat pentru a construi **servicii web** ușoare, scalabile și independente.  
Este una dintre cele mai populare metode de comunicare între aplicații pe internet.

---

## ⚙️ Principiile de bază ale REST

Un serviciu REST se bazează pe următoarele concepte fundamentale:

1. **Client–Server**  
   - Separă logica aplicației între client (interfața utilizator) și server (procesare și date).  
   - Această separare permite dezvoltarea și scalarea independentă a celor două părți.

2. **Stateless (Fără stare)**  
   - Fiecare cerere HTTP conține toate informațiile necesare.  
   - Serverul nu reține starea clientului între cereri.

3. **Cacheable (Suport pentru cache)**  
   - Răspunsurile pot fi stocate temporar (în cache) pentru a îmbunătăți performanța și a reduce încărcarea serverului.

4. **Uniform Interface (Interfață uniformă)**  
   - Comunicarea dintre client și server se face folosind convenții standardizate, de obicei **HTTP**.  
   - Exemple de metode HTTP:
     - `GET` – obține informații  
     - `POST` – trimite date către server  
     - `PUT` – actualizează date existente  
     - `DELETE` – șterge resurse  

5. **Layered System (Sistem stratificat)**  
   - REST permite existența mai multor straturi (proxy, gateway, load balancer) între client și server, fără ca acestea să afecteze funcționarea generală.

---

## 🧱 Resursele REST

- În REST, **totul este considerat o resursă** – un obiect sau un element de date accesibil printr-un **URI (Uniform Resource Identifier)**.  
  Exemple de resurse:
  - `/users` → lista utilizatorilor  
  - `/products/10` → detalii despre produsul cu ID = 10  

- Fiecare resursă poate fi reprezentată în diverse formate, de obicei:
  - **JSON (JavaScript Object Notation)**  
  - **XML (Extensible Markup Language)**  

---

## 🔄 Exemple de apeluri REST

| Tip cerere | URI | Acțiune |
|-------------|-----|----------|
| `GET /users` | Returnează lista utilizatorilor |
| `GET /users/5` | Returnează utilizatorul cu ID = 5 |
| `POST /users` | Creează un utilizator nou |
| `PUT /users/5` | Actualizează utilizatorul cu ID = 5 |
| `DELETE /users/5` | Șterge utilizatorul cu ID = 5 |

---

## 🚀 Avantajele REST

- ✅ Ușor de înțeles și implementat  
- ✅ Scalabil și performant  
- ✅ Funcționează peste protocolul HTTP standard  
- ✅ Suportat de majoritatea limbajelor de programare  
- ✅ Ideal pentru arhitecturi bazate pe microservicii și API-uri publice  

---

## 🧭 Concluzie

**REST** oferă o modalitate standardizată, simplă și eficientă de a construi servicii web.  
Este fundamentul multor aplicații moderne bazate pe **API-uri**, inclusiv arhitecturile **microservicii**, **serverless** și **cloud-native**.

---

📚 *Referințe:*  
- [IBM Cloud – What is REST?](https://www.ibm.com/cloud/learn/rest-apis)  
- [RESTful API Principles – REST API Tutorial](https://restfulapi.net/)
