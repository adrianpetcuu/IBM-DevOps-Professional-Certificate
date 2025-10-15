# 🌐 Introduction to Web Applications and APIs

## 🔹 Descriere generală

Acest document oferă o introducere în conceptele de bază ale **aplicațiilor web** și **API-urilor (Application Programming Interfaces)**.  
Scopul este de a înțelege cum funcționează aplicațiile web moderne, cum comunică între ele și cum pot fi integrate în ecosisteme software complexe.

---

## 🧱 Ce este o aplicație web?

O **aplicație web** este un software accesibil printr-un browser (precum Chrome, Firefox sau Edge), care rulează pe un **server web**.  
Utilizatorii interacționează cu aplicația prin intermediul unei interfețe web (frontend), iar logica principală se execută pe partea de server (backend).

### Exemple de aplicații web:
- Gmail, Google Docs, Facebook, YouTube
- Aplicații bancare online
- Dashboard-uri și platforme de management

---

## ⚙️ Arhitectura aplicațiilor web

O aplicație web este alcătuită, în general, din trei componente principale:

1. **Frontend (Client-side)**  
   - Partea vizibilă utilizatorului (interfața grafică).  
   - Scrisă în limbaje precum **HTML**, **CSS**, **JavaScript**.  
   - Framework-uri populare: React, Angular, Vue.js

2. **Backend (Server-side)**  
   - Se ocupă de logica aplicației, procesarea datelor și gestionarea cererilor.  
   - Scris în limbaje precum **Python (Flask, Django)**, **Java**, **Node.js**, **C#**.

3. **Baza de date (Database)**  
   - Stochează informațiile aplicației (ex: utilizatori, produse, mesaje).  
   - Exemple: MySQL, PostgreSQL, MongoDB.

---

## 🔄 Cum funcționează o aplicație web

1. Utilizatorul trimite o cerere (request) către server.  
2. Serverul procesează cererea și interacționează cu baza de date.  
3. Serverul trimite un răspuns (response) înapoi către browser.  
4. Browserul afișează datele utilizatorului sub formă de pagină web.

```text
Client (Browser) ⇄ Server (Backend) ⇄ Database
```

---

## 🔌 Ce este un API?

Un **API (Application Programming Interface)** este o interfață care permite aplicațiilor software să comunice între ele.  
API-urile definesc **modul în care se fac cererile**, **ce date sunt trimise** și **cum sunt primite răspunsurile**.

### Exemple comune de API-uri:
- API-ul Google Maps
- API-ul OpenWeather (vreme)
- API-uri bancare sau de plăți (ex: Stripe, PayPal)
- API-uri de inteligență artificială (ex: OpenAI API)

---

## 🧩 Tipuri de API-uri Web

| Tip API | Descriere | Exemple |
|----------|------------|----------|
| **REST API** | Folosește HTTP și structuri JSON. Cel mai comun tip. | Flask RESTful, FastAPI |
| **SOAP API** | Format mai vechi, bazat pe XML. | Servicii enterprise |
| **GraphQL API** | Permite cereri flexibile de date. | GitHub API, Shopify |
| **WebSockets** | Permite comunicare bidirecțională în timp real. | Chat, jocuri online |

---

## 📡 Exemple de cereri HTTP

| Metodă | Scop | Exemplu |
|--------|------|----------|
| **GET** | Obține date | `GET /users` |
| **POST** | Trimite date | `POST /users` |
| **PUT** | Actualizează date | `PUT /users/1` |
| **DELETE** | Șterge date | `DELETE /users/1` |

Exemplu de cerere JSON:
```json
POST /api/users
{
  "name": "Ana",
  "email": "ana@example.com"
}
```

---

## 💻 Exemplu simplu de API cu Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint GET
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Salut, lume!'})

# Endpoint POST
@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({'user': data, 'status': 'created'})

if __name__ == '__main__':
    app.run(debug=True)
```

🔹 Acest cod creează un API simplu care răspunde la cereri HTTP folosind Flask.

---

## 🧰 Instrumente utile pentru lucrul cu API-uri

| Scop | Instrument | Descriere |
|------|-------------|-----------|
| Testare API | Postman | Permite testarea și documentarea endpoint-urilor |
| Debugging | cURL | Utilitar în linie de comandă pentru testare |
| Documentare | Swagger / OpenAPI | Creează documentație interactivă pentru API-uri |
| Automatizare | Python requests | Trimite cereri API din scripturi Python |

---

## 🔐 Securitate API

- Folosește **HTTPS** pentru criptarea datelor  
- Adaugă **autentificare** (ex: token JWT, OAuth)  
- Limitează accesul (rate limiting)  
- Validează datele primite de la client  

---

## 🚀 Concluzie

Aplicațiile web și API-urile sunt elemente fundamentale în dezvoltarea software modernă.  
Prin înțelegerea modului în care funcționează, poți construi aplicații conectate, scalabile și sigure, capabile să comunice eficient cu alte sisteme.

---

## 📚 Resurse utile

- [MDN Web Docs – Introduction to Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)  
- [Flask RESTful Documentation](https://flask-restful.readthedocs.io/)  
- [Postman API Platform](https://www.postman.com/)  
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)  
