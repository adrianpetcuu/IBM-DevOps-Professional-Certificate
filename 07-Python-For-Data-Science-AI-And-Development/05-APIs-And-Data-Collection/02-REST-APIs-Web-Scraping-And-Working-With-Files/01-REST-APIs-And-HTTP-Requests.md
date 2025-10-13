# 🌐 REST APIs & HTTP Requests în Python

Acest ghid te ajută să înțelegi ce este un **REST API**, cum funcționează cererile **HTTP** și cum poți interacționa cu API-uri web folosind **Python** și biblioteca `requests`.

---

## 🧠 Ce este un REST API?
Un **REST API (Representational State Transfer)** este o interfață care permite aplicațiilor să comunice între ele prin **cereri HTTP**.  
Folosind un API, poți **citi, crea, actualiza sau șterge** date de pe un server.

---

## ⚙️ Metode HTTP de bază

| Metodă | Scop | Exemplu |
|--------|------|----------|
| `GET` | Citește date | `/users` – obține lista de utilizatori |
| `POST` | Creează date noi | `/users` – adaugă un utilizator nou |
| `PUT` | Actualizează complet | `/users/3` – înlocuiește datele unui utilizator |
| `PATCH` | Actualizează parțial | `/users/3` – modifică un câmp |
| `DELETE` | Șterge date | `/users/3` – șterge utilizatorul 3 |

---

## 📡 Coduri de răspuns (HTTP Status Codes)

| Cod | Semnificație |
|-----|---------------|
| `200 OK` | Cererea a avut succes |
| `201 Created` | Resursa a fost creată |
| `204 No Content` | Operațiune reușită, fără răspuns |
| `400 Bad Request` | Cerere invalidă |
| `401 Unauthorized` | Autentificare necesară |
| `403 Forbidden` | Acces interzis |
| `404 Not Found` | Resursa nu există |
| `500 Internal Server Error` | Eroare internă pe server |

---

## 🐍 Lucrul cu HTTP Requests în Python

Biblioteca `requests` este una dintre cele mai populare pentru interacțiunea cu API-uri.

### Instalare
```bash
pip install requests
```

---

## 🔹 1. Cerere `GET` — Citire date

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status:", response.status_code)
print(response.json()[:2])  # primele două rezultate
```

---

## 🔹 2. Cerere `POST` — Creare resursă

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Salut API",
    "body": "Acesta este un test",
    "userId": 1
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print(response.json())
```

---

## 🔹 3. Cerere `PUT` — Actualizare completă

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "id": 1,
    "title": "Titlu actualizat",
    "body": "Am schimbat tot conținutul",
    "userId": 1
}

response = requests.put(url, json=payload)
print("Status:", response.status_code)
print(response.json())
```

---

## 🔹 4. Cerere `PATCH` — Actualizare parțială

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {"title": "Titlu modificat"}

response = requests.patch(url, json=payload)
print("Status:", response.status_code)
print(response.json())
```

---

## 🔹 5. Cerere `DELETE` — Ștergere resursă

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)
print("Status:", response.status_code)
```

---

## 🧾 Headere & Autentificare

Unele API-uri necesită **token de acces**. Acesta se trimite prin header.

```python
import requests

url = "https://api.exemplu.com/users"
headers = {
    "Authorization": "Bearer 12345ABCDE",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print(response.status_code)
```

---

## 🧯 Tratarea erorilor

```python
import requests

try:
    r = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
    r.raise_for_status()
    print(r.json())
except requests.exceptions.HTTPError as e:
    print("Eroare HTTP:", e)
except requests.exceptions.RequestException as e:
    print("Eroare de rețea:", e)
```

---

## 🧩 Parametri în cereri (Query Params)

```python
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.json())
```

---

## 📦 Ce returnează `response`

| Proprietate | Descriere |
|--------------|------------|
| `response.status_code` | Codul de răspuns HTTP |
| `response.text` | Răspunsul ca text brut |
| `response.json()` | Conținutul convertit în obiect Python |
| `response.headers` | Headerele răspunsului |
| `response.elapsed` | Timpul de răspuns |
| `response.cookies` | Cookie-uri primite |

---

## ✅ Bune practici pentru lucrul cu API-uri

- Folosește `with requests.Session()` pentru cereri multiple la același API.  
- Tratează toate erorile (`try/except`).
- Verifică `status_code` înainte de a accesa `response.json()`.
- Evită date sensibile în URL-uri.
- Documentează API-ul și testează-l cu **Postman** sau **Insomnia**.

---

## 🧠 Recapitulare rapidă

| Funcție | Scop | Exemplu |
|----------|------|----------|
| `requests.get()` | Citește date | `GET /users` |
| `requests.post()` | Creează date noi | `POST /users` |
| `requests.put()` | Actualizează complet | `PUT /users/3` |
| `requests.patch()` | Actualizează parțial | `PATCH /users/3` |
| `requests.delete()` | Șterge date | `DELETE /users/3` |

---

## 📚 Resurse recomandate

- [Python Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) – API gratuit pentru testare
- [Postman](https://www.postman.com/) – instrument pentru testarea API-urilor

---

> **Concluzie:** REST API-urile oferă o modalitate standardizată de a comunica între aplicații. Cu biblioteca `requests`, Python face extrem de simplă trimiterea și procesarea cererilor HTTP, fie pentru testare, fie pentru integrarea cu servicii externe.
