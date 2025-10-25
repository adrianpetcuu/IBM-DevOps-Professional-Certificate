# 📘 Glosar: Administrarea Aplicațiilor cu Kubernetes

Acest glosar conține termenii esențiali folosiți în gestionarea aplicațiilor Kubernetes, împreună cu definițiile lor în limba română.

---

| Termen | Definiție |
|--------|------------|
| **Cluster Autoscaler (CA)** | O resursă API care **auto-scalează întregul cluster**, mărind sau reducând numărul de noduri disponibile pe care pot rula pod-urile. |
| **ConfigMap** | Un obiect API folosit pentru **stocarea datelor neconfidențiale** sub formă de perechi `cheie=valoare`. Pod-urile pot utiliza aceste date ca **variabile de mediu**, **argumente în linia de comandă** sau **fișiere de configurare** într-un volum. |
| **Horizontal Pod Autoscaler (HPA)** | O resursă API care **scalează automat numărul de replici ale pod-urilor**, pe baza utilizării țintă a CPU-ului sau a altor metrici personalizate. |
| **Analiză lingvistică** | Detectează tonul și intenția dintr-un text dat, analizând structura și semnificația acestuia. |
| **Catalogul IBM Cloud** | O platformă care oferă diverse **Servicii Cloud**, de la recunoaștere vizuală și procesare a limbajului natural până la creare de chatboți. |
| **Persistent Volume (PV)** | Un obiect API care reprezintă o **unitate de stocare persistentă** în cluster. Este o resursă generală, reutilizabilă, care **persistă dincolo de durata de viață a unui Pod** individual. |
| **Persistent Volume Claim (PVC)** | O cerere de resurse de stocare definite într-un `PersistentVolume`, care permite montarea acestora ca volum într-un container. |
| **Rolling Updates (Actualizări graduale)** | O metodă de **implementare automată și controlată** a modificărilor aplicației în pod-uri. Permite actualizări fără întreruperi și oferă posibilitatea de **rollback** în caz de eroare. |
| **Secrets (Secrete)** | Obiecte Kubernetes care stochează **informații sensibile**, cum ar fi parole, token-uri OAuth sau chei SSH. |
| **Service Binding (Legarea serviciilor)** | Procesul prin care o aplicație consumă **servicii externe** sau **servicii de tip back-end**, precum API-uri REST, baze de date sau servicii de mesagerie. |
| **Tone Analyzer Service** | Un serviciu IBM Cloud folosit pentru a **analiza tonul emoțional și intenția** unui text. Este adesea utilizat ca exemplu pentru explicarea conceptului de service binding. |
| **Vertical Pod Autoscaler (VPA)** | O resursă API care **adaugă resurse suplimentare (CPU, memorie)** unui container existent. Permite scalarea **verticală** a unui serviciu în cadrul unui cluster. |
| **Volume (Volum)** | Un director care conține date, accesibil de către mai multe containere din același Pod. |
| **Volume Mount (Montare volum)** | Procesul de **montare a unui volum declarat** într-un container din același Pod, pentru a-i oferi acces la date. |
| **Volume Plugin (Plugin de volum)** | Permite **integrarea sistemelor de stocare** externe în Kubernetes, făcând posibile volume persistente în Pod-uri. |

---

📘 *Acest glosar oferă o bază solidă de termeni pentru administratori de sistem, DevOps engineers și dezvoltatori care lucrează cu Kubernetes.*
