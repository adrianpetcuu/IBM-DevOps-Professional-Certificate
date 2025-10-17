# 🧩 Flask – Rute Dinamice (Dynamic Routes)

Acest ghid explică modul în care poți utiliza **rute dinamice** în Flask pentru a crea URL-uri flexibile și personalizabile.  
Rutele dinamice permit trimiterea de variabile direct prin URL și sunt esențiale pentru aplicații web și API-uri REST.

---

## 🚀 1. Ce este o rută dinamică?

O **rută dinamică** este o cale URL care conține **variabile** transmise serverului.  
Exemplu: `/user/<username>` → transmite valoarea `username` către funcția Python asociată.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def greet_user(username):
    return f"Salut, {username}!"
```

📍 Accesare:
```
http://localhost:5000/user/Ana
```
Rezultat: `Salut, Ana!`

---

## 🧱 2. Tipuri de variabile în rute

Flask permite specificarea **tipului de date** al variabilei direct în URL.

| Tip | Sintaxă | Conversie | Exemplu |
|------|----------|------------|----------|
| `string` (implicit) | `<string:valoare>` | Orice text fără `/` | `/user/Ana` |
| `int` | `<int:valoare>` | Număr întreg | `/age/25` |
| `float` | `<float:valoare>` | Număr zecimal | `/pi/3.14` |
| `path` | `<path:valoare>` | Include `/` | `/file/images/logo.png` |
| `uuid` | `<uuid:id>` | Identificator unic (UUID) | `/person/550e8400-e29b-41d4-a716-446655440000` |

---

## 🧩 3. Exemple de utilizare

### 🔹 String (implicit)
```python
@app.route('/hello/<name>')
def hello(name):
    return f"Bun venit, {name}!"
```

### 🔹 Integer
```python
@app.route('/square/<int:num>')
def square(num):
    return f"Patratul lui {num} este {num ** 2}."
```

### 🔹 Float
```python
@app.route('/price/<float:value>')
def price(value):
    return f"Pretul este {value:.2f} lei."
```

### 🔹 Path (include slash-uri)
```python
@app.route('/file/<path:subpath>')
def show_path(subpath):
    return f"Calea completă este: {subpath}"
```

---

## 🔗 4. Mai multe variabile într-o rută

Poți folosi mai multe variabile în același URL:

```python
@app.route('/sum/<int:a>/<int:b>')
def suma(a, b):
    return f"Suma este {a + b}"
```

Exemplu:
```
http://localhost:5000/sum/10/5 → Suma este 15
```

---

## 🔄 5. Redirecționări și `url_for()`

Funcția `url_for()` generează automat linkuri către funcții Flask.

```python
from flask import redirect, url_for

@app.route('/old/<username>')
def old(username):
    return redirect(url_for('new', user=username))

@app.route('/new/<user>')
def new(user):
    return f"Bun venit la noua pagină, {user}!"
```

Accesare:
```
/old/Ana → redirecționează către /new/Ana
```

---

## 🧮 6. Validare tipuri în rute

Dacă specifici `<int:id>`, iar utilizatorul introduce un text, Flask va returna automat **404 Not Found**.

```python
@app.route('/user/<int:id>')
def get_user(id):
    return f"ID-ul utilizatorului este {id}."
```

Exemplu valid: `/user/5` → funcționează  
Exemplu invalid: `/user/abc` → 404 Not Found

---

## 🧠 7. Exemple combinate (GET + variabile dinamice)

```python
from flask import request, jsonify

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    price = request.args.get('price', 10)
    return jsonify({"id": id, "price": float(price)})
```

Exemplu:
```
/product/5?price=25.5
```
Răspuns:
```json
{"id": 5, "price": 25.5}
```

---

## 🗂️ 8. Structură recomandată pentru aplicații Flask dinamice

```
project/
├── app.py
├── routes/
│   ├── users.py
│   ├── products.py
│   └── orders.py
└── templates/
    └── index.html
```

Această separare pe module te ajută să organizezi rutele pe domenii logice (ex: utilizatori, produse, comenzi).

---

## ⚙️ 9. Testare cu `curl`

```bash
curl http://localhost:5000/user/Ana
curl http://localhost:5000/sum/4/9
curl http://localhost:5000/price/9.99
```

---

## 📊 10. Cod complet exemplu

```python
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Salut, {name}!"})

@app.route('/square/<int:num>')
def square(num):
    return jsonify({"number": num, "square": num ** 2})

@app.route('/redirect/<user>')
def redirect_example(user):
    return redirect(url_for('hello', name=user))

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 📚 11. Resurse utile

- [Documentația Flask – Routing](https://flask.palletsprojects.com/en/latest/quickstart/#variable-rules)
- [Miguel Grinberg – Flask Mega Tutorial](https://blog.miguelgrinberg.com/)
- [Werkzeug Routing Converters](https://werkzeug.palletsprojects.com/en/latest/routing/)

---

## 🧭 Concluzie

Rutele dinamice fac aplicațiile Flask **flexibile** și **interactive**.  
Cu ajutorul tipurilor de variabile și al funcției `url_for()`, poți construi aplicații REST moderne, sigure și ușor de extins.

> 🔹 Rute dinamice = flexibilitate maximă pentru API-uri și pagini web personalizate.

---
