# 📘 Documentarea și Testarea API-urilor REST cu Swagger (Documenting and Testing REST APIs with Swagger)

## 🔹 Introducere

**Swagger** este un set de instrumente open-source utilizate pentru **definirea, documentarea și testarea API-urilor REST**.  
Este parte din ecosistemul **OpenAPI Specification (OAS)** și este folosit pe scară largă în dezvoltarea de microservicii și aplicații cloud-native.

Swagger permite dezvoltatorilor să:
- Descrie structura API-ului într-un format standardizat (OpenAPI/JSON/YAML).
- Genereze automat documentația interactivă.
- Testeze cereri direct din interfața grafică.

---

## 🧩 Componentele ecosistemului Swagger

| Componentă | Descriere |
|-------------|------------|
| **Swagger Editor** | Permite scrierea și editarea definițiilor API în format OpenAPI (YAML sau JSON). |
| **Swagger UI** | Oferă o interfață web interactivă pentru testarea API-urilor. |
| **Swagger Codegen** | Generează automat codul sursă pentru client sau server pe baza definiției API. |
| **OpenAPI Specification (OAS)** | Standardul care definește modul de descriere a unui API REST. |

---

## ⚙️ Structura unei definiții Swagger (OpenAPI)

Un fișier Swagger (ex: `swagger.yaml`) descrie API-ul prin următoarele secțiuni principale:

```yaml
openapi: 3.0.0
info:
  title: Exemplu API Utilizatori
  description: API pentru gestionarea utilizatorilor
  version: 1.0.0

servers:
  - url: https://api.exemplu.com/v1

paths:
  /users:
    get:
      summary: Obține lista utilizatorilor
      responses:
        '200':
          description: Listă de utilizatori returnată cu succes
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
```

---

## 🧠 Explicația secțiunilor principale

| Secțiune | Descriere |
|-----------|------------|
| **openapi** | Versiunea specificației OpenAPI (ex: 3.0.0). |
| **info** | Informații generale despre API (nume, versiune, descriere). |
| **servers** | Listează adresele de bază (base URLs) ale API-ului. |
| **paths** | Definirea endpoint-urilor și metodelor HTTP asociate (GET, POST, PUT, DELETE). |
| **components** | Include schemele (modelele de date) și alte elemente reutilizabile. |

---

## 🧰 Exemple de endpoint-uri documentate în Swagger

```yaml
paths:
  /products:
    get:
      summary: Obține lista de produse
      responses:
        '200':
          description: Listă returnată cu succes
    post:
      summary: Creează un produs nou
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
      responses:
        '201':
          description: Produs creat
  /products/{id}:
    get:
      summary: Obține produsul după ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Produs găsit
        '404':
          description: Produsul nu a fost găsit
```

---

## 🧪 Testarea API-urilor cu Swagger UI

**Swagger UI** oferă o pagină web interactivă care permite:
- Vizualizarea documentației API în format clar și organizat.
- Trimiterea de cereri directe (GET, POST, PUT, DELETE) către API.  
- Vizualizarea răspunsurilor în timp real (status, body, headers).

### ▶️ Exemplu de utilizare
1. Deschide `Swagger UI` (local sau online).  
2. Încarcă fișierul tău `swagger.yaml` sau `swagger.json`.  
3. Selectează endpoint-ul dorit.  
4. Completează parametrii necesari (ex: `id`, `body`).  
5. Apasă **"Try it out"** pentru a testa API-ul.

---

## 🚀 Beneficiile utilizării Swagger

- ✅ Documentație clară, ușor de înțeles și partajabilă.  
- ✅ Posibilitatea de a testa API-ul direct din browser.  
- ✅ Generare automată de cod pentru client și server.  
- ✅ Suport pentru versionare și standardizare.  
- ✅ Crește colaborarea între echipele de dezvoltare și testare.  

---

## 🔧 Integrarea Swagger în proiecte

### 🔸 În Python (Flask + Flasgger)
```python
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello')
def hello_world():
    '''
    Un exemplu simplu de endpoint.
    ---
    responses:
      200:
        description: Răspuns de succes
    '''
    return "Salut din Swagger!"
```

### 🔸 În Node.js (Express + Swagger UI)
```javascript
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

const app = express();
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.listen(3000, () => console.log('Serverul rulează pe portul 3000'));
```

După rulare, accesează:
```
http://localhost:3000/api-docs
```
pentru a vedea interfața Swagger UI.

---

## 🏁 Concluzie

**Swagger** este un instrument esențial pentru:
- Definirea clară a API-urilor REST.  
- Crearea documentației interactive.  
- Testarea rapidă și colaborarea între echipe.  

Prin integrarea Swagger, asiguri **transparență, consistență și calitate** în dezvoltarea și întreținerea API-urilor moderne.

---

📚 *Referințe:*  
- [Swagger Official Documentation](https://swagger.io/docs/)  
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)  
- [Flasgger – Flask Swagger Integration](https://github.com/flasgger/flasgger)
