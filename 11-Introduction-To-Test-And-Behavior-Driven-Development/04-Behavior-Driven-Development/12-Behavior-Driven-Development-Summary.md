    
# Rezumat: Behavior Driven Development (BDD)

Felicitări! Ai finalizat acest modul.  
În acest moment, ar trebui să știi următoarele:

---

## Ce este BDD?
**Behavior Driven Development (BDD)** este o abordare de dezvoltare orientată pe testare care se asigură că aplicația se comportă conform intenției.

În procesul de testare software, **nivelurile potrivite pentru aplicarea BDD** sunt:
- Testarea de integrare  
- Testarea de sistem  
- Testarea de acceptanță

BDD descrie comportamentele într-o **sintaxă unică**, pe care o pot înțelege ușor experții de domeniu, testerii, dezvoltatorii și stakeholderii.

---

## Fluxul de lucru BDD
Fluxul de lucru BDD include **trei pași principali**:

1. Crearea de exemple sau scenarii care descriu comportamentul dorit.  
2. Rularea acestor exemple ca teste automatizate.  
3. Scrierea de teste suplimentare, dacă este necesar.

Fluxul de lucru BDD duce la un document unic care acționează atât ca **specificație**, cât și ca **test** pentru software.

---

## Construirea unei specificații BDD
Pentru a construi o specificație BDD:
- Scrie o **funcționalitate (Feature)** și scenarii folosind sintaxa **Given / When / Then**.
- Instrumente precum **Cucumber** și **Behave** folosesc sintaxa **Gherkin**, în timp ce altele precum **Concordion** folosesc alte tipuri de specificații.

Când alegi un instrument BDD, ține cont de limbajele de programare și tipurile de sintaxă suportate.

---

## Rularea testelor Behave
Pentru a rula **Behave**, trebuie să creezi următoarea structură de directoare:

```
Features/
 ├── *.feature       # fișiere cu scenarii Gherkin
 └── steps/          # fișiere Python cu pașii de test
```

Când Behave este executat, acesta:
1. Citește instrucțiunile Gherkin din fiecare fișier `.feature`.  
2. Caută pașii Python corespunzători în fișierele `steps`.  
3. Execută funcțiile de test definite în acei pași.

---

## Configurarea mediului Behave
Pentru a configura mediul de lucru în Behave, trebuie să:
- Importezi `getenv()` și alte module necesare.  
- Declari variabilele globale din mediul de rulare.  
- Definesti **fixture-urile** de test.

---

## Sfaturi pentru scrierea fișierelor Feature
✅ Menține **consistența** între scenarii.  
✅ Gândește din perspectiva **experienței utilizatorului**.  
✅ Adaugă indicii vizuale care arată că sistemul a răspuns la o cerere.

Poți folosi o secțiune **Background** pentru a stabili aceeași stare inițială înainte de fiecare scenariu.

---

## Automatizarea testelor web cu Selenium
Pentru a automatiza interacțiunile cu paginile web, trebuie să:
1. Inițializezi Selenium în mediul Behave.  
2. Alegi una dintre metodele Selenium pentru identificarea elementelor (ID, clasă, nume etc.).  
3. Definiți acțiunea care trebuie efectuată asupra elementului (click, input etc.).

---

## Scrierea pașilor în Python
Pentru a scrie un pas Python:
1. Identifică cuvântul cheie și textul Gherkin.  
2. Scrie un pas Python corespunzător instrucțiunii.  
3. Creează o funcție care implementează logica acelui pas.

---

## Încărcarea datelor de test în Behave
Poți încărca și itera date de test printr-un **tabel de date** plasat în secțiunea *Background* a unei funcționalități și apoi să parcurgi conținutul acestuia cu o buclă `for`.

---

# 📘 Termeni și definiții

| Termen | Definiție |
|--------|------------|
| **after_all()** | Cod care se execută o singură dată după toate funcționalitățile. |
| **after_feature()** | Cod care se execută după fiecare feature. |
| **after_scenario()** | Cod care se execută după fiecare scenariu. |
| **after_step()** | Cod care se execută după fiecare pas. |
| **after_tag()** | Cod care se execută după fiecare tag. |
| **And** | Cuvânt cheie folosit pentru a înlocui repetarea Given/When/Then în serie. |
| **API** | Interfață de programare a aplicației (Application Programming Interface). |
| **Background** | Fixture utilizat pentru a specifica contextul înainte de fiecare scenariu. |
| **BASE_URL** | Variabilă de mediu care indică locația sistemului testat. |
| **before_all()** | Cod care se execută o singură dată înainte de toate funcționalitățile. |
| **before_feature()** | Cod care se execută înainte de fiecare feature. |
| **before_scenario()** | Cod care se execută înainte de fiecare scenariu. |
| **before_step()** | Cod care se execută înainte de fiecare pas. |
| **before_tag()** | Cod care se execută înainte de fiecare tag. |
| **BDD** | Metodologie axată pe comportamentul sistemului, observat din exterior. |
| **Concordion** | Instrument open-source BDD pentru Java, folosind limbaj natural pentru specificații. |
| **context.driver.quit()** | Închide browserul după finalizarea testelor pentru a elibera memoria. |
| **context.table** | Variabilă pentru încărcarea datelor dintr-un tabel (array de dicționare). |
| **Cucumber** | Cel mai vechi instrument BDD care folosește sintaxa Gherkin. |
| **Feature** | Primul cuvânt cheie dintr-un fișier Gherkin, urmat de titlu. |
| **Features folder** | Folder care conține fișiere `.feature` și subfolderul `steps`. |
| **getenv()** | Importează parametrii de configurare din mediul de execuție. |
| **Gherkin** | Cea mai folosită sintaxă în BDD. |
| **Given keyword** | Set de condiții prealabile necesare pentru test. |
| **Integration testing** | Testarea combinată a componentelor pentru a detecta erori de interacțiune. |
| **Scenario** | Descrie un comportament specific al unei funcționalități. |
| **Selenium** | Set de instrumente pentru automatizarea activităților browserului web. |
| **Specification** | Descriere a modului în care sistemul ar trebui să se comporte. |
| **Steps folder** | Folder care conține fișiere Python ce corespund pașilor Gherkin. |
| **step_impl()** | Funcție care implementează un pas Gherkin. |
| **System testing** | Testare completă end-to-end pentru validarea cerințelor sistemului. |
| **TDD** | Test Driven Development – se concentrează pe logica internă a sistemului. |
| **Then keyword** | Rezultatul așteptat în urma unei acțiuni a utilizatorului. |
| **Unit testing** | Testarea componentelor individuale ale aplicației. |
| **WAIT_SECONDS** | Variabilă de mediu care definește timpul de așteptare pentru răspunsul UI. |
| **When keyword** | Reprezintă acțiunea efectuată de utilizator asupra sistemului testat. |

---

## Concluzie
BDD oferă o abordare colaborativă între echipele tehnice și non-tehnice,  
unificând specificațiile, testarea și documentația într-un singur flux logic, clar și automatizabil.
