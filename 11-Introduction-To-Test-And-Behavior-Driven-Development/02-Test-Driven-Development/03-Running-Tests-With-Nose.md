# 🧪 Rularea testelor cu Nose

## 🔍 Ce este Nose?

**Nose** este un framework de testare pentru Python construit peste biblioteca standard `unittest`.  
El simplifică procesul de **descoperire, organizare și rulare a testelor** și oferă funcționalități suplimentare față de `unittest`, precum:

- Detectarea automată a testelor.
- Suport pentru plugin-uri.
- Rapoarte detaliate și colorate.
- Integrare cu code coverage și profiling.

---

## ⚙️ Instalarea Nose

Pentru a instala `nose`, folosește comanda:
```bash
pip install nose
```

După instalare, poți verifica versiunea:
```bash
nosetests --version
```

> ⚠️ Atenție: `nose` nu mai este activ mentenabil, fiind înlocuit de `nose2` sau `pytest`, dar este încă utilizat în proiecte educaționale și de tranziție.

---

## ▶️ Rularea testelor cu Nose

### 1. **Rulare de bază**
Comanda principală pentru a rula testele este:
```bash
nosetests
```
Aceasta caută automat toate fișierele care respectă convenția:
- numele începe cu `test_` sau se termină cu `_test.py`
- testele sunt definite prin metode care încep cu `test_`

### 2. **Rulare cu detalii suplimentare (verbose mode)**
Pentru a obține mai multe informații despre fiecare test rulat:
```bash
nosetests -v
```

### 3. **Oprirea la prima eroare**
Dacă vrei ca rularea testelor să se oprească imediat la primul eșec:
```bash
nosetests --stop
```

### 4. **Rulare a testelor dintr-un fișier specific**
Poți rula un fișier anume:
```bash
nosetests tests/test_example.py
```

---

## 🧩 Exemple de utilizare

```python
# test_math.py
import math
from nose.tools import assert_equal, assert_almost_equal

def test_square_root():
    assert_equal(math.isqrt(9), 3)

def test_pi_value():
    assert_almost_equal(math.pi, 3.14, places=2)
```

Rularea testelor:
```bash
nosetests -v
```
Rezultat:
```
test_square_root ... ok
test_pi_value ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

---

## 📊 Integrarea cu Code Coverage

Pentru a măsura cât din cod este acoperit de teste:
```bash
nosetests --with-coverage
```
Opțional, poți specifica un modul anume:
```bash
nosetests --with-coverage --cover-package=app
```

---

## 🧩 Alte opțiuni utile

| Opțiune | Descriere |
|----------|------------|
| `--stop` | Oprește rularea la prima eroare |
| `--with-coverage` | Activează măsurarea acoperirii codului |
| `--with-xunit` | Generează rapoarte compatibile cu Jenkins |
| `--nologcapture` | Afișează toate logurile din timpul testării |
| `-v` | Activează modul detaliat (verbose) |

---

## ✅ Concluzie

**Nose** este o unealtă puternică pentru rularea testelor în Python, oferind mai multe funcționalități decât `unittest` standard.  
Chiar dacă este mai vechi, `nose` rămâne o alegere utilă pentru învățarea conceptelor de testare automată și pentru proiecte educaționale.

> 💡 *Pentru proiecte moderne se recomandă utilizarea `pytest`, însă principiile rămân aceleași: automatizare, izolare și verificare constantă a codului.*
