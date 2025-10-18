# ⚙️ Funcționalități Suplimentare în Flask

Acest document oferă o privire de ansamblu asupra **funcționalităților suplimentare** oferite de Flask, dincolo de rutarea de bază. Vom explora caracteristici precum gestionarea sesiunilor, redirecționarea utilizatorilor, generarea URL-urilor dinamice, filtrarea șabloanelor, gestionarea erorilor și alte extensii utile.

---

## 🎯 Obiective
După parcurgerea acestui ghid, vei învăța:
- Cum să gestionezi **redirecționări și URL-uri dinamice** folosind `redirect` și `url_for`;
- Cum să lucrezi cu **fișiere statice și șabloane Jinja2**;
- Cum să utilizezi **sesiuni și cookie-uri** pentru autentificare și preferințe utilizator;
- Cum să implementezi **gestionarea erorilor personalizate**;
- Cum să extinzi Flask cu biblioteci externe.

---

## 🧭 1. Redirecționarea utilizatorilor – `redirect()`

Flask oferă funcția `redirect()` pentru a trimite utilizatorii către o altă rută.

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Pagina principală"

@app.route('/login')
def login():
    return "Pagina de autentificare"

@app.route('/admin')
def admin():
    # Redirecționează către ruta 'login'
    return redirect(url_for('login'))
```

➡️ `url_for('login')` generează automat URL-ul rutei `login`, chiar dacă acesta se schimbă ulterior.

---

## 🌐 2. Generarea dinamică de URL-uri – `url_for()`

`url_for()` generează adrese URL dinamice pe baza numelui funcției rutei.

```python
@app.route('/user/<username>')
def profile(username):
    return f"Profilul utilizatorului: {username}"

@app.route('/dashboard')
def dashboard():
    return redirect(url_for('profile', username='Ana'))
```

Rezultat: `http://localhost:5000/user/Ana`

---

## 📦 3. Lucrul cu fișiere statice și șabloane

### Fișiere statice (`/static`)
Flask servește automat fișierele din folderul `static`.

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### Șabloane HTML (`/templates`)
Motorul **Jinja2** permite inserarea variabilelor și logica de afișare în HTML.

```python
from flask import render_template

@app.route('/')
def home():
    user = "Alex"
    return render_template('index.html', user=user)
```

```html
<!-- templates/index.html -->
<h1>Bun venit, {{ user }}!</h1>
```

---

## 🔒 4. Gestionarea sesiunilor și cookie-urilor

Flask oferă modul `session` pentru a stoca informații despre utilizator între cereri.

```python
from flask import session

app.secret_key = "cheie_secreta"

@app.route('/login/<username>')
def login(username):
    session['user'] = username
    return f"Utilizator logat: {username}"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return "Delogat!"
```

Cookie-urile sunt gestionate automat, iar datele din `session` sunt criptate folosind cheia secretă a aplicației.

---

## ⚠️ 5. Gestionarea erorilor personalizate

Folosește `@app.errorhandler()` pentru a returna pagini dedicate erorilor.

```python
@app.errorhandler(404)
def not_found(e):
    return "Pagina nu există!", 404

@app.errorhandler(500)
def server_error(e):
    return "Eroare internă a serverului!", 500
```

---

## 🔁 6. Hook-uri de cerere (request hooks)

Flask permite executarea de acțiuni **înainte și după fiecare cerere** HTTP.

```python
@app.before_request
def before_request_func():
    print("Cerere primită!")

@app.after_request
def after_request_func(response):
    print("Răspuns trimis!")
    return response
```

Acestea sunt utile pentru logare, validare, sau configurarea conexiunilor la baze de date.

---

## 🧩 7. Filtre Jinja2 personalizate

Poți crea filtre noi pentru a procesa datele direct în șabloane.

```python
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]
```

În șablon:
```html
<p>{{ "Flask" | reverse }}</p>
```

Rezultat: `ksalF`

---

## 📤 8. Încărcarea fișierelor

Flask permite încărcarea de fișiere prin formulare.

```python
from flask import request

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"uploads/{file.filename}")
    return "Fișier încărcat cu succes!"
```

HTML corespunzător:
```html
<form action="/upload" method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Încarcă">
</form>
```

---

## 🧠 9. Extensii populare Flask

| Extensie | Scop |
|-----------|------|
| `Flask-SQLAlchemy` | Baze de date ORM |
| `Flask-Migrate` | Migrarea modelelor de date |
| `Flask-Login` | Gestionarea autentificării |
| `Flask-Mail` | Trimiterea e-mailurilor |
| `Flask-WTF` | Gestionarea formularelor |
| `Flask-RESTful` | Crearea API-urilor REST |

Instalare exemplu:
```bash
pip install Flask-SQLAlchemy Flask-Login Flask-Migrate
```

---

## 🧮 10. Comenzi CLI personalizate

Flask permite crearea de comenzi în linia de comandă prin `@app.cli.command()`:

```python
@app.cli.command("init-db")
def init_db():
    print("Baza de date inițializată!")
```

Rulare în terminal:
```bash
flask init-db
```

---

## ✅ Concluzie

Flask oferă un ecosistem puternic și flexibil care permite dezvoltatorilor să construiască aplicații web scalabile, sigure și ușor de întreținut. Prin utilizarea funcționalităților suplimentare — cum ar fi sesiunile, redirecturile, filtrele și CLI-ul — poți transforma o aplicație simplă într-un proiect profesional.

> 🔹 Flask = Simplitate + Extensibilitate + Control complet asupra aplicației.

---
