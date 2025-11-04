# 🧰 Unelte pentru Test Driven Development (TDD)

## 🔍 Ce sunt uneltele TDD?

În **Test Driven Development (TDD)**, procesul de dezvoltare se bazează pe ciclul **Red → Green → Refactor**, iar pentru a-l susține eficient sunt necesare unelte dedicate de testare și automatizare.  
Aceste unelte ajută la **scrierea, rularea și raportarea testelor**, facilitând integrarea testelor în fluxul zilnic de lucru.

---

## ⚙️ Principalele unelte folosite în TDD

### 1. **Unittest**
- Framework-ul standard de testare inclus în Python.
- Urmează principiul xUnit (folosit și în alte limbaje, precum JUnit în Java sau NUnit în C#).
- Permite gruparea testelor în clase, setarea și curățarea mediului de test cu `setUp()` și `tearDown()`.
- Se rulează ușor cu:
  ```bash
  python -m unittest discover
  ```

**Avantaje:**
- Vine preinstalat cu Python.
- Simplu de folosit și bine integrat în IDE-uri.

---

### 2. **Nose / Nose2**
- O extensie peste `unittest` care oferă funcționalități suplimentare.
- Descoperă automat testele fără a le înregistra manual.
- Poate genera rapoarte detaliate și se integrează cu alte plugin-uri (ex: coverage, profiling).

**Exemplu de rulare:**
```bash
nosetests -v
```

**Caracteristici cheie:**
- Rulare paralelă a testelor.
- Generare de rapoarte în formate personalizate.
- Suport pentru „fixtures” și „plugins”.

---

### 3. **Pytest**
- Cea mai populară bibliotecă modernă de testare în Python.
- Suportă testare funcțională, integrare continuă și BDD (prin `pytest-bdd`).
- Are o sintaxă simplificată și permite utilizarea de *fixtures* reutilizabile.

**Exemplu de rulare:**
```bash
pytest -v
```

**Beneficii:**
- Descoperire automată a testelor.
- Rapoarte colorate și detaliate.
- Integrare ușoară cu `coverage` și `CI/CD` pipelines.

---

### 4. **Coverage.py**
- Instrument care măsoară **acoperirea codului** de către testele scrise.
- Indică ce linii de cod au fost executate și ce porțiuni au rămas netestate.

**Exemplu de rulare:**
```bash
coverage run -m pytest
coverage report -m
```

**Rezultate:**
- Afișează procentul de cod acoperit de teste.
- Poate genera rapoarte HTML interactive pentru analiză detaliată.

---

### 5. **Mock și MagicMock (din unittest.mock)**
- Folosite pentru a **simula obiecte externe** (API-uri, baze de date, fișiere etc.) în timpul testării.
- Permit testarea izolației funcțiilor fără a depinde de componente reale.

**Exemplu:**
```python
from unittest.mock import Mock
mock_api = Mock()
mock_api.get_data.return_value = {"status": "ok"}
```

---

## 🧩 Integrarea uneltelor TDD

TDD devine eficient atunci când aceste unelte sunt **combinate**:
- Scrii testele în **Unittest** sau **Pytest**.
- Rulezi testele cu **Nose2** sau **Pytest** pentru detalii suplimentare.
- Măsori acoperirea cu **Coverage.py**.
- Simulezi dependențele externe cu **Mock**.

---

## ✅ Concluzie

Uneltele pentru TDD fac posibilă o dezvoltare **iterativă, sigură și măsurabilă**.  
Prin utilizarea corectă a acestora, dezvoltatorii pot:
- Detecta rapid erorile,
- Crește acoperirea testelor,
- Automatiza verificările și integrarea codului.

> 💡 *Adevărata putere a TDD apare atunci când testarea devine o parte naturală a procesului de scriere a codului, nu o etapă de după.*
