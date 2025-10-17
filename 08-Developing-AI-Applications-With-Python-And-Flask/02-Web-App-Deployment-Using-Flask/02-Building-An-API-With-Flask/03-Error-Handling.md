# ⚠️ Flask – Gestionarea Erorilor (Error Handling)

Acest ghid explică cum se pot gestiona erorile în aplicațiile Flask în mod eficient, folosind **coduri de stare HTTP**, **funcții personalizate** și **decoratori speciali**.  
Scopul este de a oferi utilizatorilor răspunsuri clare și sigure atunci când apar probleme.

---

## 🚀 1. Introducere

Într-o aplicație web, erorile sunt inevitabile — fie că lipsesc resurse, fie că apar excepții interne.  
Flask oferă mecanisme integrate pentru a trata aceste situații fără a întrerupe funcționarea aplicației.

Există două tipuri principale de erori:
1. **Erori HTTP** (404, 500, etc.) → răspunsuri generate automat.
2. **Excepții Python** → tratate prin `try/except` sau prin funcții Flask speciale.

---

## 🧱 2. Tratarea erorilor HTTP cu decoratori

Poți folosi decoratori precum `@app.errorhandler()` pentru a personaliza mesajele de eroare.

### Exemplu 404 – Pagina nu a fost găsită
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Pagina nu a fost găsită"}), 404
```

Când utilizatorul accesează o rută inexistentă, aplicația va returna un răspuns JSON clar.

---

## ⚙️ 3. Erori interne (500 – Internal Server Error)

### Exemplu:
```python
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Eroare internă a serverului"}), 500
```

Aceasta se activează atunci când apare o excepție neașteptată în cod.

---

## 🧩 4. Tratarea excepțiilor specifice

Poți intercepta anumite tipuri de erori Python:
```python
@app.errorhandler(ZeroDivisionError)
def handle_zero_division(e):
    return jsonify({"error": "Împărțirea la zero nu este permisă"}), 400
```

---

## 🔸 5. Folosirea `abort()` pentru generarea manuală a erorilor

Funcția `abort()` oprește execuția și trimite automat un răspuns HTTP.

```python
from flask import abort, jsonify

@app.route('/admin')
def admin():
    abort(403)  # interzis fără acces
    return jsonify({"message": "Bun venit, admin!"})
```

Poți gestiona și această eroare:
```python
@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "Acces interzis"}), 403
```

---

## 🧠 6. Returnarea codurilor de stare în mod explicit

```python
@app.route('/status')
def status():
    return jsonify({"status": "ok"}), 200

@app.route('/created')
def created():
    return jsonify({"message": "Resursă creată"}), 201
```

---

## 🧾 7. Exemplu complet de gestionare a erorilor

```python
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        abort(400, description="Împărțirea la zero nu este permisă")
    return jsonify({"result": a / b})

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e)}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Pagina nu există"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Eroare internă"}), 500
```

---

## 🧩 8. Tratarea globală cu `@app.before_request` și `@app.teardown_request`

Poți adăuga cod care rulează **înainte** sau **după** fiecare cerere, util pentru logare sau curățare de resurse.

```python
@app.before_request
def before_request():
    print("Cerere primită...")

@app.teardown_request
def teardown_request(exception):
    if exception:
        print(f"A apărut o eroare: {exception}")
```

---

## 🧰 9. Personalizarea paginilor HTML pentru erori

Pentru aplicații web cu interfață grafică (nu doar API-uri), poți crea pagini HTML dedicate.

```
templates/
├── 404.html
├── 500.html
└── 403.html
```

```python
from flask import render_template

@app.errorhandler(404)
def not_found_html(e):
    return render_template("404.html"), 404
```

---

## 🧮 10. Exemple de coduri de stare HTTP utile

| Cod | Semnificație |
|------|--------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## 🔍 11. Debug Mode și gestionarea excepțiilor

Activează modul de depanare pentru a vedea detalii complete despre erori în browser:

```bash
flask --app app run --debug
```

⚠️ **Atenție:** Nu folosi `debug=True` în producție! Expune informații sensibile despre server.

---

## 📚 12. Resurse utile

- [Documentația Flask – Error Handling](https://flask.palletsprojects.com/en/latest/errorhandling/)
- [HTTP Status Codes – MDN Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Werkzeug Exceptions](https://werkzeug.palletsprojects.com/en/latest/exceptions/)

---

## 🧭 Concluzie

Gestionarea erorilor este esențială pentru aplicații web stabile și sigure.  
Flask oferă o abordare simplă și elegantă pentru a prinde, personaliza și înregistra erorile.

> 🔹 „Un cod robust nu este acela care nu dă erori, ci acela care le tratează inteligent.”

---
