
# Configurarea Mediului (Environment Setup)

## Introducere
În cadrul framework-ului **Behave** (pentru testare BDD în Python), fișierul **environment.py** este folosit pentru a configura și controla procesele de inițializare (setup) și închidere (teardown) pentru execuția testelor.

Acest fișier permite definirea unor funcții reutilizabile care sunt apelate automat în momente specifice ale ciclului de viață al testului — înainte și după rularea *feature*-urilor, *scenariilor* sau *pașilor*.

---

## Scopul Configurării Mediului
Configurarea mediului oferă un mediu de testare constant, curat și controlat prin:
- Inițializarea configurațiilor globale.
- Gestionarea resurselor partajate (cum ar fi drivere web, baze de date sau API-uri).
- Curățarea după execuția testelor pentru a evita interferențele între rulari.

---

## Funcții Comune din environment.py

### 1. before_all(context)
Se execută **o singură dată înaintea tuturor testelor**.
```python
def before_all(context):
    print("Inițializare mediu de testare...")
    context.config.setup_logging()
```
✅ Util pentru inițializarea resurselor globale, configurarea parametrilor sau pornirea serviciilor externe.

### 2. after_all(context)
Se execută **o singură dată după terminarea tuturor testelor**.
```python
def after_all(context):
    print("Eliberare resurse și închidere mediu...")
    context.browser.quit()
```
✅ Util pentru curățare, oprirea driverelor sau închiderea conexiunilor.

### 3. before_feature(context, feature)
Se execută **înainte de fiecare fișier de tip feature**.
```python
def before_feature(context, feature):
    print(f"Pornire feature: {feature.name}")
```
✅ Util pentru configurări specifice fiecărui feature, cum ar fi încărcarea de date de test.

### 4. after_feature(context, feature)
Se execută **după fiecare fișier de tip feature**.
```python
def after_feature(context, feature):
    print(f"Feature finalizat: {feature.name}")
```
✅ Util pentru resetarea resurselor după rularea fiecărui feature.

### 5. before_scenario(context, scenario)
Se execută **înaintea fiecărui scenariu**.
```python
def before_scenario(context, scenario):
    print(f"Începe scenariul: {scenario.name}")
```
✅ Folosit frecvent pentru deschiderea browserului, conectarea la baze de date sau resetarea datelor.

### 6. after_scenario(context, scenario)
Se execută **după fiecare scenariu**.
```python
def after_scenario(context, scenario):
    print(f"Scenariu finalizat: {scenario.name}")
```
✅ Util pentru închiderea conexiunilor, capturarea logurilor sau realizarea capturilor de ecran în caz de eșec.

---

## Exemplu cu Selenium
```python
from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()

def after_all(context):
    context.browser.quit()
```

---

## Concluzii Cheie
- `environment.py` controlează evenimentele ciclului de viață al testelor.  
- Asigură că testele încep dintr-o stare curată și că resursele sunt eliberate corect.  
- Reduce redundanța prin centralizarea gestionării mediului.  

---

Hook-urile din Behave fac testele automate mai **modulare, fiabile și ușor de întreținut**, garantând comportament consistent între multiple execuții.
