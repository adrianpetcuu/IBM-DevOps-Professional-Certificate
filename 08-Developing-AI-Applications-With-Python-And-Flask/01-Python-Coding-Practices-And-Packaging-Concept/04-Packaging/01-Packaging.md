# 📦 Packaging în Python (Ghid practic în română)

Acest README te ghidează prin pașii esențiali pentru a împacheta, distribui și instala proiectele tale Python în mod profesionist (sdist, wheel, PyPI, entry points).

---

## 1) Noțiuni de bază

- **Modul**: fișier `.py` (ex: utils.py).
- **Pachet**: director cu cod + `__init__.py` (ex: mypkg/).
- **Distribuție**:
  - **sdist** (source distribution) – arhivă cu surse.
  - **wheel** (binar preconstruit) – instalare rapidă (`.whl`).

Recomandat: layout-ul **src/** pentru a evita importuri din directorul curent în timpul testelor.

```
project/
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ src/
│  └─ mypkg/
│     ├─ __init__.py
│     └─ core.py
└─ tests/
   └─ test_core.py
```

---

## 2) `pyproject.toml` (PEP 517/518)

Minimal pentru **setuptools**:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypkg"
version = "0.1.0"
description = "Un exemplu de pachet"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [{ name = "Numele tău", email = "email@exemplu.com" }]
dependencies = [
  "requests>=2.32",
]

[project.urls]
Homepage = "https://exemplu.com/mypkg"
Issues = "https://exemplu.com/mypkg/issues"

[project.scripts]
mypkg-cli = "mypkg.cli:main"   # expune o comandă în terminal

[tool.setuptools.packages.find]
where = ["src"]
```

> Alternativ, poți folosi **hatchling**, **poetry** sau **flit** ca build-backend.

---

## 3) Conținutul pachetului

`src/mypkg/__init__.py` poate expune API-ul public (ex: `from .core import calc`).  
Fișiere non-Python (șabloane, date) se includ prin `setuptools`:
- În `pyproject.toml`: `include-package-data = true` (în `[tool.setuptools]`) și reguli în `MANIFEST.in`.
- Sau `package_data={"mypkg": ["data/*.json"]}` în `setup.cfg`/config echivalent.

Exemplu `MANIFEST.in`:
```
include README.md LICENSE
recursive-include src/mypkg/data *.json
```

---

## 4) Versiuni și changelog

- Folosește **SemVer**: MAJOR.MINOR.PATCH (ex: 1.4.2).
- Ține un `CHANGELOG.md` cu ce s-a schimbat.
- Evită să hardcodezi versiunea în multiple locuri; seteaz-o în `pyproject.toml` (un singur adevăr).

---

## 5) Construire pachet

Instalează unealta modernă de build:
```bash
python -m pip install --upgrade build
```

Construiește sdist + wheel în `dist/`:
```bash
python -m build
# vei obține: dist/mypkg-0.1.0.tar.gz și dist/mypkg-0.1.0-py3-none-any.whl
```

Verifică wheel-ul:
```bash
python -m pip install dist/mypkg-0.1.0-py3-none-any.whl
```

Dezinstalare:
```bash
python -m pip uninstall mypkg -y
```

---

## 6) Publicare pe TestPyPI / PyPI

Instalează **twine**:
```bash
python -m pip install twine
```

Încarcă pe **TestPyPI** (ideal pentru verificare):
```bash
python -m twine upload --repository testpypi dist/*
# setează credențialele în .pypirc sau le introduci la prompt
```

Dacă totul e OK, încarcă pe **PyPI**:
```bash
python -m twine upload dist/*
```

Instalare din TestPyPI (exemplu):
```bash
python -m pip install -i https://test.pypi.org/simple/ mypkg==0.1.0
```

---

## 7) Entry points (CLI)

În `pyproject.toml`:
```toml
[project.scripts]
mypkg = "mypkg.cli:main"
```
`src/mypkg/cli.py`:
```python
def main():
    print("Salut din CLI!")
```

După instalare, comanda `mypkg` devine disponibilă în terminal.

---

## 8) Bune practici

- **Layout src/** + **testare** înainte de release.
- **Versionare semantică** + tag-uri Git (ex: `git tag v0.1.0`).
- **Tip hints** + `py.typed` dacă expui type info pentru consumatori.
- **CI/CD**: rulează teste + build + upload automat pe tag (GitHub Actions).
- **Evita dependințe inutile**; declare-le strict în `[project.dependencies]`.
- **Licență** și **classifiers** în `pyproject.toml` pentru claritate.
- Folosește `pip install -e .` pentru dezvoltare locală (editable mode).

---

## 9) Workflow rapid de dezvoltare

```bash
# 1. creează virtualenv
python -m venv .venv && source .venv/bin/activate

# 2. instalează dependențele de dev
python -m pip install -U pip build twine pytest

# 3. rulează testele
pytest -q

# 4. build
python -m build

# 5. upload pe TestPyPI
python -m twine upload --repository testpypi dist/*
```

---

## 10) Debugging instalare

- Importurile eșuează? Verifică `find_packages`/`packages.find` și layout-ul `src/`.
- Fisierul lipsă în wheel? Adaugă reguli în `MANIFEST.in` / `package_data`.
- CLI nu apare? Verifică `[project.scripts]` și reinstalează pachetul.
- Conflict de versiuni? Păstrează intervale de versiuni rezonabile (ex: `requests>=2.32,<3`).

---

## Resurse

- Packaging User Guide: https://packaging.python.org/
- PEP 517/518 (pyproject.toml și build backends)
- Setuptools: https://setuptools.pypa.io/
- Build: https://pypa-build.readthedocs.io/
- Twine: https://twine.readthedocs.io/
- TestPyPI: https://test.pypi.org/

---

## Concluzie

Cu un `pyproject.toml` curat, layout `src/`, teste automate și publicare prin `build` + `twine`, proiectul tău este pregătit pentru distribuție profesională (wheel + sdist) și instalare rapidă de către utilizatori.
