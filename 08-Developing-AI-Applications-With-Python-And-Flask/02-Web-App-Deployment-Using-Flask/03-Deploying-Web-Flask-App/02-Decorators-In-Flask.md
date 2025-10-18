# 🧩 Decoratori în Flask

Decoratori în Flask sunt o componentă esențială care permite **definirea rutelor**, **gestionarea cererilor HTTP**, și **extinderea funcționalităților** aplicației fără a modifica direct logica funcției. Acest concept provine din Python și este folosit pe scară largă în Flask pentru a adăuga comportamente dinamice funcțiilor.

---

## 🎯 Obiective
După parcurgerea acestui ghid, vei înțelege:
- Ce este un **decorator** în Python și Flask;
- Cum funcționează `@app.route()`;
- Cum poți crea **decoratori personalizați**;
- Cum să aplici decoratori pentru **autentificare**, **logare**, și **gestionare erori**.

---

## 🧱 1. Ce este un decorator în Python?

Un decorator este o funcție care **primește o altă funcție ca argument** și **returnează o nouă funcție** cu funcționalitate extinsă.

### Exemplu simplu:
```python
def decor(func):
    def wrapper():
        print("Înainte de funcție")
        func()
        print("După funcție")
    return wrapper

@decor
def salut():
    print("Salut, lume!")

salut()
```

Rezultat:
```
Înainte de funcție
Salut, lume!
După funcție
```

---

## 🌐 2. Decoratori în Flask – `@app.route()`

În Flask, decoratorul `@app.route()` leagă o **funcție Python** de un **URL**.

### Exemplu:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bun venit!"

@app.route('/about')
def about():
    return "Despre aplicație"
```

- `@app.route('/')` → definește ruta principală.  
- Funcția `home()` este apelată automat când utilizatorul accesează `/`.

---

## ⚙️ 3. Argumente utile ale `@app.route()`

| Parametru | Descriere |
|------------|------------|
| `rule` | Definește URL-ul rutei (ex: `/about`) |
| `methods` | Specifică metodele HTTP acceptate (`GET`, `POST`) |
| `endpoint` | Numele intern al rutei (implicit este numele funcției) |
| `strict_slashes` | Permite sau interzice „/” la finalul rutei |

### Exemplu cu metode HTTP:
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Autentificare trimisă"
    return "Afișare formular login"
```

---

## 🧠 4. Decoratori Flask personalizați

Poți crea decoratori proprii pentru a extinde comportamentul rutelor, de exemplu pentru verificarea autentificării.

### Exemplu: decorator pentru autentificare
```python
from functools import wraps
from flask import request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_logged_in = request.args.get('user') == 'admin'
        if not user_logged_in:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/dashboard')
@login_required
def dashboard():
    return "Bine ai venit în dashboard!"
```

➡️ Dacă accesezi `/dashboard?user=admin`, vei vedea mesajul.  
Dacă accesezi fără parametru, vei fi redirecționat către `/login`.

---

## 🔒 5. Folosirea mai multor decoratori

Poți aplica mai mulți decoratori pe aceeași funcție — ordinea contează.

```python
@app.route('/data')
@login_required
@log_request
def data():
    return "Date protejate"
```

Se execută de jos în sus: mai întâi `log_request`, apoi `login_required`.

---

## 🧩 6. Exemple utile de decoratori în Flask

| Decorator | Scop |
|------------|------|
| `@app.route()` | Definirea unei rute |
| `@app.before_request` | Cod executat înaintea fiecărei cereri |
| `@app.after_request` | Cod executat după fiecare cerere |
| `@app.errorhandler()` | Gestionarea erorilor personalizate |
| `@app.template_filter()` | Definirea filtrelor Jinja2 |
| `@app.cli.command()` | Adăugarea comenzilor personalizate în terminal |

### Exemplu `before_request`
```python
@app.before_request
def log_request_info():
    print("Cerere primită:", request.path)
```

### Exemplu `after_request`
```python
@app.after_request
def add_headers(response):
    response.headers["X-App-Name"] = "FlaskDemo"
    return response
```

### Exemplu `errorhandler`
```python
@app.errorhandler(404)
def page_not_found(e):
    return "Pagina nu există!", 404
```

---

## 🧮 7. Crearea unui decorator general în Flask

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator aplicat!")
        return func(*args, **kwargs)
    return wrapper

@app.route('/test')
@my_decorator
def test():
    return "Test decorator Flask!"
```

Rezultatul în consolă:  
```
Decorator aplicat!
```

---

## 🧠 8. Bune practici

✅ Folosește `@wraps(func)` din modulul `functools` pentru a păstra numele și docstring-ul original al funcției.  
✅ Evită decoratori care schimbă comportamentul răspunsurilor HTTP în mod neașteptat.  
✅ Folosește decoratori pentru validare, logare, securitate și performanță.  
✅ În aplicații mari, pune decoratori personalizați într-un fișier separat (ex: `decorators.py`).

---

## 📚 9. Resurse utile
- [Documentația Flask – Application Globals & Decorators](https://flask.palletsprojects.com/en/latest/)
- [Python Docs – functools.wraps](https://docs.python.org/3/library/functools.html)
- [Miguel Grinberg – Flask Advanced Topics](https://blog.miguelgrinberg.com/)

---

## ✅ Concluzie
Decoratori sunt o parte fundamentală a framework-ului Flask, permițând adăugarea de comportamente personalizate și control fine-grained asupra rutelor, cererilor și răspunsurilor.  
Prin înțelegerea lor, poți crea aplicații web mai modulare, sigure și ușor de extins.

---