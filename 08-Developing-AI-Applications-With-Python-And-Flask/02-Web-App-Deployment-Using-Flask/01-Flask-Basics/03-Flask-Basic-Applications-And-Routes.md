# 🧠 Flask – Aplicații de Bază și Rute

Acest ghid explică principiile fundamentale ale framework-ului Flask, concentrându-se pe **crearea de aplicații web simple** și **definirea rutelor (routes)** care gestionează cererile HTTP.

---

## 🚀 1. Ce este o aplicație Flask?

O aplicație Flask este, în esență, un **server web minimalist** care:
- ascultă cereri HTTP (GET, POST, etc.),
- procesează cererea (într-o funcție Python),
- și returnează un răspuns către client (HTML, JSON, text etc.).

### Exemplu simplu:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

➡️ Deschide în browser: `http://127.0.0.1:5000`

---

## 🧱 2. Cum funcționează o rută (`@app.route`)

O **rută** este o cale URL care declanșează o anumită funcție din aplicație.

```python
@app.route('/about')
def about():
    return "Aceasta este pagina About."
```

📌 Când accesezi `http://localhost:5000/about`, Flask apelează funcția `about()` și returnează răspunsul text.

---

## 🌐 3. Tipuri de metode HTTP

Prin argumentul `methods` poți specifica ce tipuri de cereri sunt acceptate.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Te-ai autentificat!"
    return "Formular de login."
```

### Exemple:
| Metodă | Descriere |
|---------|------------|
| `GET` | Preia informații |
| `POST` | Trimite date către server |
| `PUT` | Actualizează o resursă |
| `DELETE` | Șterge o resursă |

---

## 📦 4. Returnarea datelor în format JSON

Pentru a crea un API simplu care returnează date JSON:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message')
def api_message():
    return jsonify({"message": "Salut din Flask!"})
```

Rezultatul va fi:
```json
{"message": "Salut din Flask!"}
```

---

## 🔢 5. Variabile dinamice în rute

Poți include variabile direct în rută folosind `< >`:

```python
@app.route('/user/<username>')
def show_user(username):
    return f"Salut, {username}!"
```

Exemplu: `http://localhost:5000/user/Ana` → `Salut, Ana!`

De asemenea, poți specifica **tipul de date**:
```python
@app.route('/square/<int:num>')
def square(num):
    return f"Patratul lui {num} este {num ** 2}."
```

---

## 🧩 6. Răspunsuri HTTP personalizate

Poți trimite și coduri de stare personalizate (status codes).

```python
@app.route('/status')
def status():
    return jsonify({"status": "ok"}), 200

@app.route('/error')
def error():
    return jsonify({"error": "Ceva nu a mers bine"}), 400
```

---

## 🗂️ 7. Structura recomandată pentru o aplicație Flask

```
project/
├── app.py
├── templates/         # fișiere HTML (Jinja2)
│   └── index.html
├── static/            # fișiere CSS, JS, imagini
├── routes/            # module cu rute separate
│   └── api.py
└── models/            # fișiere pentru baze de date
```

Această structură ajută la organizarea codului pentru proiecte mai mari.

---

## 🔄 8. Redirecționare și URL-uri dinamice

Flask permite redirecționarea către alte rute:

```python
from flask import redirect, url_for

@app.route('/home')
def home():
    return "Acasă!"

@app.route('/go-home')
def go_home():
    return redirect(url_for('home'))
```

`url_for()` generează automat linkuri către funcții existente.

---

## 🧮 9. Manipularea datelor trimise prin formulare

```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Salut, {name}!"
```

HTML corespunzător:
```html
<form action="/submit" method="POST">
  <input name="name" placeholder="Introdu numele">
  <button type="submit">Trimite</button>
</form>
```

---

## ⚙️ 10. Debug Mode

Activează modul de depanare pentru a vedea erorile în browser și pentru a reîncărca automat aplicația.

```bash
flask --app app run --debug
```

---

## 📊 11. Exemple de status codes frecvente

| Cod | Semnificație |
|------|--------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 🧠 12. Concepte importante în Flask

- **Rute dinamice** – permit transmiterea variabilelor în URL.  
- **JSON responses** – folosite în API-uri REST.  
- **Redirect și url_for** – navigare între rute.  
- **Templates (Jinja2)** – permit generarea de pagini HTML dinamice.

---

## 📚 13. Resurse utile

- [Documentația oficială Flask](https://flask.palletsprojects.com/)
- [Tutorial Miguel Grinberg – Flask Mega Tutorial](https://blog.miguelgrinberg.com/)
- [Jinja2 Template Engine](https://jinja.palletsprojects.com/)

---

## 🧭 Concluzie

Prin rute și funcții simple, Flask îți permite să construiești rapid aplicații web funcționale și API-uri REST.  
Este un framework **mic, dar extrem de puternic**, perfect pentru a învăța conceptele de bază ale dezvoltării web în Python.

> 🔹 „Flask este mic, dar îți oferă libertatea de a construi lucruri mari.”

---

