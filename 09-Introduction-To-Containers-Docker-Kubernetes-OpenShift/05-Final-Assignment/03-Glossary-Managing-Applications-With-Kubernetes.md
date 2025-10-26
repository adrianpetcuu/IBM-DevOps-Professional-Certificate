# ⚙️ Administrarea aplicațiilor cu Kubernetes (Managing Applications with Kubernetes)

## 🧩 Termeni și definiții

| **Termen** | **Definiție** |
|-------------|---------------|
| **Cluster Autoscaler (CA)** | O resursă API care scalează automat clusterul în sine, crescând sau reducând numărul de noduri disponibile pe care pot rula Pods. |
| **ConfigMap** | Un obiect Kubernetes care permite stocarea datelor de configurare sub formă de perechi cheie-valoare. Oferă o metodă de gestionare a setărilor de configurare, separând logica aplicației de configurație. |
| **Horizontal Pod Autoscaler (HPA)** | Resursă API Kubernetes care ajustează automat numărul de replici de Pods în funcție de metrici definite, precum utilizarea CPU sau alți indicatori personalizați. |
| **IBM Cloud Catalog** | O colecție de servicii oferite de IBM, de la recunoaștere vizuală și procesare a limbajului natural până la crearea de chatbots. |
| **Analiză lingvistică (Linguistic Analysis)** | Procesul de detectare a tonului și intenției într-un text dat. |
| **Persistent Volume (PV)** | În API-ul Kubernetes, un Persistent Volume este o abstracție pentru stocare persistentă. Oferă opțiuni flexibile de stocare care există independent de ciclul de viață al unui Pod, asigurând persistența datelor aplicațiilor. |
| **Persistent Volume Claim (PVC)** | Un obiect API Kubernetes care solicită spațiu de stocare definit într-un Persistent Volume, permițând aplicațiilor să utilizeze stocare durabilă independent de Pods. |
| **Actualizări continue (Rolling Updates)** | Strategie care permite implementarea modificărilor aplicațiilor într-un mod controlat și automatizat pe toate Pods. Rolling Updates funcționează cu șabloane de tip Deployment și oferă posibilitatea de rollback în caz de eroare. |
| **Secrets** | Obiecte Kubernetes folosite pentru a stoca informații sensibile, precum parole, token-uri OAuth sau chei SSH, oferind o modalitate sigură de gestionare a datelor confidențiale. |
| **Legare de servicii (Service Binding)** | Procesul de conectare a aplicațiilor la servicii externe, cum ar fi API-uri REST, baze de date sau bus-uri de evenimente. |
| **Tone Analyzer Service** | Serviciu IBM Cloud care utilizează analiza lingvistică pentru a detecta tonul unui text. |
| **Vertical Pod Autoscaler (VPA)** | Resursă API Kubernetes care ajustează resursele CPU și memorie alocate unui Pod existent, permițând scalarea verticală a serviciilor dintr-un cluster. |
| **Volum (Volume)** | Director ce conține date accesibile mai multor containere dintr-un Pod. |
| **Montare volum (Volume Mount)** | Procesul de montare a unui volum declarat într-un container din același Pod, pentru acces comun la date. |
| **Plugin de volum (Volume Plugin)** | Componentă care facilitează integrarea stocării într-un Pod, permițând containerelor acces la resurse de stocare persistentă. |

---

## 🧰 Comenzi Kubernetes CLI — Administrarea aplicațiilor

| **Comandă** | **Descriere** |
|--------------|----------------|
| `kubectl autoscale deployment` | Scalează automat un Deployment Kubernetes. |
| `kubectl create configmap` | Creează o resursă de tip ConfigMap. |
| `kubectl get deployments -o wide` | Listează toate Deployment-urile cu detalii suplimentare. |
| `kubectl get hpa` | Listează resursele de tip Horizontal Pod Autoscaler (HPA). |
| `kubectl scale deployment` | Scalează manual un Deployment. |
| `kubectl set image deployment` | Actualizează imaginea curentă a unui Deployment. |
| `kubectl rollout` | Gestionează procesul de rollout al unei resurse. |
| `kubectl rollout restart` | Repornește o resursă (ex: Deployment) pentru a recrea containerele. |
| `kubectl rollout undo` | Anulează un rollout și revine la versiunea anterioară. |

---

📘 *Aceste concepte și comenzi sunt fundamentale pentru gestionarea eficientă a aplicațiilor în Kubernetes, permițând automatizarea, scalarea și actualizarea sigură a aplicațiilor containerizate.*
