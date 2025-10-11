# 🧩 Application Programming Interface (API) — Ghid practic

Un **API** (Application Programming Interface) este un set de reguli și contracte care permit aplicațiilor să **comunice între ele**. Practic, un API expune funcționalități sau date prin **endpoint-uri** pe care alte programe le pot apela în mod securizat și predictibil.

---

## 🎯 Obiective
După parcurgere, vei putea:
- Explica ce este un API și de ce este util
- Înțelege diferențele între **REST**, **GraphQL** și **SOAP**
- Folosi corect **metodele HTTP**, **codurile de status** și **headerele**
- Implementa **autentificare**, **paginare**, **versiuni** și **rate limiting**
- Documenta un API cu **OpenAPI/Swagger**
- Testa API-uri cu `curl`, Postman și Python (`requests`)

---

## 🧠 Ce este un API?
- Un API definește **ce funcții** sunt disponibile, **cum** se apelează și **ce formate** de date sunt acceptate/returnate.
- Avantaje: separă frontend de backend, permite integrarea cu terți, scalare, reutilizare.

---

## 🧭 Stiluri de API
### 1) REST (cel mai comun)
- Resurse identificate prin **URL-uri** (ex: `/users/123`).
- Operații prin **metode HTTP**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
- Transfer de date de obicei **JSON**. Stateless.

### 2) GraphQL
- O singură rută (ex: `/graphql`).
- Clientul cere exact **câmpurile** de care are nevoie.
- Puternic pentru aplicații cu **multe tipuri de relații**.

### 3) SOAP
- Protocol bazat pe **XML** și **WSDL**.
- Folosit în medii enterprise/legacy, tranzacții complexe.

---

## 🌐 Componente HTTP importante
- **Metode:**  
  - `GET` (citește), `POST` (creează), `PUT` (înlocuiește), `PATCH` (modifică parțial), `DELETE` (șterge), `HEAD`, `OPTIONS`
- **Status codes:**  
  - `200 OK`, `201 Created`, `204 No Content`  
  - `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`  
  - `500 Internal Server Error`, `503 Service Unavailable`
- **Headere uzuale:**  
  - `Content-Type: application/json`  
  - `Accept: application/json`  
  - `Authorization: Bearer <token>`  
  - `Idempotency-Key: <uuid>` (plăți/retry în siguranță)

---

## 🧩 Design de resurse (REST)
```text
GET    /users              # listare utilizatori (cu paginare)
POST   /users              # creare utilizator
GET    /users/{id}         # detalii utilizator
PATCH  /users/{id}         # modificare parțială
PUT    /users/{id}         # înlocuire totală
DELETE /users/{id}         # ștergere
```
- **Nume la plural** (`/users`, `/orders`), resurse **ierarhice**: `/users/{id}/orders`.
- Evită verbe în URL: ✅ `/users`, ❌ `/getUsers`.

---

## 🔐 Autentificare & autorizare
- **Bearer JWT** (cel mai comun pentru API-urile web/mobile)
- **OAuth 2.0 / OIDC** pentru terți și Single Sign-On
- **API Keys** pentru servicii server-to-server simple
- **mTLS** în medii enterprise

Exemplu header:
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

Verificări recomandate:
- Expirare token, rotație, **scopes/claims** (ce are voie utilizatorul), **RBAC/ABAC**.

---

## 📦 Paginare, filtrare, sortare
- **Query params**:
  - `/users?page=2&limit=20`
  - `/users?sort=created_at,desc`
  - `/users?role=admin&active=true`
- **Cursor-based** pentru liste foarte mari:
  - `/users?cursor=eyJpZCI6IjEyMyIsIm...&limit=50`

Returnează metadate de paginare:
```json
{
  "data": [ ... ],
  "meta": { "page": 2, "limit": 20, "total": 134 },
  "links": { "next": "/users?page=3&limit=20" }
}
```

---

## ♻️ Idempotency & Retry
- `GET`, `PUT`, `DELETE` **trebuie** să fie idempotente (același efect la repetare).
- Pentru `POST` (ex: plăți), folosește `Idempotency-Key`:
```http
POST /payments
Idempotency-Key: 7b8f1c1e-5c9b-4dc4-9a7a-8f6b0a1b3c2a
```
Serverul detectează duplicatele și returnează același rezultat.

---

## 🚦 Rate limiting & Throttling
- Protejează API-ul de abuz: **ex: 100 req/min/user**.
- Comunică limitele în headere:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 23
X-RateLimit-Reset: 1712345678
```

---

## 🧯 Tratarea erorilor (format consistent)
```json
{
  "error": {
    "code": "validation_error",
    "message": "Email is invalid.",
    "details": [
      {"field": "email", "issue": "invalid_format"}
    ],
    "trace_id": "req_01HZX..."
  }
}
```
- Include un **cod** stabil, mesaj ușor de înțeles, detalii pe câmpuri și un **trace id** pentru suport.

---

## 🔒 Securitate
- **TLS peste tot** (`https` only)
- **CORS** configurat corect pentru frontend-uri
- **Input validation** (server-side), sanitizare
- **Scopes/RBAC**, **least privilege**
- **Audit logging**, **WAF**, **OWASP API Security Top 10**
- Evită date sensibile în URL, loguri și răspunsuri

---

## 🧾 Documentare: OpenAPI / Swagger
- Scrie contractul în **OpenAPI 3.x** (`openapi.yaml/json`)
- Generează automat:
  - documentație interactivă (Swagger UI, Redoc)
  - SDK-uri (OpenAPI Generator)
- Exemplu minimal:
```yaml
openapi: 3.0.3
info:
  title: Users API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: OK
```

---

## 🧪 Testare & Observabilitate
- **Postman**, **Insomnia** pentru explorare manuală
- Teste automate: unit/integration/contract (Pact), **mock servers**
- **Logging corelat** (trace/span IDs), **metrics** (latency p95, error rate), **distributed tracing** (OpenTelemetry)

---

## 🛠️ Exemple rapide

### `curl`
```bash
# listare cu paginare
curl -H "Authorization: Bearer $TOKEN"      -H "Accept: application/json"      "https://api.example.com/users?page=1&limit=20"

# creare utilizator
curl -X POST "https://api.example.com/users"      -H "Authorization: Bearer $TOKEN"      -H "Content-Type: application/json"      -d '{"email":"ana@example.com","name":"Ana"}'
```

### Python (`requests`)
```python
import requests

BASE = "https://api.example.com"
TOKEN = "REPLACE_ME"
headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}

# GET
resp = requests.get(f"{BASE}/users", params={"page": 1, "limit": 20}, headers=headers)
resp.raise_for_status()
print(resp.json())

# POST
payload = {"email": "ana@example.com", "name": "Ana"}
resp = requests.post(f"{BASE}/users", json=payload, headers=headers)
resp.raise_for_status()
print(resp.json())
```

---

## ✅ Bune practici (checklist)
- [ ] Nume resurse clare, la plural (`/users`, `/orders`)
- [ ] Status codes corecte (`201` la creare, `204` fără body)
- [ ] Mesaje de eroare consistente
- [ ] Documentație OpenAPI actualizată
- [ ] Autentificare standard (OAuth2/OIDC/JWT)
- [ ] Paginare + filtrare + sortare
- [ ] Rate limiting + idempotency
- [ ] Versionare (`/v1`) + migrare controlată
- [ ] Observabilitate: logs + metrics + traces
- [ ] Securitate: TLS, input validation, secret management, least privilege

---

## 📚 Resurse utile
- *RESTful API Design* (Martin Fowler)  
- *OpenAPI Initiative* — standardul OpenAPI 3.x  
- *OWASP API Security Top 10* — riscuri și mitigații

---

> **Concluzie:** Un API bun este **predictibil, sigur, documentat și observabil**. Începe cu un contract clar (OpenAPI), respectă convențiile HTTP, folosește autentificare standard și construiește un ecosistem ușor de integrat și scalat.
