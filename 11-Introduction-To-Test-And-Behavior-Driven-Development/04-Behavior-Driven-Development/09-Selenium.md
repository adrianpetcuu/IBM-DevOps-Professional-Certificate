
# Introducere în Selenium

## Ce este Selenium?
**Selenium** este un framework open-source utilizat pentru automatizarea testării aplicațiilor web.  
Permite interacțiunea automată cu browserele web — la fel cum ar face un utilizator real — pentru a verifica funcționalitățile unei aplicații.

Selenium este compatibil cu cele mai populare limbaje de programare (Python, Java, C#, Ruby, JavaScript) și cu toate browserele majore: **Chrome, Firefox, Edge, Safari**.

---

## Componentele Selenium
Suita Selenium este alcătuită din mai multe instrumente:

### 1. **Selenium WebDriver**
Este componenta principală care permite interacțiunea cu browserele.  
Prin WebDriver, putem controla un browser (ex: Chrome) și executa acțiuni precum click, introducere text, navigare etc.

### 2. **Selenium IDE**
O extensie pentru browser care înregistrează automat acțiunile utilizatorului și generează scripturi de testare.  
Este ideală pentru începători.

### 3. **Selenium Grid**
Permite rularea testelor pe mai multe browsere, dispozitive și sisteme de operare simultan — pentru testare paralelă și distribuție a sarcinilor.

---

## Instalarea Selenium în Python

### 1. Instalează biblioteca:
```bash
pip install selenium
```

### 2. Instalează driverul corespunzător browserului (ex. ChromeDriver):
- Descarcă de la: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Asigură-te că versiunea ChromeDriver se potrivește cu versiunea browserului Chrome.

### 3. Exemplu de test simplu:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Pornește browserul Chrome
browser = webdriver.Chrome()

# Accesează un website
browser.get("https://www.example.com")

# Găsește un element și face click pe el
button = browser.find_element(By.ID, "login-button")
button.click()

# Verifică dacă titlul paginii este corect
assert "Example Domain" in browser.title

# Închide browserul
browser.quit()
```

---

## Selenium și Behave

Selenium se integrează perfect cu **Behave** pentru testarea BDD (Behavior Driven Development).  
Astfel, pașii din scenariile `.feature` pot fi legați de acțiuni reale în browser.

### Exemplu:
```gherkin
Feature: Autentificare utilizator
  Scenario: Login reușit
    Given browserul este deschis pe pagina de login
    When utilizatorul introduce date valide
    Then este redirecționat către dashboard
```

```python
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('browserul este deschis pe pagina de login')
def step_open_login_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://example.com/login")

@when('utilizatorul introduce date valide')
def step_enter_valid_data(context):
    context.browser.find_element(By.ID, "username").send_keys("testuser")
    context.browser.find_element(By.ID, "password").send_keys("password123")
    context.browser.find_element(By.ID, "login-button").click()

@then('este redirecționat către dashboard')
def step_check_dashboard(context):
    assert "dashboard" in context.browser.current_url
    context.browser.quit()
```

---

## Cele mai frecvente acțiuni în Selenium
- **Navigare**: `browser.get(url)`  
- **Click**: `element.click()`  
- **Introducere text**: `element.send_keys("text")`  
- **Citire text**: `element.text`  
- **Așteptare element**: `WebDriverWait(browser, 10).until(...)`  
- **Captură de ecran**: `browser.save_screenshot("test.png")`  

---

## Recomandări bune de practică
✅ Folosește **așteptări explicite** pentru elemente (evită `time.sleep()`).  
✅ Închide întotdeauna browserul la finalul testelor.  
✅ Folosește **Page Object Model (POM)** pentru o structură clară a testelor.  
✅ Rulează testele în mod **headless** (fără interfață) pe servere CI/CD.  

---

## Concluzie
**Selenium** este un instrument puternic pentru testarea automată a aplicațiilor web.  
Combinat cu **Behave**, oferă o metodă elegantă și scalabilă pentru a valida funcționalitățile aplicației într-un mod automatizat, clar și orientat pe comportament.
