# 🌐 Deploying Web Applications Using Flask

Acest document explică procesul de **dezvoltare, configurare și implementare (deploy)** a unei aplicații web folosind **Flask**, unul dintre cele mai populare framework-uri Python pentru dezvoltare web ușoară și rapidă.

---

## 🔍 Scopul laboratorului
În acest modul vei învăța cum să:
- Configurezi o aplicație Flask pregătită pentru producție;
- Structurezi proiectul cu directoare dedicate pentru cod, șabloane și fișiere statice;
- Rulezi aplicația local și pe un server extern;
- Înțelegi procesul de *deployment* și bunele practici pentru aplicațiile Flask.

---

## 🧱 Structura tipică a unui proiect Flask
```plaintext
my_flask_app/
│
├── app.py                # Punctul de intrare al aplicației
├── requirements.txt      # Pachetele necesare pentru instalare
├── static/               # Imagini, CSS, JS
├── templates/            # Fișiere HTML (folosind Jinja2)
└── README.md
```

---

## ⚙️ 1. Configurarea mediului local

1. Instalează Flask:
   ```bash
   pip install flask
   ```

2. Creează fișierul principal `app.py`:
   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route("/")
   def home():
       return render_template("index.html")

   if __name__ == "__main__":
       app.run(debug=True)
   ```

3. Creează directoarele:
   ```bash
   mkdir templates static
   ```

4. Adaugă fișierul HTML principal:
   ```html
   <!-- templates/index.html -->
   <h1>Bine ai venit în aplicația Flask!</h1>
   ```

5. Rulează aplicația:
   ```bash
   python app.py
   ```

Accesează în browser: 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 2. Configurarea pentru deployment

Pentru a implementa aplicația pe un server, sunt necesare câteva ajustări:

### a) Dezactivează `debug=True`
În `app.py`:
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
```

### b) Creează fișierul `requirements.txt`
Comandă:
```bash
pip freeze > requirements.txt
```
Acest fișier va lista toate pachetele necesare pentru instalare pe server.

---

## ☁️ 3. Deploy pe un server (ex: Render, PythonAnywhere, Heroku)

### Ex. Render
1. Creează un cont pe [https://render.com](https://render.com).
2. Conectează-ți repository-ul GitHub care conține aplicația Flask.
3. Adaugă fișierul `requirements.txt` și specifică comanda de start:
   ```bash
   gunicorn app:app
   ```

### Ex. PythonAnywhere
1. Încarcă fișierele din proiect în contul tău PythonAnywhere.
2. Configurează aplicația Flask în secțiunea **Web** → **Add a new web app**.
3. Selectează „Manual configuration (Flask)”.
4. Specifică fișierul `app.py` și calea către aplicația ta.

---

## 🧩 4. Gestionarea fișierelor statice și a șabloanelor

### a) Fișiere statice (`/static`)
În fișierul HTML:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

### b) Șabloane (`/templates`)
Flask folosește motorul de template-uri **Jinja2**.
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}
{% block content %}
<h1>Bine ai venit!</h1>
{% endblock %}
```

---

## 🔒 5. Bune practici pentru producție
- **Nu folosi `debug=True`** în mediul live.
- Utilizează un server WSGI (ex: **Gunicorn** sau **uWSGI**).
- Pune aplicația în spatele unui **reverse proxy** (ex: Nginx).
- Utilizează variabile de mediu pentru parole, chei API etc.
- Folosește loguri pentru erori și monitorizare.

---

## 🧠 6. Exemple de deployment real

### Exemplu cu Gunicorn + Nginx
```bash
# Instalează gunicorn
pip install gunicorn

# Rulează aplicația Flask prin gunicorn
gunicorn -w 4 app:app
```

Apoi configurează un server Nginx pentru a redirecționa traficul HTTP către Gunicorn.

---

## ✅ Concluzie
Prin acest laborator, ai învățat să:
- Rulezi o aplicație Flask local;
- Organizezi structura proiectului web;
- Configurezi un mediu pregătit pentru producție;
- Publici aplicația online folosind Render, Heroku sau PythonAnywhere.

Flask oferă un mod simplu și eficient de a crea aplicații web scalabile și rapide! 🚀

---
