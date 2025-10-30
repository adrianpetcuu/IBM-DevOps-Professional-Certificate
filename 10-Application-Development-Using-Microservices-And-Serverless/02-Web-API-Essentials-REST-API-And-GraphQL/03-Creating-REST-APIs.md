# 🌐 Crearea API-urilor REST (Creating REST APIs)

## 🔹 Introducere

Un **REST API (Representational State Transfer Application Programming Interface)** este o modalitate standardizată de a permite aplicațiilor să comunice între ele prin intermediul protocolului **HTTP**.  
API-urile REST sunt esențiale în arhitecturile **microservicii** și **cloud-native**, deoarece oferă o metodă simplă, scalabilă și sigură de interacțiune între componente.

---

## ⚙️ Principii de bază ale unui REST API

Un API REST urmează principiile stilului arhitectural REST:

1. **Client–Server** – separă logica aplicației între partea de client și server.  
2. **Stateless** – fiecare cerere conține toate informațiile necesare; serverul nu reține starea.  
3. **Cacheable** – răspunsurile pot fi salvate pentru a îmbunătăți performanța.  
4. **Uniform Interface** – folosește o interfață consistentă pentru toate resursele.  
5. **Layered System** – permite existența mai multor straturi (gateway-uri, load balancere).  

---

## 🧱 Structura unui REST API

Un API REST este compus din:

- **Resurse (Resources)** – entitățile expuse de API (ex: utilizatori, produse, comenzi).  
- **URI-uri (Uniform Resource Identifiers)** – identifică fiecare resursă, ex: `/users/5`.  
- **Metode HTTP** – definesc acțiunile care pot fi efectuate asupra resurselor.  

### 🔸 Metode HTTP uzuale:

| Metodă | Descriere | Exemplu |
|---------|------------|----------|
| **GET** | Obține o resursă sau o listă de resurse. | `GET /users` |
| **POST** | Creează o resursă nouă. | `POST /users` |
| **PUT** | Actualizează o resursă existentă. | `PUT /users/5` |
| **DELETE** | Șterge o resursă. | `DELETE /users/5` |

---

## 🧰 Componente cheie ale unui API REST

| Componentă | Descriere |
|-------------|------------|
| **Endpoint** | O adresă URL care expune o resursă. |
| **Request** | Cererea trimisă de client (conține metoda, antetele și datele). |
| **Response** | Răspunsul de la server (de obicei în format JSON). |
| **Status Code** | Codul de răspuns HTTP care indică rezultatul operației. |

### 🔸 Exemple de coduri de răspuns HTTP:

| Cod | Semnificație |
|------|--------------|
| `200 OK` | Cererea a fost procesată cu succes. |
| `201 Created` | O resursă nouă a fost creată. |
| `400 Bad Request` | Cererea este invalidă. |
| `404 Not Found` | Resursa nu a fost găsită. |
| `500 Internal Server Error` | Eroare pe server. |

---

## 💡 Exemple de design pentru un REST API

Exemplu: API pentru gestionarea utilizatorilor

| Acțiune | Metodă HTTP | Endpoint |
|----------|--------------|-----------|
| Obține toți utilizatorii | GET | `/users` |
| Creează un utilizator nou | POST | `/users` |
| Obține un utilizator după ID | GET | `/users/{id}` |
| Actualizează un utilizator | PUT | `/users/{id}` |
| Șterge un utilizator | DELETE | `/users/{id}` |

---

## 🔐 Securizarea API-urilor REST

Pentru a asigura securitatea, se folosesc:

- **TLS/HTTPS** – pentru criptarea comunicațiilor.  
- **Token-uri de autentificare** (ex: JWT – JSON Web Tokens).  
- **Rate limiting** – pentru a preveni abuzul.  
- **CORS (Cross-Origin Resource Sharing)** – pentru controlul accesului între domenii.  

---

## 🚀 Cele mai bune practici pentru crearea unui REST API

1. Folosește **nume de resurse la plural** (ex: `/users`, `/orders`).  
2. Respectă convențiile **HTTP status codes**.  
3. Documentează API-ul folosind **OpenAPI/Swagger**.  
4. Adaugă **versionare** (`/v1/users`, `/v2/users`).  
5. Folosește **pagination** pentru liste mari de date.  
6. Gestionează corect **erorile și mesajele de răspuns**.  
7. Implementează **autentificare și autorizare** adecvate.  

---

## 🧩 Legătura cu Microserviciile

Într-o arhitectură cu microservicii:
- Fiecare microserviciu își expune propriul REST API.  
- Comunicarea între microservicii se face adesea prin API-uri REST sau mesagerie (event-driven).  
- API-urile REST facilitează **scalabilitatea, independența și interoperabilitatea**.  

---

## 🏁 Concluzie

Crearea unui **REST API** eficient este fundamentală pentru aplicațiile moderne.  
Acestea permit componentelor să comunice ușor, să fie scalabile și să rămână independente.  

**REST** este coloana vertebrală a arhitecturilor **microservicii**, **serverless** și **cloud-native**.

---

📚 *Referințe:*  
- [IBM Cloud – What is REST API?](https://www.ibm.com/cloud/learn/rest-apis)  
- [Microservices.io – REST Communication Pattern](https://microservices.io/patterns/communication/rest.html)  
- [Swagger – OpenAPI Specification](https://swagger.io/specification/)
