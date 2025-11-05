# 🧪 Test Coverage

## 📖 Overview
**Test Coverage** (acoperirea testelor) este o măsură care arată cât de mult din codul sursă este acoperit de teste automate.  
Cu alte cuvinte, indică proporția de cod executată în timpul rulării testelor unitare.

Scopul este de a identifica părțile din cod care **nu sunt testate**, pentru a îmbunătăți calitatea aplicației și pentru a preveni bug-uri ascunse.

---

## 🎯 Benefits of Measuring Test Coverage
- 🔍 **Identifică codul netestat** – evidențiază funcțiile sau ramurile logice care nu sunt acoperite de teste.  
- ✅ **Asigură calitatea codului** – crește încrederea că modificările nu introduc defecte.  
- 🔁 **Îmbunătățește procesele CI/CD** – instrumentele pot bloca implementarea dacă acoperirea scade sub un anumit prag.  
- 📈 **Măsoară progresul testării** – oferă o metrică obiectivă asupra nivelului de testare.

---

## ⚙️ Tools for Test Coverage in Python

| Tool | Description |
|------|--------------|
| **coverage.py** | Cel mai popular tool pentru măsurarea acoperirii testelor. Se integrează cu `pytest` și `nose`. |
| **pytest-cov** | Plugin pentru `pytest` care adaugă suport pentru `coverage.py`. |
| **nose-cov** | Plugin pentru `nose`, permite generarea rapoartelor de acoperire. |
| **unittest** | Poate fi rulat împreună cu `coverage.py` pentru măsurători de bază. |

---

## 🧰 Installing the Required Tools
```bash
pip install coverage pytest pytest-cov
```

---

## ▶️ Running Tests with Coverage

### 🔹 1. Using `coverage.py` directly
```bash
coverage run -m pytest
coverage report -m
```

### 🔹 2. Using the `pytest-cov` plugin
```bash
pytest --cov=models --cov-report=term-missing -v
```

- `--cov=models` → specifică directorul sau modulul analizat  
- `--cov-report=term-missing` → arată exact liniile neacoperite  
- `-v` → rulare în mod *verbose*

---

## 📊 Example Output

```
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
models/__init__.py              8      0   100%
models/account.py              45      2    96%   88-89
tests/test_account.py          63      0   100%
---------------------------------------------------------
TOTAL                         116      2    98%
```

✅ În acest exemplu, acoperirea totală este **98%**, iar liniile 88–89 din `account.py` nu sunt testate.

---

## 🧱 Types of Coverage

| Type | Description |
|------|--------------|
| **Statement Coverage** | Măsoară ce linii de cod sunt executate. |
| **Branch Coverage** | Verifică dacă toate ramurile logice (if/else) au fost testate. |
| **Function Coverage** | Determină dacă toate funcțiile sunt apelate în timpul testelor. |
| **Condition Coverage** | Testează fiecare condiție booleană pentru ambele rezultate (True/False). |

---

## 🧮 Example: Generating HTML Report

```bash
coverage html
```

Apoi, deschide fișierul:
```
htmlcov/index.html
```
Acesta oferă o **vizualizare grafică** a acoperirii fiecărui fișier.

---

## 🚦 Best Practices
- Scrie teste înainte de cod (TDD) → crește acoperirea în mod natural.
- Țintește o acoperire de **80% sau mai mare**, dar evită „coverage for the sake of coverage”.
- Folosește rapoartele pentru a descoperi cod nefolosit sau blocuri logice neacoperite.
- Adaugă `pytest --cov` în pipeline-ul de CI/CD.

---

## 🧾 Summary
| Concept | Description |
|----------|-------------|
| **Goal** | Măsurarea proporției de cod testat |
| **Main Tool** | `coverage.py` |
| **Integration** | Cu `pytest` sau `nose` |
| **Output Options** | Terminal, XML, HTML |
| **Recommended Coverage** | Minimum 80% pentru cod critic |

---

## 📚 References
- [coverage.py documentation](https://coverage.readthedocs.io)
- [pytest-cov plugin](https://pytest-cov.readthedocs.io)
- IBM Skills Network – *Introduction to Test and Behavior Driven Development*
