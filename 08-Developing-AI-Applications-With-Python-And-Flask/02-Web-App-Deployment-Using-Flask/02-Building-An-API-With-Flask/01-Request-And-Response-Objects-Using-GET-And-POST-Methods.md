# 📬 Flask – Request și Response folosind metodele GET și POST

Acest ghid explică modul în care Flask gestionează **obiectele `request` și `response`**, precum și diferențele dintre metodele HTTP **GET** și **POST**, folosite frecvent pentru trimiterea și preluarea datelor în aplicațiile web.

---

## 🚀 1. Introducere

În Flask, fiecare cerere HTTP este însoțită de un obiect `request`, care conține informații despre:
- metoda folosită (`GET`, `POST`, `PUT`, `DELETE`),
- parametri din URL,
- date trimise prin formulare sau JSON,
- antete (headers) și cookie-uri.

După procesarea cererii, aplicația returnează un **obiect `response`**, care conține:
- conținutul răspunsului (HTML, JSON, etc.),
- codul de status (ex: `200 OK`, `404 Not Found`),
- antetele răspunsului.

---

## ⚙️ 2. Importuri esențiale

```python
from flask import Flask, request, jsonify
```

`request` → citește datele primite de la client.  
`jsonify` → creează un răspuns JSON valid.

---

## 🔹 3. Metoda GET

Metoda **GET** este folosită pentru a **citi date** dintr-o aplicație.  
Parametrii sunt vizibili în URL.

### Exemplu:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Anonim')
    return jsonify({"message": f"Salut, {name}!"})
```

Exemplu de apel:
```
GET /hello?name=Ana
```
Răspuns:
```json
{"message": "Salut, Ana!"}
```

📌 Observație: `request.args` este un dicționar care conține toți parametrii din URL.

---

## 🔸 4. Metoda POST

Metoda **POST** este utilizată pentru a **trimite date** către server, de obicei prin formulare sau JSON.

### Exemplu:
```python
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', 'Anonim')
    return jsonify({"status": "success", "name": name})
```

Exemplu de cerere:
```bash
curl -X POST -H "Content-Type: application/json"      -d '{"name": "Alex"}'      http://localhost:5000/submit
```

Răspuns:
```json
{"status": "success", "name": "Alex"}
```

📌 Observație: `request.get_json()` citește corpul cererii când datele sunt trimise în format JSON.

---

## 🔄 5. Compararea GET vs POST

| Caracteristică | GET | POST |
|-----------------|-----|------|
| Tip acțiune | Citește date | Trimite date |
| Vizibilitate | Parametrii în URL | Date ascunse în corpul cererii |
| Dimensiune maximă | Limitată (URL scurt) | Poate fi mare |
| Cache | Da | Nu |
| Utilizare | Căutare, filtrare | Formulare, autentificare |

---

## 🧱 6. Accesarea altor date din `request`

```python
@app.route('/info', methods=['GET'])
def info():
    return {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "remote_addr": request.remote_addr
    }
```

Afișează informații utile despre cerere, inclusiv antete HTTP.

---

## 🧩 7. Exemplu complet GET și POST

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        name = request.args.get('name', 'Anonim')
        return jsonify({"message": f"Hello {name}, ai folosit GET!"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": f"Salut {data.get('name', 'Anonim')}, ai folosit POST!"})
```

Testează în terminal:
```bash
curl "http://localhost:5000/user?name=Ana"
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alex"}' http://localhost:5000/user
```

---

## ⚙️ 8. Obiectul Response

Flask creează automat un răspuns HTTP, dar poți personaliza manual conținutul și antetele:

```python
from flask import Response

@app.route('/custom')
def custom():
    return Response("Salut din Flask!", status=202, mimetype='text/plain')
```

---

## 🧠 9. Redirecționări și coduri de stare

```python
from flask import redirect, url_for

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return "Aceasta este noua rută!"
```

---

## 📊 10. Exemple de coduri de stare (status codes)

| Cod | Semnificație |
|------|--------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 🧩 11. Combinarea formularelor HTML cu Flask

Exemplu simplu de formă POST în HTML:

```html
<form action="/submit-form" method="POST">
  <input name="user" placeholder="Introdu numele">
  <button type="submit">Trimite</button>
</form>
```

Și ruta Flask corespunzătoare:
```python
@app.route('/submit-form', methods=['POST'])
def submit_form():
    user = request.form.get('user')
    return f"Salut, {user}! Formular trimis cu succes."
```

---

## 📚 12. Resurse utile

- [Documentația Flask – Request și Response](https://flask.palletsprojects.com/en/latest/api/)
- [HTTP Methods – MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Flask Mega Tutorial – Miguel Grinberg](https://blog.miguelgrinberg.com/)

---

## 🧭 Concluzie

În Flask, obiectele **`request`** și **`response`** sunt fundamentale pentru interacțiunea client-server.  
Prin metodele **GET** și **POST**, poți gestiona cu ușurință cereri, trimite date și crea API-uri REST eficiente.

> 🔹 `GET` – citește informații.  
> 🔹 `POST` – trimite și procesează informații.

---
