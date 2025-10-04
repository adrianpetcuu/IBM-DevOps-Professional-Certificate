# 🧮 Python Expressions and Variables — Expresii și Variabile

## 📘 Ce sunt variabilele
O **variabilă** este un spațiu de memorie folosit pentru a stoca o valoare.  
În Python, o variabilă se creează automat atunci când îi atribui o valoare folosind operatorul `=`.

Exemplu:
```python
x = 10
nume = "Ana"
```
Aici, `x` este o variabilă de tip `int`, iar `nume` este o variabilă de tip `str`.

### 🔹 Reguli pentru numele variabilelor
- Numele trebuie să înceapă cu o **literă** sau cu un **underscore (`_`)**.  
- Poate conține **litere, cifre și underscore**, dar **nu poate începe cu o cifră**.  
- Python face **diferență între majuscule și minuscule** (`nume` ≠ `Nume`).  
- Evită folosirea cuvintelor rezervate (ex: `for`, `if`, `True`, `class`).

---

## 🔢 Ce sunt expresiile
O **expresie** este o combinație de **valori**, **variabile** și **operatori** care produce o nouă valoare atunci când este evaluată.

Exemplu:
```python
a = 5
b = 2
suma = a + b
```
Expresia `a + b` este evaluată, iar rezultatul (`7`) este atribuit variabilei `suma`.

---

## ➕ Operatorii principali în Python

| Operator | Descriere | Exemplu | Rezultat |
|-----------|------------|----------|-----------|
| `+` | Adunare | `5 + 3` | `8` |
| `-` | Scădere | `10 - 4` | `6` |
| `*` | Înmulțire | `3 * 5` | `15` |
| `/` | Împărțire (rezultat float) | `10 / 3` | `3.3333` |
| `//` | Împărțire întreagă | `10 // 3` | `3` |
| `%` | Restul împărțirii | `10 % 3` | `1` |
| `**` | Ridicare la putere | `2 ** 3` | `8` |

---

## 🧠 Atribuirea și reutilizarea variabilelor
Poți folosi o variabilă într-o expresie pentru a-i actualiza valoarea.

Exemplu:
```python
x = 5
x = x + 2   # noua valoare a lui x este 7
```
Python evaluează partea dreaptă a expresiei (`x + 2`) și atribuie rezultatul variabilei `x`.

De asemenea, poți combina mai multe operații:
```python
x = 10
y = x * 2 + 5
```

---

## 🔄 Atribuire multiplă
Python permite atribuirea mai multor variabile simultan:
```python
a, b, c = 1, 2, 3
```
Aceasta este o metodă rapidă și elegantă de inițializare a variabilelor.

---

## 🧩 Tipuri de expresii
- **Aritmetice** – implică operații numerice (`+`, `-`, `*`, `/` etc.)  
- **Logice** – returnează `True` sau `False` (`and`, `or`, `not`)  
- **De comparație** – compară valori (`==`, `!=`, `>`, `<`, `>=`, `<=`)  
- **De concatenare** – unesc șiruri de caractere (`"Ana" + " " + "Maria"` → `"Ana Maria"`)

---

## 🏁 Concluzie
Expresiile și variabilele sunt **fundamentele programării în Python**.  
Ele permit:
- stocarea și manipularea datelor,  
- efectuarea de calcule,  
- și crearea de programe dinamice și flexibile.

> 💬 *„În Python, totul pornește de la expresii simple și variabile clare.”*
